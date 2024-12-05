from rest_framework.test import APITestCase
from rest_framework import status

from users.tests.utils import get_member_user


class TestUserPerms(APITestCase):
    def setUp(self):
        self.user = get_member_user()
        response = self.client.post('/users/token/', {'username': 'tester', 'password': 'qwerty'})
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_user_delete(self):
        response = self.client.delete('/users/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
