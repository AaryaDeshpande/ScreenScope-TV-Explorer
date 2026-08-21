from screenscope.api import BASE_URL, REQUEST_TIMEOUT_SECONDS


def test_tvmaze_api_configuration() -> None:
    assert BASE_URL == "https://api.tvmaze.com"
    assert REQUEST_TIMEOUT_SECONDS > 0

