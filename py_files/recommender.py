class Recommender: 
    """finds/formatts the highest rated movie from the recommended genre """

    @staticmethod
    def find_best_rating(df_genre, num_recs):
        """takes an input of a data base of the specific genre as an input and returns the highest rated movie in the genre"""

        #find the highest rated movie in the specified genre
        highest_rated = df_genre.nlargest(num_recs, 'Rating')
    
        title = highest_rated["Title"].tolist()
        rating = highest_rated["Rating"].round(3).astype(str).tolist()
            #returns highest rated movie
        return Recommender.formatter(title,rating)
    
    @staticmethod
    def formatter(title, rating):
        """takes two strings or lists representing the title and the rating and concatenates them to produce the user output"""
        if isinstance(title,str):
            return f"You should watch " + title + " it has a " + rating + " star rating!"
        else:
            output_list = [f"You should watch {t} it has a {r} star rating!"
                           for t,r in zip(title, rating)]
        return "\n".join(output_list)
    
    @staticmethod
    def title_only(recommendation):
        """takes the result of find best rating function and extracts the title"""
        title = recommendation.split(" (")[0].replace("You should watch ", "")
        return title
    
