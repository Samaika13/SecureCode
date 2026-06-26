import re

class RepositoryService:
    """Handles operations related to GitHub repositories"""
    GITHUB_PATTERN = r"^https://github\.com/[\w.-]+/[\w.-]+/?$"

    @staticmethod
    def validate_github_url(url: str) -> bool:
        """Returns True if URL is a valid GitHub repository URL"""
        return re.match(RepositoryService.GITHUB_PATTERN, url) is not None