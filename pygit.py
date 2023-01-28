import logging
import os
import subprocess
from logging.handlers import RotatingFileHandler
from typing import List

from utils import logging_config

logger: logging.Logger = logging.getLogger(__name__)
logging_config.configure_logging()

test: str = "test"


class GitStatus:
    def __init__(self, repo_path: str = os.curdir):
        self.repo_path = repo_path
        self.call()

    def call(self) -> str:
        git_status_process: subprocess.CompletedProcess = subprocess.run(
            ["git", "status"], cwd=self.repo_path, text=True, capture_output=True
        )

        try:
            git_status_process.check_returncode
            self.status_raw = git_status_process.stdout
            self.status_lines: List[str] = self.status_raw.split("\n")
            if logger.level == logging.DEBUG:
                status_lines_with_nums: List[str] = [
                    f"{index}: {line}" for index, line in enumerate(self.status_lines)
                ]
                logger.debug("\n".join(status_lines_with_nums))
            return "\n".join(self.status_lines) or ""
        except subprocess.CalledProcessError as e:
            logger.error(
                f"CalledProcessError: 'git status' had exit code {e.returncode}: {e.stderr}"
            )
            return ""


if __name__ == "__main__":
    to_rotate: List = [
        handler
        for handler in logger.handlers
        if isinstance(handler, RotatingFileHandler)
    ]
    for handler in to_rotate:
        handler.doRollover()
    gs: GitStatus = GitStatus()

    for x in []:
        print(x)
