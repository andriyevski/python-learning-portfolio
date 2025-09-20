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
