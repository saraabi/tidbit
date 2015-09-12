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

        # When she hits enter, the page updates, and now the page lists her story
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(10)
        self.check_for_row_in_story_table('I bought peacock feathers from Azerbaijan')

        # There is still a text box inviting her to change her story. She writes
        # "I bought two bright red peacock feathers from a chicken farmer in Azerbaijan"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('I bought two bright red peacock feathers from a chicken farmer in Azerbaijan')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_story_table('I bought peacock feathers from Azerbaijan')
        self.check_for_row_in_story_table('I bought two bright red peacock feathers from a chicken farmer in Azerbaijan')

        # Fulan wonders whether the site will remember her stories. Then she sees that the site
        # has generated a unique URL for her -- this is some explanatory text to that effect.


        self.fail('Finish the test!')


