from datetime import datetime

class FinancialOperation:
    def __init__(self, amount: float, category: str, date: str, description: str = ""):
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.description = description

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} | {self.category} | {self.amount} | {self.description}"


class Category:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    