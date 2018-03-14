#读取整个文件
#with open("D:\git_project\python_crash_course\ch10\pi_digits.txt") as file_object:
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)

#逐行读取
print("\n")
#filename = "D:\git_project\python_crash_course\ch10\pi_digits.txt"
filename = "pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())