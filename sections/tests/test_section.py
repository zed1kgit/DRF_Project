from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section
from users.tests.utils import get_admin_user


class TestSection(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'username': 'tester', 'password': 'qwerty'})
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.test_section = Section.objects.create(title='Test Section', description='Test Description')

    def test_retrieve_section(self):
        response = self.client.get(f'/section/{self.test_section.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Section')
        self.assertEqual(response.data['description'], 'Test Description')

    def test_update_section(self):
        response = self.client.patch(f'/section/{self.test_section.id}/update/', {'title': 'Test Updated Section'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Updated Section')
        self.assertEqual(response.data['description'], 'Test Description')

    def test_delete_section(self):
        response = self.client.delete(f'/section/{self.test_section.id}/destroy/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_sections(self):
        response = self.client.get('/section/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Section')

    def test_create_section(self):
        response = self.client.post('/section/create/',
                                    {'title': 'Test Section 2', 'description': 'Test Description 2'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Section 2')
        self.assertEqual(response.data['description'], 'Test Description 2')
        response = self.client.get('/section/')
        self.assertEqual(response.data['count'], 2)
