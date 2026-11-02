import pytest

import inventory_management as inv


@pytest.fixture(autouse=True)
def clean_inventory():
    """Each test starts and ends with an empty inventory."""
    inv.inventory.clear()
    yield
    inv.inventory.clear()


@pytest.fixture
def stocked():
    inv.add_item("Apple", 0.5, 50)
    inv.add_item("Banana", 0.2, 60)


# add_item


def test_add_item_stores_price_and_stock():
    inv.add_item("Apple", 0.5, 50)
    assert inv.inventory["Apple"] == {"price": 0.5, "stock": 50}


def test_add_item_converts_numeric_strings():
    inv.add_item("Pear", "2.5", "3")
    assert inv.inventory["Pear"] == {"price": 2.5, "stock": 3}


def test_add_item_prints_success_message(capsys):
    inv.add_item("Apple", 0.5, 50)
    assert "added successfully" in capsys.readouterr().out


def test_add_item_rejects_duplicate_and_keeps_original(capsys):
    inv.add_item("Apple", 0.5, 50)
    inv.add_item("Apple", 9.9, 1)
    assert inv.inventory["Apple"] == {"price": 0.5, "stock": 50}
    assert "already exists" in capsys.readouterr().out


@pytest.mark.parametrize("price, stock", [("abc", 5), (1.0, "many")])
def test_add_item_rejects_non_numeric_values(price, stock, capsys):
    inv.add_item("Bad", price, stock)
    assert "Bad" not in inv.inventory
    assert "must be numeric" in capsys.readouterr().out


# update_stock


def test_update_stock_adds_quantity(stocked):
    inv.update_stock("Apple", 10)
    assert inv.inventory["Apple"]["stock"] == 60


def test_update_stock_subtracts_quantity(stocked):
    inv.update_stock("Apple", -20)
    assert inv.inventory["Apple"]["stock"] == 30


def test_update_stock_allows_exactly_zero(stocked):
    inv.update_stock("Apple", -50)
    assert inv.inventory["Apple"]["stock"] == 0


def test_update_stock_refuses_to_go_negative(stocked, capsys):
    inv.update_stock("Apple", -51)
    assert inv.inventory["Apple"]["stock"] == 50
    assert "Insufficient stock" in capsys.readouterr().out


def test_update_stock_missing_item(capsys):
    inv.update_stock("Ghost", 5)
    assert "not found" in capsys.readouterr().out
    assert "Ghost" not in inv.inventory


def test_update_stock_non_integer_quantity(stocked, capsys):
    inv.update_stock("Apple", "lots")
    assert inv.inventory["Apple"]["stock"] == 50
    assert "must be an integer" in capsys.readouterr().out


# check_availability


def test_check_availability_returns_stock(stocked):
    assert inv.check_availability("Banana") == 60


def test_check_availability_missing_item():
    assert inv.check_availability("Ghost") == "Item not found"


# sales_report


def test_sales_report_total_revenue(stocked):
    assert inv.sales_report({"Apple": 30, "Banana": 20}) == "Total revenue: $19.00"


def test_sales_report_reduces_stock(stocked):
    inv.sales_report({"Apple": 30, "Banana": 20})
    assert inv.inventory["Apple"]["stock"] == 20
    assert inv.inventory["Banana"]["stock"] == 40


def test_sales_report_skips_unknown_item(stocked, capsys):
    result = inv.sales_report({"Apple": 10, "Orange": 5})
    assert result == "Total revenue: $5.00"
    assert "'Orange' not found" in capsys.readouterr().out


def test_sales_report_skips_oversold_item_and_keeps_stock(stocked, capsys):
    result = inv.sales_report({"Apple": 51, "Banana": 10})
    assert result == "Total revenue: $2.00"
    assert inv.inventory["Apple"]["stock"] == 50
    assert "Insufficient stock for 'Apple'" in capsys.readouterr().out


def test_sales_report_empty_sales(stocked):
    assert inv.sales_report({}) == "Total revenue: $0.00"


def test_sales_report_can_sell_all_remaining_stock(stocked):
    assert inv.sales_report({"Apple": 50}) == "Total revenue: $25.00"
    assert inv.inventory["Apple"]["stock"] == 0


# Known issues: the current code does not validate these cases.
# strict xfail means the suite will tell you when you fix them.


@pytest.mark.xfail(strict=True, reason="add_item accepts negative stock")
def test_add_item_should_reject_negative_stock():
    inv.add_item("Odd", 1.0, -5)
    assert "Odd" not in inv.inventory


@pytest.mark.xfail(strict=True, reason="add_item accepts negative price")
def test_add_item_should_reject_negative_price():
    inv.add_item("Odd", -1.0, 5)
    assert "Odd" not in inv.inventory


@pytest.mark.xfail(strict=True, reason="sales_report accepts negative quantities")
def test_sales_report_should_ignore_negative_quantities(stocked):
    inv.sales_report({"Apple": -10})
    assert inv.inventory["Apple"]["stock"] == 50
