
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#fruityvice function to fetch data from API 
def get_fruityvice_data(this_fruit_choice):
	fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)

	#format the json data
	fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

	return fruityvice_normalized

#new section header
streamlit.header("Fruityvice Fruit Advice!")

#add error handling 
try:
	fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')

	#if no entry, then ask for one 
	if not fruit_choice:
		streamlit.error('Please select a fruit to get information.')

	#otherwise make the api call 
	else:
		fruityvice_response = get_fruityvice_data(fruit_choice)

		#write formatted data to the stream
		streamlit.dataframe(fruityvice_response)

#exit try with URLError
except URLError as e:
	streamlit.error()

#fruit load list section 
streamlit.header("This fruit load list contains:")

#function to get fruit load list 
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
		return my_cur.fetchall()

#add a button to make the call 
if streamlit.button('Get Fruit Load List'):

	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows =get_fruit_load_list()
	streamlit.dataframe(my_data_rows)

#function to insert fruit rows 
def insert_row_snowflake(new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into fruit_load_list values ('from streamlit')")
		return "Thanks for adding " + new_fruit 

#text box for user to input a new fruit they want	
add_my_fruit =  streamlit.text_input('What fruit would you like to add?','jackfruit')

#button to add fruits 
if streamlit.button('Add a Fruit to the List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	added_fruit = insert_row_snowflake(add_my_fruit)
	streamlit.text(added_fruit)

