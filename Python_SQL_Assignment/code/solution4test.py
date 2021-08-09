from unittest import TestCase
from Solution4 import departments


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.departments = departments("cur")

    def tearDown(self) -> None:
        self.departments = None

    def test_get_result(self):
        self.assertEqual(self.departments.total_compensation_by_department(), False)