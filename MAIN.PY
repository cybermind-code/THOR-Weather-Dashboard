import streamlit as st
import pandas as pd

import requests

st.markdown(

    """
<style>

    .stApp {

        background-image: url("https://drive.google.com/file/d/1fSGmkH38wuCaBRb0zCj4ebKAfEboVOfX/view?usp=sharing");

        background-size: cover;

        background-position: center;

        background-repeat: no-repeat;

    }
</style>

    """,

    unsafe_allow_html=True

)
 

st.title("THOR")

location =  st.sidebar.menu_button("LOCATION", options=["DOHA", "TOKYO", "COLOMBO", "MONACO"])

colombo_df = pd.DataFrame({"latitude":[6.9355],"LON":[79.8487]})
doha_df = pd.DataFrame({"latitude":[25.2855],"LON":[51.531]})
monaco_df = pd.DataFrame({"latitude":[43.7372],"LON":[7.4215]})
tokyo_df = pd.DataFrame({"latitude":[35.6895],"LON":[139.6917]})

st.markdown(f''':rainbow[{location}]''')

resp_doha = requests.get("https://api.open-meteo.com/v1/forecast?latitude=25.2855&longitude=51.531&daily=sunrise,sunset,daylight_duration,sunshine_duration,rain_sum,precipitation_sum,moon_phase&hourly=temperature_2m,temperature_80m,temperature_120m,temperature_180m,rain,showers,snowfall,snow_depth&current=is_day,wind_direction_10m,wind_speed_10m,surface_pressure,precipitation,rain,showers,snowfall,apparent_temperature,temperature_2m,relative_humidity_2m&past_days=1")
resp_tokyo = requests.get("https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&daily=sunrise,sunset,daylight_duration,sunshine_duration,rain_sum,precipitation_sum,moon_phase&hourly=temperature_2m,temperature_80m,temperature_120m,temperature_180m,rain,showers,snowfall,snow_depth&current=is_day,wind_direction_10m,wind_speed_10m,surface_pressure,precipitation,rain,showers,snowfall,apparent_temperature,temperature_2m,relative_humidity_2m&past_days=1")
resp_colombo = requests.get("https://api.open-meteo.com/v1/forecast?latitude=6.9355&longitude=79.8487&daily=sunrise,sunset,daylight_duration,sunshine_duration,rain_sum,precipitation_sum,moon_phase&hourly=temperature_2m,temperature_80m,temperature_120m,temperature_180m,rain,showers,snowfall,snow_depth&current=is_day,wind_direction_10m,wind_speed_10m,surface_pressure,precipitation,rain,showers,snowfall,apparent_temperature,temperature_2m,relative_humidity_2m&past_days=1")
resp_monaco = requests.get("https://api.open-meteo.com/v1/forecast?latitude=43.7372&longitude=7.4215&daily=sunrise,sunset,daylight_duration,sunshine_duration,rain_sum,precipitation_sum,moon_phase&hourly=temperature_2m,temperature_80m,temperature_120m,temperature_180m,rain,showers,snowfall,snow_depth&current=is_day,wind_direction_10m,wind_speed_10m,surface_pressure,precipitation,rain,showers,snowfall,apparent_temperature,temperature_2m,relative_humidity_2m&past_days=1")

if location == "DOHA":
  st.map(doha_df,zoom=12)
  weather_data=resp_doha
elif location == "TOKYO":
  st.map(tokyo_df,zoom=10)
  weather_data=resp_tokyo
elif location == "COLOMBO":
  st.map(colombo_df,zoom=10)
  weather_data=resp_colombo
else:
  st.map(monaco_df,zoom=14)
  weather_data=resp_monaco     
  
data = weather_data.json()

if location == "TOKYO":
  if data["current"]["snowfall"] > 0.0:
      st.snow()
elif location == "MONACO":
  if data["current"]["snowfall"] > 0.0:
      st.snow()    

#st.metric(data["current"]["temperature_2m"])
col1, col2, col3 = st.columns(3)
col1.metric("Temperature",data["current"][ "temperature_2m"])
col2.metric("Velocity",data["current"]["wind_speed_10m"])
col3.metric("Humidity",data["current"]["relative_humidity_2m"])


# sundata = weather_data.json()
# row1 = st.columns(1)
# for col in row1:
#   tile = col.container(height=150)
#   tile.write(f"sunrise: {data["daily"]["sunrise"]}")
#   tile.write("sunset:")

tab1, tab2,tab3 = st.tabs(["sunrise","sunset","moon_phase"])

with tab1:
  st.header("sunrise")
  st.metric(" ",data["daily"]["sunrise"][1])
with tab2:
  st.header("sunset")
  st.metric(" ",data["daily"]["sunset"][1])   
with tab3:
  st.header("Moon phase")
  if data["daily"]["moon_phase"][1] == 0.0 or data["daily"]["moon_phase"][1] == 1.0:
    st.image("new-moon.png")
  elif data["daily"]["moon_phase"][1] > 0.0 and data["daily"]["moon_phase"][1] <= 0.25:
    st.image("first quater moon.png")
  elif data["daily"]["moon_phase"][1] > 0.25 and data["daily"]["moon_phase"][1] <= 0.5:
    st.image("full-moon.png")
  elif data["daily"]["moon_phase"][1] > 0.5 and  data["daily"]["moon_phase"][1] <= 0.875:
    st.image("last-quarter moon.png") 


 
  