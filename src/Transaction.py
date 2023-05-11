class Transaction:
    def __init__(self, amount, order, url_ok, url_ko, transaction_type='0', currency='840', language='0', paymentmethods='C'):
        self.DS_MERCHANT_AMOUNT = str(amount)
        self.DS_MERCHANT_ORDER = str(order)
        self.DS_MERCHANT_TRANSACTIONTYPE = str(transaction_type)
        self.DS_MERCHANT_CURRENCY = str(currency)
        self.DS_MERCHANT_URLOK = url_ok
        self.DS_MERCHANT_URLKO = url_ko
        self.DS_MERCHANT_CONSUMERLANGUAGE = language
        self.DS_MERCHANT_PAYMETHODS = paymentmethods
