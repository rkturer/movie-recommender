import pandas as pd 

class MovieData:
    """gathers and filters the csv file"""
    def __init__(self, file_path:str):
        """initializes the data frame"""
        self.movies = pd.read_csv(file_path)

    def find_all_genres(self):
        """creates a list of all possible movie genres in the data frame"""
        all_genres = self.movies["Genres"].str.split("|").explode().unique()
        return all_genres 

    def sort_by_genre(self, genre):
   
        #ensures input is a string and handles incorrect inputs
        if not isinstance(genre,str):
           raise TypeError(f"Error: Genre must be a string, got {type(genre).__name__}")
    
        #creates a copy of movies and creates a list corressponding to each movies genres seperated by "|"
        #creates a dataframe of the movies and each of its corresponding genres 
        movies_exploded = self.movies.copy()
        movies_exploded["Genres"] = movies_exploded['Genres'].str.split("|")
        movies_exploded = movies_exploded.explode("Genres")

        #takes each element in the genre column and makes sure there are no spaces and all letters are lowercase
        #creates a new data frame with every movie with the desired genre
        movies_exploded["Genres"] = movies_exploded["Genres"].str.strip().str.lower()
        df_genre = movies_exploded[movies_exploded["Genres"] == genre.lower()]

        #handles genres not included within my original data frame
        if df_genre.empty:
            return "No movies from our database match this genre"

        return df_genre
    


