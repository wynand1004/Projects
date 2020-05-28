class Animal():
    number_of_animals = 0

    # Constructor
    def __init__(self, name):
        self.age = 0
        self._weight = 0.0
        self.__name = name

        Animal.number_of_animals += 1

    def set_weight(self, new_weight):
        self._weight = new_weight
    
    def get_weight(self):
        return self._weight

    def increment_number_of_animals():
        Animal.number_of_animals += 1

    def __str__(self):
        return "Name: {} Weight: {}".format(self.__name, self._weight)
    
