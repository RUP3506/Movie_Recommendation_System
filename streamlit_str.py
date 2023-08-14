import streamlit as st 
import pandas as pd
import numpy as np 
import streamlit as st 
import pandas as pd 
import pickle 
print("success")

df = pickle.load(open("movies_dict.pkl",'rb')) 
similarity = pickle.load(open("similarity.pkl",'rb'))
movies = pd.DataFrame(df) 


# now lets create webpage using the streamlit
st.title("Movie Recommender System") 



# recommend based on content
selected_title = st.selectbox(
    "Please , Choose a movie",
    movies['title'].values
)

movie_index = movies[movies['title']==selected_title].index[0]
similar_movies = sorted(list(enumerate(similarity[movie_index])),key=lambda x:x[1],reverse=True)[1:6]

if st.button("recommend"):
    for i in similar_movies:
        st.write(movies['title'][i[0]])