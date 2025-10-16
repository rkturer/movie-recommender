from movie_data import MovieData
from recommender import Recommender
from where_to_watch import WhereToWatch
from user_input import UserInterface

class App:
    """Coordinates the data, userinput, and recommender"""

    def __init__(self, file_path:str):
        """contructs variables for data, recommender and the UI"""
        self.data = MovieData(file_path)
        self.recommender = Recommender()
        self.ui = UserInterface()
        self.wtw = WhereToWatch()

    def run(self):
        
        while True:
            
            genres = self.data.find_all_genres()

            genre, num_recs = self.ui.asks_genre(genres)

            df_genre = self.data.sort_by_genre(genre)

            if isinstance(df_genre, str):
                print(df_genre)
                continue

            recommendation = self.recommender.find_best_rating(df_genre, num_recs)
            self.ui.display_recs(recommendation)

            if num_recs > 1:
                if isinstance(recommendation, str):
                    recommendation = recommendation.split("\n")
                
                titles = [self.recommender.title_only(r) for r in recommendation]
                
                fav = self.ui.choose_fav(titles)
            else:
                fav = self.recommender.title_only(recommendation)
            
            wants_stream = self.ui.ask_yes_no(f"Would you like to know where you can stream, rent, or buy {fav}?")
            if wants_stream:
                movie_id = self.wtw.convert_title_to_movie_id(fav)
                streaming, renting, purchase = self.wtw.get_streaming_options(movie_id, fav)
                print(self.ui.display_watch_options(streaming, renting, purchase, fav))

            another = self.ui.ask_yes_no("Would you like another recommendation?")
            if not another:
                print("Enjoy your movie!")
                break



if __name__ == "__main__":
    app = App("data/movie_ratings.csv")
    app.run()
