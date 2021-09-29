import streamlit as st
import pickle
import pandas as pd
import requests



similarity = pickle.load(open('similarity.pkl','rb'))
songs_list = pickle.load(open('Song_recommender.pkl','rb'))
songs = pd.DataFrame(songs_list)

#st.table(songs)

#st.write(songs)
def recommend(song):
    movie_list=[]
    recommended_songs=[]
    song_index = songs[songs['Song-Name'] + " - from " + songs['Movie']== song].index[0]
    # print(song_index)
    distances = similarity[song_index]
    r_songs_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:15]

    #print(r_songs_list)
    for i in r_songs_list:
        if i[0] == song_index:
            continue
        movie_list.append(songs['Movie'].iloc[i[0]])
    
    #print(movie_list)
    for i in r_songs_list:
        if i[0] == song_index:
            continue
        recommended_songs.append(songs['Song-Name'].iloc[i[0]])
    #print(recommended_songs)

    return recommended_songs,movie_list

st.title('Songs recommender')

selected_song = st.selectbox(
    'Select any song-',
    songs['Song-Name'].values + ' - from ' + songs['Movie']
)


if st.button('Recommend'):
    #recommend(selected_song)
    recomendations,movies = recommend(selected_song)
    # print(recomendations)
    # print(movies)
    output = {'Recommended song':[recomendations[x] for x in range(10)],'From movie':[movies[y] for y in range(10)]}
    df = pd.DataFrame(output)
    df.index = [x for x in range(1, len(df.values)+1)]
    st.table(df)