from expense.expense import Expense


class ExpenseManager(object):
    def __init__(self):
        self.expenses = []
        self.count = 0
        self._restore_expenses()

    def add(self, 
            amount: int,
            description: str,
            date: str = None,
            category: str = None
            ) -> None:
        pass

    def _restore_expenses(self): pass

    def delete(self,
               id: int
               ) -> bool:
        pass

    def view(self,
             id: int
             ) -> bool:
        pass

    def store(self,
              path: str="expenses.csv",
              ) -> bool:
        pass

    def cost(self,
             month: int = -1
             ) -> bool:
        pass