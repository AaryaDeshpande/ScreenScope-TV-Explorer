from screenscope.analysis import episodes_to_dataframe
from screenscope.contracts import EPISODE_FIELDS


def test_empty_episode_dataframe_uses_shared_columns() -> None:
    frame = episodes_to_dataframe([])
    assert tuple(frame.columns) == EPISODE_FIELDS
    assert frame.empty

