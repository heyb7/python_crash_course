#检查两个字符串相等和不等
str1 = "abc"
str2 = "bcd"

if str1 == str2:
    print("str1 == str2.")
if str1 != str2:
    print("str1 != str2.")

#使用函数 lower() 的测试
str1 = "abc"
str2 = "Abc"

if str1 == str2.lower():
    print("str1 == str2.lower().")

#检查两个数字相等、不等、大于、小于、大于等于和小于等于
num1 = 10
num2 = 20
if num1 == num2:
    print("num1 == num2.")
if num1 != num2:
    print("num1 != num2")
if num1 > num2:
    print("num1 > num2.")
if num1 < num2:
    print("num1 < num2.")
if num1 >= num2:
    print("num1 >= num2.")
if num1 <= num2:
    print("num1 <= num2.")

#使用关键字 and 和 or 的测试
if num1 > 10 and num2 > 10:
    print("num1 and num2 are > 10.")
if num1 > 10 or num2 > 10:
    print("num1 or num2 is > 10.")

#测试特定的值是否包含在列表中
list1 = ["a", "b", "c", "d"]
if "a" in list1:
    print("a is in list1.")

#测试特定的值是否未包含在列表中
if "f" not in list1:
    print("f is not in list1.")
