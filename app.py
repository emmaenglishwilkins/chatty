from flask import Flask, render_template, request, session
from chatbot import chatbot_response 

app = Flask(__name__)
app.secret_key = 'penguin'

@app.route("/")
def home():
    session['state'] = 0
	return render_template("index.html")

@app.route("/", methods=['POST'])
def botresponse():
    userInput = request.form['msg']
    state = session['state']
    print(state)
    print(chatbot_response(state, userInput))
    state, chatResponse = chatbot_response(state, userInput)
    session['state'] = state
    return render_template("index.html", data=userInput,data2=chatResponse)

if __name__ == '__main__':
	app.run()