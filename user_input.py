
import pandas as pd

def user_input(movies):
    """takes no parameters and asks the user if they know 
    what type of movie they would like to watch or like options"""
    pref = str(input("Do you know what type of movie you'd like to watch? (yes/no) ")).strip().lower()
    if pref == "yes":
        return user_input_genre()
    else:
        return user_input_options(movies)

def user_input_options(movies):
    """shows the user all of the possible movie genres to 
    pick from then requests their choice"""
    all_genres = movies["Genres"].str.split("|").explode().unique()
    print("Here are all of the genres: ", all_genres)
    return user_input_genre()

def user_input_genre():
    """takes no parameters and asks the user for the genre of movie they 
    would like recommended returns the genre"""
    desired_genre = input("Please enter the genre you would like to watch: ").strip().lower()
    return desired_genre 
