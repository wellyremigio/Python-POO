class Parent:
    hair_color = "blonde"
    speaks = ["Portuguese"]

class Child(Parent):
    hair_color = "purple"
    def __init__(self):
        super().__init__()
        self.speaks.append("English")

a = Parent()
b = Child()

print(a.hair_color)
print(b.hair_color)

print(a.speaks)
print(b.speaks)