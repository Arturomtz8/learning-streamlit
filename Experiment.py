import folium
from streamlit_folium import st_folium

import streamlit as st

st.markdown("# Third party integrations page 🎈")
st.sidebar.markdown("# Third party integration 🎈")

m = folium.Map(location=[19.43517641143954, -99.14116029436873], zoom_start=15)
folium.Marker(
    [19.43517641143954, -99.14116029436873],
    popup="Bellas Artes",
    tooltip="Bellas Artes",
).add_to(m)
st_data = st_folium(m, width=725)
