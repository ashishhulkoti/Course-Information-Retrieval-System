# Course Search Information Retrieval System

This project is a comprehensive information retrieval system for searching 500-level computer science graduate courses of Illinois Tech. It consists of a Scrapy crawler that scrapes course data from a university website, an indexer that generates a TF-IDF matrix for the search functionality, a Flask API to process search queries, and a frontend interface for user interaction.

Developed by: Ashish Hulkoti    
Institution: Illinois Institute of Technology

## Project Structure

- `CSCoursesCrawler`: The Scrapy project containing the crawler to scrape course data.
- `FlaskProcessor`: The Flask application that processes search queries and returns results.
- `FrontEnd`: Contains the HTML front end for the search interface.
- `indexer`: Contains the indexing script to generate the TF-IDF matrix and other search indexes.

## Setup

1. **Clone the Repository**
```
git clone <repository-url>
```
```
cd <repository-name>
```

2. **Install Dependencies**

Make sure you have Python installed on your system. This project requires Python 3.6+.

- For the Scrapy crawler:
  ```
  pip install scrapy beautifulsoup4
  ```
- For the indexer:
  ```
  pip install scikit-learn
  ```
- For the Flask application:
  ```
  pip install flask flask-cors
  ```

3. **Set Up the Scrapy Crawler**

Navigate to the `CSCoursesCrawler` directory and run the crawler to scrape the course data:
```
cd CSCoursesCrawler
```
```
rm CSCoursesCrawler/fetched_data/courses.json  #remove courses.json if present before running crawler
```
```
scrapy crawl college_courses -o ./CSCoursesCrawler/fetched_data/courses.json
```

The crawled data will be saved to `courses.json` in a folder "fetched_data" in the same directory.

4. **Run the Indexer**

From the project root directory, run the indexer script to process the scraped data and create search indexes:
```
cd indexer
```
```
python course_indexer.py
```

This will create `tfidf_matrix.pkl`, `inverted_index.pkl`, and `vectorizer.pkl` files which are used for searching.

5. **Start the Flask API**

Go to the `FlaskProcessor` directory from the project root directory and start the Flask server:
```
cd FlaskProcessor
```
```
flask run
```

The Flask API will be running at `http://127.0.0.1:5000/`.

6. **Launch the Frontend Interface**

Open the `index.html` file located in the `FrontEnd` directory with a web browser to access the search interface.

## Usage

1. **Perform a Search**

- Enter a search term related to course titles or descriptions in the search bar.
- Optionally, specify the number of results (`k`) you want to retrieve.
- Click on `Search` to execute the search.

2. **View Results**

The search results will be displayed on the page, listing the relevant courses along with their details such as course code, title, description, and prerequisites.


