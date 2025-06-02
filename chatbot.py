import sqlite3, csv
import re
import random
from textblob import TextBlob, Word

# DB set up 
conn = sqlite3.connect('chatty1.db', check_same_thread=False)
c = conn.cursor()

from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

model.eval()

def ai_response(state, userInput): 
    prompt = f"User: {userInput}\nBot:"
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs, 
        max_length=100, 
        num_return_sequences=1, 
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "Bot:" in response:
        chat_response = response.split("Bot:")[1].strip()
    state += 1
    return state, chat_response

def chatbot_response(state, userInput):
    flag = True
    while flag:
        sentence = userInput
        if sentence == "":
            return ("bye!")
            flag = False
        elif "hello" in sentence.lower():
            return "Hi there!"
        elif "bye" in sentence.lower():
            return "Goodbye!"
            flag = False
        else: 
            state, response = ai_response(state, sentence)
            return response
        '''
        elif check_for_greeting(sentence):
            return check_for_greeting(sentence)
        elif check_for_topic(sentence) is not None:
            return check_for_topic(sentence)
        elif check_for_reflection(sentence):
            return check_for_reflection(sentence)
        elif check_for_facts(sentence):
            return check_for_facts(sentence)
        else:
            return "Sorry I don't know what you are saying."
        '''
def main(): 
    state = 0
    while True:
        userInput = input("You: ")
        if userInput.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            break
    
        state, response = ai_response(state, userInput)
        print("Chatbot:", response)

if __name__ == '__main__':
	main()
