import streamlit as st
import pandas as pd
import requests

st.title("รายงานผู้ป่วยโรคหลอดเลือดสมอง (STROKE) ที่ปัจจุบันสูบบุหรี่สามารถเลิกบุหรี่ได้สำเร็จ")

years = [2566,2567,2568]
year = st.selectbox("เลือกปี", years, index=len(years)-1)

url = f"https://opendata.moph.go.th/api/report_data/s_i6069_ciga/{year}"

st.write("แหล่งข้อมูล:", url)

# ดึงข้อมูลจาก API
response = requests.get(url)
data = response.json()

# แปลงเป็น DataFrame
df = pd.DataFrame(data)

st.subheader(f"ข้อมูลปี {year}")
st.dataframe(df)