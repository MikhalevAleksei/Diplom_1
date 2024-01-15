from unittest.mock import Mock

from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.burger import Burger


def test_get_price():
    bun_mock = Mock(spec=Bun)
    ingredient_mock1 = Mock(spec=Ingredient)
    ingredient_mock2 = Mock(spec=Ingredient)

    bun_mock.get_price.return_value = 2.0
    ingredient_mock1.get_price.return_value = 1.0
    ingredient_mock2.get_price.return_value = 1.5

    burger = Burger()
    burger.set_buns(bun_mock)

    burger.add_ingredient(ingredient_mock1)
    burger.add_ingredient(ingredient_mock2)

    buns = (bun_mock.get_price() * 2)
    ingredient1 = ingredient_mock1.get_price()
    ingredient2 = ingredient_mock2.get_price()

    expected_price = buns + ingredient1 + ingredient2
    assert burger.get_price() == expected_price


def test_get_receipt():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = "TestBun"

    ingredient_mock1 = Mock(spec=Ingredient)
    ingredient_mock1.get_type.return_value = "Type1"
    ingredient_mock1.get_name.return_value = "Ingredient1"

    ingredient_mock2 = Mock(spec=Ingredient)
    ingredient_mock2.get_type.return_value = "Type2"
    ingredient_mock2.get_name.return_value = "Ingredient2"

    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock1)
    burger.add_ingredient(ingredient_mock2)

    receipt = burger.get_receipt()

    assert "TestBun" in receipt
    assert "Type1 ingredient1" in receipt
    assert "Type2 ingredient2" in receipt
    assert "Price: " in receipt
