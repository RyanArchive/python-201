filename = input("Enter filename: ")
content = input("Enter content: ")

with open(filename, 'w') as file:
    file.write(content)

while True:
    read = input("Read file? ")

    if read.lower() == 'n':
        break
    elif read.lower() == 'y':
        with open(filename, 'r') as file:
            print(file.read())
            break