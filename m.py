import streamlit as st

# 웹앱 기본 설정
st.set_page_config(page_title="재활 운동 가이드", page_icon="💪", layout="wide")

# 제목
st.title("💪 집에서 하는 간단 재활 운동")
st.write("불편한 부위를 선택하면, 집에서 따라할 수 있는 간단한 운동과 주의사항을 안내합니다.")

# 사이드바 선택
st.sidebar.header("👉 어디가 불편한가요?")
part = st.sidebar.selectbox("신체 부위 선택:", ["목", "어깨", "손목", "허리", "무릎", "발목"])
level = st.sidebar.radio("불편 정도:", ["가벼움", "중간", "심함"])

# 운동 데이터 (운동 이름 + 설명 + 이미지 + 주의사항)
rehab_dict = {
    "목": [
        {"name": "턱 당기기 운동", "desc": "턱을 당겨 목을 곧게 유지 (10회)", 
         "img": "neck_chin_tuck.gif", "caution": "어지럼증이 느껴지면 즉시 중단하세요."},
        {"name": "목 옆 스트레칭", "desc": "고개를 좌우로 기울여 10초 유지", 
         "img": "neck_side_stretch.gif", "caution": "과도하게 기울이지 마세요."}
    ],
    "어깨": [
        {"name": "어깨 돌리기", "desc": "앞뒤로 천천히 10회", 
         "img": "shoulder_roll.gif", "caution": "통증이 심하면 멈추세요."},
        {"name": "벽 밀기 운동", "desc": "벽을 가볍게 밀며 어깨 활성화 (10회)", 
         "img": "shoulder_wall_push.gif", "caution": "어깨가 뻐근하면 무리하지 마세요."}
    ],
    "손목": [
        {"name": "손목 스트레칭", "desc": "손가락을 뒤로 당겨 10초 유지", 
         "img": "wrist_stretch.gif", "caution": "저림이나 통증이 심하면 중단하세요."},
        {"name": "손목 굽히기 운동", "desc": "물병을 잡고 위아래 10회", 
         "img": "wrist_curl.gif", "caution": "너무 무거운 물체는 피하세요."}
    ],
    "허리": [
        {"name": "무릎 당기기", "desc": "누워서 무릎을 가슴 쪽으로 당기기 (10초)", 
         "img": "knee_to_chest.gif", "caution": "허리가 뻐근하면 강도를 줄이세요."},
        {"name": "고양이-소 자세", "desc": "허리를 둥글게/펴기 (10회)", 
         "img": "cat_cow.gif", "caution": "허리에 날카로운 통증이 있으면 중단하세요."}
    ],
    "무릎": [
        {"name": "무릎 곧게 펴기", "desc": "무릎을 쭉 펴고 10초 유지", 
         "img": "knee_extension.gif", "caution": "무릎이 덜컥거리면 중지하세요."},
        {"name": "벽 스쿼트", "desc": "벽에 등을 붙이고 앉았다 일어서기 (5~10회)", 
         "img": "wall_squat.gif", "caution": "무릎에 날카로운 통증이 있으면 멈추세요."}
    ],
    "발목": [
        {"name": "발목 돌리기", "desc": "발목을 좌우로 원형 돌리기 (10회)", 
         "img": "ankle_circle.gif", "caution": "빠르게 돌리면 삐끗할 수 있어요."},
        {"name": "발끝 들기", "desc": "서서 발끝 들었다 내리기 (15회)", 
         "img": "toe_raise.gif", "caution": "균형을 잃지 않도록 벽을 잡으세요."}
    ]
}

# 결과 출력
st.subheader(f"🏋️ {part} 운동 가이드")

for ex in rehab_dict[part]:
    col1, col2 = st.columns([1,2])  # 이미지 + 설명
    with col1:
        st.image(ex["img"], use_column_width=True)  # 운동 이미지
    with col2:
        st.markdown(f"**{ex['name']}**")
        st.write(ex["desc"])
        st.warning(f"⚠️ 주의사항: {ex['caution']}")
    st.markdown("---")

# 불편 정도에 따른 안내 메시지
if level == "가벼움":
    st.info("😊 가볍게 스트레칭 위주로 해보세요.")
elif level == "중간":
    st.warning("🙂 무리가 되지 않는 선에서 꾸준히 해보세요.")
else:
    st.error("⚠️ 불편함이 심하면 운동보다는 휴식을 우선하세요.")
