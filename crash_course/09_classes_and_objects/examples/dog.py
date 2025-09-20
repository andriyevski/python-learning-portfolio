class Dog():
    """
    Simple model of dog.
    """

    def __init__(self, name, age):
        """
        Initit atributes name and age
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Dog sit when we ask him
        """
        print(f"{self.name} is sitting!")

    def roll_over(self):
        """
        Dog roll over when we give a command.
        """
        print(f"{self.name} rolled over!")


my_dog = Dog('willie', 6)


print(f"My dog name is {my_dog.name}")
print(f"His age is {my_dog.age} year")
my_dog.sit()
my_dog.roll_over()

my_dog2 = Dog('Gordon', 5)


print(f"My second dog name is {my_dog2.name}")
my_dog2.sit()
