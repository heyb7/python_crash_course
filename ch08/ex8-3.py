def make_shirt(size, info):
    """显示T恤的信息"""
    print("\nshirt size: " + size + ".")
    print("shirt info: " + info + ".")

make_shirt("s", "I love you")
make_shirt("m", "I love you")


def make_shirt1(size,  info="I love you"):
    """显示T恤的信息"""
    print("\nshirt size: " + size + ".")
    print("shirt info: " + info + ".")

make_shirt1("L")
make_shirt1(size="S")
make_shirt1(size="M", info="hahaha")
make_shirt1(info="I love u", size="XL")
