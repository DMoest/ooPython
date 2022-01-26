#!/usr/bin/env python3

"""
f9d8662c34738bf3bb8449176d4f322d
oopython
lab2
v2
daap19
2022-01-24 21:47:06
v4.0.0 (2019-03-05)

Generated 2022-01-24 22:47:06 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
import json

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()


# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#


# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new file, put your code for the classes in it, call it
# **classes.py**.
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a get method for "ssn".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Zimba` and ssn `502075-3392`.
#
#
# Answer with per\'s getter for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#


class Person:
    """ Person class """

    def __init__(self, name, ssn, address=""):
        """ Constructor """
        self.name = name  # Instance attribute name
        self._ssn = ssn  # Instance attribute ssn
        self.address = address  # Instance attribute address

    def get_ssn(self):
        """ Get SSN number """
        return self._ssn

    def set_address(self, address):
        """ Set the address to Person class """
        input_address = (address.city, address.state, address.country)
        self.address = "Address: %s %s %s" % input_address
        return self.address

    def to_string(self):
        """ To string metod """
        return "Name: %s SSN: %s %s" % (self.name, self._ssn, self.address)


per = Person("Zimba", "502075-3392")

ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
#
# Create the magic method **_\_str_\_**, in Address, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Create a new instance of the class Address. Initiate it with the city
# `Amador`, the state `Norrland` and the country `Six Duchies` and store it
# in a variable called **per_address**.
#
# Now, go back and add the instance attribute **address** to your Person
# class. It's value should be sent as argument to constructor, give it a
# default value of and empty string, `""`.
# Create a set method for the attribute "address".
#
# Create the magic method **_\_str_\_** for Person, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"` if the person has an
# address or, `"Name: <name> SSN: <ssn>"` if its an empty string.
#
# Use Address' string representation to get address the data.
#
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#


class Address:
    """ Address class """

    def __init__(self, city, state, country):
        """ Constructor """
        self.city = city  # Instance attribute city
        self.state = state  # Instance attribute state
        self.country = country  # Instance attribute country

    def __str__(self):
        """ To string metod """
        return "Address: %s %s %s" % (self.city, self.state, self.country)


pers_address = Address("Amador", "Norrland", "Six Duchies")
per.set_address(pers_address)

ANSWER = per.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person".
# Add the instance attribute "courses" and initiate it to an empty list.
#
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
#
# Overload the `__str__` method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Use `super()` to access base method.
#
#
# Create a new instance of the class Teacher. Initiate it with the name
# `FitzChivalry` and ssn `503233-4011`.
# Use the add_course method to add the following courses, `ramverk2`,
# `htmlphp` and `linux`.
#
#
# Answer with the Teacher object's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#


class Teacher(Person):
    """ Teachers class """

    def __init__(self, name, ssn, courses=None):
        """ Constructor """
        if courses is None:  # Fix dangerous-default-value.
            courses = []

        super(Teacher, self).__init__(name, ssn)
        self.courses = courses  # Instance attribute courses

    def add_course(self, course):
        """ Add course to the list of courses for class Teacher """
        return self.courses.append(course)

    def remove_course(self, course):
        """ Removes course from list of courses for class Teacher """
        if course in self.courses:
            return self.courses.remove(course)
        return print(
            "The teacher dont have the course \"%s\" assigned." % course)

    def __str__(self):
        """ To string metod """
        string_of_courses = ""

        for item in self.courses:
            string_of_courses += str(item) + ", "

        string_of_courses = string_of_courses.strip(", ")

        return super(Teacher, self).to_string() + "Courses: " + string_of_courses

    def from_json(self, filename):
        """From json method"""
        # json_file = json.load(filename)
        # details = json.loads(json_file.read())

        with open(filename, "r") as read_file:
            details = json.load(read_file)

        print(f"{details}")

        return super(Teacher, self).__init__(details.name, details.ssn, details.courses)


fitz = Teacher("FitzChivalry", "503233-4011")
fitz.add_course("ramverk2")
fitz.add_course("htmlphp")
fitz.add_course("linux")

ANSWER = fitz.__str__()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person".
# Add the instance attribute "courses_grades" and initiate it to an empty
# list.
#
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
#
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# Create a new instance of the class Student. Initiate it with the name
# `Zimba` and ssn `619172-0731`.
# Use the add_course_grade method to add the following courses, `linux` with
# grade `5`, `design` with grade `-` and `python` with grade `3`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#


class Student(Person):
    """ Student class inherit from base-class Person """

    def __init__(self, name, ssn, address="", courses_grades=None):
        """ Constructor """
        if courses_grades is None:  # Fix dangerous-default-value.
            courses_grades = []

        super(Student, self).__init__(name, ssn, address)
        self.courses_grades = courses_grades
        self.total_score = 0
        self.average_from_grades = 0

    def add_course_grade(self, course, grade):
        """ Add a course and the grade of Student class """
        courses_grades = (course, grade)
        self.courses_grades.append(courses_grades)
        return self.courses_grades

    def average_grade(self):
        """ Calculate the average grade """
        self.average_from_grades = 0  # Reset before running new calculation.
        self.total_score = 0  # Reset before running new calculation.
        count = 0

        for course_tup in self.courses_grades:
            for grade in course_tup:
                if isinstance(grade, int):
                    count += 1
                    self.total_score += grade
                else:
                    continue

        self.average_from_grades = (self.total_score / count)
        return self.average_from_grades


student = Student("Zimba", "619172-0731")
student.add_course_grade("linux", 5)
student.add_course_grade("design", "-")
student.add_course_grade("python", 3)

ANSWER = student.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# In Teacher, create the *classmethod* **from_json** with one argument,
# `filename`.
# The *filename* is a json-file that contains data to create and return a new
# instance of the class Teacher.
# Use "teacher.json" to create a new instance of Teacher.
#
# Tip, import json and use `load` method.
#
# Answer with the new instance's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#


new_teacher = Teacher.from_json(Teacher, 'teacher.json')

ANSWER = new_teacher

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# In Teacher, create the method **to_json** that returns a JSON formatted
# dictionary.
# The dictionary should have the same structure as the file used above.
#
# Answer with a json string that has an indention of 4 spaces.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

dbwebb.exit_with_summary()
