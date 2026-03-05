import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon = '🏠'
)
st.markdown("""
<h1 style='text-align: center;'>🏠 Real Estate Insights Platform</h1>

<p style='text-align:center; font-size:18px; color:gray;'>
Explore, Analyze, Predict, and Recommend — all in one place
</p>

<hr style="margin-top:20px;margin-bottom:30px;">

<p style='font-size:17px;'>
This platform helps you <b>analyze housing data</b>, <b>predict property prices</b>, 
and <b>recommend nearby apartments</b> based on your preferences.
</p>

<p style='font-size:17px;'>
Use the <b>navigation panel on the left</b> to switch between different modules.
</p>

<br>

<h2>📊 App Overview</h2>

<h3>1️⃣ Price Prediction</h3>
<p style='font-size:16px;'>
Predict property prices based on features such as <b>area</b>, <b>location</b>, 
and <b>number of bedrooms</b>.  
Experiment with different values and instantly see the updated predicted price.
</p>

<h3>2️⃣ Analysis Dashboard</h3>
<p style='font-size:16px;'>
Explore the dataset using interactive graphs and charts.  
Visualize price distributions, common amenities, and location patterns to uncover insights.
</p>

<h3>3️⃣ Recommendations Module</h3>
<p style='font-size:16px;'>
Find similar or nearby apartments using <b>Society data</b>.  
Discover listings close to your chosen property.
</p>
""", unsafe_allow_html=True)
