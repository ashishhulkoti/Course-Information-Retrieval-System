import json
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load the course data
with open('../CSCoursesCrawler/CSCoursesCrawler/courses.json', 'r') as f:
    courses = json.load(f)

# Combine the code, title, and description into a single text field for each course
combined_texts = [' '.join([course['code'], course['title'], course['description']]) for course in courses]

print(combined_texts)

# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(combined_texts)

# Store the terms and the corresponding course IDs
terms = vectorizer.get_feature_names_out()
course_ids = [course['code'] for course in courses]

# Create an inverted index as a dictionary {term: [course_ids]}
inverted_index = {}
for i, term in enumerate(terms):
    inverted_index[term] = tfidf_matrix[:, i].nonzero()[0].tolist()

# Save the inverted index and the vectorizer for later use in query processing
with open('inverted_index.pkl', 'wb') as f:
    pickle.dump(inverted_index, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

# Save the TF-IDF matrix for later use in query processing
with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)