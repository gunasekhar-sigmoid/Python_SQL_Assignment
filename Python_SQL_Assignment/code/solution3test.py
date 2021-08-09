from unittest import TestCase
from Solution3 import Employees


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.Employees = Employees("cur")

    def tearDown(self) -> None:
        self.Employees = None

    def test_get_result(self):
        self.assertEqual(self.Employees.upload(), False)