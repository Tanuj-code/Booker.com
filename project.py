import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as stc
import time
st.set_page_config(page_title="Booker: Get your book!",
    page_icon="books",
    layout="wide")
script="""const btc = document.getElementById('act');
btc.addEventListener("click", myFunction);
function myFunction() {
  if(btc.style.backgroundColor == "orange"){
  btc.style.backgroundColor = "black";
  btc.style.color="white";
  document.getElementById('nav').style.backgroundColor="orange";
  }
  else{
  btc.style.backgroundColor ="orange";
  btc.style.color="black";
  document.getElementById('nav').style.backgroundColor="black";
  }
}"""
style="""
#nav{
  background-color: black;
  overflow: hidden;
  
}
#act {
  float: left;
  color: black;
  text-align: center;
  padding: 14px 16px; 
  background-color: #FF8C00;
  font-size: 17px;
}
#act:hover {
  background-color: orange ;
  color: black;

}
#extra{
  float: left;
  color: white;
  text-align: center;
  padding: 14px 16px; 
  
  font-size: 17px;
}
"""

st.markdown(f"""

<style>{style}
</style>
<script>
{script}
</script>
<div id="nav" class="topnav">
  <div id="act" class="active">BOOKER</div> 
  <div id="extra">Get your desired books here</div>
  
</div>

""", unsafe_allow_html=True)
book=st.text_input('',placeholder='Search books by name, author or genre')
btn=st.button('Search')
st.markdown('''<style>header {visibility: hidden;}
footer {visibility: hidden;}</style>''', unsafe_allow_html=True)

stt=st.empty()
ct=1
def func(torec, ct,  response):
         dic={}
         ct=ct+1
         with stt.container():
          
          
          col1, col2= st.columns([1, 1])
          dic[torec['volumeInfo']['title']]=1
          with col1:
                      
                      #st.write('Title:')
                      if('title' in torec['volumeInfo']):
                        st.markdown(''' <b>Title:</b>''', unsafe_allow_html=True)
                        st.write(torec['volumeInfo']['title'])
                      #st.write("Authors:")
                      if ('subtitle' in torec['volumeInfo']):
                        st.markdown(''' <b>Sub-Title:</b>''', unsafe_allow_html=True)
                        st.markdown(f''' <i>{torec['volumeInfo']['subtitle']}</i>''', unsafe_allow_html=True)
                      if('authors' in torec['volumeInfo']):
                        st.markdown(''' <b>Authors:</b>''', unsafe_allow_html=True)
                        for j in torec['volumeInfo']['authors']:
                            st.markdown(f''' <i>{j}</i>''', unsafe_allow_html=True)
                            #st.write(j)
                      #st.write('Country:')
                      if('country' in torec['saleInfo']):
                        st.markdown(''' <b>Country:</b>''', unsafe_allow_html=True)
                        st.write(torec['saleInfo']['country'])
                      
                      if('pageCount' in torec['volumeInfo']):
                        st.markdown(''' <b>Page Count:</b>''', unsafe_allow_html=True)
                        st.write(torec['volumeInfo']['pageCount'])
                      
                      #st.write('Buy Link:')
                      if ('buyLink' in torec['saleInfo']):
                        st.markdown(''' <b>Buy:</b>''', unsafe_allow_html=True)                    
                        st.write(torec['saleInfo']['buyLink'])
                      
                      
                      if('downloadLink' in torec['accessInfo']['epub']):
                           st.markdown(''' <b>Download:</b>''', unsafe_allow_html=True)
                           st.write(torec['accessInfo']['epub']['downloadLink'])
                      elif('downloadLink' in torec['accessInfo']['pdf']):
                           st.markdown(''' <b>Download:</b>''', unsafe_allow_html=True)
                           st.write(torec['accessInfo']['pdf']['downloadLink'])
                      
                      
          with col2:
                      if  ('thumbnail' in torec['volumeInfo']['imageLinks']):
                        st.markdown(f'''
                        <img src="{torec['volumeInfo']['imageLinks']['thumbnail']}" style="border: 5px solid black"> 
                        ''', unsafe_allow_html=True)
                      
          
          st.success("Recommended Books :")
          
          l=0
          for i in response:
                  
                  if('volumeInfo' not in i or 'title' not in i['volumeInfo'] or 'authors' not in i['volumeInfo'] or 'imageLinks' not in i['volumeInfo'] or len(i['volumeInfo']['title']) == 0 or  len(i['volumeInfo']['authors']) == 0 or len(i['volumeInfo']['imageLinks']['thumbnail'])==0 or i['volumeInfo']['title'] in dic):
                      continue
                  else:
                    dic[i['volumeInfo']['title']]=1
                    co1, co2= st.columns([1, 1])
                    with co1:
                        st.markdown(''' <b>Title:</b>''', unsafe_allow_html=True)
                        st.write(i['volumeInfo']['title'])
                              
                        
                        st.markdown(''' <b>Authors:</b>''', unsafe_allow_html=True)
                        for j in i['volumeInfo']['authors']:
                            
                            st.markdown(f''' <i>{j}</i>''', unsafe_allow_html=True)
                    
                    with co2:
                        st.markdown(f'''
                        <img src="{i['volumeInfo']['imageLinks']['thumbnail']}" style="border: 5px solid black"> 
                        ''', unsafe_allow_html=True)
                    ct=ct+1
                    a=st.button('Visit', key=ct)
                    ct=ct+1
                    st.markdown("---")
                    if a:
                        
                        
                        stt.empty()
                        dic.clear()
                        func(i, ct, response)
                      
                      
        
if btn or len(book) > 0:
    if btn and len(book)==0:
         wr=st.error("Please enter a valid book")
         time.sleep(2)
         wr.empty()
    else:
      stt.empty()     
      response=requests.get('https://www.googleapis.com/books/v1/volumes?q='+book+'&key=AIzaSyDlYX7U3j0SmlO49KNqRT2DKpoaY1VqwGQ&maxResults=40')
      response=response.json()['items']
      
    
      dic={}
      
      
      with stt.container():
                             
                for i in response:

                  if('volumeInfo' not in i or 'title' not in i['volumeInfo'] or 'authors' not in i['volumeInfo'] or 'imageLinks' not in i['volumeInfo'] or len(i['volumeInfo']['title']) == 0 or  len(i['volumeInfo']['authors']) == 0 or len(i['volumeInfo']['imageLinks']['thumbnail'])==0 or i['volumeInfo']['title'] in dic):
                      continue
                  col1, col2= st.columns([1, 1])
                  dic[i['volumeInfo']['title']]=1
                  with col1:
                      st.markdown(''' <b>Title:</b>''', unsafe_allow_html=True)
                      st.write(i['volumeInfo']['title'])
                      st.markdown(''' <b>Authors:</b>''', unsafe_allow_html=True)
                      for j in i['volumeInfo']['authors']:
                            st.markdown(f''' <i>{j}</i>''', unsafe_allow_html=True)
                      #st.write(i['volumeInfo']['authors'][0])
                              
                      
                      
                  with col2:
                      if  ('thumbnail' in i['volumeInfo']['imageLinks']):
                        st.markdown(f'''
                        <img src="{i['volumeInfo']['imageLinks']['thumbnail']}" style="border: 5px solid black"> 
                        ''', unsafe_allow_html=True)
                  ct=ct+1
                  a=st.button('Visit', key=ct)
                  ct=ct+1
                  
                  
                  st.markdown("---")
                  if a:
                      
                      stt.empty()
                      
                      func(i, ct, response)
                      
                
              
              
        
        
        
            