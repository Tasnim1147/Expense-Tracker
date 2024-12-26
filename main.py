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
        
        self.update_parser = ArgumentParser(
                    prog='update',
                    description='updates an existing expense',
                    parents=[self.id_parser])
        self.update_parser.add_argument('--description', 
                                        nargs=1,
                                        type=str)
        self.update_parser.add_argument('--amount', 
                                        nargs=1,
                                        type=int)
        self.update_parser.add_argument('--date', 
                                        nargs=1,
                                        type=str)
        self.update_parser.add_argument('--category', 
                                        nargs=1,
                                        type=str)
        

    def do_add(self,
               arg: str
               ) -> None:
        """add --description <description> --amount <amount>"""
        try:
            args = self.add_parser.parse_args(arg.split(' '))
            expense_id = self.manager.add(args.description, args.amount)
            if expense_id:
                print(f"Expense added successfully (ID: {expense_id})")
            else:
                print(f"Failed to add expense")
        except:
            print(f"Provided parameters are invalid: {arg}")


    def do_list(self,
                arg: str
                ) -> None:
        """list"""
        self.manager.list()

    def do_summary(self,
                   arg: str
                   ) -> None:
        """summary [--month <month> | '']"""
        try:
            args = self.month_parser.parse_args(arg.split(" "))
            if not self.manager.cost(args.month):
                print("Failed to list out expenses")
        except:
            print(f"Provided parameters are invalid: {arg}")

    def do_delete(self, 
                  arg: str
                  ) -> None:
        """delete --id <id>"""
        try:
            args = self.id_parser.parse_args(arg.split(' '))
            if not self.manager.delete(args.id):
                print(f"Expense with ID({args.id}) doesn't exist")
            else:
                print(f"Expense deleted successfully (ID: {args.id})")
        except:
            print(f"Provided parameters are invalid: {arg}")


    def do_upate(self,
                 arg: str
                 ) -> None:
        """update --id <id> [--description <description> |
                                        --amount <amount> |
                                        --date <date>]"""
        try: 
            args = self.update_parser.parse_args(arg.split(" "))
            for attribute in ['description', 'amount', 'date', 'category']:
                self.manager.update(args.id, attribute, args[attribute])
        except:
            print("Provided parameters are invalid: {arg}")

    def do_help(self, arg):
        return super().do_help(arg)
    
    def postloop(self):
        return super().postloop()
    
    def run_cli(self): self.cmdloop()
    

if __name__ == "__main__":
    expense_tracker_cli = ExpenseTracker()
    expense_tracker_cli.run_cli()
    