class Member:
    def __init__(self, name, account_number):
        self._name = name
        self.__acc = account_number
    # end of initialization
    # use encapsulation on something you want to protect (can't change easily)
    
    @property # getter for name
    def name(self):
        return self._name

    @name.setter # this method always executes when .name = VALUE is executed
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("String is expected, but not given")

    @property # using @property is creating a getter for an attribute
    def acc(self):
        return self.__acc
    
    # encapsulated attributes are always available in a class as long as you use __ before it
    # 1. Override of a Base Function: __str__()
    def __str__(self):
        return f"Member(name={self.name}, acc={self.acc})"

    # 2. Override of a Base Function: __repr__()
    def __repr__(self):
        return self.__str__()
# end of class

m1 = Member("Park", 1)
print(m1)

m1.name = "Krap"

m2 = Member("Marshall", 2)
print(m2)

member_list = [m1, m2]
print(member_list)