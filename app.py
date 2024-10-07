from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import time
import os

app = Flask(__name__)

model = SentenceTransformer('./model/')

def vectorize_text(text):
    embedding = model.encode([text], convert_to_tensor=True)
    return embedding.cpu().numpy().tolist()

@app.route('/vectorize', methods=['POST'])
def handle_vectorize():
    start_time = time.time()
    
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    result = vectorize_text(data['text'])
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution time for vectorize_text: {duration} seconds")

    return jsonify(result)

@app.route('/', methods=['GET'])
def home():
    return "Text Vectorization Service is running. Send a POST request to /vectorize to use the service."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)