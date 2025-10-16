# **Project in Progress!!!**

[![Screen Shot of Program Running in Terminal](/images/movie-recommender.jpg)]

## 🎬🎬🎬 A Movie Recommending Program 🎬🎬🎬

## **Phase One**

- Downloaded three data sets (movies.dat, user.dat and ratings.dat) off of Movie Lens 
- Cleaned and explored the data using Jupyter Notebook 
- Created a "cleaned_movies.csv" which includes:
  - MovieID
  - Average Rating (for movies w/ >5 ratings)
  - Genre
  - Title

## **Phase Two**

- Created a python files to give movie recommendations
- The "user_input.py" file handles user input in the terminal and returns the genre of the user's choosing
- The "recommender.py" file reads the my cleaned_movies.csv file and retrieves the highest rated movie from the genre the user chose

## **Phase Three**

- Created a new python file "where_to_watch.py" that uses The Movie Data Base (TMDb) API 
- I used dotenv to manage API-Keys securely 
- Retrieves where a movie could be in real time:
  - Streamed: Netflix, Disney Plus, Hulu, etc 
  - Bought or Rented

## **How To Run The Project**
### 1. Clone my repo:
```bash
git clone https://github.com/rkturer/movie-recommender.git
cd movie-recommender
```

### 2. Install Dependencies:
This project requires:
* Pandas
* requests
* python-dotenv

```bash
pip install pandas requests python-dotenv
```

### 3. Add/Create Your Own API-KEY
- If you already have a key: create an .env file and add
```ini
TMDB_API_KEY=your_api_key_here
```
-If you do NOT already have a key: Go to The Movie Data Base and create an account (it's free), get your key, follow step above

### 4. Run the program
```bash
python app.py
```

### 5. Follow the Terminal Prompts
- It will ask if you know the movie genre you want to watch
- If you would like to know where you can watch the movie in the US
- And if you would like more recommendations

## Future Updates
- Front End Interface (HTML, CSS, Flask, etc)
- Personalization of Recommendations
- Recommendations with guaranteed ways to watch in the US

## About The Creator
- Rachel Turer - Computer Science and Statistics Major At BU
- Email: [rkturer@gmail.com](mailto:rkturer@gmail.com)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/rachel-turer-857b67385)


