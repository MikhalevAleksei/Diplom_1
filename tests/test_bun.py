from Diplom_1.praktikum.bun import Bun


class TestBun:
    bun = Bun('Big_bun', 50)

    def test_get_name(self):
        bun_name = TestBun.bun.get_name()
        assert bun_name == 'Big_bun'

    def test_get_price(self):
        bun_price = TestBun.bun.get_price()
        assert bun_price == 50
