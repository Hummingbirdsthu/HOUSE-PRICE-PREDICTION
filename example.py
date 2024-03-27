import streamlit as st 
st.title("This is the app title")
st.markdown("this is a markdown")
st.header("this is a header")
st.subheader("this is a subheader")
st.caption("this is a caption")
st.code("x = 2021")
st.latex(r''' a + ar^1 + ar^2 + ar^3 ''')

#-----------------------------------------------------------

st.header("Display an image, video or audio file with Streamlit")

st.subheader("Image: ")
st.image("/Users/landiepnguyen/Desktop/file/BL/Passion/pic1.jpg")

st.subheader("Audio: ")
st.audio("/Users/landiepnguyen/Desktop/Toeic/Listening/part 1/part1.mp3")

st.subheader("Video: ")
st.video("/Users/landiepnguyen/Desktop/SW/Speaking TEST/1. TOEIC SPEAKING Actual test 4.mp4")

#-----------------------------------------------------------

st.header("Input widgets")

st.subheader("Don't text")
st.checkbox("yes")
st.button("Click")
st.radio("Pick your gender", ["Male", "Female"])
st.selectbox("Pick your gender: ", ["Male", "Female"])
st.multiselect("Choose a planet", ["Jupiter", "Mars", "Nepture"])
st.select_slider("Pick a mark", ["Bad", "Good", "Excellent"])
st.slider("Pick a number", 0, 100)

st.subheader("Input")
st.number_input("Pick a number", 0, 50)
st.text_input("Email adress: ")
st.date_input("Travelling date: ")
st.time_input("School time")
st.text_area("Description", height=2, max_chars=200)
st.file_uploader("Upload a photo")
st.color_picker("Choose your favorite color")

#-----------------------------------------------------------
import time 
st.header("Display progress and status with Streamlit")
st.balloons()
st.subheader("Progress bar")
st.progress(30)
st.subheader("Wait the execution")
with st.spinner("Wait for it..."):
    time.sleep(2)

st.subheader("Status")
st.success("You did it!")
st.error("Error")
st.warning("Warning")
st.info("It's easy to built a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

#-----------------------------------------------------------

# st.header("Sidebar and container")

# st.subheader("Sidebar")
# st.sidebar.title("This is written inside the sidebar")
# st.sidebar.button("Click")
# st.sidebar.radio("Pick your gender", ["Male", "Female"])

# container = st.container()
# container.write("This is written inside the container")
# st.write("This is written outside the container")

#-----------------------------------------------------------

st.header("Display graphs with Streamlit")

import matplotlib.pyplot as plt  
import numpy as np 

rand = np.random.normal(1,2,20)
fig, ax = plt.subplots()
ax.hist(rand, bins = 10)
st.pyplot(fig)

import pandas as pd   
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns = ["x", "y"]
)
st.subheader("line chart")
st.line_chart(df)

st.subheader("bar chart")
st.bar_chart(df)

st.subheader("area chart")
st.area_chart(df)

import altair as alt
st.subheader("altair chart")
df = pd.DataFrame(
    np.random.randn(500, 3),
    columns = ['x', 'y', 'z']
)
c = alt.Chart(df).mark_circle().encode(
    x = 'x',
    y = 'y',
    size = 'z',
    color = 'z',
    tooltip = ['x', 'y', 'z']
)
st.altair_chart(c, use_container_width = True)

st.subheader("graphviz chart")
# import graphviz as graphviz
st.graphviz_chart('''
    digraph {
                  Big_shark -> Tuna
                  Tuna -> Mackerel
                  Mackerel -> Small_fishes
                  Small_fishes -> Shimp
    }
''')

st.header("Display maps with streamlit")
df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)
st.map(df)