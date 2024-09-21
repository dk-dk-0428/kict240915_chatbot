# TEAM PROJECT
 ## 개요 
 프로젝트 폴더 : kict240915_chatbot(류동경 로컬)  
 팀명 : 도전챗봇  
 팀원 : 박보람, 배소정, 류동경, 문소정  
 주제 : 특수화재(화확약품) 대응 가이드 챗봇  

 ## Installation(사용된 패키지) 

```

pip streamlit==1.38.0
pip openai==1.44.0
pip tiktoken==0.7.0
pip langchain==0.3.0
pip unstructured==0.15.12
pip nltk==3.7
pip python-magic
pip langchain-community
pip requests
```

##개발적용
 - langchain 사용
 - 프롬프트 엔지니어링 적용 : 전 후 확실한 변화를 보기 위해 페르소나 확실히 부여 "랩퍼소방관"
 - 스트림릿 적용
 - gpt4 사용 => gpt4o-mini 로 변경사용 추천

  

## 결과예시
pdf를 텍스트로 변환 코드 : pdf_file.py  

최종완성파일 : chatbot_lang_gpt4_prompt_streamlit.py
![119chatbot_result](119chatbot_result.png)

## RAG 파일
 data.txt  
 <참고> 
  data.txt dhl 파일은 rag 구축에 활용하고자 하였으나 실패한 자료임
  | 연번 | 파일명                                                | 결과       |
  |------|------------------------------------------------------|------------|
  | 1    | (아파트관리자) 화재 피난안전매뉴얼.pdf                  | 변환성공했으나, 파일 너무 커서 사용 못함    |
  | 2    | (아파트입주자) 화재 피난행동 요령.pdf                   | 변환성공했으나, 파일 너무 커서 사용 못함     |
  | 3    | 2020 유해물질 비상대응 핸드북.pdf                      | 변환성공했으나, 파일 너무 커서 사용 못함     |
  | 4    | 특수화재 대응매뉴얼. pdf                               | 변환성공했으나, 파일 너무 커서 사용 못함   |   
  | 5    | 화재폭발 누출사고 예방가이드북.pdf                      | 그림파일인듯.  텍스트 변환 안됨            |
  | 6    | 화학사고 현장 대응 물질 정보집.pdf                      | 그림파일인듯.  텍스트 변환 안됨   |
  | 7    | 화학사고 테러 대응장비 사용자 운영 매뉴얼(2020).pdf      | 그림파일인듯.  텍스트 변환 안됨   |
  

 
 
 

