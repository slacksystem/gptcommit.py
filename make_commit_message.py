import logging
import os
import re
import subprocess
from typing import List

import requests

import prompts
from utils import logging_config

logger: logging.Logger = logging.getLogger(__name__)
logging_config.configure_logging()


def git_status(repo_path: str = os.curdir) -> str:
    """
    Uses the prompts from prompts module
    to create a commit message
    """

    git_status_process: subprocess.CompletedProcess = subprocess.run(
        ["git", "status"], cwd=repo_path, check=True
    )

class GitStatus:
    def __init__(self, repo_path: str = os.curdir):
        self.repo_path = repo_path
        self.git_status_process_output: str = self.git_status_process.stdout.decode("utf-8")
        self.git_status_process_output_lines: List[str] = self.git_status_process_output.split("\n")
        self.git_status_process_output_lines = [line for line in self.git_status_process_output_lines if line]
    
    def call(self) -> str:


def prepare_file_diff_prompt(file_diff: str):
    ...
