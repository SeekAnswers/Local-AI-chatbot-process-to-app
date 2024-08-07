from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

# Initialize the Llama 3 model
model = OllamaLLM(model='llama3')

# Define the prompt template
template = ChatPromptTemplate.from_template("Question: {question}\nAnswer: Let's think step by step.")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        context = data.get('context', '')
        question = data.get('question', '')
        
        # Generate a response using the Llama 3 model
        prompt = template.format(question=question)
        result = model.invoke(prompt)
        
        # Extract the generated text
        response_text = result['text']
        
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
