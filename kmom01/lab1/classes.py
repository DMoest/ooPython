#!/usr/bin/env python3

"""
Classes module
ooPython - lab1 kmom01
Daniel Andersson, daap19
"""


class Cat:
    """Cat class"""

    # Static Class Attribute
    nr_of_paws = 4

    def __init__(self, name, eye_color, lives_left=(-1)):
        """Constructor method."""
        self.lives_left = lives_left
        self.name = name
        self.eye_color = eye_color

    def get_lives_left(self):
        """Getter method for lives left."""
        return self.lives_left

    def set_lives_left(self, input_lives_left):
        """Setter method for lives left"""
        self.lives_left = input_lives_left

        return self.lives_left

    def description(self):
        """Description method to display information about the Cat object."""
        output_string = "My cat's name is {}, has {} eyes and {} lives left to live."

        return output_string.format(self.name, self.eye_color, self.lives_left)


class Duration:
    """Duration class"""

    def __init__(self, hours, minutes, seconds):
        """Class Constructor Method"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, input_object):
        """ Add to the object with duration class """

        self.hours += input_object.hours
        self.minutes += input_object.minutes
        self.seconds += input_object.seconds

        return self

    def display(self):
        """ Display duration hh-mm-ss """
        hour = str(self.hours).zfill(2)
        minute = str(self.minutes).zfill(2)
        second = str(self.seconds).zfill(2)
        output_string = f"{hour}-{minute}-{second}"

        return output_string

    @staticmethod
    def duration_to_sec(duration_string):
        """ Duration to seconds from string (HH-MM-SS) """
        duration_list = duration_string.split("-")
        x = 3600
        index = 0
        seconds = 0

        while x >= 1:
            value = int(duration_list[index]) * x
            seconds += value
            x = x / 60
            index += 1

        return int(seconds)

    def smaller_then(self, input_object):
        """ Compare self to input object """
        if self.hours < input_object.hours:
            result = True

        elif self.hours == input_object.hours and \
                self.minutes < input_object.minutes:
            result = True

        elif self.hours == input_object.hours and \
                self.minutes == input_object.minutes and \
                self.seconds < input_object.seconds:
            result = True

        else:
            result = False

        return result
