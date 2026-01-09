import unittest
from models import FinancialOperation

class TestFinancialOperation(unittest.TestCase):
    def test_operation_creation(self):
        operation = FinancialOperation(100, "Доход", "2023-10-01", "Зарплата")
        self.assertEqual(operation.amount, 100)
        self.assertEqual(operation.category, "Доход")
        self.assertEqual(operation.description, "Зарплата")

if __name__ == "__main__":
    unittest.main()

    