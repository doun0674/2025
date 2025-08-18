import streamlit as st
import random

# -------------------------------
# 행동 조합별 취미 추천 데이터
# -------------------------------
hobby_rules = {
    frozenset(["🌳 밖에서 활동하기", "🤝 사람들과 어울리기"]): "⚽ 축구",
    frozenset(["🌳 밖에서 활동하기", "💪 몸을 움직이기"]): "⛰️ 등산",
    frozenset(["🏠 집에서 조용히 있기", "🎶 음악/예술 즐기기"]): "🎨 그림 그리기",
    frozenset(["🏠 집에서 조용히 있기", "🧩 새로운 걸 배우기"]): "📖 독서",
    frozenset(["🎶 음악/예술 즐기기", "🤝 사람들과 어울리기"]): "🎤 밴드 활동",
    frozenset(["💪 몸을 움직이기", "🧩 새로운 걸 배우기"]): "🥊 복싱",
}

# -------------------------------
# 앱 기본 설정
# -------------------------------
st.set_page_config(page_title="취미 추천 사이트", page_icon="🎯", layout="centered")

st.title("✨ 취미 추천 사이트 ✨")
st.markdown("여러 가지 행동을 선택하면, 당신에게 딱 맞는 **하나의 취미**를 추천해드릴게요! 🏖️")

# 행동 선택
actions = st.multiselect(
    "좋아하는 행동을 모두 골라보세요 👇",
    ["🌳 밖에서 활동하기", "🏠 집에서 조용히 있기", "🎶 음악/예술 즐기기", 
     "🤝 사람들과 어울리기", "🧩 새로운 걸 배우기", "💪 몸을 움직이기"]
)

# 버튼 클릭 시 결과 출력
if st.button("🔮 내 취미 추천 받기"):
    if len(actions) < 2:
        st.warning("👉 최소 2개 이상 행동을 선택해주세요!")
    else:
        key = frozenset(actions)
        hobby = hobby_rules.get(key, random.choice(["🎬 영화 감상", "📷 사진 찍기", "🍳 요리"]))
        
        st.subheader("🌟 추천 취미 🌟")
        st.success(f"당신에게 어울리는 취미는 바로... **{hobby}** 입니다! 🚀")
