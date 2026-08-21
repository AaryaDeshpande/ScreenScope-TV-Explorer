from screenscope.contracts import DETAIL_FIELDS, MEDIA_FIELDS, SUPPORTED_MEDIA_TYPES


def test_shared_contracts_have_unique_fields() -> None:
    assert len(MEDIA_FIELDS) == len(set(MEDIA_FIELDS))
    assert len(DETAIL_FIELDS) == len(set(DETAIL_FIELDS))


def test_core_media_fields_are_present() -> None:
    required = {"id", "media_type", "title", "rating", "popularity"}
    assert required.issubset(MEDIA_FIELDS)
    assert SUPPORTED_MEDIA_TYPES == ("movie", "tv")
