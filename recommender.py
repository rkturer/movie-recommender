
import pandas as pd 

from user_input import user_input, user_input_options, user_input_genre

def main():  
    
    movies = pd.read_csv("data/cleaned_movies.csv")
    print(movies.head())
    while True:
        genre = str(user_input(movies))

        recommendation = find_best_rating(movies, genre)

        display(recommendation)

        another = str(input("Would you like another recommendation? (yes/no) "))
        if another.lower() != "yes":
            print("Enjoy your movie!")
            break

def find_best_rating(movies, genre):
    """takes an input of a string genre as an input and returns the highest rated movie in the genre"""
    
    #ensures input is a string and handles incorrect inputs
    if not isinstance(genre,str):
        raise TypeError(f"Error: Genre must be a string, got {type(genre).__name__}")

    #creates a copy of movies and creates a list corressponding to each movies genres seperated by "|"
    #creates a dataframe of the movies and each of its corresponding genres 
    movies_exploded = movies.copy()
    movies_exploded["Genres"] = movies_exploded['Genres'].str.split("|")
    movies_exploded = movies_exploded.explode("Genres")

    #takes each element in the genre column and makes sure there are no spaces and all letters are lowercase
    #creates a new data frame with every movie with the desired genre
    movies_exploded["Genres"] = movies_exploded["Genres"].str.strip().str.lower()
    df_genre = movies_exploded[movies_exploded["Genres"] == genre.lower()]

    #handles genres not included within my original data frame
    if df_genre.empty:
        return "No movies from out database match this genre"

    #find the highest rated movie in the specified genre
    highest_rated = df_genre.loc[df_genre['Rating'].idxmax()]
    
    #returns highest rated movie
    return formatter(highest_rated["Title"], str(round(highest_rated["Rating"],3)))

def formatter(title, rating):
    """takes two strings representing the title and the rating and concatenates them to produce the user output"""
    output = "You should watch " + title + " it has a " + rating + " star rating!"
    return(output)

def display(output):
    """displays the output to the user"""
    print(output)
    

if __name__ == "__main__":
    main()