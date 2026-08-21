from screenscope.analysis import results_to_dataframe
from screenscope.contracts import MEDIA_FIELDS


def test_empty_results_dataframe_uses_shared_columns() -> None:
    frame = results_to_dataframe([])
    assert tuple(frame.columns) == MEDIA_FIELDS
    assert frame.empty
