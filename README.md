# Lab02 Streamlit LLM App

실습 PDF 요구사항에 맞춘 Streamlit 멀티페이지 앱입니다.

## 파일 구조

```text
streamlit_app.py
pages/
  1_Chat.py
  2_Library_Chatbot.py
  3_ChatPDF.py
requirements.txt
```

`utils.py`를 따로 두지 않고, 각 페이지 파일 안에 필요한 OpenAI 호출 함수와 API Key 입력 함수를 포함했습니다.

## 기능

1. 첫 페이지
   - OpenAI API Key를 `st.text_input(..., type="password")`로 입력
   - API Key를 `st.session_state.openai_api_key`에 저장
   - 질문 입력 후 OpenAI Responses API 응답 출력
   - `@st.cache_data`로 같은 입력이면 캐시된 응답 반환

2. Chat 페이지
   - `st.chat_input`, `st.chat_message`를 이용한 채팅 UI
   - OpenAI Responses API 사용
   - Clear 버튼으로 기존 대화 삭제

3. Library Chatbot 페이지
   - 국립부경대학교 도서관 규정/운영세칙 핵심 내용을 문자열로 저장
   - 해당 문자열을 근거로 답변
   - 예시 질문: 도서관 휴관일, 학부생 책 대여 권수

4. ChatPDF 페이지
   - `st.file_uploader`로 PDF 1개 업로드
   - OpenAI Vector Store + File Search 사용
   - Clear 버튼으로 대화 내용과 vector store 삭제

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Streamlit Cloud 배포

1. 이 폴더의 파일을 GitHub 저장소에 업로드합니다.
2. Streamlit Cloud에서 GitHub 계정으로 로그인합니다.
3. `Create app`을 누릅니다.
4. 저장소를 선택하고 Main file path를 `streamlit_app.py`로 설정합니다.
5. Deploy 후 생성된 앱 링크를 제출합니다.

## 주의

OpenAI API Key는 앱 화면에서 입력받도록 구현되어 있으므로 GitHub에 API Key를 올리지 마세요.
