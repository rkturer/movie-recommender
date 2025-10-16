
import pandas as pd

class UserInterface: 
    """handles user input and output"""

    @staticmethod
    def asks_genre(genres):
        """takes no parameters and asks the user if they know 
        what type of movie they would like to watch or like options"""
        pref = str(input("Do you know what type of movie you'd like to watch? (yes/no) ")).strip().lower()
        if pref == "yes":
            return UserInterface.get_genre_and_num(genres)
        else:
            return UserInterface.show_genre_options(genres)

    @staticmethod
    def show_genre_options(genres):
        """shows the user all of the possible movie genres to 
        pick  from then requests their choice"""
        print(genres)
        return UserInterface.get_genre_and_num(genres)

    @staticmethod
    def get_genre_and_num(genres):
        """takes no parameters and asks the user for the genre of movie they 
        would like recommended returns the genre"""
        lower_genres = [g.lower() for g in genres]
        while True:
            desired_genre = str(input("Please enter the genre you would like to watch: ")).strip().lower()
            if desired_genre.lower() in lower_genres:
                break
            else:
                print("Please enter a movie listed above. Check your spelling.")
        
        while True:
            try: 
                num_recs = int(input("How many recommendations would you like? (input an integer): "))
                if num_recs > 0:
                    break
                else: 
                    print("Please type a positive number")
            except ValueError: 
                print("Invalid Input: Please type an integer")
                
        return desired_genre, num_recs 
    
    @staticmethod
    def display_recs(recommendations):
        """displays the recommendation for the user"""
        print(recommendations)

    @staticmethod
    def ask_yes_no(question):
        """asks user a question returns boolean true is answer is yes else returns false"""
        return input(f"{question} (yes/no): ").strip().lower() == 'yes'

    @staticmethod
    def choose_fav(titles):
        """asks the user which of their desired outputs they want to know more about assuming that num_rec>1"""
        lower_titles = [r.lower() for r in titles]
        while True:    
            pref = str(input("Which movie would the best?(Type The Title) ")).strip()
            if pref.lower() in lower_titles:        
                return pref
            else:
                print("Your spelling was likely incorrect\nTry Again!")
        
    @staticmethod
    def display_watch_options(streaming, renting, purchase, title):

        """takes the streaming options, renting options, purchasing options, and the title as parameters and 
        returns a nicely formatted output of where the movie is avaliable for the user to read"""

        #creates an empty list for return value to go 
        parts = []

        #if logic checks to see if there are options for each category: streaming, renting, purchasing  
        if isinstance(streaming, list): 
            parts.append(f"You can stream {title} on {', '.join(streaming)}")

        if isinstance(renting, list): 
            parts.append(f"You can rent {title} on {', '.join(renting)}")


        if isinstance(purchase, list): 
            parts.append(f"You can purchase {title} on {', '.join(purchase)}")

        #takes care of no options in the states 
        if not parts:
            return f"There are no streaming, renting, or purchasing options for {title} in the United States of America"

        return "\n".join(parts)


