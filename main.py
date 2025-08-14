# from dotenv import load_dotenv
# load_dotenv()

# 인증키 가져오기 (환경 변수에 등록한 API 키를 가져옴)
# import os
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API를 직접 사용하는 방법
# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은 ")
# print(result)

import streamlit as st
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title("인공지능 시인")
content = st.text_input('시의 주제를 제시해주세요')

if st.button("시 작성 요청하기"):
    with st.spinner(content + '에 대한 시 작성중'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)

# # Completion 요청 (prompt -> completion)
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         # developer 역할 - 전반적인 동작 방식 정의
#         {"role": "developer", "content": "You are a helpful programming assistant."},
#         # user 역할 - 실제 요청 내용
#         {"role": "user", "content": "파이썬에서 파일을 읽는 방법을 알려주세요."},
#     ],
#     temperature=0.7,
#     max_tokens=1000,
# )

# # 결과 출력
# print(response)
# print("="*100)
# print("id:", response.id)
# print("-"*100)
# print('model:', response.model)
# print("-"*100)
# print("text:", response.choices[0].message.content)
# print("-"*100)
# print("usage:", response.usage)