from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from tidbit.views import home_page
from tidbit.models import *

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

class EntryModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        # user = User.objects.get(username='saraabi')
        first_item = Entry()
        first_item.text = 'The first (ever) story entry'
        # first_tiem.user = user
        first_item.save()

        second_item = Entry()
        second_item.text = "Second story"
        # second_item.user = user
        second_item.save()

        saved_items = Entry.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) story entry')
        self.assertEqual(second_saved_item.text, 'Second story')

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-story-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        Entry.objects.create(text='entry1')
        Entry.objects.create(text='entry2')

        response = self.client.get('/lists/the-only-story-in-the-world/')

        self.assertContains(response, 'entry1')
        self.assertContains(response, 'entry2')

class NewListTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new story item'}
        )

        self.assertEqual(Entry.objects.count(), 1)
        new_item = Entry.objects.first()
        self.assertEqual(new_item.text, 'A new story item')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list entry'}
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/the-only-story-in-the-world/')
