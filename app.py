'''
Driver code of the app.
To run it you neet to install streamlit v.1.0 and run in the terminal
streamlit run app.py
Do not forget to set the current working directory where app.py is!
'''

import streamlit as st
from framework.multipage import MultiPage
import pages

# App layout settings
about_info = 'Investing real money using this app is highly discouraged.'
menu_items = {'About': about_info}

st.set_page_config(page_title='Stock Crawler',\
                    page_icon='📈',\
                    layout='wide',\
                    initial_sidebar_state='auto',\
                    menu_items=menu_items)

# Create an instance of the app 
app = MultiPage()
home = pages.home(title = 'Home')
checkStock = pages.checkStock(title = 'Get Stock Prices')
yoloData = pages.getAltData(title = 'Get Alternative Data')
trade = pages.trade(title = 'Yolo Trade')

# Add pages of your application here
app.add_page(home)
app.add_page(checkStock)
app.add_page(yoloData)
app.add_page(trade)

# The main app
app.run()
