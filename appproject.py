import streamlit as st
import requests
import pycountry
from api import apiKEY

st.title('news app')
st.radio('news category chsen:',('technology', 'poliutics', 'sports''business'))
col1, col2= st.columns(2)    ,
with col1:
    user= st.text_input('enter country')
with col2:
    category= st.radio('news category chsen:',('technology', 'poliutics', 'sports''business'))
    btn= st.button('enter')
if btn:
    country= pycountry.countries.get(name=user).alpha_2
    url= f"https:./newsapi.org/v2/top-headlines?country={country}&apiKey={apiKey}"
    r= requests.get(url)
    r= r.json()
    articles= r['articles']
    for article in articles:
        st.header(article['title'])
        st.markdown(f"<span style='background-color:blue;padding:10px;border-radius:'> Published at: {article['publishedAt']}</span>", unsafe_allow_html=True)
        #st.write(article['publishedAt'])
        if article['author']:
            st.write(article['author'])
        st.write(article['source']['name'])
        st.write(article['description'])
        st.image(article['urlToImage'])

