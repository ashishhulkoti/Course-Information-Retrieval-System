from flask import Flask, request, jsonify
import pickle
from sklearn.metrics.pairwise import linear_kernel
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the vectorizer and TF-IDF matrix
with open('../indexer/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('../indexer/tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

# Load course data if needed for details in results
with open('../CSCoursesCrawler/CSCoursesCrawler/courses.json', 'r') as f:
    courses = json.load(f)

# The search function that takes a query and returns the most relevant courses
def search(query, top_k=10):
    query_vector = vectorizer.transform([query])
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-top_k-1:-1]
    
    # Extract the course details for the top K results
    results = [{'code': courses[i]['code'], 'title': courses[i]['title'], 'description': courses[i]['description'], 'prerequisites': courses[i]['prerequisites']} for i in related_docs_indices]
    return results

@app.route('/search', methods=['POST'])
def search_endpoint():
    data = request.json
    query = data['query']
    top_k = data.get('top_k', 10)

    # Call the search function and return results
    results = search(query, top_k)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
