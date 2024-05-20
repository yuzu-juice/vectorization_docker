from sentence_transformers import SentenceTransformer
import json
import time

model = SentenceTransformer('./model/')

def vectorize_text(text):
    embedding = model.encode([text], convert_to_tensor=True)
    return embedding.cpu().numpy().tolist()

def handler(event, context):
    print('event:', event)
    print('context:', context)
    
    start_time = time.time()
    result = vectorize_text(event['text'])
    end_time = time.time()
    
    duration = end_time - start_time
    print(f"Execution time for vectorize_text: {duration} seconds")
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }