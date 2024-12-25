from cmd import Cmd
from typing import Optional


class ExpenseTracker(Cmd):

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)

    """expense-tracker add --description <description> --amount <amount>"""
    def do_add(self,
               arg: str
               ) -> None:
        pass

    def do_list(self,
                arg: str
                ) -> None:
        pass

    """expense-tracker summary [--month <month> | '']"""
    def do_summary(self,
                   arg: str
                   ) -> None:
        pass

    """expense-tracker delete --id <id>"""
    def do_delete(self, 
                  arg: str
                  ) -> None:
        pass

    """expense-tracker update --id <id> [--description <description> |
                                         --amount <amount> |
                                         --date <date>]"""
    def do_upate(self,
                 arg: str
                 ) -> None:
        pass

    def do_help(self, arg):
        return super().do_help(arg)
    
    def postloop(self):
        return super().postloop()
    
    def run_cli(self): self.cmdloop()
    

if __name__ == "__main__":
    expense_tracker_cli = ExpenseTracker()
    expense_tracker_cli.run_cli()
    