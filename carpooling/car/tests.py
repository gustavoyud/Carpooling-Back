from rest_framework.test import APITestCase
from .models import Users

# Create your tests here.
class UsersAPITestCase(APITestCase):
    def setUp(self):
        user = Users.objects.create(
            name='teste', 
            email='teste@teste.com',
            geral_register=32121,
            address='teste',
            complement='teste123',
            ZIP=12345678,
            neighborhood='Teste',
            city='test',
            federal_unit='TS',
            phone=123214421,
            celphone=43123123,
            username='testando',
            )
    def test_single_user(self):
        user_count = Users.objects.count()
        self.assertEqual(user_count, 1)