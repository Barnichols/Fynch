import sys, os
sys.path.insert(0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     '..')
    )
)
import fynch
import unittest

class TestFynchSym(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.sym = fynch.FynchSym()

    def test_model(self):
        self.assertEqual(0,0)

    def test_reset(self):
        self.assertEqual(0,0)

    def test_feedback(self):
        self.assertEqual(0,0)

    def test_step(self):
        self.assertEqual(0,0)

    def test_perturbation(self):
        self.assertEqual(0,0)

if __name == "__main__":
    unittest.main()
