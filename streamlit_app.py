import streamlit as slit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

slit.title('My Parents New Healthy Diner')

##added new lines
slit.header('Breakfast Favorites')
slit.text('🥣Omega 3 & Blueberry Oatmeal')
slit.text('🥗Kale, Spinach & Rocket Smoothie')
slit.text('🐔Hard-Boiled Free-Range Egg')
slit.text('🥑🍞Avocado Toast')

##add new header
slit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

##import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = slit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
# slit.dataframe(my_fruit_list)

slit.dataframe(fruits_to_show)

#Create a repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    #slit.text(fruityvice_response.json())  #removing this line to remove the raw JSON
    # take the json version of the response and normalize it
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized
  
#New Section to display fruitvice api response
slit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = slit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    slit.error("Please Select a fruit to get information.")
  else:
    back_from_function = get_fruitvice_data(fruit_choice)
    # output it in the screen as a table
    slit.dataframe(back_from_function)

except URLError as e:
    slit.error()
    
#don't run anything past here while we troubleshoot
slit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**slit.secrets["snowflake"])
my_cur = my_cnx.cursor()
##my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
slit.header("The fruit load list contains:")
slit.dataframe(my_data_rows)

#Allow end user to add a fruit to the list
add_my_fruit = slit.text_input('What fruit would you like to add?')
slit.write('Thanks for adding ',add_my_fruit)

my_cur.execute("Insert into PC_RIVERY_DB.public.fruit_load_list values ('from streamlit')")
