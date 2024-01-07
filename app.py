import streamlit as st
import pickle
import numpy as np
import difflib
import requests

@st.cache_resource
def load_model(model_name):
    loaded_model = pickle.load(open(model_name,'rb'))
    return loaded_model

@st.cache_data
def load_data(data_name):
    movies_data = pickle.load(open(data_name,'rb'))
    return movies_data

loaded_model = load_model('movies_recommendation_model.sav')
movies_data = load_data('movies_data.sav')

recommendations = []
posters = []
years = []


def movie_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key=ecbc365ff86d398b81a5b9d7f004fd02'
    data = requests.get(url)
    data = data.json()
    if "poster_path" in data:
        poster_path = data['poster_path']
        if poster_path != None:
            full_path = 'https://image.tmdb.org/t/p/w500'+poster_path
        else:
            full_path = 'https://media.discordapp.net/attachments/666640575767904256/1193587343307837551/livewhale_ed8ade68e3bea1a1dc55b272ed8a43e4_1649271413.png?ex=65ad41d6&is=659accd6&hm=2bbbee3bf87f108146bd95c0b7b06eff3733faaf222a65debfc4655fc34ca0ce&=&format=webp&quality=lossless'
    else:
        full_path = 'https://media.discordapp.net/attachments/666640575767904256/1193587343307837551/livewhale_ed8ade68e3bea1a1dc55b272ed8a43e4_1649271413.png?ex=65ad41d6&is=659accd6&hm=2bbbee3bf87f108146bd95c0b7b06eff3733faaf222a65debfc4655fc34ca0ce&=&format=webp&quality=lossless'
    return full_path


def movies_recommend(input_data):
    arr = []
    arr1 = []
    arr2 = []
    movie_name = input_data
    list_of_all_titles = movies_data['movie title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_close_match[0]
    id_of_the_movie = movies_data[movies_data['movie title'] == close_match]['id'].values[0]
    similarity_score = list(enumerate(loaded_model[id_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

    i = 1
    k = 1
    movies = ''
    for movie in sorted_similar_movies:
        if(k == 1):
            k+=1
            continue
        index = movie[0]
        title_from_index = movies_data[movies_data.id==index]['movie title'].values[0]
        id_from_index = movies_data[movies_data.id==index]['path'].values[0]
        year_from_index = movies_data[movies_data.id==index]['year'].values[0]
        if (i == 11):
            break
        arr.append(title_from_index)
        poster = movie_poster(id_from_index)
        arr1.append(poster)
        arr2.append(year_from_index)
        i+=1
    return arr,arr1,arr2




movies_list = movies_data['movie title'].values
st.title("Movie Recommendations Web App")
movie = st.selectbox('Select movie from dropdown',movies_list)


if st.button('Show Recommendations'):
    recommendations, posters, years = movies_recommend(movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(recommendations[0])
        release = "Release Date: "+str(years[0])
        st.text(release)
    with col2:
        st.image(posters[1])
        st.text(recommendations[1])
        release = "Release Date: "+str(years[1])
        st.text(release)
    with col3:
        st.image(posters[2])
        st.text(recommendations[2])
        release = "Release Date: "+str(years[2])
        st.text(release)
    with col4:
        st.image(posters[3])
        st.text(recommendations[3])
        release = "Release Date: "+str(years[3])
        st.text(release)
    with col5:
        st.image(posters[4])
        st.text(recommendations[4])
        release = "Release Date: "+str(years[4])
        st.text(release)
    with col1:
        st.image(posters[5])
        st.text(recommendations[5])
        release = "Release Date: "+str(years[5])
        st.text(release)
    with col2:
        st.image(posters[6])
        st.text(recommendations[6])
        release = "Release Date: "+str(years[6])
        st.text(release)
    with col3:
        st.image(posters[7])
        st.text(recommendations[7])
        release = "Release Date: "+str(years[7])
        st.text(release)
    with col4:
        st.image(posters[8])
        st.text(recommendations[8])
        release = "Release Date: "+str(years[8])
        st.text(release)
    with col5:
        st.image(posters[9])
        st.text(recommendations[9])
        release = "Release Date: "+str(years[9])
        st.text(release)
