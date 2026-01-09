import csv
from models import FinancialOperation

class CSVStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_operations(self):
        operations = []
        try:
            with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    operations.append(FinancialOperation(
                        float(row["amount"]),
                        row["category"],
                        row["date"],
                        row["description"]
                    ))
        except FileNotFoundError:
            print("Файл не найден, создан новый.")
        return operations

    def save_operations(self, operations):
        with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category", "date", "description"])
            writer.writeheader()
            for operation in operations:
                writer.writerow({
                    "amount": operation.amount,
                    "category": operation.category,
                    "date": operation.date.strftime("%Y-%m-%d"),
                    "description": operation.description
                })

    