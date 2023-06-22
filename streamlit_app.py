
import streamlit
import pandas

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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), list(my_fruit_list)[0:1])


# Display the table on the page.

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


