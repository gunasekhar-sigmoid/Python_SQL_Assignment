from unittest import TestCase
from Solution2 import Total_compensation


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.Total_compensation = Total_compensation("cur")

    def tearDown(self) -> None:
        self.Total_compensation = None

    def test_get_result(self):
        self.assertEqual(self.Total_compensation.compensation(), False)