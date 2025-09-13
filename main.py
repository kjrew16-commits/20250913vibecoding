import streamlit as st
import random

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="MBTI 공부법 추천", page_icon="📚", layout="centered")

# --- 타이틀 ---
st.title("✨ MBTI 유형별 공부법 추천 ✨")
st.write("자신의 MBTI를 선택하면 가장 찰떡같이 어울리는 공부법을 알려드려요! 😎")

# --- MBTI 목록 ---
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# --- 공부법 추천 사전 ---
study_tips = {
    "INTJ": "계획표 만들기 📅 + 목표 달성 체크 ✔️",
    "INTP": "궁금한 건 끝까지 파고들기 🔍 + 개념 연결하기 🧩",
    "ENTJ": "스터디 리더하기 🗣️ + 목표를 수치화하기 📊",
    "ENTP": "토론으로 아이디어 폭발 💡 + 친구랑 문제 맞추기 🎯",
    "INFJ": "조용한 공간에서 몰입하기 🌌 + 마인드맵 정리 🌀",
    "INFP": "감정에 몰입하는 공부 🎶 + 자기 보상 시스템 🍫",
    "ENFJ": "친구 가르쳐주면서 배우기 👩‍🏫 + 함께 계획 세우기 🤝",
    "ENFP": "재미있게! 🎉 색깔펜 정리 🌈 + 노래로 암기 🎵",
    "ISTJ": "체계적인 노트 필기 📖 + 규칙적인 복습 🔁",
    "ISFJ": "작은 목표 세우고 차근차근 🪜 + 플래시카드 📇",
    "ESTJ": "시간 관리 철저하게 ⏰ + 스터디 규칙 만들기 📏",
    "ESFJ": "친구와 함께 퀴즈 풀기 🤩 + 칭찬과 피드백 💬",
    "ISTP": "실험과 체험 위주 🔬 + 실전 문제 풀이 📝",
    "ISFP": "편안한 분위기 🌿 + 그림·도식으로 정리 🎨",
    "ESTP": "몸으로 배우기 🏃 + 제한시간 두고 퀴즈 ⏳",
    "ESFP": "음악과 함께 공부 🎧 + 발표나 퍼포먼스로 암기 🎤"
}

# --- 선택 박스 ---
choice = st.selectbox("당신의 MBTI를 골라주세요! 🧐", mbti_types)

# --- 버튼 ---
if st.button("📖 나의 맞춤 공부법 보기"):
    tip = study_tips.get(choice, "아직 준비 중이에요! 🛠️")
    emojis = ["🔥", "🚀", "🌟", "🍀", "💎", "🎯", "💡", "📌"]
    st.success(f"{choice} 유형에게 딱 맞는 공부법은... {random.choice(emojis)}\n\n👉 {tip}")
    st.balloons()
