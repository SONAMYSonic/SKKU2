import streamlit as st
from openai import OpenAI

OPENAI_KEY = st.secrets["API_KEY"]

# 1. 키와 함께 ChatGPT에 접속한다.
client = OpenAI(
    api_key=OPENAI_KEY,
)

st.title("🎁제품 홍보 포스터 생성기")
keyword = st.text_input("키워드를 입력하세요.")

# 2. 모델과 함께 내용을 입력해서 요청한다.
if st.button("생성하기🔥"):
    if not keyword:
        st.warning("키워드를 입력해주세요!")
    else:
        with st.spinner("홍보 문구 생성 중... 잠시만 기다려주세요."):
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "입력 받은 키워드에 대한 300자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
                    },
                    {
                        "role": "user",
                        "content": keyword,
                    }

                ],
                model="gpt-4o-mini",
            )

        result = chat_completion.choices[0].message.content
        st.write(result)

        with st.spinner("이미지 생성 중입니다."):
            response = client.images.generate(
                model="dall-e-3",
                prompt="제품 홍보를 위한 이미지 생성: " + keyword,
                size="1024x1024",
                n=1,
            )

        image_url = response.data[0].url
        st.image(image_url, caption="생성된 홍보 이미지", use_column_width=True)