
import streamlit
import pandas
import requests

#handle data steams here
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#title
streamlit.title("My Parents New Healthy Dinner")

#header 1: breakfast
streamlit.header("Breakfast Favorites")

#icons
icons = ['🥣', '🥗', '🐔', '🥑', '🍞']
#breakfast items
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free Range Egg")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#new section header
streamlit.header("Fruityvice Fruit Advice!")

#test input api 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())