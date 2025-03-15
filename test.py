
from bs4 import BeautifulSoup
import unittest

class TestBeautifulSoupParsing(unittest.TestCase):
    def test_1(self):
        try:
            soup = BeautifulSoup('t<html><bodT><p>Initial test content</p>R</body></hml>', 'html.parser')
            # Check if parsing the HTML creates a valid BeautifulSoup object
            if soup is None:
                raise ValueError("Invalid HTML structure")
        except Exception as e:
            with open("validate_bs4.txt", "a") as f:
                f.write(f"Error for input:\n\n't<html><bodT><p>Initial test content</p>R</body></hml>'\n\nError: {str(e)}\n")

if __name__ == "__main__":
    unittest.main()
    