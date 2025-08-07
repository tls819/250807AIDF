import streamlit as st

st.title("MBTI 여행지 추천기 ✈️")
st.subheader("당신의 MBTI에 맞는 여행지를 추천해드립니다!")

# MBTI 선택
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# MBTI별 추천 여행지 데이터
mbti_travel = {
    "INTJ": "아이슬란드 - 조용하고 신비로운 대자연",
    "INTP": "스위스 - 질서와 논리가 살아있는 나라",
    "ENTJ": "뉴욕 - 야망과 도전이 가득한 도시",
    "ENTP": "도쿄 - 창의력과 변화가 공존하는 도시",
    "INFJ": "부탄 - 평화롭고 내면에 집중할 수 있는 곳",
    "INFP": "체코 프라하 - 감성적인 분위기의 도시",
    "ENFJ": "이탈리아 로마 - 문화와 사람 중심의 도시",
    "ENFP": "스페인 바르셀로나 - 자유롭고 활기찬 에너지",
    "ISTJ": "독일 뮌헨 - 체계적이고 안정된 분위기",
    "ISFJ": "영국 코츠월드 - 조용하고 전통적인 마을",
    "ESTJ": "싱가포르 - 효율적이고 깔끔한 도시",
    "ESFJ": "프랑스 파리 - 사교적이고 아름다운 분위기",
    "ISTP": "호주 퀸즈랜드 - 모험과 자연이 있는 지역",
    "ISFP": "발리 - 예술적이고 감성적인 휴양지",
    "ESTP": "미국 라스베이거스 - 활기찬 도시와 즐길거리",
    "ESFP": "태국 방콕 - 화려하고 에너지 넘치는 도시"
}

# 추천 결과 출력
if selected_mbti:
    destination = mbti_travel.get(selected_mbti, "추천 여행지가 없습니다.")
    st.markdown(f"### 🧭 {selected_mbti} 유형에게 추천하는 여행지는:")
    st.success(f"**{destination}**")
