import pytest

from Diplom_1.burger import Burger
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient


@pytest.fixture
def sample_burger():
    bun = Bun(name="Sample Bun", price=200.00)
    ingredient1 = Ingredient(name="Ingredient1", price=100.00,
                             ingredient_type="Type1")
    ingredient2 = Ingredient(name="Ingredient2", price=150.00,
                             ingredient_type="Type2")

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    return burger
