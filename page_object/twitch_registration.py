from page_object.base_page import BasePage
from playwright.sync_api import expect


class TwitchRegistration(BasePage):

    def click_the_register_button(self):
        self.page.locator('[data-a-target="signup-button"]').click()

    def registration_pop_up_appears(self):
        expect(self.page.locator('.auth-modal__left-content')).to_be_visible()

    def registration_header_is_displayed(self):
        expect(self.page.locator('#modal-root-header')).to_be_visible()

    def twitch_icon_is_displayed(self):
        expect(self.page.locator('.hYFjkm.tw-svg')).to_be_visible()

    def close_button_is_displayed(self):
        expect(self.page.locator('[data-a-target="modalClose"]')).to_be_visible()

    def username_input_field_is_empty(self):
        expect(self.page.locator('#signup-username')).to_be_empty()

    def password_input_field_is_empty(self):
        expect(self.page.locator('#password-input')).to_be_empty()





