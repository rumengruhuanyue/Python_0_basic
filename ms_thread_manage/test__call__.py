class Entity:
    def __init__(self, size, x, y):
        self.x, self.y = x, y

    def __call__(self, x, y):
        self.x, self.y = x, y

    def getdata(self):
        return self.x, self.y


e = Entity(1, 2, 3)
print(e.getdata())
e(4, 5)  # 实例可以象函数那样执行，并传入x y值，修改对象的x y
print(e.getdata())
