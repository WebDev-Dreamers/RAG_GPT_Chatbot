from openai import OpenAI
import os

# GPT API key 가져오기
api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(text):
    
    # OpenAI API 인스턴스 생성 시 API 키 전달
    client = OpenAI(api_key=api_key)

    print(text)
    
    # GPT API에 대화 요청 보내기
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}  # 음성 인식으로 변환된 텍스트 입력
        ]
    )

    return response.choices[0].message


# 텍스트 입력
text = '안녕, 너를 소개해줘'


# GPT API 호출하여 필요한 정보 추출
message = get_gpt_response(text)


print(message.content)               # 안녕하세요! 저는 당신의 도움이 되는 인공지능 비서입니다. 궁금한 점이 있거나 도움이 필요하신 경우 언제든지 물어보세요. 어떻게 도와드릴까요?