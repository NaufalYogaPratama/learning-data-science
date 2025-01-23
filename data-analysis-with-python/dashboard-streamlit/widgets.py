import streamlit as st
import datetime
import pandas as pd

# Input Widgets
# Text input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

# Text-area
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# Number Input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

# Date Input
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

# File Uplaoder
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Camera Input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)



# Button Widgets
# Button
if st.button('Say hello'):
    st.write('Hello there')

# Checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('Welcome to MyApp')

# Radio Button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

# Select Box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Multiselect
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)