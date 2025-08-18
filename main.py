import streamlit as st

# -------------------------------
# 직업 추천 데이터 (예시)
# -------------------------------
jobs = {
    "INTJ": ["전략 기획자", "데이터 과학자", "연구원"],
    "INFJ": ["상담사", "작업치료사", "작가"],
    "ENTP": ["창업가", "마케팅 전문가", "기획자"],
    "ESFP": ["배우", "이벤트 플래너", "홍보 전문가"],
    # 나머지도 추가 가능
}

# -------------------------------
# 앱 UI 시작
# -------------------------------
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💡", layout="centered")

st.title("✨ MBTI 기반 직업 추천 사이트 ✨")
st.markdown("당신의 **MBTI**를 선택하면 어울리는 직업을 추천해드립니다! 💼")

# MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=sorted(jobs.keys())
)

# 버튼 클릭 시 결과 출력
if st.button("추천 직업 보기"):
    st.subheader(f"🌟 {mbti} 유형 추천 직업 🌟")
    for job in jobs[mbti]:
        st.write(f"- {job}")

    st.success("추천된 직업 중에서 마음에 드는 걸 탐색해보세요! 🚀")

# -------------------------------
# 디자인 요소
# -------------------------------
st.markdown("---")
st.caption("Made with ❤️ by Streamlit")

