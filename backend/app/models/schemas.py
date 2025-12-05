from pydantic import BaseModel

class IngestRequest(BaseModel):
    source: str                 # 파일 이름 또는 문서 출처
    text: str                   # 문서 전체 텍스트
