from screenscope.details import display_title


def test_display_title_prefers_normalized_title() -> None:
    assert display_title({"title": "Dune", "original_title": "Dune"}) == "Dune"


def test_display_title_handles_missing_value() -> None:
    assert display_title({}) == "Untitled"
