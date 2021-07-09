import main

while True:
    statement = input(">>> ")
    if statement=='exit':exit()
    result = main.run(statement)
    print(result)
