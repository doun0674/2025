import streamlit as st
import random

# -------------------------------
# 행동 조합별 취미 추천 데이터
# -------------------------------
hobby_rules = {
    frozenset(["🌳 밖에서 활동하기", "🤝 사람들과 어울리기"]): ("⚽ 축구", "함께 뛰며 땀 흘리는 최고의 팀 스포츠!"),
    frozenset(["🌳 밖에서 활동하기", "💪 몸을 움직이기"]): ("⛰️ 등산", "자연과 함께하는 건강한 라이프스타일 🌲"),
    frozenset(["🏠 집에서 조용히 있기", "🎶 음악/예술 즐기기"]): ("🎨 그림 그리기", "감정을 색으로 표현하는 치유의 시간 🎨"),
    frozenset(["🏠 집에서 조용히 있기", "🧩 새로운 걸 배우기"]): ("📖 독서", "책 속에서 새로운 세상을 탐험하기 📚"),
    frozenset(["🎶 음악/예술 즐기기", "🤝 사람들과 어울리기"]): ("🎤 밴드 활동", "함께 음악을 만들어가는 짜릿한 경험 🎶"),
    frozenset(["💪 몸을 움직이기", "🧩 새로운 걸 배우기"]): ("🥊 복싱", "도전과 성장, 강인한 멘탈을 길러주는 스포츠 💪"),
}

# -------------------------------
# 앱 기본 설정
# -------------------------------
st.set_page_config(page_title="취미 추천 사이트", page_icon="🎯", layout="wide")

# -------------------------------
# 헤더
# -------------------------------
st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        text-align: center;
        color: #ff4b4b;
        font-weight: bold;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #333333;
    }
    .hobby-card {
        background-color: #fff3e6;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .hobby-title {
        font-size: 40px;
        font-weight: bold;
        color: #ff7f50;
    }
    .hobby-desc {
        font-size: 20px;
        color: #444444;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🌈 취미 추천 사이트 🌈</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">좋아하는 행동을 선택하면 당신에게 딱 맞는 취미를 찾아드려요! 🎉</div>', unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# 행동 선택
# -------------------------------
actions = st.multiselect(
    "👉 좋아하는 행동을 모두 선택하세요:",
    ["🌳 밖에서 활동하기", "🏠 집에서 조용히 있기", "🎶 음악/예술 즐기기", 
     "🤝 사람들과 어울리기", "🧩 새로운 걸 배우기", "💪 몸을 움직이기"]
)

# -------------------------------
# 추천 결과
# -------------------------------
if st.button("✨ 내 취미 추천 받기 ✨"):
    if len(actions) < 2:
        st.warning("👉 최소 2개 이상 행동을 선택해주세요!")
    else:
        key = frozenset(actions)
        hobby, desc = hobby_rules.get(
            key, 
            random.choice([
                ("🎬 영화 감상", "다양한 세상 속으로 빠져드는 즐거움 🎥"),
                ("📷 사진 찍기", "순간을 영원히 담아내는 감각 📸"),
                ("🍳 요리", "맛과 향으로 창의력을 표현하는 시간 🍲"),
                ("🕺 댄스", "몸으로 음악을 즐기며 스트레스 해소 💃")
            ])
        )
        
        st.markdown(
            f"""
            <div class="hobby-card">
                <div class="hobby-title">{hobby}</div>
                <div class="hobby-desc">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------
# 푸터
# -------------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | 🎯 Hobby Recommender")
