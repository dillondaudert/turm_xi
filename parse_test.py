#Unit tests for the parse function

import unittest
from err import ParseError
from turm import State
from parse_tm import _parse_transition, _parse_state

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

    def test_parse_transition(self):
        cases = [("q0;a;L", True, ("q0", ["a"], ["L"])),
                 ("q0;b;R", True, ("q0", ["b"], ["R"])),
                 ("q1;cd;F", False),
                 ("whatsup;what;S", True, ("whatsup", ["what"], ["S"])),
                 ("a;B,C;L,L", True, ("a", ["B", "C"], ["L", "L"])),
                 ("a;B;L,L", False),
                 ("a;a;a;a", False),
                 ("q0;B,B;L", False)]

        for case in cases:
            if case[1] == True:
                #Expect a properly formed tuple
                self.assertEqual(case[2], _parse_transition(case[0]))
            else:
                #Expect ParseError
                with self.assertRaises(ParseError):
                    _parse_transition(case[0])




if __name__ == "__main__":
    unittest.main()
