import unittest

import helloParse


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class HelloParseTest(unittest.TestCase):
    def test_hello(self):
        content = helloParse.getContent('hello.py')
        self.assertEqual(helloParse.findHello(content), True)

    def test_hello2(self):
        content = 'def hello():\n x = \'hello\'\n return \'Hello, World!\''
        self.assertEqual(helloParse.findHello(content), True)

    def test_hello3(self):
        content = "def hello():\n  return \"Goodbye, World!\""
        self.assertEqual(helloParse.findHello(content), False)

    def test_hello4(self):
        content = "def hello():\n  return \"Hello, World\""
        self.assertEqual(helloParse.findHello(content), False)

if __name__ == '__main__':
    unittest.main()
