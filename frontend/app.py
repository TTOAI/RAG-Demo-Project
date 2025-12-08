import os
from typing import Any, Dict, List

import requests
import streamlit as st


DEFAULT_BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def get_backend_url(raw_url: str) -> str:
    url = raw_url.strip()
    if url.endswith("/"):
        url = url[:-1]
    return url or DEFAULT_BACKEND_URL


def call_api(method: str, url: str, **kwargs) -> Dict[str, Any]:
    resp = requests.request(method, url, timeout=30, **kwargs)
    resp.raise_for_status()
    return resp.json()


def render_header() -> str:
    st.set_page_config(page_title="RAG Demo", layout="wide")
    st.title("RAG Demo (FastAPI + Streamlit)")
    st.caption("Ask questions against your ingested documents through the existing FastAPI backend.")

    backend_input = st.text_input("Backend URL", value=DEFAULT_BACKEND_URL)
    backend_url = get_backend_url(backend_input)

    cols = st.columns(3)
    with cols[0]:
        if st.button("Check Backend Health"):
            try:
                data = call_api("GET", f"{backend_url}/")
                st.success(f"Backend reachable: {data}")
            except Exception as e:  # noqa: BLE001
                st.error(f"Health check failed: {e}")

    with cols[1]:
        st.write("Endpoints used: `/query` (RAG) and `/search` (vector search).")
    with cols[2]:
        st.write("Tip: keep this app running while you ingest content via the backend.")

    st.divider()
    return backend_url


def render_query_tab(backend_url: str) -> None:
    st.subheader("Ask with RAG (`/query`)")
    question = st.text_area("Ask a question", placeholder="예: 학사 경고 기준이 어떻게 되나요?", height=120)
    ask = st.button("Ask", type="primary")

    if ask:
        if not question.strip():
            st.warning("질문을 입력해 주세요.")
            return

        with st.spinner("Querying backend..."):
            try:
                data = call_api("GET", f"{backend_url}/query", params={"q": question})
            except Exception as e:  # noqa: BLE001
                st.error(f"요청 실패: {e}")
                return

        st.success("답변을 가져왔습니다.")
        st.markdown("**Answer**")
        st.write(data.get("answer", ""))

        evidences: List[Dict[str, Any]] = data.get("evidences", [])
        if evidences:
            with st.expander("근거 보기 (retrieved chunks)"):
                for idx, ev in enumerate(evidences, start=1):
                    st.markdown(f"**{idx}. score={ev.get('score')} source={ev.get('source')} chunk_id={ev.get('chunk_id')}**")
                    st.write(ev.get("text", ""))
                    st.divider()


def render_search_tab(backend_url: str) -> None:
    st.subheader("Vector Search (`/search`)")
    query = st.text_area("Search query", placeholder="예: 휴학 신청 절차", height=100)
    top_k = st.slider("Top K", min_value=1, max_value=10, value=5)
    search = st.button("Search")

    if search:
        if not query.strip():
            st.warning("검색어를 입력해 주세요.")
            return

        with st.spinner("Searching in Qdrant..."):
            try:
                data = call_api("GET", f"{backend_url}/search", params={"q": query, "top_k": top_k})
            except Exception as e:  # noqa: BLE001
                st.error(f"검색 실패: {e}")
                return

        st.success("검색 결과를 가져왔습니다.")
        for idx, hit in enumerate(data, start=1):
            st.markdown(f"**{idx}. score={hit.get('score')} source={hit.get('source')} chunk_id={hit.get('chunk_id')}**")
            st.write(hit.get("text", ""))
            st.divider()


def main() -> None:
    backend_url = render_header()
    tab1, tab2 = st.tabs(["Ask (RAG)", "Search only"])
    with tab1:
        render_query_tab(backend_url)
    with tab2:
        render_search_tab(backend_url)


if __name__ == "__main__":
    main()
