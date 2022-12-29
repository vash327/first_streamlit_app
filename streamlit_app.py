import streamlit as slit

slit.title('My Parents New Healthy Diner')

##added new lines
slit.header('Breakfast Favorites')
slit.text('🥣Omega 3 & Blueberry Oatmeal')
slit.text('🥗Kale, Spinach & Rocket Smoothie')
slit.text('🐔Hard-Boiled Free-Range Egg')
slit.text('🥑🍞Avocado Toast')

##add new header
slit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

##importing panda
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = slit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
# slit.dataframe(my_fruit_list)

slit.dataframe(fruits_to_show)

#New Section to display fruitvice api response
slit.header("Fruityvice Fruit Advice!")
fruit_choice = slit.text_input('What fruit would you like information about?','Kiwi')
slit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#slit.text(fruityvice_response.json())  #removing this line ti remove the raw JSON

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
slit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**slit.secrets["snowflake"])
my_cur = my_cnx.cursor()
##my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
slit.header("The fruit load list contains:")
slit.dataframe(my_data_row)

