from dataclasses import dataclass, field
from datetime import date
from typing import Union

@dataclass
class Expense:

    id: int
    amount: int
    description: str
    date: str = field(default_factory=lambda: date.today())
    category: str = field(default_factory=lambda: "N/A")

    def __str__(self):
        return f"Expense {self.id} {self.amount} {self.description} incurred at {self.date}"
    
    def update(self, 
               attribute: str,
               value: Union[int, str]
               ) -> bool:
        if hasattr(self, attribute):
            # Needs to check for the values and convert (date) into proper format
            setattr(self, attribute, value)
            return True
        return False


if __name__ == "__main__":
    e = Expense(1, 100, "Random")
    print(e)