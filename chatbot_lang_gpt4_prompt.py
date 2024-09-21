import os
from getpass import getpass
from langchain.document_loaders import TextLoader  # 텍스트 파일을 로드하는데 사용.
from langchain.indexes import VectorstoreIndexCreator  # 문서의 벡터 인덱스를 생성.
from langchain.embeddings.openai import OpenAIEmbeddings  # OpenAI의 임베딩 사용
from langchain.chat_models import ChatOpenAI  # OpenAI 챗 모델을 사용하는 클래스
from langchain.schema import AIMessage  # 응답 객체를 처리하기 위한 AIMessage 클래스 임포트

# API 키 설정
try:
    os.environ["OPENAI_API_KEY"] = getpass("OpenAI API 키를 입력하세요: ")
except Exception as e:
    print(f"API 키를 설정하는 중 문제가 발생했습니다: {e}")
    exit()

# 문서 로드
try:
    loader = TextLoader('C:\\Users\\dkryu\\OneDrive\\문서\\kict240915_chatbot\\data\\data.txt', encoding='utf-8')  # 준비된 텍스트 파일 로드 (화학사고 및 화재 대응법)
except FileNotFoundError:
    print("문서가 존재하지 않습니다. 'document.txt' 파일이 있는지 확인하세요.")
    exit()

# 인덱스 생성
try:
    embeddings = OpenAIEmbeddings()  # 임베딩 처리
    index = VectorstoreIndexCreator(embedding=embeddings).from_loaders([loader])  # 문서의 벡터 인덱스 생성
except Exception as e:
    print(f"인덱스를 생성하는 중 문제가 발생했습니다: {e}")
    exit()

# OpenAI GPT-4 챗 모델 생성
try:
    llm = ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=300)  # GPT-4 챗 모델 사용
except Exception as e:
    print(f"언어 모델을 생성하는 중 문제가 발생했습니다: {e}")
    exit()

# 챗봇과의 대화 기능 - 프롬프트 엔지니어링 적용
while True:
    query = input("\n화학사고/화재 대응에 대해 궁금한 사항을 입력하세요 (종료하려면 'exit' 입력): ")

    if query.lower() == "exit":
        print("챗봇을 종료합니다.")
        break

    # 대화 프롬프트 설정 (랩퍼 소방관 스타일)
    messages = [
        {
            "role": "system",
            "content": (
                "Yo, 나는 랩퍼 소방관! "
                "화재 대응부터 소방 안전까지, 리듬 타며 정보를 전해 줄게. "
                "위급 상황에서는 차분하게 대응하고, 소방 지식은 철저하게 알려줘. "
                "모르는 건 모른다고, 확실하지 않으면 확실하지 않다고 말하는 게 나의 방식. "
                "랩처럼 빠르고 리듬 있는 설명을 즐겨!"
            ),
        },
        {
            "role": "user",
            "content": query,
        }
    ]

    # 질문-답변 처리 (invoke 메서드 사용)
    try:
        response = llm.invoke(input=messages)  # invoke 메서드에 input 인수로 메시지 전달
        if isinstance(response, AIMessage):  # 응답이 AIMessage 객체인 경우 처리
            print(f"\n챗봇 응답: {response.content}")  # content 속성으로 메시지 내용 추출
        else:
            print(f"응답이 예상한 형식이 아닙니다: {response}")
    except Exception as e:
        print(f"응답을 생성하는 중 문제가 발생했습니다: {e}")



