from openai import OpenAI
import os
from getpass import getpass
import chardet

# API 키를 안전하게 입력받음
# API_KEY = getpass.getpass("OpenAI API 키를 입력하세요: ")
os.environ["OPENAI_API_KEY"] = getpass("OpenAI API 키를 입력하세요: ")