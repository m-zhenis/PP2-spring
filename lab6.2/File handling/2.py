import os

path = "C:\\Users\\m-zhenis\\git_test\\labs\\lab6.2\\File handling"

print("Current Path:", path)

print("Existence: ")
if os.access(path, os.F_OK):
    print("Yes")
    
print("Readability: ")
if os.access(path, os.R_OK):
    print("Yes")
    
print("Writability: ")
if os.access(path, os.W_OK):
    print("Yes")
    
print("Executability: ")
if os.access(path, os.X_OK):
    print("Yes")
