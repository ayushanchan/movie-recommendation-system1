import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    mi = movies[movies['title'] == movie].index[0]
    distances = similarity[mi]
    ml = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in ml:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

md = pickle.load(open('md.pkl', 'rb'))
movies = pd.DataFrame(md)
similarity = pickle.load(open('sim.pkl', 'rb'))

st.title('binge it off (ayush)')

selected_movie_name = st.selectbox(
    'Type the movie you like:',
    movies['title'].values
)

if st.button('Check Our Recommendations'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

