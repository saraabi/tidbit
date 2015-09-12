from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_story_and_retrieve_it_later(self):
        # Fulan has head about a cool new online personal story app. She checks it out:
        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention stories
        self.assertIn('Stories', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Stories', header_text)

        # She is invited to enter in today's story straight away
        inputbox = self.broswer.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter the story of your day'
        )

        # She types "I bought peacock feathers from Azerbaijan" into a text box
        inputbox.send_keys('I bought peacock feathers from Azerbaijan')

        # When she hits enter, the page updates, and now the page lists her story
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'I bought peacock feathers from Azerbaijan' for row in rows)
        )

        # There is still a text box inviting her to change her story. She writes
        # "I bought two bright red peacock feathers from a chicken farmer in Azerbaijan"


        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
