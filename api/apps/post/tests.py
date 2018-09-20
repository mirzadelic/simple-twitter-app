from django.urls import reverse

from rest_framework.test import APITestCase

from .models import Post


class PostTests(APITestCase):

    def setUp(self):
        self.post1 = Post.objects.create(name='Mirza', content='First tweet')
        self.post2 = Post.objects.create(name='Bob', content='My first tweet')

        self.url = reverse('api:post:post-list')

    def test__api__get(self):
        ''' Test get list of posts
        '''

        response = self.client.get(self.url)
        data = response.json()

        self.assertEqual(response.status_code, 200)

        self.assertEqual(data[0]['name'], self.post2.name)
        self.assertEqual(data[0]['content'], self.post2.content)

        self.assertEqual(data[1]['name'], self.post1.name)
        self.assertEqual(data[1]['content'], self.post1.content)

    def test__api__post(self):
        ''' Test post new post
        '''

        data = {
            'name': 'Jane',
            'content': 'Hi all'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(Post.objects.count(), 3)

        new_post = Post.objects.first()
        self.assertEqual(data['name'], new_post.name)
        self.assertEqual(data['content'], new_post.content)

    def test__api__put(self):
        ''' Test update post
        '''

        new_data = {
            'content': 'My first post'
        }
        url = reverse('api:post:post-detail', kwargs={'pk': self.post1.pk})
        response = self.client.patch(url, new_data)

        data = response.json()
        self.assertEqual(data['content'], new_data['content'])

        self.assertEqual(response.status_code, 200)

        post = Post.objects.get(pk=self.post1.pk)
        self.assertEqual(post.content, new_data['content'])

    def test__api__delete(self):
        ''' Test update post
        '''

        url = reverse('api:post:post-detail', kwargs={'pk': self.post1.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

        self.assertEqual(Post.objects.count(), 1)
