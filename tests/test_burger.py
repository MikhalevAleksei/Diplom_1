import pytest

from Diplom_1.praktikum import ingredient_types
from Diplom_1.burger import Burger
from Diplom_1.praktikum.bun import Bun


class TestBurger:

    def test_set_buns(self):
        bun = Bun(name="Sample Bun", price=2.0)
        burger = Burger()
        burger.set_buns(bun)
        assert isinstance(burger.bun, Bun)

    @pytest.mark.parametrize(
        'ingredient, expected_result', [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, ['SAUCE']),
            (ingredient_types.INGREDIENT_TYPE_FILLING, ['FILLING'])
        ]
    )
    def test_add_ingredient(self, ingredient, expected_result):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == expected_result

    def test_remove_ingredient(self, sample_burger):
        sample_burger.remove_ingredient(0)

        assert len(sample_burger.ingredients) == 1

    def test_price_after_removing_of_ingredient(self, sample_burger):
        actual_price = sample_burger.get_price()
        sample_burger.remove_ingredient(0)

        assert sample_burger.get_price() == actual_price - 100

    def test_move_ingredient(self, sample_burger):
        initial_ingredients = sample_burger.ingredients.copy()

        sample_burger.move_ingredient(0, 1)

        assert sample_burger.ingredients[0] == initial_ingredients[1]
        assert sample_burger.ingredients[1] == initial_ingredients[0]

    def test_get_price(self, sample_burger):
        assert sample_burger.get_price() == 650
