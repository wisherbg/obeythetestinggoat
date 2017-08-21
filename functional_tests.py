from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):

    # Edith has heard of a website that provides to-do lists to users
    # She goes online to check its capabilities
    self.browser.get('http://localhost:8000')

    # She immediately sees that the title has To-Do in it.

    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # She is invited to enter a to-do item straight away

    # She types "Buy peacock feathers" into a text box

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in the to-do list

    # There is still a text box inviting her to add another item.
    # She enters "User peacock feathers to make a fly"

    # The page updates itself and now shows both items on her list

    # Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL for her
    # There is explanatory text about that\

    # She visits that URL and her to-do list is still there

    # Satisfied, she goes back to sleep

if __name__ == '__main__':
  unittest.main(warnings='ignore')