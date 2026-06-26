from app.services.repo_service import RepositoryService

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
        "rhello world"
    )