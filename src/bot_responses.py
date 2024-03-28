from bot_message import *
from data import DataController
from utility import encodeMessage

class BotResponse:
    @staticmethod
    def welcome(rerun=False):
        msg = BotMessage.get_message(BotResponseType.WELCOME)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)
    
    @staticmethod
    def patient_who(rerun=False):
        msg = BotMessage.get_message(BotResponseType.PATIENT_WHO)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)
    
    @staticmethod
    def new_patient(rerun=False):
        msg = BotMessage.get_message(BotResponseType.NEW_PATIENT)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def ask_name(rerun=False):
        msg = BotMessage.get_message(BotResponseType.NAME)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def ask_age(rerun=False):
        msg = BotMessage.get_message(BotResponseType.AGE)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def ask_gender(rerun=False):
        msg = BotMessage.get_message(BotResponseType.GENDER)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def invalid_age(rerun=False):
        msg = BotMessage.get_message(BotResponseType.INVALID_AGE)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def ask_symptom(rerun=False):
        msg = BotMessage.get_message(BotResponseType.SYMPTOM)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def ask_more_symptoms(rerun=False):
        msg = BotMessage.get_message(BotResponseType.MORE_SYMPTOM)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def symptom_added(symptom,rerun=False):
        print("symptom add")
        msg = BotMessage.get_message(BotResponseType.SYMPTOM_ADDED).format(symptom=symptom)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def symptom_exists(symptom,rerun=False):
        msg = BotMessage.get_message(BotResponseType.SYMPTOM_EXISTS).format(symptom=symptom)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def symptom_removed(symptom,rerun=False):
        msg = BotMessage.get_message(BotResponseType.AGE).format(symptom=symptom)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def disease_detected(disease,rerun=False):
        print("disease")
        msg = BotMessage.get_message(BotResponseType.DISEASE).format(disease=disease)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

    @staticmethod
    def feedback(rerun=False):
        msg = BotMessage.get_message(BotResponseType.FEEDBACK)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)
    @staticmethod
    def feedback_thanks(rerun=False):
        msg = BotMessage.get_message(BotResponseType.FEEDBACK_THANKS)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)
    
    @staticmethod
    def bye(rerun=False):
        msg = BotMessage.get_message(BotResponseType.BYE)
        DataController.add_messages(encodeMessage(msg,True),rerun=rerun)

