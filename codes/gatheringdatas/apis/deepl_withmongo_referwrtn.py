# refer from : https://velog.io/@king/deepl-api
# > pip install deepl # from https://pypi.org/project/deepl/

import pymongo
import deepl

# MongoDB 연결 설정
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['study_test']
collection = db['chatdoctor_dataset']

# Deepl API 토큰 설정
deepl_token = 'your auth_key'
translator = deepl.Translator(deepl_token)

# 주기적으로 실행할 함수
def translate_documents():
    # MongoDB에서 문서 가져오기
    documents = collection.find({}).limit(2)
    
    for document in documents:
        # 필요한 필드 추출
        instruction = document['instruction']
        input_text = document['input']
        
        # Deepl API 호출 및 응답 처리
        message = instruction
        result = translator.translate_text(message, target_lang="KO")

        print(result.text)        
        if response.status_code == 200:
            translation_result = response.json()['translations'][0]['text']
            
            # 번역 결과를 MongoDB에 업데이트
            collection.update_one(
                {'_id': document['_id']},
                {'$set': {'output': translation_result}}
            )

# import time            
def main():
    translate_documents()
    # while True:
    #     translate_documents()
        
    #     # 주기적으로 실행할 시간 간격 (예: 1시간마다)
    #     time.sleep(3600)

if __name__ == '__main__':
    main()
