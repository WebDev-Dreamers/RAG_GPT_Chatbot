## langchain 라이브러리 기반 Chroma DB 구성 파일

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import pandas as pd


# 추가 수집한 QA 추가
def add_vectorDB():
    embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
    database = Chroma(persist_directory = "./vectorDB", embedding_function = embeddings)
    
    # CSV 파일 불러오기
    csv_filename = 'aivle_faq.csv'
    data = pd.read_csv(csv_filename, encoding='utf-8-sig')

    # CSV -> List로 변환
    text_list = data['content'].tolist()
    meta_list = []
    for meta in data['category'].tolist():
        meta_list.append({'category' : meta})
        
    # 모든 QA 리스트 document 구성
    documents = [Document(metadata = meta_list[i], page_content=text_list[i]) for i in range(len(text_list))]

    # document DB에 추가
    database.add_documents(documents)
    
    print('Vector DB에 새로운 Data가 추가되었습니다.')


add_vectorDB()