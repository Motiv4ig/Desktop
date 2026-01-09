import tkinter as tk
from tkinter import messagebox
from storage import CSVStorage
from models import FinancialOperation

class FinancialPlannerApp:
    def __init__(self):
        self.storage = CSVStorage("data/operations.csv")
        self.operations = self.storage.load_operations()

        self.root = tk.Tk()
        self.root.title("Финансовый планировщик")

        # Элементы интерфейса
        self.amount_entry = tk.Entry(self.root)
        self.category_entry = tk.Entry(self.root)
        self.date_entry = tk.Entry(self.root)
        self.description_entry = tk.Entry(self.root)

        tk.Button(self.root, text="Добавить операцию", command=self.add_operation).pack()
        tk.Button(self.root, text="Показать операции", command=self.show_operations).pack()

    def add_operation(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get()
        description = self.description_entry.get()

        try:
            operation = FinancialOperation(float(amount), category, date, description)
            self.operations.append(operation)
            self.storage.save_operations(self.operations)
            messagebox.showinfo("Успех", "Операция добавлена!")
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректные данные!")

    def show_operations(self):
        for operation in self.operations:
            print(operation)

    def run(self):
        self.root.mainloop()

    