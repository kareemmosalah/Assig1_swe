from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """Abstract base class for Payment methods."""
    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentMethod):
    """Concrete implementation for PayPal payment."""
    def pay(self, amount):
        return f"Paid ${amount:.2f} using PayPal."


class CreditCard(PaymentMethod):
    """Concrete implementation for Credit Card payment."""
    def pay(self, amount):
        return f"Paid ${amount:.2f} using Credit Card."