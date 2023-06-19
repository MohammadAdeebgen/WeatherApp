import streamlit as st
import pickle
import requests

st.header('Weather webapp')
cities = pickle.load(open("city_list.pkl","rb"))
city = st.selectbox('Enter city name',options=cities)

with open("Style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

def gettemp(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=18500828a455681bfd7e5fee3cab4a0c&units=metric'
    res = requests.get(url)
    res = res.json()
    weather = res['weather'][0]['main']
    city = res['name']
    description = res['weather'][0]['description']
    temp_min = res['main']['temp_min']
    temp_max = res['main']['temp_max']
    humidity = res['main']['humidity']
    country = res['sys']['country']
    return [weather,city,description,temp_min,temp_max,humidity,country]

if st.button('Check Weather'):
    col1,col2,col3,col4,col5,col6= st.columns(6)
    weather,city,description,temp_min,temp_max,humidity,country = gettemp(city)
    with col1:
        st.write('City')
        st.write(city)
    with col2:
        st.write('Weather')
        st.write(weather)
    with col3:
        st.write('Description')
        st.write(description)
    with col4:
        st.write('Temp_Min')
        st.write(temp_min,'°C')
    with col5:
        st.write('Temp_Max')
        st.write(temp_max,'°C')
    with col6:
        st.write('Humidity')
        st.write(humidity,'%')




