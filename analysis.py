import pandas as pd

def calculate_balance(operations):
    incomes = sum(op.amount for op in operations if op.amount > 0)
    expenses = sum(op.amount for op in operations if op.amount < 0)
    return incomes + expenses

def analyze_by_category(operations):
    df = pd.DataFrame([vars(op) for op in operations])
    return df.groupby("category")["amount"].sum()

    