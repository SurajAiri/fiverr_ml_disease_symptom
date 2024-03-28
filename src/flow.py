import streamlit as st
from data import *
from bot_responses import BotResponse
from display_message import display_messages
from input_button import *
from predict import DiseaseDetector
from symptoms import model_symptoms


class RunFlow:
    def __init__(self):
        # Custom CSS styling for button width
        st.markdown(
            """
            <style>
            /* Target the container holding the buttons within each column */
            div.row-widget.stButton > button { 
                width: 100%; 
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        self.predictor = DiseaseDetector()

    # disease detection
    def predict_disease(self):
        symptoms = DataController.get_patient_symptoms()
        return self.predictor.predict(symptoms)
    

    # callbacks
    def patient_who_callback(self,value):
        msg = "I am patient." if value.lower() == "self" else "I am searching for someone else"
        DataController.add_messages(encodeMessage(msg,isBot=False))
        DataController.change_state(ProgramState.GENDER)
        DataController.set_bot_replied_status(False)
        
    def disease_callback(self,isFirst:bool):
        DataController.set_bot_replied_status(False)
        if isFirst:
            DataController.change_state(ProgramState.ASK_FEEDBACK)
        else:
            DataController.change_state(ProgramState.NEW_PATIENT)

    def feedback_thanks_callback(self,isFirst:bool):
        DataController.set_bot_replied_status(False)
        if isFirst:
            DataController.change_state(ProgramState.BYE)
        else:
            DataController.change_state(ProgramState.NEW_PATIENT)
            
    def ask_feedback_callback(self,feedback):
        DataController.add_messages(encodeMessage(feedback,isBot=False))
        DataController.set_bot_replied_status(False)
        DataController.change_state(ProgramState.FEEDBACK)


    def ask_gender_callback(self,value):
        msg = "I am Male." if value == Gender.MALE else "I am Female."
        DataController.add_messages(encodeMessage(msg,isBot=False))
        DataController.change_state(ProgramState.NAME)
        DataController.set_bot_replied_status(False)

    def ask_name_callback(self,value):
        print("ask name callbacks")
        DataController.add_messages(encodeMessage(f"My name is {value}",isBot=False))
        DataController.set_patient_name(value)
        DataController.change_state(ProgramState.AGE)
        DataController.set_bot_replied_status(False)
    
    def ask_age_callback(self,value):
        print('value',value)
        if value == None:
            return
        msg = f'I am {value} years old'
        DataController.add_messages(encodeMessage(msg,isBot=False))
        age = 0
        try:
            age = int(value)
            if age < 1 or age > 100:
                DataController.add_messages(encodeMessage(BotResponse.invalid_age()))
                return

            DataController.set_patient_age(age)
            DataController.set_bot_replied_status(False)
            DataController.change_state(ProgramState.SYMPTOM)
        except:
            DataController.add_messages(encodeMessage(BotResponse.invalid_age()))
            return
        
        
    def add_symptom_callback(self,value):
        print("add symptom",value)
        DataController.add_messages(encodeMessage(f"Add {value} symptom.",isBot=False))
        if DataController.add_patient_symptom(value):
            print('added')
            BotResponse.symptom_added(value)
        else:
            print('already exists')
            BotResponse.symptom_exists(value)
        DataController.set_bot_replied_status(False)
        if len(DataController.get_patient_symptoms()) > 4:
            DataController.change_state(ProgramState.DISEASE)
        time.sleep(0.1)
        st.rerun()

    def remove_symptom_callback(self,value):
        DataController.add_messages(encodeMessage(f"Remove {value} symptom.",isBot=False))
        DataController.remove_patient_symptom(value)
        BotResponse.symptom_removed(value)
        DataController.set_bot_replied_status(False)
        time.sleep(0.1)
        st.rerun()

    def detect_symptom_callback(self):
        DataController.set_bot_replied_status(False)
        DataController.change_state(ProgramState.DISEASE)
        time.sleep(0.1)
        st.rerun()



    # ui
    def welcome(self):
        # if DataController.bot_replied_status():
        #     return
        DataController.change_state(ProgramState.PATIENT_WHO)
        BotResponse.welcome(rerun=True)

    def patient_who(self):
        opts = ['Self','Other']
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            BotResponse.patient_who(rerun=False)

        display_messages()
        display_2_options(opts,[lambda:self.patient_who_callback(opts[0]),lambda:self.patient_who_callback(opts[1])])
    
    def ask_gender(self):
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            BotResponse.patient_who(rerun=False)
        display_messages()
        display_2_options(['Male','Female'],[lambda:self.ask_gender_callback(Gender.MALE),lambda:self.ask_gender_callback(Gender.FEMALE)])


    def ask_name(self):
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            BotResponse.ask_name(rerun=False)
        display_messages()
        display_input_field("Enter patient's name",on_submit= self.ask_name_callback)
        
    def ask_age(self):
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            BotResponse.ask_age(rerun=False)
        display_messages()
        display_input_field("Enter patient's age",on_submit= self.ask_age_callback)
        
    def ask_symptom(self):
        symptoms = DataController.get_patient_symptoms()
        print(len(symptoms),'symptoms length')
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            if len(symptoms) > 0:
                BotResponse.ask_symptom(rerun=False)
            else:
                BotResponse.ask_more_symptoms(rerun=False)
                
        display_messages()
        if len(symptoms) < 1:
            # only add symptom (1)
            symptom_popup("Add Symptom",model_symptoms,on_submit= self.add_symptom_callback)
        elif len(symptoms) < 3:
            # add and remove symptom (2)
            add_remove_symptom_popup(symptoms,DataController.get_patient_symptoms(),on_add=self.add_symptom_callback,on_remove=self.remove_symptom_callback)

        elif len(symptoms) < 4:
            # add and remove symptom (3)
            # detect disease btn
            add_remove_detect_symptom_popup(symptoms,DataController.get_patient_symptoms(),on_add=self.add_symptom_callback,on_remove=self.remove_symptom_callback,on_detect=self.detect_symptom_callback)
        else:
            self.detect_symptom_callback()
            # auto call detect disease 

    def detect_disease(self):
        # symptoms = DataController.get_patient_symptoms()
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            disease = self.predict_disease()
            BotResponse.disease_detected(disease)

        display_messages()
        # feedback and new patient
        display_2_options(['Feedback','New Patient'],[lambda:self.disease_callback(True),lambda:self.disease_callback(False)])

    def feedback_thanks(self):
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            BotResponse.feedback_thanks()
        display_messages()
        # thanks and new patient
        display_2_options(['Bye','New Patient'],[lambda:self.feedback_thanks_callback(True),lambda:self.disease_callback(False)])

    def ask_feedback(self):
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            BotResponse.feedback()
        display_messages()
        # thanks and new patient
        display_input_field("Write Feedback",on_submit=self.ask_feedback_callback)
    
    def new_patient(self):
        print('new patient',DataController.get_patient_symptoms())
        msg = "I want to try for new patient"
        DataController.add_messages(encodeMessage(msg,isBot=False))
        BotResponse.new_patient()
        DataController.clear_patient_data()
        DataController.change_state(ProgramState.PATIENT_WHO)
        time.sleep(0.1)
        st.rerun()

    
    def bye(self):
        msg = "Bye"
        DataController.add_messages(encodeMessage(msg,isBot=False))
        if not DataController.bot_replied_status():
            DataController.set_bot_replied_status(True)
            BotResponse.bye()
        display_messages()
        if st.button("Try New Patient"):
            self.new_patient()

    

    def run(self):
        state = DataController.get_program_state()
        print("run_flow: ",state)
        if state == ProgramState.WELCOME:
            self.welcome()
        if state == ProgramState.PATIENT_WHO:
            self.patient_who()
        if state == ProgramState.GENDER:
            self.ask_gender()
        if state == ProgramState.NAME:
            self.ask_name()
        if state == ProgramState.AGE:
            self.ask_age()
        if state == ProgramState.SYMPTOM:
            self.ask_symptom()
        if state == ProgramState.DISEASE:
            self.detect_disease()
        if state == ProgramState.FEEDBACK:
            self.feedback_thanks()
        if state == ProgramState.ASK_FEEDBACK:
            self.ask_feedback()
        if state == ProgramState.NEW_PATIENT:
            self.new_patient()
        if state == ProgramState.BYE:
            self.bye()
