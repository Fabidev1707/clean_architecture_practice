import Application.case_use_banking_sys as bank_case_use
#Capa de presentacion
def main():
    transaction_counter=0
    account_counter=1000
    trx_counter=1000
    mov_counter=1000

    while True:
        print(f"\n{'*'*40} Wellcome to Bankapp, where you can manage your balance but also your life! {'*'*40}")
        print("\tDo not you have an account yet? Create one!")
        answer=input("Would you like to create an account? (y/n) or [Enter] to exit: ").lower()

        if answer.strip() == "":
            print("\nThank you for using our service, have a greate day!")
            break
        elif answer == "y":
            user_name=input("What is your first name?: ").capitalize()
            
            if user_name.strip()=="":
                continue

            user_email=input("What is your email adress? ")
            print("\t****Select your current country****")
            print("Mexico:MEX")
            print("United satates of america:USA")
            print("Chile:CHL")
            print("Argentina:AR")
            print("Colombia:COL")
            user_country=input("Type your answare: ").upper()
            user_password=input("Please, create a strong and reliable password: ")

            user=bank_case_use.CaseUseRegisterUser.register_user(user_name, user_email, user_country)
            account=bank_case_use.CaseUseRegisterAccount.register_account(account_counter, user_password, user)
            
            account_counter+=1

            print(f"\nYour account was successfully created!, your acoount number is '{account.account_number}'")
            print("\t ****Please log in to start making your life better****")
            continue
        else:
            user_account_number=input("\nType your account number: ")
            user_password=input("Type your password: ")

            account_datails=bank_case_use.CaseUseUserAuthentication.user_authentication(user_account_number, user_password)
            if account_datails:
                account=bank_case_use.CaseUseGetAccount.get_account(account_datails)
                while True:
                    print(f"\n\t What Would you like to do today?")
                    print("1.Check my balance")
                    print("2.Withdraw money")
                    print("3.Make a deposit")
                    print("4.Transfer money")
                    print("5.Show history movements")
                    print("6.Exit")
                    op=input("Type your option: ")

                    match op: 
                        case "1":
                            print(f"\n{'-'*40}")
                            print(f"Your current balance is: {account.balance:,.2f} {account.currency}")
                            print(f"{'-'*40}")
                        case "2": 
                            try:
                                withdraw_amount=int(input("\nHow much would you like to withdraw? "))
                            except ValueError:
                                print("Just type numbers! Please try it again.\n")
                                continue
                            except Exception:
                                print("Something went wrong getting the amount! Please try it again.\n")
                                continue

                            withdrawal_result=bank_case_use.CaseUseWithdrawMoney.withdraw_money(account, withdraw_amount, trx_counter, mov_counter, transaction_counter)

                            if withdrawal_result:
                                trx_counter+=1
                                transaction_counter+=1
                                mov_counter+=1

                                op=input("Would you like to print your receipt? (y/n): ").lower()

                                if op == "y":
                                    bank_case_use.CaseUseMovementTicket.get_movement_ticket(withdrawal_result)
                                elif op == "n":
                                    continue
                                else:
                                    print("That option does not exist! Please try again.")
                                    continue
                            else:
                                continue
                        case "3":
                            continue
                        case "4":
                            continue
                        case "5":
                            bank_case_use.CaseUseGetHistory.get_movements(account)
                        case "6":
                            break
                        case _:
                            print("That option does not exist, please try again!")
                            continue

if __name__=="__main__":
    main()