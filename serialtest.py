import unittest
from serial import SerialGenerator

class TestSerialGenerator(unittest.TestCase):
    def test_initialization(self):
        serial = SerialGenerator(start=100)
        self.assertEqual(serial.start, 100)
        self.assertEqual(serial.next, 100)

    def test_generate(self):
        serial = SerialGenerator(start=100)
        self.assertEqual(serial.generate(), 100)
        self.assertEqual(serial.generate(), 101)
        self.assertEqual(serial.generate(), 102)

    def test_reset(self):
        serial = SerialGenerator(start=100)
        serial.generate()
        serial.reset()
        self.assertEqual(serial.generate(), 100)

if __name__ == '__main__':
    unittest.main()

