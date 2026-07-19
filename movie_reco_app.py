
import pandas as pd
import pickle
import streamlit as st
import requests


st.set_page_config(
    page_title="Movie AI Recommendation",
    layout="wide"
)

TMDB_API_KEY = st.secrets["TMDB_API_KEY"]

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"

    data = requests.get(url).json()

    poster = "https://image.tmdb.org/t/p/w500" + data["poster_path"]

    link = f"https://www.themoviedb.org/movie/{movie_id}"

    return poster, link


movies = pickle.load(open("movies.pkl", "rb"))
top_similarity = pickle.load(open("top_similarity.pkl","rb"))

movies = pd.DataFrame(movies)

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    movie_list = top_similarity[movie_index][:6]

    recommended_movies = []
    recommended_posters = []
    recommended_links = []

    for index, score in movie_list:

        movie_data = movies.iloc[index]

        movie_id = movie_data.movie_id

        poster, link = fetch_movie_details(movie_id)

        recommended_movies.append(movie_data.title)
        recommended_posters.append(poster)
        recommended_links.append(link)
    
    return recommended_movies, recommended_posters, recommended_links

st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select a Movie", movies["title"].values)

if st.button("Recommend movies matching to my interest"):

    names, posters, links = recommend(selected_movie)

    for i in range(len(names)):

        if i % 3 == 0:
            cols = st.columns(3)

        with cols[i % 3]:

            st.image(posters[i], width=300)

            st.write(f"**{names[i]}**")

            st.markdown(f"[View Details]({links[i]})")