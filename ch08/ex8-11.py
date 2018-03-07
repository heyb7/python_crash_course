def show_magicians(names):
    """显示魔术师的名字"""
    print("all of magician: ")
    for name in names:
        print(name)

def make_great(names):
    num = len(names) - 1
    while num >= 0:
        names[num] = "the Great " + names[num]
        num -= 1
    return names

magician_names = ['john', 'eric', 'lily']
show_magicians(magician_names)

print("\nGreat magicians:")
great_magicians = make_great(magician_names[:])
show_magicians(great_magicians)

print("\noriginal magicians:")
show_magicians(magician_names)