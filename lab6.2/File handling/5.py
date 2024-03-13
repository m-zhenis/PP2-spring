with open("C:\\Users\\m-zhenis\\git_test\\labs\\lab6.2\\File handling\\Example.txt", "a") as txt:
    a = list(input("Write list: ").split())
    for i in a:
        txt.write(i + " ")
