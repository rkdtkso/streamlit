import streamlit as st
from openai import OpenAI

DEFAULT_MODEL = "gpt-4.1-mini"


def render_api_key_input() -> str:
    """API Key를 sidebar에서 입력받고 session_state에 저장합니다."""
    if "openai_api_key" not in st.session_state:
        st.session_state.openai_api_key = ""

    st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        key="openai_api_key",
        placeholder="sk-...",
        help="페이지를 이동해도 같은 세션에서는 값이 유지됩니다.",
    )
    return st.session_state.openai_api_key.strip()


@st.cache_data(show_spinner="LLM 응답을 생성하는 중입니다...")
def cached_simple_response(api_key: str, question: str, model: str = DEFAULT_MODEL) -> str:
    """입력이 같으면 OpenAI API를 다시 호출하지 않고 캐시된 응답을 반환합니다."""
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=question,
    )
    return response.output_text


st.set_page_config(page_title="Lab02 Streamlit LLM App", page_icon="🤖")

st.title("Lab02: LLM 응답 앱")
st.write(
    "질문을 입력하면 OpenAI Responses API로 응답을 생성합니다. "
    "동일한 API Key, 질문, 모델 조합은 `@st.cache_data`로 캐시됩니다."
)

api_key = render_api_key_input()
model = st.sidebar.selectbox(
    "Model",
    ["gpt-4.1-mini", "gpt-4.1", "gpt-4o-mini"],
    index=0,
)

question = st.text_area("질문을 입력하세요", height=160, placeholder="예: Streamlit의 session_state가 무엇인가요?")

col1, col2 = st.columns([1, 1])
with col1:
    submit = st.button("응답 생성", type="primary")
with col2:
    if st.button("캐시 비우기"):
        cached_simple_response.clear()
        st.success("캐시를 비웠습니다.")

if submit:
    if not api_key:
        st.warning("왼쪽 사이드바에 OpenAI API Key를 입력하세요.")
    elif not question.strip():
        st.warning("질문을 입력하세요.")
    else:
        try:
            answer = cached_simple_response(api_key, question.strip(), model)
            st.subheader("LLM 응답")
            st.markdown(answer)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

st.divider()
st.markdown(
    "### 구현 확인\n"
    "- `st.text_input(..., type='password')`로 API Key 입력\n"
    "- `st.session_state.openai_api_key`에 API Key 저장\n"
    "- `@st.cache_data`로 같은 입력의 LLM 응답 캐시\n"
    "- `pages/` 폴더를 이용한 Chat, Chatbot, ChatPDF 멀티페이지 구성\n"
    "- `utils.py` 없이 각 페이지 파일 안에 필요한 함수를 포함"
)
