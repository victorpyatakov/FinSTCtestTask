from django.test import TestCase

from .models import Dealer, Car


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_dealer = Dealer.objects.create(name='test_dealaer', city='Spb')
        test_dealer.save()

        test_car = Car.objects.create(dealer_id=test_dealer, name='test_car', price='2000.00', color='black')
        test_car.save()

    def test_car_content(self):
        car = Car.objects.get(id=1)
        car_dealer = f'{car.dealer_id}'
        car_name = f'{car.name}'
        car_price = f'{car.price}'
        car_color = f'{car.color}'
        self.assertEqual(car_dealer, 'test_dealaer')
        self.assertEqual(car_name, 'test_car')
        self.assertEqual(car_price, '2000.00')
        self.assertEqual(car_color, 'black')
