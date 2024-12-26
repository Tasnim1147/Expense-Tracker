from cmd import Cmd
from typing import Optional
from expense.manager import ExpenseManager
from argparse import ArgumentParser

class ExpenseTracker(Cmd):

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        
        self.manager = ExpenseManager()

        self.id_parser = ArgumentParser()
        self.id_parser.add_argument('--id', type=int, required=True)

        self.month_parser = ArgumentParser()
        self.id_parser.add_argument('--month', type=int, required=True)

        self.add_parser = ArgumentParser(
                    prog='add',
                    description='adds a new expense',
                    usage='add --description <description> --amount <amount>')
        self.add_parser.add_argument('--description', 
                                     nargs=1,
                                     type=str,
                                     required=True)
        self.add_parser.add_argument('--amount', 
                                     nargs=1,
                                     type=int,
                                     required=True)
        

    def do_add(self,
               arg: str
               ) -> None:
        """add --description <description> --amount <amount>"""

        pass

    def do_list(self,
                arg: str
                ) -> None:
        pass

    """summary [--month <month> | '']"""
    def do_summary(self,
                   arg: str
                   ) -> None:
        pass

    """delete --id <id>"""
    def do_delete(self, 
                  arg: str
                  ) -> None:
        pass

    """update --id <id> [--description <description> |
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
    