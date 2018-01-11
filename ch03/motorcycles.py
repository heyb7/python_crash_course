motorcycles1 = ["honda", "yamaha", "suzuki"]
print(motorcycles1)

#修改列表元素
motorcycles1[0] = "ducati"
print(motorcycles1)
print("*" * 30)

#在列表中添加元素
motorcycles2 = ["honda", "yamaha", "suzuki"]
print(motorcycles2)
motorcycles2.append("ducati")
print(motorcycles2)
print("*" * 30)

motorcycles3 = []
motorcycles3.append("honda")
motorcycles3.append("yamaha")
motorcycles3.append("suzuki")
print(motorcycles3)
print("*" * 30)

#列表中插入元素
motorcycles4 = ["honda", "yamaha", "suzuki"]
motorcycles4.insert(0, "ducati")
print(motorcycles4)
print("*" * 30)

#列表中删除元素
# 使用del语句删除
motorcycles5 = ["honda", "yamaha", "suzuki"]
print(motorcycles5)

del motorcycles5[0]
print(motorcycles5)
print("*" * 30)

# 使用pop()方法删除
motorcycles6 = ["honda", "yamaha", "suzuki"]
print(motorcycles6)
popped_motorcycle = motorcycles6.pop()
print(motorcycles6)
print(popped_motorcycle)
print("*" * 30)

motorcycles7 = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles7.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print("*" * 30)

motorcycles8 = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles8.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print("*" * 30)

#根据值删除元素
motorcycles9 = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles9)
motorcycles9.remove("ducati")
print(motorcycles9)
print("*" * 30)

motorcycles10 = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles10)

too_expensive = "ducati"
motorcycles10.remove(too_expensive)
print(motorcycles10)
print("\nA " + too_expensive.title() + " is too expensive for me.")

