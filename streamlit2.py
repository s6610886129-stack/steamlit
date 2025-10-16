import streamlit as st
import pandas as pd
import requests

st.title("อัตราแลกเปลี่ยนจาก USD")

url = "https://v6.exchangerate-api.com/v6/6165cc4d72124b2cb070a207/latest/USD"
response = requests.get(url)
data = response.json()

# เข้าถึงข้อมูลอัตราแลกเปลี่ยน
rates = data["conversion_rates"]

thb_rate = rates.get("THB")
st.write(f"1 USD = {thb_rate:,.2f} THB")

# เลือกสกุลเงิน
options = ['EUR', 'THB', 'JPY', 'CNY', 'KRW']
selected = st.selectbox("เลือกสกุลเงิน", options, index=1)

# คำนวณอัตราแลกเปลี่ยน
rate = rates.get(selected)

st.subheader(f"1 USD = {rate:,.2f} {selected}")
