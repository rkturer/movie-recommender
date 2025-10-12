
import pandas as pd 

from user_input import user_input

from where_to_watch import convert_title_to_movie_id, get_streaming_options

def main():  
    
    movies = pd.read_csv("data/cleaned_movies.csv")
    while True:
        genre = str(user_input(movies))
        
        recommendation = find_best_rating(movies, genre)

        if recommendation == "No movies from our database match this genre":
            print(recommendation + "\nOr your spelling was incorrect")
            reset = str(input("Would you like to search for another recommendation? (yes/no) "))
            if reset == "yes": 
                continue
            else:
                print("Thank you for trying the movie-recommender program!")
                break

        display(recommendation)
        
        title = title_only(recommendation)

        wants_stream = str(input("Would you like to know where you can stream " + title + "? (yes/no) ")).lower()
        
        if wants_stream == "yes":

            movie_id = convert_title_to_movie_id(title)

            streaming, purchase, buy = get_streaming_options(movie_id, title)

            print(display_watch_options(streaming, purchase, buy, title))

        

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
        return "No movies from our database match this genre"

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

def display_watch_options(streaming, renting, purchase, title):

    """takes the streaming options, renting options, purchasing options, and the title as parameters and 
    returns a nicely formatted output of where the movie is avaliable for the user to read"""

    #boolean checkers to return a different message API has no information at all for how to watch the title
    x = False
    y = False
    z = False

    #if else logic checks to see if there are options for each category: streaming, renting, purchasing  
    if type(streaming) == list: 
        streaming_string = "You can stream " + title + " on " + ', '.join(streaming)
    else:
        #changes boolean checker to true if no option is avaible
        x = True 
        streaming_string = streaming
    if type(renting) == list: 
        renting_string = "You can rent " + title + " on " + ', '.join(renting)
    else:
        y = True 
        renting_string = renting 

    if type(purchase) == list: 
        purchase_string = "You can purchase " + title + " on " + ', '.join(purchase)
    else:
        z = True
        purchase_string = purchase

    #will be make sense once i add a new function to ensure one of the ratings are us based
    if x and y and z == True:
        output = "In the United States there is no where to rent, stream, or buy " + title + "according to the Movie Data Base API" 
        return output #,america_rec() --> will search until it finds the highest rated movie with an american option in the API

    return streaming_string + "\n" + renting_string + "\n" + purchase_string 

def title_only(recommendation):
    """takes the result of find best rating function and extracts the title"""
    title = recommendation.split(" (")[0].replace("You should watch ", "")
    return title
    
if __name__ == "__main__":
    main()