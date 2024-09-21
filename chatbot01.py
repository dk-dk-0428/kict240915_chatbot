import openai
import getpass

# 터미널에서 사용자로부터 API 키를 입력받기
api_key = getpass.getpass("OpenAI API 키를 입력하세요: ")

# OpenAI API 설정
openai.api_key = api_key

# 여러 인코딩 시도 및 문서 내용 로드 함수
def load_document(file_path):
    encodings = ['utf-8', 'ISO-8859-1', 'Windows-1252']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"{file_path} 파일을 읽을 수 없습니다. 지원되는 인코딩이 없습니다.")

# 여러 문서 내용을 하나로 합치는 함수
def load_multiple_documents(file_paths):
    combined_document = ""
    for file_path in file_paths:
        document_content = load_document(file_path)
        combined_document += document_content + "\n"  # 문서들 사이에 구분을 위해 줄바꿈 추가
    return combined_document

# 질문-답변 생성 함수 (최신 API 방식으로 수정)
def ask_question(documents, question):
    prompt = f"다음 문서를 바탕으로 질문에 답하세요:\n\n{documents}\n\n질문: {question}\n답변:"

    # OpenAI API 호출 (최신 GPT-3.5 또는 GPT-4 모델 사용)
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 또는 "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7  # 응답의 다양성 조절
    )

    # 응답에서 가장 첫 번째 메시지 선택
    ai_message = response['choices'][0]['message']['content'].strip()
    return ai_message

# 4개의 텍스트 파일 경로
file_paths = ['C:\\Users\\dkryu\\OneDrive\\문서\\kict240915_chatbot\\data\\화학물질화재블로그등​.txt']

# 여러 문서의 내용을 하나로 합침
combined_documents = load_multiple_documents(file_paths)

# 질문에 대한 응답 생성
query = "염산으로 인한 화재 발생시 대응은?"
response = ask_question(combined_documents, query)

# 결과 출력
print(response)
