import streamlit as st
import plotly.express as px
from backend import get_data

st.title("WEATHER FORECAST APP FOR NEXT FEW DAYS")
place = st.text_input("Place :")
day = st.slider("No. of days -", min_value=1, max_value=5, help="Select number of forecast days ")
option = st.selectbox("Select the data to view ", ("Temperature", "Sky"))
st.subheader(f"{option} for next {day} days in {place} :")

if place:
    filtered_data = get_data(place, day)
    

    # filter data based on 'option'
    if option == 'Temperature':
        dates = [data['dt_txt'] for data in filtered_data]
        temps = [data['main']['temp'] for data in filtered_data]
        plot = px.line(x=dates, y=temps, labels={"x" : "Dates", "y" : "Temperature (C)"})
        st.plotly_chart(plot)
        
    if option == 'Sky':
        filtered_data = [data['weather'][0]['main'] for data in filtered_data]
        images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                  "Snow":"images/snow.png", "Rain":"images/rain.png"}
        image_representation = [images[weather] for weather in filtered_data]
        st.image(image_representation, width=100)

