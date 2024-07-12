import re
import requests
import pandas as pd

# 정규 표현식을 사용하여 특수문자 제거
def clean_text(text):
    text = re.sub(r'[^\?가-힣A-Z0-9\s]', '', text)  # 한글, 영어, 숫자, 공백만 남기기
    text = re.sub(r'\s+', ' ', text)              # 여러 공백을 하나로
    return text



# AIVLE 지원자 QA 홈페이지 Crawling
def crawling():
    # 세션 객체 생성
    session = requests.Session()

    # 세션 내에서 첫 번째 요청 보내기 (예: 로그인)
    session_url = 'https://aivle.kt.co.kr/home/brd/faq/main?mcd=MC00000056'

    response = session.get(session_url)
    response.raise_for_status()  # 요청 성공 여부 확인

    data_list = []

    # 로그인 후 세션을 통해 다른 요청 보내기
    for i in range(8):
        data_url = f'https://aivle.kt.co.kr/home/brd/faq/listJson?ctgrCd=&pageIndex={i}'
        response = session.get(data_url)

        data = response.json()
        
        for ele in data['returnList']:
            
            category = clean_text(ele['ctgrNm'])
            content = clean_text(ele['atclTitle'] + ele['atclCts'])
            
            item = {
                'category': category,
                'content': content
            }
            
            data_list.append(item)


    # 데이터프레임 생성
    data = pd.DataFrame(data_list)

    # 세션 종료
    session.close()

    # 데이터프레임을 CSV 파일로 저장
    csv_filename = 'a.csv'
    data.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    return data


crawling()

