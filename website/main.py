import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Virtual Herbal Garden", layout="wide")

st.title("🌱 Virtual Herbal Garden")
st.header("Explore the world of medicinal Plants from SAACHIN BABA")
st.markdown("Discover the **healing power** of nature as you explore plants used in traditional healing systems. "
            "Learn about their benefits, usage, and where to find them!")

# 🔧 Image loading with error handling
try:
    img = Image.open("background.jpg")
    st.image(img, caption='A glimpse of the Virtual Herbal Garden', use_container_width=True)
except FileNotFoundError:
    st.warning("⚠️ 'background.jpg' not found. Please make sure it's in the same folder as this script.")

st.sidebar.title("Explore by Category")
option = st.sidebar.selectbox("Choose a healing tradition", ["Ayurbeda", "Unani", "Siddha", "Homeopathy"])

def display_plants(category):
    if category == "Ayurbeda":
        plants = {
            'Plant Name': ['Tulsi', 'Yarsaganda', 'Brahmi'],
            'Scientific Name': ['Ocimum tenuiflorum', 'Withania somnifera', 'Bacopa monnieri'],
            'Medicinal Uses': ['Anti-inflammatory', 'Stress relief', 'Memory enhancement']
        }
    elif category == "Unani":
        plants = {
            'Plant Name': ['Trachyspermum ammi', 'Azadirachta indica', 'Lawsonia inermis'],
            'Scientific Name': ['Trachyspermum ammi', 'Azadirachta indica', 'Lawsonia inermis'],
            'Medicinal Uses': ['Digestive aid', 'Blood purifier', 'Cooling agent']
        }
    elif category == "Siddha":
        plants = {
            'Plant Name': ['Aloe vera', 'Neem', 'Thuthuvalai'],
            'Scientific Name': ['Aloe barbadensis', 'Azadirachta indica', 'Solanum trilobatum'],
            'Medicinal Uses': ['Skin care', 'Antibacterial', 'Respiratory health']
        }
    else:
        plants = {
            'Plant Name': ['Aloe vera', 'Neem', 'Thuthuvalai'],
            'Scientific Name': ['Aloe barbadensis', 'Azadirachta indica', 'Solanum trilobatum'],
            'Medicinal Uses': ['Skin care', 'Antibacterial', 'Respiratory health']
        }

    df = pd.DataFrame(plants)
    st.table(df)

display_plants(option)

# --- Search function added here ---
def search_plants(query, category):
    if category == "Ayurbeda":
        plants = {
            'Plant Name': ['Tulsi', 'Yarsaganda', 'Brahmi'],
            'Scientific Name': ['Ocimum tenuiflorum', 'Withania somnifera', 'Bacopa monnieri'],
            'Medicinal Uses': ['Anti-inflammatory', 'Stress relief', 'Memory enhancement']
        }
    elif category == "Unani":
        plants = {
            'Plant Name': ['Trachyspermum ammi', 'Azadirachta indica', 'Lawsonia inermis'],
            'Scientific Name': ['Trachyspermum ammi', 'Azadirachta indica', 'Lawsonia inermis'],
            'Medicinal Uses': ['Digestive aid', 'Blood purifier', 'Cooling agent']
        }
    elif category == "Siddha":
        plants = {
            'Plant Name': ['Aloe vera', 'Neem', 'Thuthuvalai'],
            'Scientific Name': ['Aloe barbadensis', 'Azadirachta indica', 'Solanum trilobatum'],
            'Medicinal Uses': ['Skin care', 'Antibacterial', 'Respiratory health']
        }
    else:
        plants = {
            'Plant Name': ['Aloe vera', 'Neem', 'Thuthuvalai'],
            'Scientific Name': ['Aloe barbadensis', 'Azadirachta indica', 'Solanum trilobatum'],
            'Medicinal Uses': ['Skin care', 'Antibacterial', 'Respiratory health']
        }

    df = pd.DataFrame(plants)

    mask = df['Plant Name'].str.contains(query, case=False, na=False) | \
           df['Medicinal Uses'].str.contains(query, case=False, na=False)

    return df[mask]

search = st.text_input("Search for a medicinal plant by name or property")
if search:
    st.write(f"Results for: {search}")
    results_df = search_plants(search, option)
    if not results_df.empty:
        st.table(results_df)
    else:
        st.write("No matching plants found.")

st.header("Medicinal Plants Gardens Around The World 🌍")
st.markdown("Discover where medicinal plants are cultivated and preserved")

garden_locations = pd.DataFrame({
    'lat': [28.7041, 27.7000, 27.6760],
    'lon': [77.1025, 85.3333, 83.4636],
    'location': ['Delhi, India', 'Kathmandu, Nepal', 'Butwal, Nepal']
})

st.map(garden_locations)

st.header("Explore Popular Medicinal Plants")
st.markdown("Here are some widely used medicinal plants and their benefits.")

col1, col2, col3 = st.columns(3)

with col1:
    try:
        st.image("tulsi_image.jpg", caption="Tulsi", use_container_width=True)
    except FileNotFoundError:
        st.warning("Tulsi image not found")
    st.write("**Tulsi (Ocimum tenuiflorum)**: Anti-inflammatory, boosts immunity")

with col2:
    try:
        st.image("yarsaganda_image.jpg", caption="Yarsaganda", use_container_width=True)
    except FileNotFoundError:
        st.warning("Yarsaganda image not found")
    st.write("**Yarsaganda (Withania somnifera)**: Reduces stress, improves vitality")

with col3:
    try:
        st.image("neem_image.jpg", caption="Neem", use_container_width=True)
    except FileNotFoundError:
        st.warning("Neem image not found")
    st.write("**Neem (Azadirachta indica)**: Antibacterial, purifies the blood")

st.header("Medicinal Properties of Key Plants")
df = pd.DataFrame({
    "Plant": ['Tulsi', 'Neem', 'Yarsaganda'],
    'Anti-inflammatory': [4, 5, 3],
    'Antibacterial': [2, 5, 1],
    'Stress-relief': [1, 1, 5]
})

fig = px.bar(df, x='Plant', y=['Anti-inflammatory', 'Antibacterial', 'Stress-relief'],
             title="Medicinal Properties of Selected Plants", barmode='group')

st.plotly_chart(fig)

st.header('Take a Quiz: Test Your Herbal Knowledge')

with st.form(key='quiz'):
    q1 = st.radio("Which plant is called the queen of herbs?", ["Tulsi", "Yarsaganda", "Neem"])
    q2 = st.radio("Which plant is well known for its antibacterial properties?", ["Tulsi", "Neem", "Aloe Vera"])
    submit = st.form_submit_button("Submit")

if submit:
    st.balloons()
    st.write("Your answers have been submitted!")
    st.write("Correct Answer 1: Tulsi")
    st.write("Correct Answer 2: Neem")

st.markdown("---")
st.markdown("**Created by Saachin** | Powered by Streamlit")
