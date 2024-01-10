class TestSampleBurger:
    def test_sample_burger_name(self, sample_burger):
        name = sample_burger.bun.get_name()
        assert name == "Sample Bun"

    def test_sample_burger_price(self, sample_burger):
        price = sample_burger.bun.get_price()
        assert price == 200.00

    def test_sample_burger_quantity(self, sample_burger):
        quantity = len(sample_burger.ingredients)
        assert quantity == 2

    def test_sample_burger_name_of_first_ingredient(self, sample_burger):
        name_of_first_ingredient = sample_burger.ingredients[0].get_name()
        assert name_of_first_ingredient == "Ingredient1"

    def test_sample_burger_price_of_first_ingredient(self, sample_burger):
        price_of_first_ingredient = sample_burger.ingredients[0].get_price()
        assert price_of_first_ingredient == 100.00

    def test_sample_burger_name_of_second_ingredient(self, sample_burger):
        second_ingredient = sample_burger.ingredients[1].get_name()
        assert second_ingredient == "Ingredient2"

    def test_sample_burger_price_of_second_ingredient(self, sample_burger):
        price_of_second_ingredient = sample_burger.ingredients[1].get_price()
        assert price_of_second_ingredient == 150.00
