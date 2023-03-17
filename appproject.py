import streamlit as st
import requests
base_url= "https://jobs.github.com/positions.json?description=python&location=miami"
def get_data(url):
    resp= requests.get(url)
    return resp.json()
JOB_HTML_TEMPLATE= """
<div>
<h4>{}</h4>
<h4>{}</h4>
<h4>{}</h4>
<h4>{}</h4>
</div>
"""""
def main():
    menu ["Home", "About"]
    choice = st.sidebar.selectbox("Menu",  menu)
    st.title("Devdeeds- search jobs")
    if choice== "Home":
        st.subheader("home")
        with st.form(key='searchform'):
            nav1, nav2, nav2= st.beta_columns([3,2,1])
            with nav1:
                search_term =st.text_input("search")
        with nav2:
            location = st.text_input("location")
with nav3:
    st.text("search")
    submit_search = st.form_submit_button()
st.success("search {} in {}" .format(search_term, location))
col1, col2 = st.beta_columns([2,1])
with col1:
    if submit_search:
        search_url = base_url.format(search_term, location)
        data= get_data(search_url)
        num_of_results= len(data)
        st.subheader("showing {} jobs".format(num_of_results))
        st.write(data)
"created at : Fri apr 30 15:o3:35 UTC 2021"
"company: Inficon"
"company_url : https://www.click2apply.net/b7Loy6uYowklhbWOHe18N"
"location: East Syracuse, New york 13057"
"title: Senior Software Engineer"
"description"
for i in data:
    job_title== i['title']
    job_location == i['location']
    company = i['company']
    company_url = i['company_url']
    job_post_date = i['created at']
    job_desc = i['description']
    job_howtoapply = i['how to']
    st.markdown(JOB_HTML_TEMPLATE.format(job_title, company, job_location,job_post_date),
    unsafe_allow_html=True)
                #st.write(job_title)
  with st.beta_expander("description"):
    stc.html(JOB_DES_HTML_TEMPLATE.format(job_desc),scrolling=True)
        with st.beta_expander("how apply"):
    stc.html(JOB_DES_HTML_TEMPLATE.format(job_howtoapply,scrolling=True)
             with col2:
        with st.form(key='email_form'):
            st.write("be first to get job info")
            email= st.text_input("Email")
    submit email= st.form_submit_button(label='sUBSCRIBE')
if submit_email:
st.success("message sent to {}".format(email))






