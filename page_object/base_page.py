from playwright.sync_api import Page
import random


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_link(self, link):
        """Basic method to open the link from playwright api"""
        self.page.goto(link)

    def randomWord_mails(self, value):
        """
            Basic method to add random email to elements
            :param value: an argument that indicates how much characters you want to add (integer)

        """
        consonants = "abcdfghjklmnpqrstvwxyz"
        email = '@gmail.com'
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(value)) + email

    def randomWord(self, value):
        """
            Basic method to add random text to elements
            :param value: an argument that indicates how much characters you want to add (integer)

        """
        consonants = "abcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(value))
