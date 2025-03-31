from unittest import TestCase
from unittest import main

def myabs(n):
    if n>0:
        return n
    if n<0:
        return -n

class TestAbsFunction(TestCase):
    def test_positive_number(self):
        self.assertEqual(myabs(10), 10)

    def test_negative_number(self):
        self.assertEqual(myabs(-10), 10)

    def test_zero(self):
        self.assertEqual(myabs(0), 0)

main()