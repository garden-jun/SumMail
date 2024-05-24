from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

import summarization
import speech



app = FastAPI()

class mail(BaseModel) :
	speech: str
	contents: str
	subject: str
	length: int


# api 테스트 코드
@app.get("/")
async def read_root() :
	return "This is root path from FastAPI Backend v3"


# 텍스트 요약
@app.get("/summary")
async def image_to_text(mail: mail):
	# return summarization.summary()
	return speech.generate_content(mail)
