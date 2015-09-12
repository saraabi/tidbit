from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from tidbit.views import home_page
from tidbit.models import Entry, List

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

class ListAndEntryModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()
        # user = User.objects.get(username='saraabi')
        first_item = Entry()
        first_item.text = 'The first (ever) story entry'
        first_item.list = list_
        # first_tiem.user = user
        first_item.save()

        second_item = Entry()
        second_item.text = "Second story"
        second_item.list = list_
        # second_item.user = user
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Entry.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) story entry')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Second story')
        self.assertEqual(second_saved_item.list, list_)

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' % (list_.id,))
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Entry.objects.create(text='entry1', list=correct_list)
        Entry.objects.create(text='entry2', list=correct_list)
        other_list = List.objects.create()
        Entry.objects.create(text='other entry1', list=other_list)
        Entry.objects.create(text='other entry2', list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id,))

        self.assertContains(response, 'entry1')
        self.assertContains(response, 'entry2')
        self.assertNotContains(response, 'other entry1')
        self.assertNotContains(response, 'other entry2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)

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
        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))

class NewEntryTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/add_item' % (correct_list.id,),
            data = {'item_text': 'A new entry for an existing list'}
        )

        self.assertEqual(Entry.objects.count(),1)
        new_item = Entry.objects.first()
        self.assertEqual(new_item.text, 'A new entry for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/add_item' % (correct_list.id,),
            data = {'item_text': 'A new entry for an existing list'}
        )

        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))

