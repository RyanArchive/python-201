with open('to write.txt', 'w') as file:
    file.write("A content was written here.")

with open('to write.txt', 'a') as file:
    file.write("\nA content was appended.")