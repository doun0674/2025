import streamlit as st

st.set_page_config(page_title="스트레칭 가이드 🏠", page_icon="🧘", layout="centered")

st.title("🏋️ 간단 스트레칭 가이드")
st.write(" 부위를 선택하면 적절한 스트레칭 방법과 ⚠️ 주의사항을 알려드립니다.")

# 선택 옵션
discomfort_area = st.selectbox(
    "어느 부위를 선택 할건가요?",
    [
        "목",
        "어깨",
        "허리",
        "무릎",
        "손목",
        "발목",
        "눈 휴식 운동"
    ]
)

# 스트레칭 안내 함수
def show_exercise(area):
    if area == "목":
        st.subheader("🧘 목 스트레칭")
        st.write("- 고개를 천천히 좌우로 기울여주세요 (각 10초 유지, 5회 반복)")
        st.write("- 턱을 살짝 당기며 목 뒤를 늘려주세요 (10초 유지, 3회)")
        st.warning("⚠️ 통증이 심하면 중단하세요. 무리한 압박 금지!")

    elif area == "어깨":
        st.subheader("💪 어깨 스트레칭")
        st.write("- 팔을 가슴 앞으로 교차해 당겨주세요 (10초 유지, 5회 반복)")
        st.write("- 양손을 깍지 끼고 머리 위로 올려 기지개 켜듯 늘려주세요")
        st.warning("⚠️ 어깨에 날카로운 통증이 느껴지면 멈추세요.")

    elif area == "허리":
        st.subheader("🙆 허리 스트레칭")
        st.write("- 무릎을 세우고 누운 자세에서 무릎을 가슴 쪽으로 당겨주세요 (10초 유지, 5회)")
        st.write("- 네발 자세에서 등을 천천히 말아 올리고 내리세요 (고양이 자세, 10회)")
        st.warning("⚠️ 허리에 힘이 과도하게 들어가지 않도록 주의하세요.")

    elif area == "무릎":
        st.subheader("🦵 무릎 스트레칭")
        st.write("- 의자에 앉아 다리를 쭉 뻗고 발끝을 당겼다 밀었다 하세요 (10회)")
        st.write("- 허벅지 근육 강화: 벽에 등을 대고 의자 앉듯이 10초 버티기")
        st.warning("⚠️ 날카로운 통증이 있으면 중단하세요.")

    elif area == "손목":
        st.subheader("✋ 손목 스트레칭")
        st.write("- 손바닥을 앞으로 펴고 반대 손으로 손가락을 천천히 젖히세요 (10초 유지, 5회)")
        st.write("- 주먹을 쥐고 돌리며 손목 관절 풀어주기 (10회)")
        st.warning("⚠️ 손목이 붓거나 열감이 있으면 중단하세요.")

    elif area == "발목":
        st.subheader("🦶 발목 스트레칭")
        st.write("- 의자에 앉아 발목을 원 그리듯 천천히 돌려주세요 (각 방향 10회)")
        st.write("- 까치발로 5초 버티고 천천히 내려오기 (10회)")
        st.warning("⚠️ 불안정한 바닥에서는 수행하지 마세요.")

    elif area == "눈 휴식 운동":
        st.subheader("👀 눈 스트레칭")
        st.write("- 눈을 감고 손바닥으로 따뜻하게 덮어주세요 (30초)")
        st.write("- 먼 곳 → 가까운 곳 번갈아 바라보기 (10회)")
        st.warning("⚠️ 눈이 충혈되거나 통증이 심하면 전문가에게 상담하세요.")

# 선택한 부위 출력
show_exercise(discomfort_area)
