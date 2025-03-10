from flask import Flask, render_template, request
from chatbot import chatbot_response 

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/", methods=['POST'])
def botresponse():
    userInput = request.form['msg']
    chatResponse = chatbot_response(userInput)
    return render_template("index.html", data=userInput,data2=chatResponse)

if __name__ == '__main__':
	app.run()