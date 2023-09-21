import time

from page_object.twitch_registration import TwitchRegistration



class TestUserRegistration:
    def test_user_registration_with_valid_data_by_email(self, set_up):
        user = TwitchRegistration(set_up)
        user.open_link('https://www.twitch.tv/')
        user.click_the_register_button()
        user.registration_pop_up_appears()
        user.registration_header_is_displayed()
        time.sleep(5)
