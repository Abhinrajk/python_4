#2. Online Payment System (Polymorphism)


class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)


class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card.")


class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI.")


class WalletPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Wallet.")


# Creating payment objects
payment1 = CreditCardPayment()
payment2 = UPIPayment()
payment3 = WalletPayment()

# Processing payments (Polymorphism)
payments = [payment1, payment2, payment3]

for payment in payments:
    payment.pay(1000)