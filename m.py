import streamlit as st

# 운동 추천 데이터
exercises = {
    "목 스트레칭": {
        "desc": "목을 천천히 좌우로 기울이며 긴장을 완화하는 스트레칭입니다.",
        "warning": "너무 세게 꺾지 말고, 통증이 느껴지면 즉시 중단하세요."
    },
    "어깨 돌리기": {
        "desc": "어깨를 크게 원을 그리며 돌려주어 뭉친 근육을 풀어줍니다.",
        "warning": "팔을 무리해서 크게 돌리면 관절에 무리가 갈 수 있습니다."
    },
    "허리 스트레칭": {
        "desc": "허리를 좌우로 천천히 돌려 긴장을 완화하는 동작입니다.",
        "warning": "허리에 통증이 있다면 범위를 줄여서 가볍게 진행하세요."
    },
    "손목 스트레칭": {
        "desc": "손목을 아래로 젖힌 상태에서 반대손으로 살짝 당겨줍니다.",
        "warning": "손목이 시큰거리면 강도를 줄이고, 오래 유지하지 마세요."
    }
}

# 앱 제목
st.title("💪 간단한 스트레칭 추천 앱")

st.write("아래에서 원하는 스트레칭을 선택하면 설명과 주의 상황을 확인할 수 있어요!")

# 선택 박스
choice = st.selectbox("운동을 선택하세요", ["선택 안 함"] + list(exercises.keys()))

# 선택 결과 표시
if choice != "선택 안 함":
    st.subheader(f"👉 {choice}")
    st.write(exercises[choice]["desc"])
    st.warning(exercises[choice]["warning"])
else:
    st.info("운동을 선택하면 설명이 표시됩니다.")
