from Domain.banking_sys_domain import Bank, User, Account, Transaction, Movement
from Repository.bank_repository import BankRepository
from Repository.database import user_dict, account_dict, history_transaction, history_movement

class CaseUseRegisterUser():
    def register_user(user_name:str, user_email:str, user_country:str):
        user=User(user_name, user_email, user_country)
        bank_repository=BankRepository(user_dict, account_dict, history_transaction, history_movement)

        bank_repository.save_user(user)

        return user

class CaseUseRegisterAccount():
    def register_account(account_counter:int, user_password:str, user:User):
        bank_repository=BankRepository(user_dict, account_dict, history_transaction, history_movement)

        account_number=Bank.account_number_generator(account_counter)
        currency=Bank.get_currency_by_country(user.country)
        initial_balance=Bank.get_initial_balance_by_currency(currency)

        account=Account(account_number, user_password, initial_balance, currency)

        bank_repository.save_account(account)

        return account

class CaseUseGetAccount():
    def get_account(account_datails:dict):
        account=Account(account_datails["account"],account_datails["password"], account_datails["balance"], account_datails["currency"])

        return account



class CaseUseUserAuthentication():
    def user_authentication(account_number:str, account_password:str):
        bank_repository=BankRepository(user_dict, account_dict, history_transaction, history_movement)
        account_datails=bank_repository.get_account_by_password(account_number, account_password)

        return account_datails



class CaseUseWithdrawMoney():
    def withdraw_money(account:Account, withdraw_amount:float, trx_counter:int, mov_counter:int, transaction_counter:int):
        bank_repository=BankRepository(user_dict, account_dict, history_transaction, history_movement)

        minimum_withdraw=Bank.get_minimum_withdraw_by_currency(account.currency)
        withdraw_result=account.withdraw_money(withdraw_amount, minimum_withdraw)
        if withdraw_result:
            try:
                bank_repository.save_account(account)
                transaction=Transaction(trx_counter, withdraw_amount, account.currency, "Withdraw", withdraw_result)
            except Exception:
                print("Something went wrong making the transaction!")
                return False

            transaction_result=bank_repository.save_transaction(transaction)
            if transaction_result is None:
                print("Something went wrong with the transaction!")
                return False
            else:
                Bank.update_transaction_counter(transaction_counter)
                movement=Movement(mov_counter,account.account_number,"EXPEDENTURE",transaction.date,transaction.amount,transaction.currency,account.balance,"Withdraw transaction",transaction.id_transaction)
                movement_result=bank_repository.save_movement(movement)

                if movement_result is None:
                    print("Something went wrong with the movement!")
                    return False
                else:
                    return movement
        else:
            return False

class CaseUseMovementTicket():
    def get_movement_ticket(movement:Movement):
        movement_ticket=movement.movement_ticket_generator()
        return movement_ticket

class CaseUseGetHistory():
    def get_movements(account:Account):
        bank_repository=BankRepository(user_dict, account_dict, history_transaction, history_movement)

        if account.account_number in bank_repository.movement.keys():
            bank_repository.show_movements(account)
        else:
            print(f"\n{'*'*40}")
            print("You do not have movements stored yet!")
            print(f"{'*'*40}")

