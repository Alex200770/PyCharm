from abc import ABC, abstractmethod

class PaymentSystem(ABC):

    @abstractmethod
    def pay(self): ...

class WebMoney(PaymentSystem):

    def __init__(self, id):
        self.id = id

    def pay(self):
        print(self.id)

class CryptoGateway(PaymentSystem):

    def __init__(self, crypto_wallet):
        self.crypto_wallet = crypto_wallet

wm = WebMoney('1209')
wm.pay()
