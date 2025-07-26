marksheet = {"Alice": 85,"Bob": 78,"Charlie": 92,"David": 88}

a = input("Enter the students's name: ")

if a in marksheet:
    print("{}'s marks: {}".format(a,marksheet[a]))
else:
    print("Student not found.")
