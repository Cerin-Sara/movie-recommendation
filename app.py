import streamlit as st
import pickle
import requests

#key=f0b2a26975c2ebc77425556a8a56f4f6
#req=https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
movies=pickle.load(open('movie_last.pkl','rb'))
similarity = pickle.load(open('similarity_last.pkl','rb'))

st.title("Movie Forum")
st.header('Recommendation for you.')
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f0b2a26975c2ebc77425556a8a56f4f6&language=en-US'
    data = requests.get(url)
    data = data.json()
    poster_path= data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "",
    movie_list
)
st.write('Movie from your watchlist:', selected_movie)

if st.button('RECOMMEND'):
    recommended_movie_names,recommended_movie_poster=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_poster[0], use_column_width=True)

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_poster[1], use_column_width=True)

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_poster[2], use_column_width=True)

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_poster[3], use_column_width=True)

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_poster[4], use_column_width=True)


if st.button('HOME'):
     st.write('')
else:
     st.write('')