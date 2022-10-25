import pandas as pd
import streamlit as st
from pickle import load

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/premium-photo/front-view-pile-books-with-copy-space_23-2148255858.jpg?w=2000");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 



st.title('Model Deployment: Book Recommendation System:books:')





user_sim_df = load(open('user_sim_df.sav','rb'))
data = load(open('data.sav','rb'))
user_id = st.number_input('user_id',min_value=0)
st.button('Enter')

def show_image(val):
    return '<a href="{}"><img src="{}" width=60></img></a>'.format(val, val)

def recommend_book_to(user_id):
    if user_id in list(user_sim_df):
        sim_user = list(user_sim_df.sort_values([user_id],ascending=False).head(1).index)
        print("Similar User:",sim_user)
        
    else:
        return 'Invalid Entry'
    book = data[data['User_Id'] == sim_user[0]]                   
    top = pd.DataFrame(book.sort_values('Book_Rating',ascending=False).head(3),columns=data.columns,)
    return top[['ISBN','Title']].set_index('ISBN')

st.success('Recommended Books are:')

st.markdown("""
<style>
.big-font {
    font-size:100px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">recommend_book_to(user_id)</p>', unsafe_allow_html=True)

st.write(recommend_book_to(user_id))
st.success('If you don’t like to read, you haven’t found the right book:book:')
