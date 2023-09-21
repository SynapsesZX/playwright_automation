import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect
from api.api_body import DeveloperRegistrationApi
from page_object.api_base_page import BasePage
import requests
import json


class TestDeveloperRegistration(BasePage):

    def test_developer_registration_with_valid_data(self):
        email = BasePage.randomWord_mails(self, value=7)
        username = BasePage.randomWord(self, value=7)
        request = requests.post("https://b08cbmkhu1.execute-api.us-west-2.amazonaws.com/api/developers",
                                json=DeveloperRegistrationApi.developer_registration_body(self, email,
                                                                                          username))
        request_body = request.json()

        return print(request_body['data']['id'])

    def test_test(self, create_developer):
        issues = create_developer
        print(issues)
