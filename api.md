# Wallets

Types:

```python
from paymanai.types import WalletGetWalletResponse
```

Methods:

- <code title="get /wallets/{id}">client.wallets.<a href="./src/paymanai/resources/wallets.py">get_wallet</a>(id) -> <a href="./src/paymanai/types/wallet_get_wallet_response.py">WalletGetWalletResponse</a></code>

# Version

Methods:

- <code title="get /version">client.version.<a href="./src/paymanai/resources/version.py">get_server_version</a>() -> BinaryAPIResponse</code>

# Balances

Types:

```python
from paymanai.types import BalanceGetCustomerBalanceResponse, BalanceGetSpendableBalanceResponse
```

Methods:

- <code title="get /balances/customers/{customerId}/currencies/{currency}">client.balances.<a href="./src/paymanai/resources/balances.py">get_customer_balance</a>(currency, \*, customer_id) -> <a href="./src/paymanai/types/balance_get_customer_balance_response.py">BalanceGetCustomerBalanceResponse</a></code>
- <code title="get /balances/currencies/{currency}">client.balances.<a href="./src/paymanai/resources/balances.py">get_spendable_balance</a>(currency) -> <a href="./src/paymanai/types/balance_get_spendable_balance_response.py">BalanceGetSpendableBalanceResponse</a></code>

# Payments

Types:

```python
from paymanai.types import (
    PaymentInitiateCustomerDepositResponse,
    PaymentSearchDestinationsResponse,
    PaymentSendPaymentResponse,
)
```

Methods:

- <code title="post /payments/customer-deposit-link">client.payments.<a href="./src/paymanai/resources/payments.py">initiate_customer_deposit</a>(\*\*<a href="src/paymanai/types/payment_initiate_customer_deposit_params.py">params</a>) -> <a href="./src/paymanai/types/payment_initiate_customer_deposit_response.py">PaymentInitiateCustomerDepositResponse</a></code>
- <code title="get /payments/search-destinations">client.payments.<a href="./src/paymanai/resources/payments.py">search_destinations</a>(\*\*<a href="src/paymanai/types/payment_search_destinations_params.py">params</a>) -> <a href="./src/paymanai/types/payment_search_destinations_response.py">PaymentSearchDestinationsResponse</a></code>
- <code title="post /payments/send-payment">client.payments.<a href="./src/paymanai/resources/payments.py">send_payment</a>(\*\*<a href="src/paymanai/types/payment_send_payment_params.py">params</a>) -> <a href="./src/paymanai/types/payment_send_payment_response.py">PaymentSendPaymentResponse</a></code>
