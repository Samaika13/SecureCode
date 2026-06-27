from app.services.repo_service import RepositoryService

path = RepositoryService.clone_repository(
    "https://github.com/openai/openai-python"
)

print(path)