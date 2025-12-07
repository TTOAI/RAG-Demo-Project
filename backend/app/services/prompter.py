def build_prompt(query: str, contexts: list):
    context_text = "\n\n".join([c["text"] for c in contexts])

    prompt = (
        "다음은 참고할 문서 조각들이야.\n"
        "----------------------\n"
        f"{context_text}\n"
        "----------------------\n"
        "위 문서 내용을 참고해서 답변해. "
        "문서에 없는 내용은 추측하지 말고 '정보 없음'이라고 말해.\n\n"
        f"질문: {query}\n"
        "답변:"
    )

    return prompt.strip()
