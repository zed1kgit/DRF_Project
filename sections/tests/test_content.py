from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section, SectionContent
from users.tests.utils import get_admin_user


class TestSectionContent(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'username': 'tester', 'password': 'qwerty'})
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.test_section = Section.objects.create(
            title='Test Section',
            description='Test Description'
        )
        self.test_content = SectionContent.objects.create(
            section=self.test_section,
            title='Test Content title',
            content='Test Content'
        )

    def test_content_list(self):
        response = self.client.get('/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Content title')

    def test_content_create(self):
        response = self.client.post('/content/create/', {
            'section': self.test_section.pk,
            'title': 'Test Content title 2',
            'content': 'Test Content 2',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Content title 2')
        self.assertEqual(response.data['content'], 'Test Content 2')
        self.assertEqual(self.client.get('/content/').data['count'], 2)

    def test_content_retrieve(self):
        response = self.client.get(f'/content/{self.test_content.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Content title')
        self.assertEqual(response.data['content'], 'Test Content')

    def test_content_update(self):
        response = self.client.patch(f'/content/{self.test_content.pk}/update/', {
            'title': 'Test Content title 2',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Content title 2')
        self.assertEqual(response.data['content'], 'Test Content')

    def test_content_destroy(self):
        response = self.client.delete(f'/content/{self.test_content.pk}/destroy/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
