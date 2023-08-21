from models import *
import openai

def getOpenAI():
    API_Key = ""
    openai.api_key = API_Key
    return openai

def CreateChatCompletion(model, messages):

    openAi = getOpenAI()
    completion = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )

    return completion
    