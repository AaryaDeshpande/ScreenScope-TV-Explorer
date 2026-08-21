import pytest

from screenscope.api import BASE_URL, IMAGE_BASE_URL, build_headers


def test_tmdb_api_configuration() -> None:
    assert BASE_URL == "https://api.themoviedb.org/3"
    assert IMAGE_BASE_URL == "https://image.tmdb.org/t/p/w500"


def test_bearer_headers() -> None:
    headers = build_headers("example-token")
    assert headers["Authorization"] == "Bearer example-token"
    assert headers["accept"] == "application/json"


def test_empty_bearer_token_is_rejected() -> None:
    with pytest.raises(ValueError):
        build_headers("  ")
