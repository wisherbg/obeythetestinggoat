from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):

    # Edith has heard of a website that provides to-do lists to users
    # She goes online to check its capabilities
    self.browser.get(self.live_server_url)

    # She immediately sees that the title and header has To-Do in it.

    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # She is invited to enter a to-do item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    # She types "Buy peacock feathers" into a text box
    inputbox.send_keys('Buy peacock feathers')

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in the to-do list
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

    # There is still a text box inviting her to add another item.
    # She enters "Use peacock feathers to make a fly"
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)
    
    # The page updates itself and now shows both items on her list
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
    self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

    self.fail('Finish the test!')

    # Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL for her
    # There is explanatory text about that\

    # She visits that URL and her to-do list is still there

    # Satisfied, she goes back to sleep