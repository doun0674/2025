import streamlit as st

# 웹앱 제목
st.title("🏠 집에서 할 수 있는 간단 재활 운동 가이드")

st.write("불편한 신체 부위를 선택하면, 집에서 따라할 수 있는 간단한 운동 방법과 주의사항을 알려드립니다.")

# 선택 옵션
body_part = st.selectbox(
    "불편한 부위를 선택하세요:",
    ["목", "어깨", "허리", "무릎", "손목"]
)

# 부위별 운동 가이드 및 주의사항
if body_part == "목":
    st.subheader("📌 목 스트레칭")
    st.image("https://www.verywellhealth.com/thmb/z2APs35CydOWmNhH1WZfB-7sxaU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/neck-stretch-56a8e6de3df78cf772a1dffe.jpg", caption="목 옆 근육 늘리기")
    st.write("- 의자에 바르게 앉아 한쪽 손으로 머리를 잡고 천천히 옆으로 당겨주세요.")
    st.write("- 반대쪽도 동일하게 10~15초 유지합니다.")
    st.warning("⚠️ 통증이 심하면 중단하세요.")

elif body_part == "어깨":
    st.subheader("📌 어깨 스트레칭")
    st.image("https://www.verywellfit.com/thmb/91GmC8E8hB5xYpSzH-wT7QbXYRA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/shoulder-stretch-56a8e6c35f9b58b7d0f8a9f1.jpg", caption="어깨 가슴 스트레칭")
    st.write("- 팔을 가슴 앞으로 교차시켜 반대 손으로 잡아주세요.")
    st.write("- 15~20초간 유지하며 양쪽 어깨 모두 시행합니다.")
    st.warning("⚠️ 어깨 충돌 증후군이 있으면 조심하세요.")

elif body_part == "허리":
    st.subheader("📌 허리 스트레칭")
    st.image("https://www.verywellhealth.com/thmb/yLwKy7zj8-nmK4IupWquYeqiYPo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/knee-to-chest-stretch-56a8e6a23df78cf772a1df2d.jpg", caption="무릎 당기기 스트레칭")
    st.write("- 바닥에 누워 무릎을 가슴 쪽으로 당겨주세요.")
    st.write("- 허리가 바닥에 붙도록 유지하면서 15초간 실시합니다.")
    st.warning("⚠️ 허리 디스크 환자는 무리하지 마세요.")

elif body_part == "무릎":
    st.subheader("📌 무릎 근력 강화 운동")
    st.image("https://www.verywellfit.com/thmb/5W7Wq3XU8f4zTHkDJ5Tmn7Q7DYw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/straightlegraise-56a8e6f45f9b58b7d0f8ab9d.jpg", caption="무릎 스트레이트 레그 레이즈")
    st.write("- 바닥에 누워 한쪽 다리를 곧게 펴고 천천히 들어올립니다.")
    st.write("- 10회씩 3세트 진행하세요.")
    st.warning("⚠️ 무릎 통증이 심하면 중단하세요.")

elif body_part == "손목":
    st.subheader("📌 손목 스트레칭")
    st.image("https://www.verywellhealth.com/thmb/RWlG8Q6p2ClJvRU4Fod4c1H0rRU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/wrist-flexor-stretch-56a8e6f33df78cf772a1dfeb.jpg", caption="손목 굴곡 스트레칭")
    st.write("- 한쪽 팔을 앞으로 뻗고 손바닥을 위로 향하게 합니다.")
    st.write("- 반대 손으로 손끝을 잡고 천천히 젖혀줍니다.")
    st.warning("⚠️ 손목 터널 증후군이 있으면 전문가 상담이 필요합니다.")

# 공통 안내
st.info("💡 운동은 통증이 없는 범위 내에서만 실시하세요. 통증이 심하면 전문가에게 상담을 권장합니다.")
