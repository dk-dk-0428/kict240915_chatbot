import PyPDF2

def extract_text_from_pdf_and_save(pdf_file, output_filename):
    # PDF 파일에서 텍스트 추출
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # 텍스트 파일로 저장
    with open(output_filename, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

    # 다운로드 링크 제공
    return output_filename

# 예시 사용
pdf_file_path = "C:\\Users\\dkryu\\OneDrive\\문서\\kict240915_chatbot\\data\\(아파트 관리자) 화재 피난안전 매뉴얼.pdf"  # 입력 PDF 파일 경로
output_text_file = "C:\\Users\\dkryu\\OneDrive\\문서\\kict240915_chatbot\\data\\(아파트 관리자) 화재 피난안전 매뉴얼.txt"  # 출력 텍스트 파일 경로

# PDF에서 텍스트 추출 및 파일 저장
extracted_file = extract_text_from_pdf_and_save(pdf_file_path, output_text_file)
print(f"텍스트 파일이 생성되었습니다: {extracted_file}")

