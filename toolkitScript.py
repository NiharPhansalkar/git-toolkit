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
    branches = [input(f"Enter branch{i+1} name: ") for i in range(totalBranches)]
    commitTable = {}

    for individualBranch in branches:
        branch = repoObject.commit(individualBranch);
        commitTable[individualBranch] = list(repoObject.iter_commits(branch))


    uniqueValues = {commit for lst in commitTable.values() for commit in lst}

    columns = {name: [None] * len(uniqueValues) for name in commitTable}
    data = {name: [value if value in lst else None for value in uniqueValues] for name, lst in commitTable.items()}
    df = pd.DataFrame(data)

    df.to_csv('output.csv', index=False)

diffCommits(repo)
