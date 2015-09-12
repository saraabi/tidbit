from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_story_table(self, row_text):
        table = self.browser.find_element_by_id('id_story_table')
        rows = table.find_elements_by_tag_name('tr')        
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_story_and_retrieve_it_later(self):
        # Fulan has head about a cool new online personal story app. She checks it out:
        self.browser.get(self.live_server_url)

        # She notices that the page title and header mention stories
        self.assertIn('Stories', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Stories', header_text)

        # She is invited to enter in today's story straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter the story of your day'
        )

        # She types "I bought peacock feathers from Azerbaijan" into a text box
        inputbox.send_keys('I bought peacock feathers from Azerbaijan')

        # When she hits enter, she is taken to a new URL, and now the page lists her story as
        # an item in a table.
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(10)
        fulan_story_url = self.browser.current_url
        self.assertRegex(fulan_story_url, '/stories/.+')
        self.check_for_row_in_story_table('I bought peacock feathers from Azerbaijan')

        # There is still a text box inviting her to change her story. She writes
        # "I bought two bright red peacock feathers from a chicken farmer in Azerbaijan"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('I bought two bright red peacock feathers from a chicken farmer in Azerbaijan')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_story_table('I bought peacock feathers from Azerbaijan')
        self.check_for_row_in_story_table('I bought two bright red peacock feathers from a chicken farmer in Azerbaijan')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information of Fulan's is
        ## coming through from cookies etc.
        self.browser.quit()
        self.browser - webdriver.Firefox()

        # Francis visits the homepage. There is no sign of Fulan's stories.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('I bought peacock feathers from Azerbaijan', page_text)
        self.assertNotIn('I bought two bright red peacock feathers from a chicken farmer in Azerbaijan', page_text)

        # Francis starts a new list by entering a new item. He is less interesting than Fulan.
        inputbox - self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('I bought milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_story_url = self.browser.current_url
        self.assertRegex(francis_story_url, '/stories/.+')
        self.assertNotEqual(francis_story_url, fulan_story_url)

        # Again, there is no trace of Fulan's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('I bought peacock feathers from Azerbaijan', page_text)
        self.assertIn('I bought milk', page_text)

        # Satisfied, they both go back to sleep.

        self.fail('Finish the test!')


