"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calcula o valor máximo de moeda estrangeira que pode ser obtido.

    :param budget: float - A quantidade de dinheiro que você planeja trocar.
    :param exchange_rate: float - O valor unitário da moeda estrangeira (taxa base).
    :param spread: int - A porcentagem cobrada como taxa de câmbio (lucro da casa de câmbio).
    :param denomination: int - O valor de uma única nota da moeda estrangeira.
    :return: int - O valor máximo que você pode obter em notas da denominação especificada.
    """
    # 1. Calcular a taxa de câmbio efetiva, incluindo o spread.
    # O spread torna a moeda estrangeira mais cara.
    effective_rate = exchange_rate * (1 + (spread / 100))

    # 2. Calcular quanto da moeda estrangeira você pode comprar com seu orçamento.
    # (Ex: R$ 1000 / 5.20 R$/€ = 192.30 €)
    total_foreign_currency = budget / effective_rate

    # 3. Calcular o valor final com base na denominação das notas.
    # Você só pode receber um número inteiro de notas.
    # (Ex: 192.30 € // 20 € = 9 notas)
    # (9 notas * 20 € = 180 €)
    final_value = (total_foreign_currency // denomination) * denomination

    return int(final_value)
