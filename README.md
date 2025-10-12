# movie-recommender
Project in Progress!!!

🎬🎬🎬 A movie recommending program 🎬🎬🎬

#**phase one**

Downloaded three data sets (movies.dat, user.dat and ratings.dat) off of Movie Lens 

Cleaned and explored the data using Jupyter Notebook 

Created a "cleaned_movies.csv" which includes MovieID, Rating (average rating for movies w/ >5 ratings), Genre, and Title

##**phase two**

Created a python files to give movie recommendations

the "user_input.py" file handles user input in the terminal and returns the genre of the user's choosing

The  "recommender.py" file reads the my cleaned_movies.csv file and retrieves the highest rated movie from the genre the user chose

##**phase three**

Created a new python file "where_to_watch.py" that uses The Movie Data Base (TMDb) API 
I used deotenv to manage API-Keys securely 
Retrieves where a movie could be in real time:
  Streamed: Netflix, Disney Plus, Hulu, etc 
  Bought
  Rented 


