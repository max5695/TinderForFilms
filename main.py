import requests
import pandas as pd
import json
import random
from transformers import GPT2LMHeadModel, GPT2Tokenizer



API_KEY = 'YOUR_OMDB_API_KEY'
BASE_URL = 'http://www.omdbapi.com/'



def fetch_movie(title, year=None):
    params = {
        'apikey': API_KEY,
        't': title
    }
    if year:
        params['y'] = year
    response = requests.get(BASE_URL, params=params)
    try:
        response.raise_for_status()  # Überprüft, ob der HTTP-Statuscode ein Fehler ist
        data = response.json()
        if 'imdbID' in data:
            return data
        else:
            print(f"Fehler beim Abrufen von Daten für {title} ({year}): {data.get('Error', 'Unbekannter Fehler')}")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP-Fehler beim Abrufen von Daten für {title} ({year}): {http_err}")
    except Exception as err:
        print(f"Ein Fehler ist aufgetreten beim Abrufen von Daten für {title} ({year}): {err}")
    return None


def load_movies_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_user_ratings(ratings, file_path):
    with open(file_path, 'w') as file:
        json.dump(ratings, file, indent=4)


def get_random_movie(movies):
    year = random.choice(list(movies.keys()))
    movie = random.choice(movies[year])
    return movie, year


def get_movie_recommendation(user_ratings):
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    prompt = (
        "Hier sind die Bewertungen der Nutzer:\n"
        f"{json.dumps(user_ratings, indent=4)}\n"
        "Basierend auf diesen Bewertungen, welchen Film würden Sie empfehlen und warum?"
    )
    inputs = tokenizer.encode(prompt, return_tensors="pt", truncation=True, max_length=1024)  # Eingabelänge begrenzen
    outputs = model.generate(inputs, max_new_tokens=300, num_return_sequences=1, no_repeat_ngram_size=2)  # max_new_tokens erhöhen und Wiederholungen vermeiden

    recommendation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return recommendation.strip()




def main():
    movies = load_movies_from_json('TinderForFilms/MovieDB/5years.json')
    user_ratings = []

    while True:
        movie, year = get_random_movie(movies)
        print(f"Title: {movie['Title']}\nDirector: {movie['Director']}\nSynopsis: {movie['Synopsis']}\nYear: {year}")
        
        rating = input("Bewerten Sie den Film mit 'Like', 'Dislike', 'Neutral' oder geben Sie 'Done' ein, um zu beenden: ").strip().lower()
        if rating == 'done':
            break
        elif rating in ['like', 'dislike', 'neutral']:
            user_ratings.append({
                'Title': movie['Title'],
                'Year': year,
                'Rating': rating
            })
        else:
            print("Ungültige Eingabe. Bitte bewerten Sie den Film mit 'Like', 'Dislike', 'Neutral' oder geben Sie 'Done' ein, um zu beenden.")

    save_user_ratings(user_ratings, 'TinderForFilms/user_ratings.json')
    print("Ihre Bewertungen wurden gespeichert.")

    recommendation = get_movie_recommendation(user_ratings)
    print(f"Empfohlener Film: {recommendation}")



if __name__ == "__main__":
    main()