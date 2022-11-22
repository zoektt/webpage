import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=':tada:', layout='wide')


# ------LOAD local CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style?", unsafe_allow_html=True)
local_css("style/style.css")


# -----LOAD ASSETS------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_BgGAtj.json")
img_contact_form = Image.open("images/102642-contact.gif")
img_lottie_animation = Image.open("images/negotiation-skills-in-a-project-1130x573.png")

# ------ HEADER SECTION ------
with st.container():
    st.subheader("Hi, I am Tan Tan :wave:")
    st.title("A Data Scientist with Software Development Passion")
    st.write("I am interested in coding, mechanical keyboards and comedies")
    st.write("[Learn More >](https//pythonandvba.com)") #or use the link from other workss

# -------- WHAT I DO -----------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube / Github I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - learning how to train machine learning models
            - want to learn Data Science to perform meaningful and impactful analysis
            - are trying to have fun!
            
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you would find out the latest updates :wink:
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

# ------ADD PROJECT SECTION ------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Web application Development using Django Framework - Quora + Legal Blogs + Live Chat")
        st.write(
            """
            This project was created with 2 other CMU CS classmates in our web app development class
            The functions include the basic authentication, user profile page (lawyer and legal advice seekers are different),
            blogging and commenting functions, post ratings, and live chat.
            The design was pretty basic (Bootstrap) but we spent most of the time on building the backend and functionalities
            """
        )
        st.markdown("[Watch Demo Video...](https://youtu.be/TXSOitGoINE")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        st.image(img_contact_form)
    with text_column:
        st.subheader("Student Facial Recognition checkin system / Flask Data Visualization Project")
        st.write(
            """
            This project was created with 3 other CMU students in our java class
            The functions include the frontend created JavaFX, the connection to JDBC backend and facial recognition module using OpenCV
            """
        )
        st.markdown("[Watch Demo Video...](https://youtu.be/TXSOitGoINE")

# ----- CONTACT FORM ------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    #Documentation: https: //formsubmit.co/ !!! Change email address !!!
    contact_form = """
    <form action="https://formsubmit.co/zoecontactme@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()