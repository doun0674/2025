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
    frozenset(["🖥️ 기술을 좋아하기", "🧩 새로운 걸 배우기"]): ("👨‍💻 코딩", "세상을 바꾸는 프로그램을 직접 만들기 💻"),
    frozenset(["🍳 손으로 만드는 걸 좋아하기", "🎶 음악/예술 즐기기"]): ("🍰 베이킹", "오븐에서 피어나는 달콤한 창의력 🧁"),
    frozenset(["🌍 여행을 좋아하기", "📷 기록하기"]): ("📸 여행 사진", "세계를 사진 속에 담아 추억으로 남기기 🌍"),
    frozenset(["🐶 동물을 좋아하기", "🌳 밖에서 활동하기"]): ("🐕 반려견과 산책", "사랑하는 반려동물과 즐기는 힐링 타임 🐾"),
    frozenset(["🎮 게임하기", "🤝 사람들과 어울리기"]): ("🎲 보드게임", "오프라인에서 함께 즐기는 전략과 웃음 😂"),
    frozenset(["🌍 여행을 좋아하기", "🤝 사람들과 어울리기"]): ("✈️ 배낭여행", "사람들과의 만남과 모험이 함께하는 여정 🗺️"),
    frozenset(["📷 기록하기", "🏠 집에서 조용히 있기"]): ("📔 다이어리 쓰기", "하루의 기억을 글과 그림으로 남기기 ✍️"),
}

# -------------------------------
# 랜덤 취미 후보 풀
# -------------------------------
random_hobbies = [
    ("🎬 영화 감상", "다양한 세상 속으로 빠져드는 즐거움 🎥"),
    ("📷 사진 찍기", "순간을 영원히 담아내는 감각 📸"),
    ("🍳 요리", "맛과 향으로 창의력을 표현하는 시간 🍲"),
    ("🕺 댄스", "몸으로 음악을 즐기며 스트레스 해소 💃"),
    ("🎮 게임", "몰입감 넘치는 가상 세계 속 모험 🎮"),
    ("🎯 다트", "정확성과 집중력을 기르는 취미 🎯"),
    ("🌱 가드닝", "작은 씨앗에서 시작되는 힐링 타임 🌿"),
    ("🎭 연극 감상", "무대 위에서 펼쳐지는 살아있는 이야기 🎭"),
]

# -------------------------------
# 앱 기본 설정
# -------------------------------
st.set_page_config(page_title="취미 추천 사이트", page_icon="🎯", layout="wide")

# -------------------------------
# 헤더 디자인
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
        background: linear-gradient(135deg, #f9f3ff, #ffe7d9);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0px 6px 25px rgba(0,0,0,0.15);
        margin-top: 25px;
        animation: fadeIn 1.5s;
    }
    .hobby-title {
        font-size: 42px;
        font-weight: bold;
        color: #ff7f50;
    }
    .hobby-desc {
        font-size: 22px;
        color: #444444;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🌈 취미 추천 사이트 🌈</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">좋아하는 행동을 여러 개 선택하면, 당신에게 꼭 맞는 취미를 찾아드려요! 🎉</div>', unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# 행동 선택
# -------------------------------
actions = st.multiselect(
    "👉 좋아하는 행동을 모두 골라보세요:",
    [
        "🌳 밖에서 활동하기", "🏠 집에서 조용히 있기", "🎶 음악/예술 즐기기", 
        "🤝 사람들과 어울리기", "🧩 새로운 걸 배우기", "💪 몸을 움직이기",
        "🖥️ 기술을 좋아하기", "🍳 손으로 만드는 걸 좋아하기", "🌍 여행을 좋아하기",
        "📷 기록하기", "🐶 동물을 좋아하기", "🎮 게임하기"
    ]
)

# -------------------------------
# 추천 결과
# -------------------------------
if st.button("✨ 내 취미 추천 받기 ✨"):
    if len(actions) < 2:
        st.warning("👉 최소 2개 이상 행동을 선택해주세요!")
    else:
        key = frozenset(actions)
        hobby, desc = hobby_rules.get(key, random.choice(random_hobbies))
        
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
