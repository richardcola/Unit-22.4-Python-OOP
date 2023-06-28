class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start):
        """
        Initialize the SerialGenerator with a start number.
        
        Parameters:
        - start (int): The starting number for the serial generator.
        """
        self.start = start
        self.current = start
    
    def generate(self):
        """
        Generate the next sequential number.
        
        Returns:
        - int: The next sequential number.
        """
        number = self.current
        self.current += 1
        return number
    
    def reset(self):
        """
        Reset the number back to the original start number.
        """
        self.current = self.start
    
    def __repr__(self):
        """
        Return a string representation of the SerialGenerator.
        
        Returns:
        - str: A descriptive string representation of the SerialGenerator.
        """
        return f"<SerialGenerator start={self.start} next={self.current}>"
        

# Test the SerialGenerator class
serial = SerialGenerator(start=100)

print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
print(serial.generate())  # Output: 102

serial.reset()
print(serial.generate())  # Output: 100

print(repr(serial))  # Output: <SerialGenerator start=100 next=101>
