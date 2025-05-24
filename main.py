from fastapi import FastAPI

chatbot = FastAPI()


@chatbot.get("/")

def root():
    return "RESUME CHATBOT"