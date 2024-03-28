from enum import Enum
from typing import Final
import random as rnd

BotResponseType = Enum("BotResponseType",["WELCOME",'NAME','GENDER','PATIENT_WHO','AGE','SYMPTOM','MORE_SYMPTOM','FEEDBACK',"FEEDBACK_THANKS",'NEW_PATIENT','BYE',"DISEASE", "INVALID_AGE","SYMPTOM_ADDED","SYMPTOM_REMOVED","SYMPTOM_EXISTS"])

class BotMessage:
    __message : Final[dict] = {
    BotResponseType.WELCOME: [
        "Welcome! I'm here to assist you with disease detection.",
        "Hello there! I'm your virtual assistant for disease detection.",
        "Greetings! Let's work together to assess your symptoms.",
        "Hi! I'm here to help you understand your health better.",
        "Good day! I'm ready to assist you in identifying potential health concerns.",
        "Welcome aboard! Let's start by discussing your health.",
        "Hello! I'm here to provide support in understanding your symptoms.",
        "Greetings! Let's begin by talking about how you're feeling.",
        "Hi there! I'm your personal health assistant. How can I assist you today?",
        "Welcome! Let's work together to evaluate any health issues you may have."
    ],
    BotResponseType.NAME: [
        "Thank you. Could you please provide the name of the patient?",
        "Got it. What's the name of the patient?",
        "Noted. May I know the name of the patient?",
        "Understood. Could you please share the name of the patient?",
        "Great. What is the name of the patient?",
        "Acknowledged. Can you provide the name of the patient?",
        "Gotcha. Could you kindly share the name of the patient?",
        "Thanks for sharing. What's the name of the patient?",
        "Appreciate it. Before we proceed, could you provide the name of the patient?",
        "Perfect. Let's start by knowing the name of the patient."
    ],
    BotResponseType.PATIENT_WHO: [
        "Is the patient you?",
        "Are we discussing your symptoms or the symptoms of another person?",
        "Are we evaluating your health or someone else's?",
        "Should I assess your symptoms or those of someone else?",
        "Are we talking about your health or someone else's?",
        "Is it your health we're discussing or someone else's?",
        "Should I consider your symptoms or those of someone else?",
        "Are we discussing your condition or someone else's?",
        "Whose symptoms are we evaluating, yours or someone else's?",
        "Should I focus on your symptoms or those of someone else?"
    ],
    BotResponseType.GENDER: [
        "What is the gender of the patient?",
        "Could you tell me the gender of the patient?",
        "Is the patient male, female, or other?",
        "What gender does the patient identify with?",
        "Could you provide the gender of the patient?",
        "Is the patient a male, female, or other?",
        "Could you kindly share the gender of the patient?",
        "What gender does the patient belong to?",
        "Please specify the gender of the patient.",
        "In terms of gender, is the patient male, female, or other?"
    ],
    BotResponseType.AGE: [
        "How old is the patient?",
        "Can you tell me the age of the patient?",
        "What is the age of the patient?",
        "May I know the age of the patient?",
        "How many years has the patient been alive?",
        "Could you provide me with the age of the patient?",
        "What age bracket does the patient fall into?",
        "Could you kindly share the age of the patient?",
        "How many years young is the patient?",
        "In which age group does the patient belong?"
    ],
    BotResponseType.SYMPTOM: [
        "Please describe the symptoms.",
        "What symptoms is the patient experiencing?",
        "Could you tell me more about the symptoms?",
        "Describe the symptoms the patient is feeling.",
        "What specific symptoms are troubling the patient?",
        "Can you elaborate on the symptoms the patient is facing?",
        "Let's talk about the symptoms the patient is having.",
        "What are the main symptoms bothering the patient?",
        "Tell me about any symptoms the patient has noticed.",
        "What symptoms has the patient been experiencing lately?"
    ],
    BotResponseType.MORE_SYMPTOM: [
        "Do you have any other symptoms to mention?",
        "Are there any additional symptoms you'd like to share?",
        "Are there more symptoms the patient is experiencing?",
        "Should I consider any other symptoms?",
        "Are there any other symptoms besides these?",
        "Are there additional symptoms we should discuss?",
        "Should I know about any other symptoms?",
        "Are there more symptoms the patient wants to tell me about?",
        "Are there any other symptoms the patient has noticed?",
        "Does the patient have further symptoms to mention?"
    ],
    BotResponseType.FEEDBACK: [
        "How are you feeling about the provided information?",
        "Do you have any feedback on the information shared?",
        "What do you think about the information so far?",
        "Any thoughts or feedback on the information provided?",
        "Would you like to provide any feedback on the discussion?",
        "Is there anything you'd like to share about the conversation?",
        "Do you have any comments or feedback on our discussion?",
        "What's your opinion on the information shared?",
        "How do you feel about the assistance provided?",
        "Any comments or feedback you'd like to give?"
    ],
    # BotResponseType.NEW_PATIENT: [
    #     "Welcome! Let's start by assessing the symptoms of the patient.",
    #     "Hello! I'm here to help with the health concerns of the patient.",
    #     "Nice to meet you! Let's discuss the symptoms of the patient.",
    #     "Hello there! Let's begin by talking about the health of the patient.",
    #     "Welcome aboard! Let's evaluate the symptoms of the patient.",
    #     "Hi! I'm here to assist in understanding the health of the patient.",
    #     "Greetings! Let's start by discussing any symptoms the patient has.",
    #     "Hi there! I'm your virtual assistant for health concerns.",
    #     "Welcome! Let's work together to address the health issues of the patient.",
    #     "Hello! Let's start by assessing the current health status of the patient."
    # ],
     BotResponseType.BYE: [
        "Goodbye! Feel free to return if you have more questions.",
        "Farewell! Don't hesitate to come back if you need further assistance.",
        "Take care! If you have more concerns, I'll be here to help.",
        "Goodbye! Remember, I'm here to assist you whenever you need.",
        "Farewell! If you have more symptoms to discuss, just let me know.",
        "Take care! You can always reach out if you have more questions.",
        "Goodbye for now! Feel free to reach out anytime for assistance.",
        "Farewell! If you need more support, don't hesitate to contact me.",
        "Take care! Don't forget you can come back if you need more help.",
        "Goodbye! Stay healthy, and remember I'm here if you need me."
    ],
    BotResponseType.DISEASE: [
    "Based on the symptoms provided, it seems the patient might be suffering from {disease}.",
    "After analyzing the symptoms, it appears that the patient could have {disease}.",
    "The symptoms described align with {disease}. It's possible the patient is affected by it.",
    "Considering the symptoms, {disease} is a potential concern for the patient.",
    "The symptoms reported suggest {disease} as a possible condition the patient is experiencing.",
    "It's likely that the patient is suffering from {disease} based on the symptoms presented.",
    "The symptoms are indicative of {disease}. It's advisable to consider this as a potential diagnosis.",
    "Given the symptoms mentioned, {disease} could be the underlying issue for the patient.",
    "It seems probable that the patient is affected by {disease} considering the symptoms provided.",
    "The symptoms described are consistent with {disease}. It's important to further investigate."
],
    BotResponseType.SYMPTOM_ADDED: [
        "Got it, {symptom} has been added to the list of symptoms.",
        "Noted, {symptom} has been included as a new symptom.",
        "Thank you, {symptom} has been added to the symptoms list.",
        "{symptom} has been successfully added to the list of symptoms.",
        "Acknowledged, {symptom} is now included among the symptoms.",
        "Great, {symptom} has been added to the symptoms list.",
        "Thanks for the update, {symptom} has been added.",
        "{symptom} has been incorporated as a new symptom.",
        "Appreciate it, {symptom} is now part of the symptoms list.",
        "Perfect, {symptom} has been added as a new symptom."
    ],
    BotResponseType.SYMPTOM_REMOVED: [
        "Got it, {symptom} has been removed from the list of symptoms.",
        "Noted, {symptom} has been removed as a symptom.",
        "Thank you, {symptom} has been removed from the symptoms list.",
        "{symptom} has been successfully removed from the list of symptoms.",
        "Acknowledged, {symptom} is no longer included among the symptoms.",
        "Great, {symptom} has been removed from the symptoms list.",
        "Thanks for the update, {symptom} has been removed.",
        "{symptom} has been removed as a symptom.",
        "Appreciate it, {symptom} has been removed from the symptoms list.",
        "Perfect, {symptom} has been successfully removed."
    ],
    BotResponseType.SYMPTOM_EXISTS: [
        "Yes, {symptom} is already included in the list of symptoms.",
        "{symptom} is already present among the symptoms.",
        "Indeed, {symptom} is already listed as a symptom.",
        "Yes, {symptom} has already been reported as a symptom.",
        "Certainly, {symptom} is already among the listed symptoms.",
        "{symptom} has already been included in the symptoms list.",
        "Affirmative, {symptom} is already part of the symptoms.",
        "Yes, {symptom} was already present in the symptoms list.",
        "Yes, {symptom} has previously been reported as a symptom.",
        "Indeed, {symptom} is already included in the symptoms."
    ],
    BotResponseType.INVALID_AGE:[
        "You entered invalid age. Please enter integer value from 1 to 100."
        ],
    BotResponseType.NEW_PATIENT: [
    "Thank you for reaching out. Let's try to detect if you're a new patient.",
    "Thanks for contacting us. Let's see if you're a new patient.",
    "Appreciate your interest. Let's check if you're a new patient.",
    "Thanks for getting in touch. Let's determine if you're a new patient.",
    "Thank you for reaching out. Let's find out if you're a new patient.",
    "Thanks for contacting us. Let's see if you're new here.",
    "Appreciate your interest. Let's check if you're new to us.",
    "Thanks for getting in touch. Let's determine if you're new here.",
    "Thank you for reaching out. Let's see if you're new to our system.",
    "Thanks for contacting us. Let's find out if you're new to our service."
],
BotResponseType.FEEDBACK_THANKS:[
    "Thank you for your valuable feedback. It helps us improve our service.",
    "Thanks for sharing your feedback. We appreciate your input!",
    "Appreciate your feedback. Thank you for taking the time to share your thoughts!",
    "Thank you for providing feedback. Your input is valuable to us!",
    "Thanks a lot for your feedback. We'll take it into consideration!",
    "We appreciate your feedback. Thank you for helping us enhance our service!",
    "Thank you for sharing your thoughts. Your feedback is important to us!",
    "Thanks for the feedback! We'll use it to make our service even better.",
    "Appreciate your input. Thank you for helping us improve!",
    "Thank you for your feedback. We're grateful for your contribution!"
]
    }
    
    
   
    @staticmethod
    def get_message(purpose:BotResponseType) -> str:
        opts = BotMessage.__message[purpose]
        ind = rnd.randint(0,len(opts)-1)
        return opts[ind]
