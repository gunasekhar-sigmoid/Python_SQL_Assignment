from unittest import TestCase
from Solution1 import employees


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.employees = employees("cur")

    def tearDown(self) -> None:
        self.employees = None

    def test_get_result(self):
        self.assertEqual(self.employees.emp(), False)
