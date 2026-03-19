from grok_search.sources import sanitize_answer_text, split_answer_and_sources


def test_sanitize_answer_text_strips_think_blocks():
    text = "<think>\ninternal reasoning\n</think>\nThe capital of France is Paris."
    assert sanitize_answer_text(text) == "The capital of France is Paris."


def test_split_answer_and_sources_strips_think_and_keeps_sources():
    text = """
<think>
internal reasoning
</think>
The capital of France is Paris.

## Sources
- [Britannica](https://www.britannica.com/place/France)
""".strip()
    answer, sources = split_answer_and_sources(text)
    assert answer == "The capital of France is Paris."
    assert sources == [{"title": "Britannica", "url": "https://www.britannica.com/place/France"}]
