#import streamlit as st
import requests
token='secret_jmaR7EWtxKMWPB8GvTnx1yjwbPzUUNW9QrGlouTLIX9'
databaseid='064c9fddf0f74cf786d0e16ff2ae608f'

headers= {

"Authorization": "bearer" + token,
"Content-Type": "application/json",
"Notion-Version": "2021-05-13"
}
#query from database


def queryDatabase(databaseID, headers):
    #readUrl= f"https://api.notion.com/v1/databases/(databaseID)/query"
    readUrl = f"https://api.notion.com/v1/databases/(databaseID)/query"
    res= requests.request("POST", readUrl, headers=headers)
    data= res.json()
    return res,data

#retrieving from database
def retrieveDatabase(databaseID, headers):
    readUrl= f"https://api.notion.com/v1/databases/{databaseID}"
    res= requests.request("GET", readUrl, headers=headers)
    data= res.json()
    return res , data
#
res, data= queryDatabase(databaseID, headers)
st.write(res.status_code)
st.json(data)
