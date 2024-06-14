
from summarization import summarize_text
import google.generativeai as genai
import os

GOOGLE_API_KEY= "google_api_key"

genai.configure(api_key=GOOGLE_API_KEY)


def generate_content(mail):
    model = genai.GenerativeModel('gemini-pro')

    speech = mail["speech"]
    contents = mail["contents"]
    length = mail["length"]
    subject = mail["subject"]


    response_summary = summarize_text(contents, length) 

    response_speech = model.generate_content(f'다음 문장을 {speech}: 어투로 바꿔줘'+response_summary.text)
    print(response_speech.text)

    return response_speech.text


mail = {
    "speech": "과거를 떠올려보자. 방송을 보던 우리의 모습을. 독보적인 매체는 TV였다. 온 가족이 둘러앉아 TV를 봤다. 간혹 가족들끼리 뉴스와 드라마, 예능 프로그램을 둘러싸고 리모컨 쟁탈전이 벌어지기도  했다. 각자 선호하는 프로그램을 ‘본방’으로 보기 위한 싸움이었다. TV가 한 대인지 두 대인지 여부도 그래서 중요했다. 지금은 어떤가. ‘안방극장’이라는 말은 옛말이 됐다. TV가 없는 집도 많다. 미디어의 혜 택을 누릴 수 있는 방법은 늘어났다. 각자의 방에서 각자의 휴대폰으로, 노트북으로, 태블릿으로 콘텐츠 를 즐긴다.",
    "contents": "과거를 떠올려보자. 방송을 보던 우리의 모습을. 독보적인 매체는 TV였다. 온 가족이 둘러앉아 TV를 봤다. 간혹 가족들끼리 뉴스와 드라마, 예능 프로그램을 둘러싸고 리모컨 쟁탈전이 벌어지기도  했다. 각자 선호하는 프로그램을 ‘본방’으로 보기 위한 싸움이었다. TV가 한 대인지 두 대인지 여부도 그래서 중요했다. 지",
    "subject": "과거를 떠올려보자",
    "length": 20
}

    

generate_content(mail)