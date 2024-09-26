import pytest
from src.calculator import sum
from src.bank_account import BankAccount

def test_sum():
    a = 4
    b = 5

    assert sum(4, 5) == 9

@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_ammounts(ammount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected

# TODO: Create a test that doesn't allow the deposit to be negative
def test_deposit_negative_amount():
    account = BankAccount(balance=1000, log_file="transactions.txt")
    with pytest.raises(ValueError):
        account.deposit(-100)

@pytest.mark.parametrize("initial_balance, deposit_amount, expected_balance, exception", [
    (1000, 500, 1500, None),   # Depósito positivo
    (1000, 0, 1000, None),     # Depósito de cero
    (1000, -100, 1000, ValueError)  # Depósito negativo
])
def test_deposit(initial_balance, deposit_amount, expected_balance, exception):
    account = BankAccount(balance=initial_balance, log_file="transactions.txt")

    if exception:
        with pytest.raises(exception):
            account.deposit(deposit_amount)
    else:
        new_balance = account.deposit(deposit_amount)
        assert new_balance == expected_balance