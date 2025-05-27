from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Ονομα application
chatbot = FastAPI()

# Επιτρεπουμε στο frontend να στειλει requests
chatbot.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
@chatbot.get("/")
def root():
    return "RESUME CHATBOT"



# Λεξικο με keys διαφορα keywords και values
# καταλληλες πληροφοριες που επιστρεφονται
resumeData = {
    "projects" : "Simple raytracing, PPM image viewer,Simulation of the greek elections with C",
    "education" : "I study Computer Science at the  University of Crete and am on the second year",
    "skills" : "Good knowledge of C/C++, Python (and libraries like Pandas,Numpy,Matplot etc), Java and OOP",
    "experience" :  "I have worked as a waiter and as an assistant barman",
    "hobbies" : "Studying various subjects,reading comics, playing video games and watching movies"
}

class Question(BaseModel):
    prompt : str

# Δηλωνουμε ενα post request το οποιο θα επιστρεφει αναλογη απαντηση στην ερωτηση του χρηστηη
@chatbot.post("/chat")
def get(question: Question):
    q = question.prompt.lower()

    if "projects" in q:
        return {"reply" : resumeData["projects"]}
    elif "education" in q:
        return {"reply" : resumeData["education"]}
    elif "skills" in q:
        return {"reply" : resumeData["skills"]}
    elif "hobbies" in q:
        return {"reply" : resumeData["hobbies"]}
    elif "experience" in q:
        return {"reply" : resumeData["experience"]}
    else:
        return {"reply" : "Sorry but i couldn't find any matches.Feel free to ask about my projects,education or skills"}

