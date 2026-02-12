import streamlit as st # 스트림릿 라이브러리 읽어와서 st라고 부르기

st.title("안녕하세요")

if st.button("노크하기"):
    st.write("여기 재만있어요~")

st.write("동의? 어 보감~ 하시면 아래 내용 체크~")
agree = st.checkbox("동의합니다")

if agree:
    st.write("당신은 동의했습니다.")

option = st.selectbox("연락을 어떻게 받을래요?", ("이메일", "전화", "문자"))

age = st.slider("몇살?", 0, 100)
st.write("저는" + str(age) + "살 입니다")

text_name = st.text_input("이름을 입력해주세요")
text_intro = st.text_area("자기소개 해주세요")

st.image("https://www.carscoops.com/wp-content/uploads/2024/11/Chevrolet-Corvette-ZR1-2.webp")

# streamlit run app.py

# 일반적으로 웹사이트를 만들기 위해서는
# HTML, CSS, 서버 언어를 알아야 한다
# 스트림릿을 이용하면 파이썬 하나로 모든게 가능하다