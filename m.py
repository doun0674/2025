import streamlit as st
import random

st.set_page_config(page_title="🍚 밥먹을 때 볼 영상 추천기", page_icon="🍱", layout="centered")

# 배경 꾸미기
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #ffecd2 0%, #fcb69f 100%);
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align: center; color: #ff5733;'>🍱 밥먹을 때 볼 영상 추천 🍱</h1>", unsafe_allow_html=True)
st.write("식사하면서 보기 좋은 영상을 추천해드릴게요! 😋")

# 선택지
mood = st.multiselect(
    "👉 어떤 분위기의 영상을 원하세요?",
    ["🤣 웃긴 영상", "📺 예능/토크쇼", "🎬 영화 클립", "🎵 음악/공연", 
     "📚 교양/다큐", "🎮 게임 방송", "🍴 먹방", "🐶 귀여운 동물", "⚡ 짧고 빠른 영상(Shorts)", "🧘 차분하고 편안한 영상"]
)

# 영상 데이터
videos = {
    "🤣 웃긴 영상": [
        "https://www.youtube.com/watch?v=9bZkp7q19f0",
        "https://www.youtube.com/watch?v=QH2-TGUlwu4"
    ],
    "📺 예능/토크쇼": [
        "https://www.youtube.com/watch?v=RO4e4l3XZ2k",
        "https://www.youtube.com/watch?v=6vZCC0Qw2TQ"
    ],
    "🎬 영화 클립": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=tgbNymZ7vqY"
    ],
    "🎵 음악/공연": [
        "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
        "https://www.youtube.com/watch?v=kXYiU_JCYtU"
    ],
    "📚 교양/다큐": [
        "https://www.youtube.com/watch?v=lTTajzrSkCw",
        "https://www.youtube.com/watch?v=VYOjWnS4cMY"
    ],
    "🎮 게임 방송": [
        "https://www.youtube.com/watch?v=HgzGwKwLmgM",
        "https://www.youtube.com/watch?v=xvFZjo5PgG0"
    ],
    "🍴 먹방": [
        "https://www.youtube.com/watch?v=jofNR_WkoCE",
        "https://www.youtube.com/watch?v=QJO3ROT-A4E"
    ],
    "🐶 귀여운 동물": [
        "https://www.youtube.com/watch?v=tntOCGkgt98",
        "https://www.youtube.com/watch?v=J---aiyznGQ"
    ],
    "⚡ 짧고 빠른 영상(Shorts)": [
        "https://www.youtube.com/shorts/jNQXAC9IVRw",
        "https://www.youtube.com/shorts/aqz-KE-bpKQ"
    ],
    "🧘 차분하고 편안한 영상": [
        "https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "https://www.youtube.com/watch?v=lFcSrYw-ARY"
    ]
}

# 버튼 클릭 시 추천
if st.button("🍽️ 추천 받기!"):
    if mood:
        chosen_mood = random.choice(mood)
        video_link = random.choice(videos[chosen_mood])
        st.success(f"👉 {chosen_mood} 추천 영상!")
        st.video(video_link)
    else:
        st.warning("먼저 원하는 분위기를 선택해주세요! 😉")
