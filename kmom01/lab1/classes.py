"""
Classes module
ooPython - lab1 kmom01
Daniel Andersson, daap19
"""



class Cat():
    """Cat class"""


    """Static Class Attributes"""
    nr_of_paws = 4


    def __init__(self, name, eye_color, lives_left=(-1)):
        """Constructor method."""
        self.lives_left = lives_left
        self.name = name
        self.eye_color = eye_color


    def getLivesLeft(self):
        """Getter method for lives left."""

        return self.lives_left


    def setLivesLeft(self, input_lives_left):
        """Setter method for lives left"""
        self.lives_left = input_lives_left

        return self.lives_left


    def description(self):
        """Description method to display information about the Cat object."""
        outputText = "My cat's name is {}, has {} eyes and {} lives left to live."

        return outputText.format(self.name, self. eye_color, self.lives_left)



class Duration():
    """Duration class"""

    def __init__(self, hours, minutes, seconds):
        """Class Constructor Method"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def __add__(self, inputObject):
        """ Add to the object with duration class """
        self.hours += inputObject.hours
        self.minutes += inputObject.minutes
        self.seconds += inputObject.seconds

        return self


    def display(self):
        """ Display duration hh-mm-ss """
        hour = str(self.hours).zfill(2)
        minute = str(self.minutes).zfill(2)
        second = str(self.seconds).zfill(2)
        outputString = "{}-{}-{}"

        return outputString.format(hour, minute, second)


    def duration_to_sec(self):
        """ Duration to seconds from string (HH-MM-SS) """
        sec = 0
        h = 3600 * int(self[:2])
        m = 60 * int(self[3:5])
        s = int(self[6:])
        sec += (h + m + s)

        return sec


    def smaller_then(self, inputObject):
        """ Compare self to input object """
        if self.hours < inputObject.hours:
            return True
        elif self.hours == inputObject.hours and \
                self.minutes < inputObject.minutes:
            return True
        elif self.hours == inputObject.hours and \
                self.minutes == inputObject.minutes and \
                self.seconds < inputObject.seconds:
            return True

        return False
