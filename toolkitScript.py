# Install GitPython and Pandas

from git import Repo, InvalidGitRepositoryError
from pathlib import Path
import pandas as pd

repoPath = Path(input("Enter the absolute path to your repository: ")).expanduser()
repo = None

while True:
    if repoPath.exists():
        try:
            repo = Repo(repoPath)
            break
        except InvalidGitRepositoryError:
            print("The path provided is not a git repository")
            repoPath = Path(input("Enter the absolute path to your repository: ")).expanduser()
    else:
        print("Please enter a correct repository path")
        repoPath = Path(input("Enter the absolute path to your repository: ")).expanduser()


def diffCommits(repoObject):
    totalBranches = int(input("How many branches will you like to add? "))
    branches = []
    commitTable = {}
    finalValues = {}
    for i in range(totalBranches):
        branchName = input(f"Enter branch{i+1} name: ")
        branches.append(branchName)

    for individualBranch in branches:
        branch = repo.commit(individualBranch);
        commitTable[individualBranch] = list(repo.iter_commits(branch));

diffCommits(repo)
