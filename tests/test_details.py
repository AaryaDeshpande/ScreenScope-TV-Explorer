from screenscope.details import plain_text_summary


def test_plain_text_summary_removes_html() -> None:
    assert plain_text_summary("<p>A <b>great</b> show.</p>") == "A great show."


def test_plain_text_summary_handles_missing_value() -> None:
    assert plain_text_summary(None) == "No summary is available."

