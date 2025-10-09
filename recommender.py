
import pandas as pd 

movies = pd.read_csv("data/cleaned_movies.csv")

def main():

    genre = user_input_genre()
    title, rating = find_best_rating(genre)
    output = formatter(title, rating)
    display(output)


def user_input_genre():
    """takes no parameters and asks the user for the genre of movie they 
    would like recommended returns the genre"""
    desired_genre = str(input("Please enter the genre you would like to watch: "))
    return desired_genre


def find_best_rating(genre):
    """takes an input of a string genre as an input and returns the highest rated movie in the genre"""
    
    #ensures input is a string and handles incorrect inputs
    if not isinstance(genre,str):
        raise TypeError(f"Error: Genre must be a string, got {type(genre).__name__}")

    #creates a new data frame of all the movies in the column genre
    df_genre = movies[movies['Genres'].str.lower() == genre.lower()]

    #handles genres not included within my original data frame
    if df_genre.empty:
        return "No movies from out database match this genre"

    #find the highest rated movie in the specified genre
    highest_rated = df_genre.loc[df_genre['Rating'].idxmax()]
    
    #returns highest rated movie
    return highest_rated["Title"], str(round(highest_rated["Rating"],3))

def formatter(title, rating):
    """takes two strings representing the title and the rating and concatenates them to produce the user output"""
    return "You should watch " + title + " it has a " + rating + " star rating!"

def display(output):
    """displays the output to the user"""
    print(output)
    
if __name__ == "__main__":
    main()