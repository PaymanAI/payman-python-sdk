# Version

Methods:

- <code title="get /version">client.version.<a href="./src/paymanai/resources/version.py">get_server_version</a>() -> BinaryAPIResponse</code>

# Me

Methods:

- <code title="get /me">client.me.<a href="./src/paymanai/resources/me.py">me</a>() -> BinaryAPIResponse</code>

# Balances

Types:

```python
from paymanai.types import BalanceGetSpendableBalanceResponse
```

Methods:

- <code title="get /balances/currencies/{currency}">client.balances.<a href="./src/paymanai/resources/balances.py">get_spendable_balance</a>(currency) -> <a href="./src/paymanai/types/balance_get_spendable_balance_response.py">BalanceGetSpendableBalanceResponse</a></code>

# Payments

Types:

```python
from paymanai.types import PaymentSendPaymentResponse
```

Methods:

- <code title="post /payments/send-payment">client.payments.<a href="./src/paymanai/resources/payments.py">send_payment</a>(\*\*<a href="src/paymanai/types/payment_send_payment_params.py">params</a>) -> <a href="./src/paymanai/types/payment_send_payment_response.py">PaymentSendPaymentResponse</a></code>

# SpendLimits

Methods:

- <code title="get /spend-limits">client.spend_limits.<a href="./src/paymanai/resources/spend_limits.py">get_spend_limits</a>() -> BinaryAPIResponse</code>
