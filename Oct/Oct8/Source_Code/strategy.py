class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError()

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)


payment_context = PaymentContext(CreditCardPayment())
payment_context.execute_payment(100)

payment_context.set_strategy(PayPalPayment())
payment_context.execute_payment(150)
