file = open('output.txt','w+')

content  = input("Enter text yo write to the file: ")

file.write(content)
print("Data successfully written to output.txt")


file = open('output.txt','a')
content_2 = input("Enter additional text to append: ")
file.write("\n" + content_2)
print("Data successfully appended.")


print("\nFinal content of output.txt")
with open("output.txt",'r') as file:
    content = file.read()
    print(content)

file.close()
