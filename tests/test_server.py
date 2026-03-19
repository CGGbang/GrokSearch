from grok_search.server import _build_web_search_content


def test_build_web_search_content_prefers_clean_answer():
    content = _build_web_search_content(
        "<think>hidden</think>\nVisible answer.",
        [],
        None,
    )
    assert content == "Visible answer."


def test_build_web_search_content_returns_error_message_when_grok_fails():
    content = _build_web_search_content(
        "",
        [{"url": "https://example.com"}],
        "HTTPStatusError: 502 Bad Gateway",
    )
    assert content == "Grok answer generation failed: HTTPStatusError: 502 Bad Gateway"
