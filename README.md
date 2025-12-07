# foss-2025-2-final

## 이름
이주영

## 학번 
20216818

## 동기
<p>
LLM의 기술적 발전은 많은 곳에서 도움이 되고 있다.
하지만 LLM은 아직 학습하지 못한 최신 정보, 특정 분야, 조직 내부 데이터 등에 대해서는 정확한 답변을 주지 못한다.
또한 이것은 할루시네이션 문제 혹은 신뢰도가 낮고 설명력이 부족한 정보의 생성으로 이어진다.
<br>
이와 관련하여 본 프로젝트에서는 RAG를 사용하여 Qdrant를 포함한 다양한 무료 오픈소스 도구만으로 문서 기반 질의응답 시스템을 구현함으로써 사용자의 관심 분야에 대한 정확도 높은 답변을 제공하는 것을 목표로 한다.
</p>
<p>
검색 증강 생성(Retrieval-augmented generation, RAG)은 대형 언어 모델 (LLM)이 새로운 정보를 검색하고 통합할 수 있도록 하는 기술이다.
RAG를 사용하면 LLM은 지정된 문서 집합을 참조할 때까지 사용자 쿼리에 응답하지 않는다. 
이 문서들은 LLM의 기존 훈련 데이터의 정보를 보완한다.
이를 통해 LLM은 훈련 데이터에서 사용할 수 없는 도메인 특정 및 업데이트된 정보를 사용할 수 있다.
예를 들어, 이는 LLM 기반 챗봇이 내부 회사 데이터에 접근하거나 권위 있는 출처를 기반으로 응답을 생성하는 데 도움이 된다. 
(출처: [위키백과 - 검색증강생성성](https://ko.wikipedia.org/wiki/%EA%B2%80%EC%83%89%EC%A6%9D%EA%B0%95%EC%83%9D%EC%84%B1))
</p>

## 수행 내용

### 1. 실행환경 세팅
- Docker Compose 기반 FastAPI + Qdrant 환경 구성
- 서버 및 Swagger 정상 동작 확인

### 2. 문서 Ingestion & Chunking
- 문서 정제 기능 구현
- 문서를 일정 길이의 chunk로 분할
- `/ingest` API를 통해 chunk 결과 반환

### 3. Embedding
- Sentence-Transformers(all-MiniLM-L6-v2) 기반 embedding 적용
- `/test-embed` API로 embedding 벡터 테스트

### 4. Qdrant Vector DB upsert & search
- Qdrant 컬렉션 자동 생성
- chunk + embedding → Qdrant 저장
- `/search?q=` API로 관련 chunk 검색
- end-to-end ingestion 파이프라인 완성

## 토의

### 어려웠던 점

### 실험

### 비교 및 대안

#### 검색 엔진 / 벡터 데이터베이스
- Qdrant
    - 벡터 검색 품질 높음
    - 일반적인 문서 검색용 RAG
- Weaviate
    - GraphQL API라 개발 쉬움
    - multimodal vector 연동 쉬움
    - 이미지 + 텍스트 검색
- Elasticsearch
    - 키워드 검색
    - 하이브리드 검색 기반 RAG
- Milvus
    - 세계에서 가장 빠르고 확장성 좋은 벡터DB
    - 초대규모 RAG 시스템
- Vespa.ai
    - 대규모 검색엔진급 서비스

#### Agent/Workflow/RAG 프레임워크
- CrewAI
    - 핵심: Multi-Agent Collaboration
    - 각 Agent는 서로 다른 역할(Role), 업무(Task), 도구(Tool) 등을 가짐
    - Agent 간 메시지 전달로 협업
    - 협업 기반 Workflow
    - Orchestrator가 Workflow를 기반으로 Task 수행 제어
- LangGraph
    - 핵심: State Machine 기반 도구 오케스트레이션
    - Workflow를 State Machine 기반 그래프로 구성
    - 상태 확인 → 조건 평가 → Node(Agent/Tool) 호출 → 상태 업데이트 → 반복
- CAMEL-AI
    - 핵심: Role-Playing 기반 Multi-Agent Reasoning
    - Agent들은 역할(Role)에 기반해 서로 대화하며 문제 해결
    - Agent A 발화 → Agent B 발화 → Agent A 발화 → 반복
- LlamaIndex
    - 핵심: RAG에 최적화된 Pipeline Orchestration & Data Indexing
    - 다양한 데이터 소스를 구조화된 인덱스로 변환
    - Multilingual embedding, Multimodal embedding 등 RAG 데이터 인덱싱을 위한 자체 embedding 모델 제공
    - Query Engine이 질문 종류에 따라 최적의 RAG Retrieval Pipeline을 자동 구성

### 느낀 점
