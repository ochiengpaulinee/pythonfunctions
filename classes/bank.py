class Account:
    bank = "KCB"

    def __init__(self,account_number,withdrawals,deposits,loan_balance):
        self.account_number = account_number
        self.withdrawals = []
        self.deposits= []
        self.loan_balance=0

    def balance(self):
        balance_amount = {self.deposit - self.withdrawals}
        return f"{balance_amount}"

    def open_account(self):
        return f"John opened a {self.bank} account {self.account_number} and deposited {self.deposit}ksh"

    def deposit(self,amount):
        transaction={
            "amount":amount,
            "narration":self.deposits
        }
        self.deposits.append(transaction) 
        return f"{transaction}"


    def withdrawal(self,withdraw):
        withdrawal_transacion={
            "amount":withdraw,
            "narration":"withdrawal"
        }
        self.withdrawals.append(withdrawal_transacion)
        return f"{withdrawal_transacion}"

    def print_statement(self):
        transactions=self.deposits+self.withdrawals
        for transaction in transactions:
            return f"{transaction['narration']}-{transaction['amount']}"

    def borrow_loan(self,loan_amount):
        if self.loan_balance>0:
            return f"YOur account has an outstanding loan"
        if loan_amount<100:
            return f"Requested loan amount must be more than 100"
        if len(self.deposits)<10:
            return f"Customer must have at least made 10 deposits"
        if loan_amount>sum(self.deposits)/3:
            return f"Loan amount must be less than or equal ti 1/3 of total deposits"
        self.loan_balance+=loan_amount



    def repay_loan(self,repay_loan):
        loan_balance-=repay_loan
        if repay_loan>loan_balance:
            balance+=repay_loan

    # Add a transfer method which accepts two attributes 
    # (amount and instance of another account). 
    # If the amount is less than the current 
    # instances balance, the method transfers the
    #  requested amount from the current account 
    #  to the passed account. The transfer is
    #   accomplished by reducing the current 
    #   account balance and depositing the requested 
    #   amount to the passed account.

    def transfer_cash(self,transfer_amount,account):
        if transfer_amount<balance:
            cash=balance-transfer_amount
            account+=cash
        return account
