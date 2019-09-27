class Animal:

    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1

    def eat(self):
        print("The {} can eat".format(self.name))

    def run(self):
        print(self.age)

    def active(self):
        print("All animals are active")


mamal = Animal("Dog", [34,5,2])

mamal.run()
mamal.active()
