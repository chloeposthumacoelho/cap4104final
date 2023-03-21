import streamlit as st
import requests
import pycountry
from api import apiKEY
apiKey='0a54baab3c394337aa46d1ea286cfb24'

st.title('news app final CAP 4104 ')
st.radio('news category chosen:',('technology', 'poliutics', 'sports''business'))
col1, col2= st.columns(2)    ,
with col1:
    user= st.text_input('enter country')
with col2:
    category= st.radio('news category chsen:',('technology', 'poliutics', 'sports''business'))
    btn= st.button('enter')
if btn:
    #asking user for country input, ex us for us news and turns it into alpha_2 through user method
    country= pycountry.countries.get(name=user).alpha_2
    url= f"https:./newsapi.org/v2/top-headlines?country=us&apiKey=0a54baab3c394337aa46d1ea286cfb24"
   
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

