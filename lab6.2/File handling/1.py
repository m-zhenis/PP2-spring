import os

path = os.chdir("C:\\Users\\arsen\\git_test\\labs\\lab 6\\Files and directories manipulation")

print("Directories:", [item for item in os.listdir(path) if os.path.isdir(item)])

print("Files:", [item for item in os.listdir(path) if os.path.isfile(item)])

print("All dir and files:", os.listdir(path))