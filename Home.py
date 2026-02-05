import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon = '🏠'
)

# Main Title
st.title("🏠 Real Estate Insights Platform")
st.subheader("Explore, Analyze, Predict, and Recommend — all in one place.")


# Introduction Section
# st.markdown("""
# ---
# """)
st.subheader("""
1. This platform helps you analyze housing data, predict property prices, and recommend nearby apartments based on your preferences.
""")
st.subheader("2. Use the **navigation panel on the left** to switch between different modules.")
st.markdown("""
 --- 
 """)

# App Overview / Modules Section
st.header("📊 App Overview / Modules")

st.markdown("""
#### 1️⃣ Price Prediction  
Predict property prices based on features such as **area**, **location**, and **number of BedRooms**.  
Experiment with different values and instantly see the **new predicted price changes**.

#### 2️⃣ Analysis Dashboard  
Explore the Data with **interactive graphs and charts**.  
Visualize **price distributions**, **Common Amenities**, and **location patterns** to uncover hidden insights.

#### 3️⃣ Recommendations Module  
Find **similar or nearby apartments** using **Society data**.  
Discover listings close to your chosen property.

---
""")