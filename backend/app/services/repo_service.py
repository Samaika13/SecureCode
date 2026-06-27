import re
import os
from pathlib import Path
from git import Repo

class RepositoryService:
    """Handles operations related to GitHub repositories"""
    GITHUB_PATTERN = r"^https://github\.com/[\w.-]+/[\w.-]+/?$"

    REPOSITORY_DIRECTORY = Path("repos")

    SUPPORTED_EXTENSIONS = {
            ".py",
            ".js",
            ".ts",
            ".tsx",
            ".java"
        }
    
    @staticmethod
    def validate_github_url(url: str) -> bool:
        """Returns True if URL is a valid GitHub repository URL"""
        return re.match(RepositoryService.GITHUB_PATTERN, url) is not None

    @staticmethod
    def get_repository_name(repo_url: str) -> str:
        """Extracts the repo name from GitHub URL"""
        return repo_url.rstrip("/").split("/")[-1]
    
    @staticmethod
    def repository_exists(repo_name: str) -> bool:
        """returns True if repo has already been cloned"""
        return(
            RepositoryService.REPOSITORY_DIRECTORY / repo_name
        ).exists()
    
    @staticmethod
    def clone_repository(repo_url: str) -> Path:
        """Clones a GitHub repository if it has not already been cloned and returns the local path."""
        repo_name = RepositoryService.get_repository_name(repo_url)
        local_path = (
            RepositoryService.REPOSITORY_DIRECTORY / repo_name
        )

        # Create the repos directory if it doesn't exist
        RepositoryService.REPOSITORY_DIRECTORY.mkdir(exist_ok=True)
        
        # If already cloned...
        if local_path.exists():
            return local_path

        # Otherwise clone it
        Repo.clone_from(repo_url, local_path)
        return local_path
    
    @staticmethod
    def list_source_files(repo_path: Path) -> list[Path]:
        """Returns all supported source code files in the repository."""

        source_files = []

        for file in repo_path.rglob("*"):
            if file.is_file() and file.suffix in RepositoryService.SUPPORTED_EXTENSIONS:
                source_files.append(file)

        return source_files