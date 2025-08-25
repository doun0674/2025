import streamlit as st

st.set_page_config(page_title="스트레칭 가이드", page_icon="🤸", layout="wide")

st.title("🤸 스트레칭 가이드")
st.write("건강을 위해 다양한 스트레칭 방법과 주의사항을 확인해보세요! 💪")

# 스트레칭 데이터
exercises = [
    {
        "name": "목 스트레칭 🧘",
        "desc": "고개를 천천히 좌우로 기울이며 목 근육을 풀어줍니다.",
        "caution": "⚠ 갑작스럽게 세게 당기지 말고, 통증이 느껴지면 즉시 중단하세요.",
        "img": "https://images.unsplash.com/photo-1599058917765-8f8798a2df45"
    },
    {
        "name": "어깨 스트레칭 🏋️",
        "desc": "한쪽 팔을 가슴 앞으로 당겨 어깨 근육을 늘려줍니다.",
        "caution": "⚠ 반동을 주지 말고 호흡을 편안히 유지하세요.",
        "img": "https://images.unsplash.com/photo-1594737625785-c3b7301b1d5a"
    },
    {
        "name": "허리 스트레칭 🧍",
        "desc": "양손을 머리 위로 올리고 천천히 옆으로 기울여 옆구리와 허리를 늘립니다.",
        "caution": "⚠ 허리에 무리가 가지 않도록 천천히 진행하세요.",
        "img": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1"
    },
    {
        "name": "다리 스트레칭 🦵",
        "desc": "바닥에 앉아 다리를 벌리고 상체를 앞으로 숙입니다.",
        "caution": "⚠ 무릎을 과도하게 눌러 펴지 않도록 주의하세요.",
        "img": "https://images.unsplash.com/photo-1599058900330-79f16b6e7f41"
    },
    {
        "name": "종아리 스트레칭 🚶",
        "desc": "벽을 짚고 한쪽 다리를 뒤로 뻗어 종아리를 늘려줍니다.",
        "caution": "⚠ 발뒤꿈치가 바닥에서 떨어지지 않도록 주의하세요.",
        "img": "https://images.unsplash.com/photo-1594737625785-c3b7301b1d5a"
    },
    {
        "name": "손목 스트레칭 ✋",
        "desc": "손바닥을 위로 하고 손가락을 잡아 당겨 손목을 늘립니다.",
        "caution": "⚠ 손목에 통증이 있으면 강하게 당기지 마세요.",
        "img": "https://images.unsplash.com/photo-1606813909027-9ec49f8ff69e"
    }
]

# 스트레칭 카드 형식 출력
for ex in exercises:
    with st.container():
        st.subheader(ex["name"])
        st.image(ex["img"], use_container_width=True)  # 이미지 출력
        st.write(f"📖 설명: {ex['desc']}")
        st.write(f"{ex['caution']}")
        st.markdown("---")
