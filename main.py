import pandas as pd

class Expense:
    # class representing single expense

    def __init__(self,name,value) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name},{self.value}"
class User:
    # single user who will be in the calculation
    def __init__(self,name,saldo = 0.0,) -> None:
        self.name = name
        self.saldo = saldo
        
    def __str__(self) -> str:
        return f"{self.name}"

class ExpenseList:
    # list of all expenses of a particular user
    def __init__(self) -> None:
        self.data = {'expenseNames': [], 
                    'expenseValues': []}
        self.owner = ''

    def toDF(self):
        self.df = pd.DataFrame(self.data, columns= ['expenseNames','expenseValues'])      

    def __str__(self) -> str:
        self.toDF()
        return f"Lista wydatków, właściciel {self.owner}:\n"+str(self.df)

    def addExpense(self,expense):
        self.data['expenseNames'].append(expense.name)
        self.data['expenseValues'].append(expense.value)

    def setOwner(self,name):
        self.owner = name

wyd1 = Expense('japko', 500)
wyd2 = Expense('paliwko',489)
#print(wyd1,wyd2)

lista1 = ExpenseList()
lista1.addExpense(wyd1)
lista1.addExpense(wyd2)
lista1.setOwner("Zulus")

print(lista1)

#lista1.toDF()
