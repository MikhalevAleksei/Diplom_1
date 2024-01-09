def test_sample_burger(sample_burger):
    assert sample_burger.bun.get_name() == "Sample Bun"
    assert sample_burger.bun.get_price() == 200.00
    assert len(sample_burger.ingredients) == 2
    assert sample_burger.ingredients[0].get_name() == "Ingredient1"
    assert sample_burger.ingredients[0].get_price() == 100.00
    assert sample_burger.ingredients[1].get_name() == "Ingredient2"
    assert sample_burger.ingredients[1].get_price() == 150.00
