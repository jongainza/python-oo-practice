"""Python serial number generator."""


class SerialGenerator:
    def __init__(self, start=0):
        """Initiates series"""
        self.start = self.next = start

    def __repr__(self):
        """Represents initial number in serie and first following"""
        return f"Serial generator starts at {self.start} and next number in serie is {self.next +1}"

    def generate(self):
        """Generate next number in serie"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reserts serie to initial number"""
        self.next = self.start

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
