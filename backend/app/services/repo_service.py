import re
import os
from pathlib import Path
from git import Repo

class RepositoryService:
    """Handles operations related to GitHub repositories"""
    GITHUB_PATTERN = r"^https://github\.com/[\w.-]+/[\w.-]+/?$"

    @staticmethod
    def validate_github_url(url: str) -> bool:
        """Returns True if URL is a valid GitHub repository URL"""
        return re.match(RepositoryService.GITHUB_PATTERN, url) is not None
    
    REPOSITORY_DIRECTORY = Path("repos")

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
        """clones github repo if it's not already clones and returns local math to repo"""
        repo_name = RepositoryService.get_repository_name(repo_url)
        local_path = (
            RepositoryService.REPOSITORY_DIRECTORY / repo_name
        )

        """create repos directory if it doesn't exist"""
        RepositoryService.REPOSITORY_DIRECTORY.mkdir(exist_ok=True)
        
        """If already cloned, then it just returns the path"""
        if local_path.exists():
            return local_path

        """otherwise, clone it"""
        Repo.clone_from(repo_url, local_path)
        return local_path