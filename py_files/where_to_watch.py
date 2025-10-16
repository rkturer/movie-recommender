
from dotenv import load_dotenv 
import os 
import requests

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

class WhereToWatch:

    @staticmethod
    def convert_title_to_movie_id(highest_rated_title):
        """takes the highest rated title as parameter and returns the corresponding 
        movie id within the movie data base api """

        #uses the url for later use 
        url = "https://api.themoviedb.org/3/search/movie"

        #sets my api key and uses query to request data about the movie from the parameter 
        params = {
            "api_key": api_key,
            "query": highest_rated_title}
        
        #requests data from the api server using the url, my api-key, and the movie title 
        response = requests.get(url, params=params)

        #converts the data into dictionary
        movie_data = response.json()

        #extracts the first indexed element in results (normally most relevant one)
        results = movie_data["results"][0]

        #takes care of senario of the movie not being in the data base 
        if results == None:
            return "Your movie was not in The Movie Data Base API"
        
        #finds and returns the numerical id corresponding to the movies title 
        movie_id_tmdb = results['id']
        return movie_id_tmdb
        
    @staticmethod
    def get_streaming_options(movie_id_tmdb, highest_rated_title):

        """parameter is the movie id found in the "convert_title_to_movieid" fucntion
        and uses it to search the api for where the movie can be streamed, bought, or rented """
        
        #dyanmically create a API request using formatting string where the parameter "movie_id_tmdb" is added the the url
        url = f"https://api.themoviedb.org/3/movie/{movie_id_tmdb}/watch/providers"
        
        #stores api key as a parameter 
        params = {"api_key": api_key,}

        #requests the api for the information using the dynamic url and my api key 
        response = requests.get(url, params=params)

        #converts raw data into a dictionary
        movie_provider = response.json()

        #filters the data down to only United States 
        us_results = movie_provider.get("results", {}).get("US", {})

        #handles if no us streaming, renting, or purchasing services have the movie 
        if us_results == {}:
            streaming_providers = "On the Movie Data Base API, no streaming services in the US have, " + highest_rated_title
            renting_options = "On the Movie Data Base API, no renting services in the US have, " + highest_rated_title
            purchase_options = "On the Movie Data Base API, there are no sites to purchase " + highest_rated_title + " in the US"
        
        #uses list comprehension to extract the provider names from the lists of dictionaries 
        else:
            streaming_providers = [my_dict["provider_name"] for my_dict in us_results.get("flatrate", [])] or "No streaming options avaliable on The Movie Data Base API"
            renting_options = [my_dict["provider_name"] for my_dict in us_results.get("rent", [])] or "No renting options avaliable on The Movie Data Base API"
            purchase_options = [my_dict["provider_name"] for my_dict in us_results.get("buy", [])] or "No purchasing options avaliable on The Movie Data Base API"

        #returns 3 lists of providers corresponding to each option 
        return streaming_providers, renting_options, purchase_options



        
