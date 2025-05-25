from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

