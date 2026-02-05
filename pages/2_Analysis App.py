import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(page_title="Analytical App")

st.title("Analysis")

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))
wordcloud  = WordCloud(width = 800, height = 800,
                      background_color='white',
                      stopwords=set(['s']),
                      min_font_size= 10 ).generate(feature_text)



group_df = new_df.groupby('sector').mean(numeric_only=True)[['price','price_per_sqft','built_up_area','latitude','longitude']]

st.header("Sector Per Sqft Geomap")

fig = px.scatter_map(group_df, lat='latitude', lon='longitude', color = 'price_per_sqft',size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        zoom=10,
                        map_style = "open-street-map", width = 1200,
                        height=700, hover_name=group_df.index)

st.plotly_chart(fig, config = {"width" : 'stretch'})

st.header("Most Common Amenities")
# plt.figure(figsize=(8,8), facecolor=None)
fig, ax = plt.subplots(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad = 0)
st.pyplot(fig)

st.header("Area vs Price")

property_type = st.selectbox("Property Type",['flat', 'house'])
if property_type == 'flat':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, config = {"width" : 'stretch'})
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, config = {"width" : 'stretch'})


st.header("BHK Pie chart")

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,"Overall")

selected_sector = st.selectbox("Select Sector", sector_options)
if selected_sector == "Overall":
    fig2 = px.pie(new_df, names = 'bedRoom' )
    st.plotly_chart(fig2, config = {"width" : 'stretch'})
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names = 'bedRoom' )
    st.plotly_chart(fig2, config = {"width" : 'stretch'})

st.header("Most Common BHK Price Comparison")

fig3 = px.box(new_df[new_df['bedRoom'] <= 4],  x='bedRoom', y='price' )
st.plotly_chart(fig3,config = {"width" : 'stretch'})

st.header("Side by Side Distplot of Property Type")


fig4, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], kde=True, ax=axes[0])
axes[0].set_title('Flat price')

sns.histplot(new_df[new_df['property_type'] == 'house']['price'], kde=True, ax=axes[1])
axes[1].set_title('House price')

st.pyplot(fig4, width='stretch')

# -> dono ek saath
subset = new_df[new_df['property_type'].isin(['flat','house'])]

fig5, ax = plt.subplots(figsize=(12, 5))

# Overlaid histograms
sns.histplot(
    data=subset, x='price', hue='property_type',hue_order=['house','flat'],
    stat='density', common_norm=False, bins=40,
    alpha=0.3, element='step', ax=ax
)

# Overlaid KDE lines
sns.kdeplot(
    data=subset, x='price', hue='property_type',hue_order=['house','flat'],legend=False,
    ax=ax
)

ax.set_xlabel('price(Crores)')
ax.set_ylabel('Density')
st.pyplot(fig5, width='stretch')

















