import sys, os
sys.path.append(os.path.abspath(os.curdir))
from expense import Expense
from datetime import date
from display.tabulate import tabulate

class ExpenseManager(object):
    def __init__(self):
        self.expenses: list[Expense] = []
        self.count: int = 1
        self._restore_expenses()

    def add(self, 
            amount: int,
            description: str,
            date: date = None,
            category: str = None
            ) -> int:
        if (amount < 0 and not description): return 0
        expense = Expense(id=self.count,
                          amount=amount,
                          description=description)
        if category: expense.category = category
        if date: expense.date = date 
        self.expenses.append(expense)
        self.count += 1
        return self.count - 1   

    def _restore_expenses(self): pass

    def delete(self,
               id: int
               ) -> int:
        for idx, expense in enumerate(self.expenses):
            if expense.id == id:
                self.expenses.pop(idx)
                return id
        return 0

    def view(self,
             id: int
             ) -> bool:
        expenses = list(filter(lambda expense: expense.id == id,
                        self.expenses))
        if expenses:
            print(expenses[0])
            return id
        else:
            return 0

    def store(self,
              path: str="expenses.csv",
              ) -> bool:
        pass

    def list(self) -> None:
        if self.expenses:
            tabulate(contents=list(map(
                lambda expense: {
                    'ID': expense.id,
                    'Date': expense.date,
                    'Description': expense.description,
                    'Amount': "$" + str(expense.amount),
                }, self.expenses
            )))
        else:
            tabulate(headers=['ID', 'Date', 'Description', 'Amount'])

    def cost(self,
             month: int = -1
             ) -> int:
        year = date.today().year
        if month != -1: 
            if (not 1 <= month <= 12): return -1
            return sum(list(filter(lambda expense: expense.date.month == month \
                                and expense.date.year == year, self.expenses)))
        else:
            return sum(list(filter(lambda expense: expense.date.month == month, 
                                   self.expenses)))
        

if __name__ == '__main__':
    m = ExpenseManager()
    print(m.add(10, "desc1"))
    print(m.add(20, "desc2"))
    print(m.view(1))
    print(m.view(-1))
    print(m.delete(1))
    print(m.add(30, "desc3"))
    m.list()
    