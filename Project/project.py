import pandas as pd
import streamlit as st
import pickle
import numpy

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://pbs.twimg.com/media/E2egBX1XMAIqg2c.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 








user_sim_df = pickle.load(open('user_sim_df.sav','rb'))
most_sim_users = pickle.load(open('most_sim_users.sav','rb'))
books_pivot = pickle.load(open('books_pivot.sav','rb'))

user_id_unique = most_sim_users.unique()
user_id = sorted(user_id_unique)


def show_image(val):
    return '<a href="{}"><img src="{}" width=60></img></a>'.format(val, val)

def recommend_book_to(User_Id):
    if User_Id in list(user_sim_df):
        sim_user = list(user_sim_df.sort_values([User_Id],ascending=False).head(1).index)
        print("Similar User:",sim_user)
        
    else:
        return 'Invalid Entry'
    book = books_pivot[books_pivot['User_Id'] == sim_user[0]]                   
    top = pd.DataFrame(book.sort_values('Book_Rating',ascending=False).head(3),columns=books_pivot.columns,)
    return top[['ISBN','Title']].set_index('ISBN')



st.title('Model Deployment: Book Recommendation System:books:')
User_Id = st.selectbox(
    "Type or select a user from the dropdown",
    user_id
)
st.button('Enter')
st.success('Recommended Books are:')
st.write(recommend_book_to(User_Id))






