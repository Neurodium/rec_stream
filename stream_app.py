import streamlit as st
import requests


url = "http://localhost:7071/api/HttpTrigger1"


st.write("Enter user ID:")
user_id = st.number_input(label="User ID")
if st.button("Send"):
    params = {'user': user_id}
    response = requests.get(url, params=params)
    data = response.json()
    st.write(f"Recommended articles for user {user_id}:")
    for art_pos, article in data['articles'].items():
        st.write(f"Article {art_pos}: {article}")




