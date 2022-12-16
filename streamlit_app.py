import streamlit as slit

slit.title('My Parents New Healthy Diner')

##added new lines
slit.header('Breakfast Favorites')
slit.text('🥣Omega 3 & Blueberry Oatmeal')
slit.text('🥗Kale, Spinach & Rocket Smoothie')
slit.text('🐔Hard-Boiled Free-Range Egg')
slit.text('🥑🍞Aavacado Toast')

##add new header
slit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

##importing panda
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
slit.dataframe(my_fruit_list)
