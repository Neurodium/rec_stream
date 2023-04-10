import streamlit as st
import requests
import os


url = "https://p9recarticles.azurewebsites.net/api/httptrigger1"


st.write("Enter user ID:")
user_id = st.number_input(label="User ID", min_value=0, format='%d')
if st.button("Send"):
    params = {'user': user_id}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        st.write(f"Recommended articles for user {user_id}:")
        for art_pos, article in data['articles'].items():
            st.write(f"Article {art_pos}: {article}")
    except:
        st.write(f"Incorrect User ID")




