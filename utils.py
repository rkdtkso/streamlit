import streamlit as st
from openai import OpenAI

DEFAULT_MODEL = "gpt-4.1-mini"


def render_api_key_input() -> str:
    """Render a shared API-key input. Multipage apps share session_state."""
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


def require_api_key() -> str:
    api_key = render_api_key_input()
    if not api_key:
        st.info("왼쪽 사이드바에 OpenAI API Key를 입력하세요.")
        st.stop()
    return api_key


@st.cache_data(show_spinner="LLM 응답을 생성하는 중입니다...")
def cached_simple_response(api_key: str, question: str, model: str = DEFAULT_MODEL) -> str:
    """Return a cached OpenAI Responses API result for unchanged inputs."""
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        input=question,
    )
    return response.output_text


def response_from_messages(
    api_key: str,
    messages: list[dict],
    model: str = DEFAULT_MODEL,
    instructions: str | None = None,
    tools: list[dict] | None = None,
) -> str:
    client = OpenAI(api_key=api_key)
    kwargs = {
        "model": model,
        "input": messages,
    }
    if instructions:
        kwargs["instructions"] = instructions
    if tools:
        kwargs["tools"] = tools
    response = client.responses.create(**kwargs)
    return response.output_text
