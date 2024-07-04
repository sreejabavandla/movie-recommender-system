import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    api_key = 'ca7ec1ceafd833b0764ecd453c7092f2'
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
def recommend(movie):
    mov_ind = movies[movies['title'] == movie].index[0]
    dist = similarity[mov_ind]
    movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_posters = []
    recommendations_list = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster
        recommendations_list.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommendations_list, recommended_movies_posters
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movies Recommender System')

selected_movie = st.selectbox(
    "Select a Film",
    movies['title'].values)

if st.button("Recommend"):
    recommendation, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(recommendation[0])
        st.image(posters[0])

    with col2:
        st.header(recommendation[1])
        st.image(posters[1])

    with col3:
        st.header(recommendation[2])
        st.image(posters[2])

    with col4:
        st.header(recommendation[3])
        st.image(posters[3])

    with col5:
        st.header(recommendation[4])
        st.image(posters[4])



