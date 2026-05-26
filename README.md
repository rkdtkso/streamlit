# Lab02 Streamlit LLM App

첨부 실습 PDF의 요구사항을 구현한 Streamlit 멀티페이지 앱입니다.

## 파일 구조

```text
streamlit_lab02_solution/
├── streamlit_app.py              # 1번: 질문 입력 → LLM 응답, API Key session_state, cache_data
├── utils.py                      # 공통 OpenAI/Session 함수
├── requirements.txt
└── pages/
    ├── 1_Chat.py                 # 2번: Chat 페이지, Responses API 챗봇, Clear 버튼
    ├── 2_Library_Chatbot.py      # 3번: 국립부경대학교 도서관 챗봇
    └── 3_ChatPDF.py              # 4번: PDF 업로드, OpenAI File Search, Vector store Clear
```

## 로컬 실행

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

브라우저가 열리면 왼쪽 사이드바에 OpenAI API Key를 입력하세요.

## GitHub 업로드

1. GitHub에서 새 저장소를 만듭니다.
2. 이 폴더 안의 파일을 모두 업로드합니다.
3. 저장소 루트에 `streamlit_app.py`, `requirements.txt`, `pages/` 폴더가 있어야 합니다.

## Streamlit Cloud 배포

1. Streamlit Cloud에 GitHub 계정으로 로그인합니다.
2. Create app을 누릅니다.
3. GitHub 저장소를 선택합니다.
4. Main file path를 `streamlit_app.py`로 지정합니다.
5. Deploy를 누릅니다.
6. 배포가 끝나면 생성된 Streamlit Cloud URL을 과제 제출란에 제출합니다.

## 제출 전 확인 체크리스트

- [ ] 첫 페이지에서 질문 입력 후 LLM 응답이 출력되는가?
- [ ] API Key가 페이지 이동 후에도 유지되는가?
- [ ] 동일한 질문/모델/API Key 조합에서 `@st.cache_data` 캐시가 작동하는가?
- [ ] Chat 페이지에서 대화가 이어지고 Clear 버튼으로 초기화되는가?
- [ ] Library Chatbot 페이지에서 "도서관 휴관일?", "학부생 책 대여 권수?"에 답하는가?
- [ ] ChatPDF 페이지에서 PDF 1개를 업로드하고 질문할 수 있는가?
- [ ] ChatPDF Clear 버튼이 vector store와 대화 내용을 삭제하는가?

## 참고

`pages/2_Library_Chatbot.py`의 `LIBRARY_RULES` 문자열은 과제 예시 질문에 답할 수 있도록 핵심 조항을 정리한 것입니다. 교수님이 원문 전체 삽입을 요구하면 국립부경대학교 규정집에서 도서관 규정/운영세칙 내용을 추가로 붙여 넣으세요.
