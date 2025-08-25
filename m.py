import streamlit as st

st.set_page_config(page_title="스트레칭 도우미", page_icon="🧘", layout="centered")

# 메인 제목
st.markdown("<h1 style='text-align: center; color:#4CAF50;'>🧘 집에서 하는 간단 스트레칭 가이드</h1>", unsafe_allow_html=True)
st.write("---")

# 불편한 부위 선택
st.subheader("📍 불편한 부위를 선택하세요")
part = st.selectbox("부위 선택", ["목", "어깨", "허리", "무릎", "손목", "발목"])

# 아픈 강도 선택
st.subheader("⚖️ 통증 강도를 선택하세요")
pain_level = st.radio("현재 통증 정도", ["🙂 가벼움", "😐 중간", "😣 심함"])

# 스트레칭 데이터
stretches = {
    "목": {
        "동작": "천천히 고개를 좌우로 기울이며 스트레칭",
        "시간": "10~15초 유지, 3회 반복",
        "주의": "갑작스럽게 고개를 돌리지 마세요."
    },
    "어깨": {
        "동작": "어깨를 천천히 앞뒤로 크게 돌리기",
        "시간": "15회씩 2세트",
        "주의": "통증이 심하면 범위를 줄이세요."
    },
    "허리": {
        "동작": "무릎을 가슴 쪽으로 당겨 스트레칭",
        "시간": "20초 유지, 3회 반복",
        "주의": "허리에 날카로운 통증이 있으면 중단하세요."
    },
    "무릎": {
        "동작": "의자에 앉아 다리 뻗어 무릎 스트레칭",
        "시간": "15초 유지, 5회 반복",
        "주의": "무릎이 붓거나 열감이 있으면 피하세요."
    },
    "손목": {
        "동작": "손바닥을 펴고 반대손으로 손가락을 당겨 스트레칭",
        "시간": "10초 유지, 5회 반복",
        "주의": "저림이 심하면 중단하세요."
    },
    "발목": {
        "동작": "발목을 천천히 원을 그리며 돌리기",
        "시간": "각 방향 10회씩",
        "주의": "통증이 심하면 범위를 줄이세요."
    }
}

# 강도별 안내
intensity = {
    "🙂 가벼움": "✅ 가볍게 시작해도 좋아요.",
    "😐 중간": "⚠️ 무리하지 말고 동작을 천천히 하세요.",
    "😣 심함": "🚫 운동보다는 휴식과 전문가 상담이 우선입니다."
}

# 결과 표시
st.write("---")
st.markdown(f"""
<div style="background-color:#f9f9f9; padding:20px; border-radius:15px; box-shadow:2px 2px 10px #ddd;">
    <h2 style="color:#4CAF50;">📌 추천 스트레칭</h2>
    <p><b>부위:</b> {part}</p>
    <p><b>동작:</b> {stretches[part]['동작']}</p>
    <p><b>시간/횟수:</b> {stretches[part]['시간']}</p>
    <p><b>주의사항:</b> {stretches[part]['주의']}</p>
    <p><b>강도 안내:</b> {intensity[pain_level]}</p>
</div>
""", unsafe_allow_html=True)
