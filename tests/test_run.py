import pytest

from src.yatl.utils import (
    DirectoryNotFoundError,
    create_context,
    is_skipped,
    load_test_yaml,
    search_files,
)


def test_create_context_with_valid_data_returns_context(data):
    "Test that create_context returns a context with valid data."
    context = create_context(data)
    assert context is not None
    assert context["base_url"] == "https://yandex.ru"
    assert context["name"] == "ping"


def test_create_context_with_empty_data_returns_empty_context():
    "Test that create_context returns an empty context with empty data."
    context = create_context({})
    assert len(context) == 0


@pytest.mark.parametrize("expected", [True, False])
def test_is_skipped(expected):
    """Проверяет, что is_skipped возвращает значение ключа 'skip' (по умолчанию False)."""
    item = {"skip": expected}
    assert is_skipped(item) is expected


def test_load_test_yaml():
    "Test that load_test_yaml returns a dictionary with test data."
    data = load_test_yaml("tests/data/ping.yatl.yaml")
    assert data is not None
    assert len(data) > 0


def test_load_test_yaml_with_invalid_file():
    "Test that load_test_yaml returns None with invalid file."
    with pytest.raises(FileNotFoundError):
        load_test_yaml("tests/data/not_found.yatl.yaml.invalid")


def test_search_files():
    "Test that search_files returns a list of files."
    files = search_files("tests/data")
    assert len(files) == 2


@pytest.mark.parametrize("content", ["", "  \n\t", "# comment\n  # another comment\n"])
def test_search_files_ignores_empty_yaml_files(tmp_path, content):
    "Test that empty YAML files are excluded from test discovery."
    empty_test = tmp_path / "empty.yatl.yaml"
    empty_test.write_text(content, encoding="utf-8")

    assert search_files(str(tmp_path)) == []
    assert search_files(str(empty_test)) == []


def test_search_files_with_invalid_path():
    "Test that search_files raises a clear error with invalid path."
    with pytest.raises(
        DirectoryNotFoundError, match="Directory does not exist: tests/data/not_found"
    ):
        search_files("tests/data/not_found")
