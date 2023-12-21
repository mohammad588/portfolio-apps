import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.row import row
import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO
#

def read_excel_file(file_path):
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    return df

def display_app_details(app_data):
    expander = st.expander(app_data["Field2"])  # Adjust the column name
    with expander:
        col1, col2 = st.columns([1, 3])  # Adjust column ratios as needed

        col1.image(app_data["Image"], caption=app_data["Field2"], use_column_width=True)

        col2.text("Ranking:")
        col2.text(app_data['Field'])  # Adjust the column name
        col2.text("Parent Company:")
        col2.text(app_data['Field3'])  # Adjust the column name
        col2.text(app_data['Text'])  # Adjust the column name
        col2.text(f"${app_data['Text1']}")  # Adjust the column name
        col2.text(app_data['Field7'])  # Adjust the column name
        col2.text("Link to App:")
        col2.write(f"[{app_data['_Text']}]({app_data['_Link']})")  # Adjust the column name
        col2.text(app_data['Text2'])  # Adjust the column name
        col2.text("Sensor Tower Link:")
        col2.write(f"[Sensor Tower]({app_data['Field1']})")  # Adjust the column name
        col2.write(app_data['Text3'])  # Adjust the column name


def home():
    st.title("Revenue generated(billions) ")
    data = {'google play revenue(total)': [15,21.2,24.8,30.6,38.6,47.9,42.3],
            'google play revenue(gaming)': [14.3,17.4 ,21.6 ,25.2 ,31.9 ,37.3 ,31.3],
            'google play revenue(apps)': [ 0.7,3.8,3.2,5.4,6.7 ,10.6 , 11.5],
            'app store revenue(total)': [28.6, 38.5,46.6,58.4,72.3,85.1,86.8],
            'app store revenue(gaming)': [23.4, 29.6,32.3 ,38 ,47.6 ,52.3 ,50],
            'app store revenue(apps)': [4.8,8.9 ,14.3 ,20.4 ,24.7 ,	32.8 ,36.3 ],
           }
    years = list(range(2016, 2023))

    # Create a DataFrame with years as the index
    df = pd.DataFrame(data, index=years)

    # Convert DataFrame values to strings without commas
    df_str = df.applymap(lambda x: f"{x:.0f}")

    # Display the DataFrame without commas using st.table
    st.table(df_str)

    # Create a line chart
    st.line_chart(df)


    st.title("App Revenue Data")
    st.write(""""The mobile app industry has been active for over a decade now, generating billions of dollars in revenue for Apple, Google and thousands of mobile app developers.

While originally not perceived as necessary by Apple or Google, which did not add app stores to the first versions of iOS and Android, it has become a key revenue stream for both of them.

Even with less than 15 percent market share, iOS has led the way in revenue generation for app developers. This is partly due to iPhone being more popular in regions with high income, such as Japan and the United States, which also tend to spend more on apps.

In comparison, Google Play’s largest markets are India, South-east Asia and South America, which typically generate less revenue per user. Apple also operates in China, while the Google Play store is banned in the country. Several third-party Android app stores are available in China, and are estimated to generate over $8 billion in yearly revenue.

Both platforms have matured in the past few years, adding new ways for developers to increase revenue generation. These include a multi-purpose advertising platform, in-app purchasing systems and subscription services, all of which is covered in this app market analysis.

Subscription revenues have increased rapidly over the past few years, as every app tries to entice users to purchase a monthly or annual subscription to get premium services. Almost every app category now has leaders which sell subscriptions, whether that’s in music, video, health, fitness, wellness, language learning, or even food delivery.

In the past two years, there has been a collective effort by developers to reduce the percentage of revenue Apple and Google take for in-app purchases, alongside providing alternative ways for users to pay for subscriptions. Apple and Google have compromised slightly, adjusting the percentage take from 30 to 15 percent, but developers and anti-competitive departments are calling for further revisions.

What will be the next big money maker for this app economy? Some expect the metaverse, or some form of it, to be where app developers spend a lot of their resources in the next decade, perhaps trying to replicate the success of Roblox and Minecraft in building an in-game economy. """)
    st.write("by mashood")
# google play
def google_play():
    def top_free():
        # Assuming the Excel file for top free apps is named 'top_free.xlsx'
        file_path = 'full top free.xlsx'  # Adjust the file path

        apps_data = read_excel_file(file_path)
        for _, app_data in apps_data.iterrows():
            display_app_details(app_data)

    def top_paid():
        # Assuming the Excel file for top free apps is named 'top_free.xlsx'
        file_path = 'top paid full.xlsx'  # Adjust the file path

        apps_data = read_excel_file(file_path)
        for _, app_data in apps_data.iterrows():
            display_app_details(app_data)

    def top_grossing():
    # Assuming the Excel file for top free apps is named 'top_free.xlsx'
        file_path = 'top grossing full.xlsx'  # Adjust the file path

        apps_data = read_excel_file(file_path)
        for _, app_data in apps_data.iterrows():
            display_app_details(app_data)


    play_options = option_menu(
        menu_title=None,
        options=["top free", "top paid", "top grossing"],
        icons=["bag-fill", "currency-dollar", "suit-heart-fill"],
        default_index=0,
        orientation="horizontal")
    if play_options == "top free":
        top_free()
    elif play_options == "top paid":
        top_paid()
    elif play_options == "top grossing":
        top_grossing()
# app store
def app_store():


    def top_free1():
        file_path = 'top free 2.xlsx'  # Adjust the file path

        apps_data = read_excel_file(file_path)
        for _, app_data in apps_data.iterrows():
            display_app_details(app_data)


    def top_paid1():
        # Assuming the Excel file for top free apps is named 'top_free.xlsx'
        file_path = 'top paid 2.xlsx'  # Adjust the file path

        apps_data = read_excel_file(file_path)
        for _, app_data in apps_data.iterrows():
            display_app_details(app_data)


    def top_grossing1():
        # Assuming the Excel file for top free apps is named 'top_free.xlsx'
        file_path = 'top grossing 2.xlsx'  # Adjust the file path

        apps_data = read_excel_file(file_path)
        for _, app_data in apps_data.iterrows():
            display_app_details(app_data)

    app_options = option_menu(
        menu_title=None,
        options=["top free", "top paid", "top grossing"],
        icons=["bag-fill", "currency-dollar", "suit-heart-fill"],
        default_index=0,
        orientation="horizontal")

    if app_options == "top free":
        top_free1()
    elif app_options == "top paid":
        top_paid1()
    elif app_options == "top grossing":
        top_grossing1()
# Horizontal navigation bar 1
selected = option_menu(
    menu_title=None,
    options=["home", "google play", "app store"],
    icons=["house", "google", "apple"],
    default_index=0,
    orientation="horizontal")
if selected == "home":
    home()
elif selected == "google play":
    google_play()
elif selected == "app store":
    app_store()