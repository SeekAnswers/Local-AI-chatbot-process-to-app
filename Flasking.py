#Integrating the Python code with a Flutter app, first pip installed Flask into the environment


from pyexpat import model
from flask import Flask, request, jsonify
#from ollama import Ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


app = Flask(__name__)


# Initialize the model, in this case llama3 from Ollama
llama = OllamaLLM(model='llama3')

# Define the prompt template
template = ChatPromptTemplate.from_template("Question: {question}\nAnswer: Let's think step by step.")

@app.route('/chat', methods=['GET'])
def chat():
    data = request.json
    context = data.get('context', '')
    question = data.get('question', '')

# Generate a response using the Llama 3 model
    # input_text = f"{context} {question}"
    # result = llama.invoke({"context": context, "question": question})
    prompt = template.invoke({"question": question})
    result = model.invoke(prompt)
# Call your chain.invoke() method here ie
    #result = chain.invoke({"context": context, "question": question})
# In this case, extract the generated text
    response_text = result['text']
         
    return jsonify({"response": result})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

