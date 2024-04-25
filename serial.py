"""Python serial number generator."""

class SerialGenerator:
    # docstring that 
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    # Initalizing/constructor func
def __init__(self, start=100):
        """Sets up inital attributes"""

        self.start = start
        self.next = start

def __repr__(self):
        """For debuging purposes, represents each iteration."""

        return f"{self.start}, {self.next}"

def nextstage(self):
        """Return next serial."""

        self.next += 1
        return self.next - 1

def reset(self):
        """Resets to start"""

        self.next = self.start
        


