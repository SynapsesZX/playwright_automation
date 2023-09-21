import requests
import json
import pytest
from page_object.api_base_page import BasePage
import requests


class DeveloperRegistrationApi(BasePage):

    def developer_registration_body(self, email, username):
        body = {"email": "fghjgfjhjhgghghhghghgj@gmail.com",
                "first_name": "fdjdgfdjgfj",
                "last_name": "drfgjsdjfjd",
                "partner": {
                    "address": "QA",
                    "city": "QA",
                    "company_name": "QA",
                    "country": "US",
                    "description": "<p>fghfghghghghgfhfg</p>",
                    "short_description": "gfhgfh hgfhgfhgfhgfhgfhfgh fghfgfg",
                    "logo_path": "1691993311772456file_yose84l09p297bg16755hga.png",
                    "categories": ["47de5ab7-1500-4928-942c-9a7c567b8f7d"],
                    "postal_code": "QA",
                    "state": "US-AL",
                    "website": "https://www.google.com/"},
                "password": "I5594176960infqy!",
                "phone_number": "+56756565",
                "username": "fjghghghggfdjgdfjj"}

        body['email'] = email
        body['username'] = username
        return body
