#Unit tests for the parse function

import unittest
from err import ParseError
from turm import State
from parse_tm import _parse_state

class TestParseMethods(unittest.TestCase):

    def test_parse_state(self):
        cases = [("q0,F",True),
                 ("q0,N", True),
                 ("q0,F,hi",False),
                 ("q0,q0",False),
                 ("q1,N", True)]

        for case in cases:
            if case[1] == True:
                #Expect a state to return
                self.assertTrue(type(_parse_state(case[0],True)) == State)

            else:
                #Expect a ParseError exception
                with self.assertRaises(ParseError):
                    _parse_state(case[0],False)


if __name__ == "__main__":
    unittest.main()
