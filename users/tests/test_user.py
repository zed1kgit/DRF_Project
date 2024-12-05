from rest_framework.test import APITestCase
from rest_framework import status

from users.tests.utils import get_admin_user

class TestUser(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'username': 'tester', 'password': 'qwerty'})
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_user_create(self):
        data = {
            'username': 'tester2',
            'password': '123321123',
            'email': 'created_tester@test.com',
            'role': 'moderator',
        }
        response = self.client.post('/users/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'tester2')

    def test_user_update(self):
        response = self.client.patch(f'/users/{self.user.pk}/update/', {
            'email': 'updated_tester@test.com',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'updated_tester@test.com')

    def test_user_delete(self):
        response = self.client.delete(f'/users/{self.user.pk}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_list(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['username'], 'tester')

    def test_user_detail(self):
        response = self.client.get(f'/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'tester')

