import streamlit as st
from streamlit_lottie import  st_lottie
import requests


st.set_page_config(page_title = "Banking App" , layout = "centered")
def load_lottieur(url:str):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "http://assets9.lottiefiles.com/packages/lf20_u4yrau.json"
lottie_json = load_lottieur(lottie_url)

st_lottie(lottie_json, speed=1, height=200, key="Banking")


st.title("NOVA BANK ")
st.header('Our Banking Interface')
st.subheader('Welcome to our banking interface, thanks for trusting our services')
st.write('Use the icon to your left to navigate through ; ')
st.write('# Withdrawal')
st.write('# &')
st.write('# Deposit')
st.write('Within your current and savings account')



