import unittest
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart


class TestCart(unittest.TestCase):
    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", cost=19.95))
        cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", cost=24.95))
        self.assertEqual(cart.total_cost(), 44.90)

    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0)))
        self.assertEqual(len(cart.items), 20)

    def test_discount_valid(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))
        cart.sort_by_title()
        self.assertEqual(
            [d.title for d in cart.items],
            ["Aladdin", "Star Wars", "The Lion King"],
        )

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))
        cart.sort_by_cost()
        self.assertEqual(
            [d.title for d in cart.items],
            ["Star Wars", "The Lion King", "Aladdin"],
        )


if __name__ == "__main__":
    unittest.main()
