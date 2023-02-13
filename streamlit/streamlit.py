import streamlit as st

st.set_page_config (
    page_title = "환전소",
    layout = "wide",
    initial_sidebar_state = "expanded",
    menu_items = {
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'about' : "# 유재웅 제작"
    }   
)
st.title('환전소')
st.subheader("KRW -> BRL")
number = st.number_input('KRW')
st.write('BRL', number * 0.00409)