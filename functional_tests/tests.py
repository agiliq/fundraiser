from random import randint

from django.test.client import Client
from django.contrib.auth.models import User
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from campaigns.models import Category
from people.models import Person


class RegisterSigninTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.delete_all_cookies()
        self.c = Client()
        self.user = User.objects.create_superuser(
            username="admin", email="admin@agiliq.com", password="admin")
        self.test_user1 = {'username': 'test_1',
                           'password': 'pass_1',
                           'email': 'test_1@testing.com',
                           'address': '#101, test street, test apartments',
                           'website': 'http://www.one-test.com', }
        self.registration({'username': 'test_2',
                           'password': 'pass',
                           'email': 'test_2@testing.com',
                           'address': '#202, test street, test apartments',
                           'website': 'http://www.two-test.com', })
        self.categories = ['App', 'Music', 'Art', 'Technology', 'Publishing']
        for each in self.categories:
            Category.objects.create(name=each)

    def tearDown(self):
        self.browser.quit()

    def registration(self, user_dict):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_partial_link_text("Sign Up").click()
        username = self.browser.find_element_by_name('username')
        password1 = self.browser.find_element_by_name('password1')
        password2 = self.browser.find_element_by_name('password2')
        email = self.browser.find_element_by_name('email')
        address = self.browser.find_element_by_name('address')
        website = self.browser.find_element_by_name('website')

        username.send_keys(user_dict['username'])
        password1.send_keys(user_dict['password'])
        password2.send_keys(user_dict['password'])
        email.send_keys(user_dict['email'])
        address.send_keys(user_dict['address'])
        website.send_keys(user_dict['website'])
        website.send_keys(Keys.ENTER)

        self.assertIsNotNone(
            self.browser.find_elements_by_class_name('help-inline'))
        self.assertEqual(self.live_server_url, self.browser.current_url[:-1])
        user_link = self.browser.find_element_by_partial_link_text(
            user_dict['username'].capitalize())
        self.assertIsNotNone(user_link)
        self.assertEqual(user_link.get_attribute('class'), 'dropdown-toggle')

        menu = self.browser.find_element_by_partial_link_text(
            user_dict['username'].capitalize())

        self.assertIsNotNone(menu)

        menu.send_keys(Keys.DOWN, Keys.ENTER)

    def login(self, usrname, passwrd):
        login_link = self.browser.find_element_by_partial_link_text("Login")
        login_link.click()
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.clear()
        password.clear()
        username.send_keys(usrname)
        password.send_keys(passwrd)
        password.send_keys(Keys.ENTER)
        menu = self.browser.find_elements_by_partial_link_text(
            usrname.capitalize())

        self.assertIsNotNone(menu)
        # self.assertIsNone(
        #     self.browser.find_elements_by_class_name('help-inline'))

    def create_campaign(self, user_tup, category=0):
        self.login(user_tup[0], user_tup[1])
        self.browser.find_element_by_partial_link_text(
            'Create a Campaign').click()
        cat = self.browser.find_element_by_id('id_category')
        if not category:
            cat.find_elements_by_tag_name('option')[randint(1, 5)].click()
        else:
            cat.find_elements_by_tag_name('option')[category].click()
        self.browser.find_element_by_id('id_campaign_name').send_keys(
            'Campaign one')
        self.browser.find_element_by_id('id_target_amount').clear()
        self.browser.find_element_by_id('id_target_amount').send_keys(
            '15000')
        self.browser.find_element_by_id('id_cause').send_keys('Test Cause')

        self.browser.find_element_by_name('fund-dist-desc1').send_keys(
            'This')
        self.browser.find_element_by_name('fund-dist-amt1').send_keys(
            '10000')
        self.browser.find_element_by_xpath(
            "//table[@class='fund-dist']\
            //i[@class='icon-plus-sign']").click()
        self.browser.find_element_by_name('fund-dist-desc2').send_keys(
            'That')
        self.browser.find_element_by_name('fund-dist-amt2').send_keys(
            '5000')

        self.browser.find_element_by_name(
            'rewards1').send_keys('Reward one point zero')
        self.browser.find_element_by_xpath("//table[@class='rewards']\
            //i[@class='icon-plus-sign']").click()
        self.browser.find_element_by_name(
            'rewards2').send_keys('Reward two point zero')

        self.browser.find_element_by_name(
            'name1').clear()
        self.browser.find_element_by_name(
            'name1').send_keys(self.test_user1['username'].capitalize())
        self.browser.find_element_by_name(
            'role1').send_keys('Some role')
        self.browser.find_element_by_name(
            'short-description1').send_keys('Blah bio')
        self.browser.find_element_by_name(
            'fb-url1').send_keys('http://fb.com/testone')
        self.browser.find_element_by_xpath(
            "//table[@class='team-member']\
            //i[@class='icon-plus-sign']").click()
        self.browser.find_element_by_name(
            'name2').send_keys('Other guy')
        self.browser.find_element_by_name(
            'role2').send_keys('Does nothing')
        self.browser.find_element_by_name(
            'short-description2').send_keys('Retard')
        self.browser.find_element_by_name(
            'fb-url2').send_keys('http://fb.com/reetart')
        self.browser.find_element_by_tag_name(
            'button').submit()
        self.browser.find_element_by_link_text(
            'My Campaigns').click()
        self.assertIsNotNone(
            self.browser.find_elements_by_partial_link_text('Campaign one'))
        self.browser.find_element_by_partial_link_text(
            user_tup[0].capitalize()).send_keys(
            Keys.DOWN, Keys.ENTER)

    def approve_campaign(self):
        self.login('admin', 'admin')
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_partial_link_text('Unapproved').click()
        self.browser.find_element_by_tag_name('button').click()
        self.browser.find_element_by_partial_link_text(
            'Admin').send_keys(Keys.DOWN, Keys.ENTER)

    def test_can_new_user_register(self):
        self.registration(self.test_user1)

    def test_can_registered_user_login_and_logout(self):
        self.browser.get(self.live_server_url)
        login = self.browser.find_element_by_partial_link_text("Login")
        login.click()
        self.login('test_2', 'pass')
        menu = self.browser.find_element_by_partial_link_text(
            'Test_2')

        self.assertIsNotNone(menu)

        menu.send_keys(Keys.DOWN, Keys.ENTER)

        self.assertIsNotNone(
            self.browser.find_element_by_partial_link_text("Sign Up"))

    def test_unregistered_user_can_not_login(self):
        self.browser.get(self.live_server_url)
        login_link = self.browser.find_element_by_partial_link_text("Login")
        login_link.click()
        login_link = self.browser.find_element_by_partial_link_text("Login")
        login_link.click()
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.clear()
        password.clear()
        username.send_keys('unregistered')
        password.send_keys('somepassword')
        password.send_keys(Keys.ENTER)
        self.assertIn(
            "Please enter a correct username and password",
            self.browser.find_element_by_class_name('help-inline').text, )

    def test_redirects_new_user_to_login_page(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_partial_link_text(
            'Create a Campaign').click()
        self.assertIn('http://localhost:8081/accounts/login',
                      self.browser.current_url)

    def test_unapproved_campaigns_does_not_appear_on_home_page(self):
        self.create_campaign(('test_2', 'pass'))
        self.browser.get(self.live_server_url)
        self.assertEqual(
            self.browser.find_elements_by_partial_link_text('Campaign one'),
            [])

    def test_approved_campaigns_appear_on_home_page(self):
        self.create_campaign(('test_2', 'pass'))
        self.approve_campaign()
        self.browser.get(self.live_server_url)
        self.assertIsNotNone(
            self.browser.find_element_by_partial_link_text('Campaign one'))

    def test_user_can_donate_on_other_users_campaign(self):
        self.registration(self.test_user1)
        self.create_campaign((self.test_user1['username'],
                              self.test_user1['password']))

        # self.browser.get(self.live_server_url)
        self.approve_campaign()

        self.login('test_2', 'pass')

        self.browser.find_element_by_link_text('Campaign one').click()
        self.browser.find_element_by_tag_name('button').click()
        self.browser.find_element_by_name(
            'donation').send_keys('10123')
        self.browser.find_element_by_xpath(
            "//input[@type='submit']").submit()
        self.assertIsNotNone(
            self.browser.find_elements_by_xpath('//td[p=10123]'))

    def test_campaign_appears_under_right_category(self):
        self.registration(self.test_user1)
        self.create_campaign((self.test_user1['username'],
                              self.test_user1['password']),
                             3, )
        self.approve_campaign()
        self.browser.find_element_by_partial_link_text('Categories').click()
        self.browser.find_element_by_partial_link_text(
            self.categories[2]).click()
        self.assertIsNotNone(
            self.browser.find_element_by_partial_link_text('Campaign one'))
