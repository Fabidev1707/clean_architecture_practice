from abc import ABC, abstractmethod
from datetime import datetime

class Bank ():
    #Class virables
    transfer_commission=.10
    minimum_withdraw={"MX":50, "USD":20, "ARS":1000, "CLP":1000, "COP":10000}
    transaction_counter=0
    bunch_currency={"MEX":"MX", "USA":"USD", "AR":"ARS", "CHL":"CLP", "COL":"COP"}

    #Class methods 
    @classmethod
    def update_transfer_commision(cls, new_commision:float) -> None:
        cls.transfer_commission=new_commision

    @classmethod
    def update_minimum_withdraw(cls, new_minimum_withdraw:float) -> None:
        cls.minimum_withdraw=new_minimum_withdraw

    @classmethod
    def update_transaction_counter(cls,new_cunter_value:int) -> None:
        cls.transaction_counter=new_cunter_value
    
    @classmethod
    def add_currency(cls, country:str, currency:str) -> None:
        cls.bunch_currency[country]=currency

    @classmethod
    def get_initial_balance_by_currency(cls, currency:str) -> float:
        if currency in cls.minimum_withdraw.keys():
            return cls.minimum_withdraw[currency]*2
        else:
            return cls.minimum_withdraw['USD']*2
    
    @classmethod
    def get_currency_by_country(cls, country:str):
        if country in cls.bunch_currency.keys():
            return cls.bunch_currency[country]
        else:
            return cls.bunch_currency["USA"]
        
    @classmethod    
    def get_minimum_withdraw_by_currency(cls, currency:str):
        if currency in cls.minimum_withdraw.keys():
            return cls.minimum_withdraw[currency]
        else:
            return cls.minimum_withdraw["USD"]
        
    @classmethod    
    def transfer_commission_calculer(cls, amount:float) -> float:
        return amount*cls.transfer_commission
    
    @staticmethod
    def account_number_generator(counter:int):
        return "".join(["XXXXXXXXXXXX",str(counter)])

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
    def __id_generator(self) ->str:
        try:
            transaction_id="-".join(("TRX",str(self.__transaction_counter)))
            return transaction_id
        except ValueError:
            print("\nThe acction counter must be an int type!")
            return None
        except Exception:
            print("\nSomething went wrong!")
            return None

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

    def __id_generator(self):
        try:
            movement_id_str= "-".join(("MOV",str(self.__counter_id)))
        except ValueError:
            print("\nThe movement counter must be an int type")
            return None
        except Exception:
            print("\nSomething went wrong!")
            return None
        
        return movement_id_str

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