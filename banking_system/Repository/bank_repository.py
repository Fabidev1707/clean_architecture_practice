from Domain.banking_sys_domain import User, Account, Transaction, Movement, TransferCommission

class UserRepository():
    def __init__(self, user_db:dict):
        self.__user_db=user_db

    @property
    def user(self):
        return self.__user_db
    
    def get_user_by_email(self, email:str) -> dict|bool:
            if email in self.__user_db.keys():
                return self.__user_db[email]
            else:
                print("That user does not exist!")
                return False
            
    def save_user(self, user:User):
        if user.email in self.__user_db.keys():
            print("\nThat email is alredy used")
        else:
            try:
                self.__user_db[user.email]={
                    "name":user.user_name,
                    "email":user.email,
                    "country":user.country
                }
            except KeyError:
                print("\nThat key does not exist!")
            except Exception as e:
                print(e)
                print("\nSomething went wrong registing your user! Please try again")

class AccountRepository():
    def __init__(self, account_db:dict):
        self.__account_db=account_db

    def get_account_by_password(self, account_number, password) -> dict|bool:
                if account_number in self.__account_db.keys():
                    if self.__account_db[account_number]["password"]==password:
                        return self.__account_db[account_number]
                    else:
                        return False
                else:
                    return False
                
    def save_account(self, user_account:Account):
        try:
            self.__account_db[user_account.account_number]={
                "account":user_account.account_number,
                "password":user_account.password,
                "balance":user_account.balance,
                "currency":user_account.currency
            }
        except KeyError:
            print("\nThat key does not exist!")
        except Exception:
            print("\nSomething went wrong!")

class TransactionRepository():
    def __init__(self, transaction_db:dict):
        self.__transaction_db=transaction_db

    @property
    def transaction(self):
        return self.__transaction_db
    
    def save_transaction(self, transaction:Transaction) -> str|None:
        try:
            transaction_detail={
                "date": transaction.date,
                "amount": transaction.amount,
                "currency": transaction.currency,
                "concept": transaction.concept, 
                "status": transaction.status
            }

            if transaction.recipient_name is None or transaction.recipient_account is None:
                pass
            else:
                transaction_detail["recipient"]={"recipient_name":transaction.recipient_name, "recipient_account": transaction.recipient_account}
        
            self.__transaction_db[transaction.id_transaction]= transaction_detail
        except KeyError:
            print("\nThat key does not exist!\n")
        except Exception as e:
            print(e)
            print("\nSomething went wrong registing history transaction!\n")
        
        return transaction.id_transaction

class MovementRepository():
    def __init__(self, movement_db:dict):
        self.__movement_db=movement_db

    @property
    def movement(self):
        return self.__movement_db

    def save_movement(self, movement:Movement) -> bool|None:
        try:
            movement_dict_model={
                "id_movement": movement.id,
                "date": movement.date,
                "account": movement.account_number,
                "type": movement.type_movement,
                "amount": movement.amount,
                "currency": movement.currency,
                "current_balance": movement.balance,
                "description": movement.description, 
                "transaction_reference": movement.transaction_reference
            }
        except KeyError:
            print("\nThat key does not exist!")
            return None
        except Exception:
            print("\nSomething went wrong registing history movements!\n")
            return None
        
        if  movement.account_number in self.__movement_db:
            self.__movement_db[movement.account_number].append(movement_dict_model)
            print ("\nHistory successfully saved")
            return True
        else: 
            self.__movement_db.setdefault(movement.account_number,[])
            self.__movement_db[movement.account_number].append(movement_dict_model)
            print ("\nHistory successfully saved")
            return True
    
    def show_movements(self,account:Account):
        history_movements=self.__movement_db[account.account_number]
        for movement in history_movements:
            print(f"{'-'*40}")
            print(f"{'*'*10} Appbank receipt {'*'*10}")
            print(f"{'-'*40}\n")
            print(f"Id movement: {movement['id_movement']}")
            print(f"Date: {movement['date']}")
            print(f"Account number: {movement['account']}")
            print(f"Type of movement: {movement['type']}")
            print(f"Amount: {movement['amount']:,.2f} {movement['currency']}")
            print(f"New balance: {movement['current_balance']:,.2f} {movement['currency']}")
            print(f"Movement description: {movement['description']}") 
            print(f"Transaction reference: {movement['transaction_reference']}")
            print(f"{'-'*40}\n")

#We´re going to build a new class that acceses to the database, a new repository called CommissionRepository  

class TransferCommissionRepository():
    def __init__(self, commission_db:dict):
        self.__commission_db=commission_db

    @property
    def get_commission(self):
        return self.__commission_db

    def save_commission(self, commission:TransferCommission):
        self.__commission_db['transfer_commission']=commission.commission_value