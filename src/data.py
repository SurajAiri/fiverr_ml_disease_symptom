from enum import Enum
import time
import streamlit as st
from bot_message import BotMessage, BotResponseType
import constants
from utility import encodeMessage

ProgramState = Enum("ProgramState",['WELCOME','PATIENT_WHO','GENDER','NAME','AGE','SYMPTOM','DISEASE','ASK_FEEDBACK','FEEDBACK','BYE',"NEW_PATIENT"])
Gender = Enum("Gender",['MALE','FEMALE'])



class DataController:
    __messages = st.session_state.get(constants.MESSAGE_KEY,[])
    __program_state = st.session_state.get(constants.PROGRAM_STATE_KEY,ProgramState.WELCOME)
    __bot_message_shown = st.session_state.get(constants.BOT_MESSAGE_SHOWN_KEY,False)

    # patient info
    __patient_name:str =  st.session_state.get(constants.PATIENT_NAME_KEY,'')
    __patient_gender:Gender = st.session_state.get(constants.PATIENT_GENDER_KEY,Gender.MALE)
    __patient_age: int = st.session_state.get(constants.PATIENT_AGE_KEY,0)
    __patient_symptoms: list  =  st.session_state.get(constants.PATIENT_SYMPTOMS_KEY,[])
    __patient_disease:str = st.session_state.get(constants.PATIENT_DISEASE_KEY,'')
    

    @staticmethod
    def bot_replied_status() -> bool:
        return DataController.__bot_message_shown
    @staticmethod 
    def set_bot_replied_status(value:bool):
        DataController.__bot_message_shown = value
        st.session_state[constants.BOT_MESSAGE_SHOWN_KEY] = DataController.__bot_message_shown

    @staticmethod
    def get_patient_name() -> str:
        return DataController.__patient_name
    
    @staticmethod
    def get_patient_age() -> int:
        return DataController.__patient_age
    
    @staticmethod
    def get_patient_disease() -> str:
        return DataController.__patient_disease
    
    @staticmethod
    def get_patient_symptoms() -> list:
        return DataController.__patient_symptoms
    
    @staticmethod
    def get_patient_gender() -> Gender:
        return DataController.__patient_gender
    

    @staticmethod
    def set_patient_name(value):
        DataController.__patient_name = value
        st.session_state[constants.PATIENT_NAME_KEY] = DataController.__patient_name
    
    @staticmethod
    def set_patient_gender(value):
        DataController.__patient_gender = value
        st.session_state[constants.PATIENT_GENDER_KEY] = DataController.__patient_gender
    
    @staticmethod
    def set_patient_age(value):
        DataController.__patient_age = value
        st.session_state[constants.PATIENT_AGE_KEY] = DataController.__patient_age
    
    @staticmethod
    def set_patient_disease(value):
        DataController.__patient_disease = value
        st.session_state[constants.PATIENT_DISEASE_KEY] = DataController.__patient_disease
    
    @staticmethod
    def add_patient_symptom(value) -> bool:
        print("adding ",value, DataController.__patient_symptoms)
        if value in DataController.__patient_symptoms:
            return False  
        DataController.__patient_symptoms.append(value)
        st.session_state[constants.PATIENT_SYMPTOMS_KEY] = DataController.__patient_symptoms
        return True
  
    @staticmethod
    def remove_patient_symptom(value) -> bool:
        if value not in DataController.__patient_symptoms:
            return False  
        DataController.__patient_symptoms.remove(value)
        st.session_state[constants.PATIENT_SYMPTOMS_KEY] = DataController.__patient_symptoms
        return True

    @staticmethod
    def clear_data():
        DataController.clear_patient_data()
        DataController.set_bot_replied_status(False)


    @staticmethod 
    def clear_patient_data():
        st.session_state[constants.PATIENT_NAME_KEY] = ""
        st.session_state[constants.PATIENT_AGE_KEY] = 0
        st.session_state[constants.PATIENT_GENDER_KEY] = Gender.MALE
        st.session_state[constants.PATIENT_DISEASE_KEY] = ""
        st.session_state[constants.PATIENT_SYMPTOMS_KEY] = []
        DataController.__patient_name = ""
        DataController.__patient_age = 0
        DataController.__patient_gender = Gender.MALE
        DataController.__patient_disease = ""
        DataController.__patient_symptoms = []

    @staticmethod
    def change_state(state:ProgramState):
        DataController.__program_state = state
        st.session_state[constants.PROGRAM_STATE_KEY] = DataController.__program_state

    @staticmethod
    def get_program_state()->ProgramState:
        return DataController.__program_state

    @staticmethod
    def add_messages(message,rerun=False):
        print("we got call")
        DataController.__messages.append(message)
        st.session_state[constants.MESSAGE_KEY] = DataController.__messages
        if rerun:
            time.sleep(0.1)
            st.rerun()

    @staticmethod
    def get_messages():
        return DataController.__messages

    @staticmethod
    def clear_messages():
        st.session_state[constants.MESSAGE_KEY] = []

    @staticmethod
    def welcome_message():
        if len(DataController.__messages) == 0:
            welcome = BotMessage.get_message(BotResponseType.WELCOME)
            DataController.add_messages(encodeMessage(msg=welcome,isBot=True))