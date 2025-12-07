import streamlit as st
import pickle


model = pickle.load(open('All_Star_model.pkl', 'rb'))

st.set_page_config(page_title="All Star Predictor")

st.header("All Star Prediction")
st.write("Enter player statistics to predict if they will be an All Star")

col1,col2,col3,col4 = st.columns(4)

with col1:
    G = st.number_input("Games Played")
    GS = st.number_input("Games Started")
    MP = st.number_input("Minutes Played")
    FG = st.number_input("Field Goals Made")
    FGA = st.number_input("Field Goals Attempted")

with col2:
    FGP = st.number_input("Field Goal Percentage")
    P3P = st.number_input("Three Point Percentage")
    P2P = st.number_input("Two Point Percentage")
    EFGP = st.number_input("Eff Field Goal Percentage")
    FT = st.number_input("Free Throws Made")

with col3:
    FTA = st.number_input("Free Throws Attempted")
    FTP = st.number_input("Free Throw Percentage")
    ORB = st.number_input("Offensive Rebounds")
    DRB = st.number_input("Defensive Rebounds")
    TRB = st.number_input("Total Rebounds")

with col4:
    AST = st.number_input("Assists")
    STL = st.number_input("Steals")
    BLK = st.number_input("Blocks")
    TOV = st.number_input("Turnovers")
    PTS = st.number_input("Points Scored")


button = st.button("Predict")

if button:
    input_data = [G, GS, MP, FG, FGA, FGP, P3P, P2P, EFGP, FT, FTA, FTP, ORB, DRB, TRB, AST, STL, BLK, TOV, PTS]
    prediction = model.predict([input_data])
    if prediction[0] == 1:
        st.success("The player is likely to be an All Star!")
    else:
        st.error("The player is unlikely to be an All Star.")
