import csv
from flask import Flask, render_template,request,redirect,url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


app = Flask(__name__)


with open('file.txt','r') as file:
    conversation = file.read()

bott = ChatBot("HealthCare ChatBot")
trainer = ListTrainer(bott)
trainer.train([   
    "Hello",
    "Hi there!",
    "Hi",
    "Hello!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    'What is your name?', 
    'My name is Health ChatBot',
    'Who created you?',
    'Shreyas Mane, Aditya Tajane and Aditya Mhaske'
    "Tell me about yourself",
    "My name is Medical Diagnosis Chatbot. The Healthcare Chatbot project is developed to help the people to predict their health issue early at home before they visit the doctor or hospital for the minor problems. ",
    "I am not feeling well",
    "Enter your symptoms and predict the disease.",
    "I have Fungal infection",
    "Do not worry. Take precautions such as keep your skin clean and dry, particularly the folds of your skin. wash your hands often, especially after touching animals or other people.",
    "Should I consult doctor",
    "Consult doctor if you are ill from more than 2 days",

 ])
trainer = ChatterBotCorpusTrainer(bott)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home(): 
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bott.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
