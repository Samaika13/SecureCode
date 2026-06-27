from app.services.repo_service import RepositoryService
from pathlib import Path

def test_valid_github_url():
    assert RepositoryService.validate_github_url(
        "https://github.com/openai/openai-python"
    )

def test_invalid_github_url():
    assert not RepositoryService.validate_github_url(
        "https://google.com"
    )

def test_random_string():
    assert not RepositoryService.validate_github_url(
        "hello world"
    )

def test_get_repository_name():
    assert(
        RepositoryService.get_repository_name(
            "https://github.com/openai/openai-python"
        )
        == "openai-python"
    )

def test_repository_does_not_exist():
    Path("repos").mkdir(exist_ok=True)
    assert not RepositoryService.repository_exists(
        "this_repo_should_not_exist"
    )