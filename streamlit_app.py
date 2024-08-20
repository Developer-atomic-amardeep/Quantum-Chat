import streamlit as st
import yaml
from yaml.loader import SafeLoader
from streamlit_authenticator import Authenticate


with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login(
    fields=['username', 'password'])

if authentication_status == False:
    st.error('Username/password is incorrect')

if authentication_status == None:
    st.warning('Please enter your username and password')

if authentication_status == True:

# --page-setup--

    Query_Engine_page = st.Page(
        page="views/Query-Engine.py",
        title=" Query-Engine",
        icon="💬",
        default=True
    )

    Settings_page = st.Page(
        page="views/Settings.py",
        title="Settings",
        icon="⚙"
    )

    Upload_document_page = st.Page(
        page="views/Upload-Document.py",
        title="Upload-Document",
        icon="📤"
    )

    # --------Navigation-Setup------------

    pg = st.navigation(
        {
            "Chat" : [Query_Engine_page],
            "Configurations" : [Settings_page,Upload_document_page]
        }
    )

    # ---------Logo-&-Sidebar-text---------

    st.logo("Assets/logo-2.png")
    st.sidebar.text("Made by amardeep yadav 🔥")

    # ---------run-pages----------

    pg.run()

