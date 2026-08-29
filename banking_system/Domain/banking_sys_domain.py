from abc import ABC, abstractmethod
from datetime import datetime

class Commission(ABC):
    @abstractmethod
    def get_commission_value(self):...

    @abstractmethod
    def update_commission_value(self, new_commission:float):...

    @abstractmethod
    def calculate_commission(self, amount:float):...


class TransferCommission(Commission):
    def __init__(self, commission_value:float):
        self.__commision_value=commission_value

    @property
    def get_commission_value(self):
        return self.__commision_value
    
    #We need to protect this function, just admins can use it, I think we should implement an access key 
    @get_commission_value.setter
    def update_commission_value(self, new_commission):
        self.__commision_value=new_commission

    def calculate_commission(self, amount):
        return self.get_commission_value*amount

class Currency():
    def __init__(self, bunch_of_cunrrencies:dict):
        self.__currencies=bunch_of_cunrrencies

    @property
    def get_bunch_of_currencies(self):
        return self.__currencies

    #We need to protect this function and of course add more validations
    @get_bunch_of_currencies.setter
    def insert_new_currency(self, country:str, currency:str):
        self.get_bunch_of_currencies[country]=currency

    def get_currency_by_country(self, country:str):
        if country in self.get_bunch_of_currencies.keys():
            return self.get_bunch_of_currencies[country]
        else:
            return self.get_bunch_of_currencies["USA"] 
        

class MinimumWithdraw():
    def __init__(self, bunch_of_minimum_values:dict):
        self.__minimum_withdrawals=bunch_of_minimum_values

    @property
    def get_minimum_withdrawals(self):
        return self.__minimum_withdrawals

    #We need to protect this function and of course add more validations
    @get_minimum_withdrawals.setter
    def insert_new_minimum(self, currency:str, currency_value:float):
        self.get_minimum_withdrawals[currency]=currency_value

    def get_minimum_by_currency(self, currency):
        if currency in self.get_minimum_withdrawals.keys():
            return self.get_minimum_withdrawals[currency]
        else:
            return self.get_minimum_withdrawals["USD"]

class AccountNumber():
    #We know this is not the correct way to create an accounto number or number card, this is just a practice. 
    def __init__(self, prefix:str, counter:int):
        self.prefix=prefix
        self.counter=counter

    def get_account_number(self):
        try:
            account_number="".join([self.prefix,str(self.counter)])
            return account_number
        except ValueError:
            print("\nThe counter must be an int type!")
            return None
        except Exception:
            print("\nSomething went wrong!")
            return None

class FinancialActivityId():
    def __init__(self, prefix:str, counter:int):
        self.__prefix=prefix
        self.__counter=counter

    @property
    def get_prefix(self):
        return self.__prefix

    @property
    def get_counter(self):
        return self.__counter

    def get_id(self):
        try:
            transaction_id="-".join((self.__prefix,str(self.__counter)))
            return transaction_id
        except ValueError:
            print("\nThe counter must be an int type!")
            return None
        except Exception:
            print("\nSomething went wrong!")
            return None

class User (): 
    #Instance variables
    def __init__(self, name, email, country):
        self.__name=name
        self.__email=email
        self.__country=country

    #Instance methods

    @property
    def user_name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email

    @property
    def country(self):
        return self.__country
        
class Account():
    #Instance variables
    def __init__(self, account_number:str, password:str, balance:float, currency:str):
        self.__account_number = account_number
        self.__balance = balance
        self.__currency= currency
        self.__password = password
        self.__status = True

    @property
    def account_number(self) ->str:
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def currency(self):
        return self.__currency

    @property
    def password(self):
        return self.__password

    @property
    def status(self):
        return self.__status
    
    def __valid_withdraw_amount(self,amount:float, minimum_withdraw:float) ->bool:
        if amount>=minimum_withdraw:
            if amount<=self.balance:
                return True
            else:
                print("Sorry, you do not have enough balance for this transaction!")
                return False
        else:
            print(f"Invalid amount, the mimimum withdraw is ${minimum_withdraw:,.2f} {self.currency}")
            return False

    def withdraw_money(self, amount:float, minimum_withdraw:float) -> bool:
        amount_analyze_result=self.__valid_withdraw_amount(amount, minimum_withdraw)
        if amount_analyze_result:
            self.__balance-=amount
            print(f"Please, take your cash ${amount:,.2f} {self.currency}")
            return True
        else:
            return False

class Transaction ():
    def __init__(self, transaction_counter:int, amount:float, currency:str, concept:str, status:bool|str, trx_id:str=None, date:str=None, recipient_name:str=None, recipient_account:str=None):
        self.__transaction_counter=transaction_counter
        self.__trx_id=trx_id
        self.__date=date
        self.__amount=amount
        self.__currency=currency
        self.__concept=concept
        self.__status=status
        self.__recipient_name=recipient_name
        self.__recipient_account=recipient_account
    
    #Instance methods
    @property
    def id_transaction(self):
        id=self.__id_generator()
        self.__trx_id=id
        return self.__trx_id

    def __date_generator(self):
        current_date=datetime.today()
        current_date_str= datetime.strftime(current_date,"%d/%m/%Y, %H:%M:%S")
        return current_date_str

    @property
    def date(self):
        current_date=self.__date_generator()
        self.__date=current_date
        return self.__date

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @property
    def concept(self):
        return self.__concept

    @property
    def status(self) -> str:
        if self.__status:
            self.__status="ACCEPTED"
            return self.__status
        else:
            self.__status="DENIED"
            return self.__status

    @property
    def recipient_name(self) ->str:
        return self.__recipient_name

    @property
    def recipient_account(self) ->str:
        return self.__recipient_account
    
    
    
    #Cortamos aquí
    
class Movement():
    def __init__(self, counter_id:str, account_number:str, type_movement:str, date:str, amount:float, currency:str, current_balance:str, description:str, transaction_reference:str, movement_id:str=None):
        self.__counter_id=counter_id
        self.__movement_id=movement_id
        self.__account_number=account_number
        self.__type_movement=type_movement
        self.__date=date
        self.__amount=amount
        self.__currency=currency
        self.__current_balance=current_balance
        self.__description=description
        self.__transaction_reference=transaction_reference

    @property
    def id(self):
        movement_id=self.__id_generator()
        self.__movement_id=movement_id
        return self.__movement_id

    @property
    def account_number(self):
        return self.__account_number

    @property
    def type_movement(self):
        return self.__type_movement

    @property
    def date(self):
        return self.__date

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @property
    def balance(self):
        return self.__current_balance

    @property
    def description(self):
        return self.__description

    @property
    def transaction_reference(self):
        return self.__transaction_reference
    
    def movement_ticket_generator(self):
        print(f"{'-'*40}")
        print(f"{'*'*10} Appbank receipt {'*'*10}")
        print(f"{'-'*40}\n")
        print(f"Id movement: {self.__movement_id}")
        print(f"Date: {self.__date}")
        print(f"Account number: {self.__account_number}")
        print(f"Type of movement: {self.__type_movement}")
        print(f"Amount: {self.__amount:,.2f} {self.__currency}")
        print(f"New balance: {self.__current_balance:,.2f} {self.__currency}")
        print(f"Movement description: {self.__description}") 
        print(f"Transaction reference: {self.__transaction_reference}")
        print(f"{'-'*40}\n")