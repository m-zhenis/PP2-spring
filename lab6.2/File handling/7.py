import os

path = "C:\\Users\\m-zhenis\\git_test\\labs\\lab6.2\\File handling\\Example.txt"

with open(path, "r") as txt:
    contents = txt.read()
    
file_path = os.path.join("C:\\Users\\Admin\\Desktop\\pp2\\PY\\LAB6\\Files and directories manipulation", "Copy.txt")

with open(file_path, "w") as txt:
    txt.write(contents)
    
print ("File was successufully created!")
