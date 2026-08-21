from screenscope.contracts import CAST_FIELDS, EPISODE_FIELDS, SHOW_FIELDS


def test_shared_contracts_have_unique_fields() -> None:
    assert len(SHOW_FIELDS) == len(set(SHOW_FIELDS))
    assert len(EPISODE_FIELDS) == len(set(EPISODE_FIELDS))
    assert len(CAST_FIELDS) == len(set(CAST_FIELDS))


def test_core_identifiers_are_present() -> None:
    assert {"id", "name"}.issubset(SHOW_FIELDS)
    assert {"id", "name", "season", "number"}.issubset(EPISODE_FIELDS)
    assert {"person_id", "person_name", "character_name"}.issubset(CAST_FIELDS)

