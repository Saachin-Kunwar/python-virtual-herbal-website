import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Virtual Herbal Garden",
    page_icon="🌿",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: #00ff99;
}

.stButton>button {
    background-color: #00cc66;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stTextInput>div>div>input {
    border-radius: 10px;
}

.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,255,100,0.3);
    margin-bottom: 20px;
}

.footer {
    text-align:center;
    padding:20px;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🌿 Virtual Herbal Garden")
st.subheader("Explore Medicinal Plants from Around the World")

# ---------------- HERO IMAGE ----------------
try:
    img = Image.open("background.jpg")
    st.image(img, use_container_width=True)
except:
    st.warning("Background image not found.")

# ---------------- DATA ----------------
plant_data = {

    "Ayurveda": [
        ["Tulsi", "Ocimum tenuiflorum", "Boosts immunity"],
        ["Ashwagandha", "Withania somnifera", "Stress relief"],
        ["Brahmi", "Bacopa monnieri", "Memory enhancement"],
        ["Turmeric", "Curcuma longa", "Anti-inflammatory"],
        ["Giloy", "Tinospora cordifolia", "Fever reduction"],
        ["Amla", "Phyllanthus emblica", "Rich in Vitamin C"],
        ["Shatavari", "Asparagus racemosus", "Women's health support"],
        ["Moringa", "Moringa oleifera", "Nutritional supplement"]
    ],

    "Unani": [
        ["Ajwain", "Trachyspermum ammi", "Digestive aid"],
        ["Neem", "Azadirachta indica", "Blood purifier"],
        ["Henna", "Lawsonia inermis", "Cooling agent"],
        ["Fenugreek", "Trigonella foenum-graecum", "Controls blood sugar"],
        ["Fennel", "Foeniculum vulgare", "Improves digestion"],
        ["Black Seed", "Nigella sativa", "Boosts immunity"],
        ["Licorice", "Glycyrrhiza glabra", "Soothes throat"],
        ["Mint", "Mentha", "Relieves stomach discomfort"]
    ],

    "Siddha": [
        ["Aloe Vera", "Aloe barbadensis", "Skin care"],
        ["Neem", "Azadirachta indica", "Antibacterial"],
        ["Thuthuvalai", "Solanum trilobatum", "Respiratory health"],
        ["Vetiver", "Chrysopogon zizanioides", "Cooling effect"],
        ["Indian Borage", "Plectranthus amboinicus", "Cough relief"],
        ["Karisalankanni", "Eclipta alba", "Liver health"],
        ["Turmeric", "Curcuma longa", "Wound healing"],
        ["Bael", "Aegle marmelos", "Digestive support"]
    ],

    "Homeopathy": [
        ["Calendula", "Calendula officinalis", "Wound healing"],
        ["Arnica", "Arnica montana", "Pain relief"],
        ["Nux Vomica", "Strychnos nux-vomica", "Digestive issues"],
        ["Chamomile", "Matricaria chamomilla", "Calming effect"],
        ["Belladonna", "Atropa belladonna", "Fever relief"],
        ["Rhus Toxicodendron", "Toxicodendron radicans", "Joint pain relief"],
        ["Gelsemium", "Gelsemium sempervirens", "Anxiety relief"],
        ["Aconite", "Aconitum napellus", "Cold and fever support"]
    ]
}

# ---------------- RECOMMENDATION DATA ----------------
recommendation_data = {
    "Stress": ["Ashwagandha", "Brahmi", "Chamomile"],
    "Immunity": ["Tulsi", "Neem", "Giloy", "Black Seed"],
    "Skin Care": ["Aloe Vera", "Neem", "Calendula"],
    "Digestion": ["Ajwain", "Nux Vomica", "Fennel", "Mint"],
    "Pain Relief": ["Arnica", "Turmeric"],
    "Memory": ["Brahmi"],
    "Respiratory Problems": ["Thuthuvalai", "Tulsi", "Indian Borage"],
    "Fever": ["Giloy", "Belladonna", "Aconite"],
    "Joint Pain": ["Rhus Toxicodendron", "Turmeric"],
    "Anxiety": ["Gelsemium", "Ashwagandha"]
}

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌱 Navigation")

category = st.sidebar.selectbox(
    "Choose Tradition",
    list(plant_data.keys())
)

# ---------------- METRICS ----------------
st.header("📊 Herbal Statistics")

total_plants = sum(len(plants) for plants in plant_data.values())

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Traditions", "4")

with col2:
    st.metric("Medicinal Plants", total_plants)

with col3:
    st.metric("Countries Covered", "3")

# ---------------- DISPLAY DATA ----------------
st.header(f"🌿 {category} Medicinal Plants")

df = pd.DataFrame(
    plant_data[category],
    columns=["Plant Name", "Scientific Name", "Benefits"]
)

st.dataframe(df, use_container_width=True)

# ---------------- SEARCH ----------------
st.header("🔍 Search Plants")

search = st.text_input("Search by plant name or benefit")

if search:
    filtered_df = df[
        df["Plant Name"].str.contains(search, case=False) |
        df["Benefits"].str.contains(search, case=False)
    ]

    if not filtered_df.empty:
        st.success(f"{len(filtered_df)} result(s) found")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.error("No matching plants found.")

# ---------------- DOWNLOAD BUTTON ----------------
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "⬇ Download Plant Data",
    csv,
    "medicinal_plants.csv",
    "text/csv"
)

# ---------------- MAP ----------------
st.header("🌍 Herbal Gardens Around the World")

map_data = pd.DataFrame({
    'lat': [28.7041, 27.7172, 27.6760, 19.0760],
    'lon': [77.1025, 85.3240, 83.4636, 72.8777]
})

st.map(map_data)

# ---------------- PLANT CARDS ----------------
st.header("🌿 Popular Medicinal Plants")

cols = st.columns(4)

plants = [
    ("Tulsi", "Boosts immunity"),
    ("Neem", "Antibacterial properties"),
    ("Ashwagandha", "Reduces stress"),
    ("Aloe Vera", "Improves skin health")
]

for col, plant in zip(cols, plants):
    with col:
        st.markdown(f"""
        <div class="card">
            <h3>{plant[0]}</h3>
            <p>{plant[1]}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- CHART ----------------
st.header("📈 Medicinal Properties Analysis")

chart_df = pd.DataFrame({
    "Plant": ["Tulsi", "Neem", "Ashwagandha", "Aloe Vera"],
    "Immunity": [5, 4, 3, 2],
    "Antibacterial": [2, 5, 1, 4],
    "Stress Relief": [1, 1, 5, 2]
})

fig = px.bar(
    chart_df,
    x="Plant",
    y=["Immunity", "Antibacterial", "Stress Relief"],
    barmode="group",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- PLANT RECOMMENDATION SYSTEM ----------------
st.header("🤖 Plant Recommendation System")

problem = st.selectbox(
    "Select Your Health Concern",
    list(recommendation_data.keys())
)

if st.button("Get Recommendation"):

    recommended_plants = recommendation_data[problem]

    st.success(f"Recommended Plants for {problem}")

    for plant in recommended_plants:
        st.markdown(f"""
        <div class="card">
            <h3>🌿 {plant}</h3>
            <p>Recommended for: {problem}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- QUIZ ----------------
st.header("🧠 Herbal Quiz")

score = 0

with st.form("quiz_form"):

    q1 = st.radio(
        "Which herb improves memory?",
        ["Tulsi", "Brahmi", "Neem"]
    )

    q2 = st.radio(
        "Which herb is antibacterial?",
        ["Neem", "Brahmi", "Arnica"]
    )

    q3 = st.radio(
        "Which plant is best for skin care?",
        ["Aloe Vera", "Ajwain", "Belladonna"]
    )

    submitted = st.form_submit_button("Submit Quiz")

if submitted:

    if q1 == "Brahmi":
        score += 1

    if q2 == "Neem":
        score += 1

    if q3 == "Aloe Vera":
        score += 1

    st.success(f"🎉 Your Score: {score}/3")

    if score == 3:
        st.balloons()

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Made with ❤️ by Saachin  | Streamlit Herbal Project
</div>
""", unsafe_allow_html=True)