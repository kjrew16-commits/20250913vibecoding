import streamlit as st
import pandas as pd
import altair as alt
import os

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="MBTI 국가별 분포", page_icon="🌍", layout="centered")

# --- 데이터 불러오기 ---
@st.cache_data
def load_data():
    file_name = "countriesMBTI_16types.csv"
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
    else:
        uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            st.stop()
    return df

df = load_data()

# --- 타이틀 ---
st.title("🌍 국가별 MBTI Top10 분석")
st.write("MBTI 유형을 선택하면, 해당 유형 비율이 높은 국가 Top10을 보여드려요! 🏆")

# --- MBTI 유형 선택 ---
mbti_types = [col for col in df.columns if col != "Country"]
choice = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

# --- Top10 국가 추출 ---
top10 = df[["Country", choice]].sort_values(by=choice, ascending=False).head(10)

# --- Altair 차트 ---
chart = (
    alt.Chart(top10)
    .mark_bar(color="skyblue")
    .encode(
        x=alt.X(choice, title=f"{choice} 비율"),
        y=alt.Y("Country", sort="-x", title="국가"),
        tooltip=["Country", choice]
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)

# --- 데이터 테이블 ---
st.subheader("📋 데이터 보기")
st.dataframe(top10.reset_index(drop=True))
