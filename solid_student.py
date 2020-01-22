class Student():

# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort_number = 0
       
# Define getters for all properties.

    @property 
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
                return ""

    @property 
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
                return ""
    
    @property 
    def age(self):
        try:
            return self.__age
        except AttributeError:
                return 0
    
    @property 
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
                return 0

    
    # The full name property should return first name and last name separated by a space. It's value cannot be set.
    
    @property 
    def full_name(self):
        try:
            return self.__first_name + " " + self.__last_name
        except AttributeError:
                return ""
    
    
    # Define a setter for all but the read only property.
    
    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Yo')

    
    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Bo')

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Mo')

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('Mo')
    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}."

chris_word = Student()
chris_word.first_name = "Chris"
chris_word.last_name = "Word"
chris_word.age = 37
print(chris_word)



# mike = Student()
# mike.first_name = "Mike"
# mike.last_name = "Ellis"
# mike.age = 35
# mike.cohort_number = 39

# print(mike)


