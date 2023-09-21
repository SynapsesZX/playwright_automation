import pytest

from page_object.developer_registration import DeveloperRegistration
from playwright.sync_api import Page
import time


class TestDeveloperRegistration:
    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_required_data_step1(self, set_up, page: Page):
        user = DeveloperRegistration(set_up)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer')
        user.click_start_now_button()
        user.step_1_of_4_label_appears()
        user.next_button_is_disabled()
        user.write_valid_data_in_email_input_field()
        user.write_valid_data_in_username_input_field()
        user.write_valid_data_in_first_name_input_field()
        user.write_valid_data_in_last_name_input_field()
        user.focus_lost()
        user.next_button_is_enabled()
        user.click_the_next_button()
        user.phone_number_not_marked_as_required()
        user.step_2_of_4_label_appears()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_required_data_step1(self, set_up, page: Page):
        user = DeveloperRegistration(set_up)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer')
        user.click_start_now_button()
        user.step_1_of_4_label_appears()
        user.next_button_is_disabled()
        user.write_invalid_data_in_email_input_field()
        user.focus_lost()
        user.email_data_validation_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_empty_required_data_step1(self, set_up, page: Page):
        user = DeveloperRegistration(set_up)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer')
        user.click_start_now_button()
        user.step_1_of_4_label_appears()
        user.next_button_is_disabled()
        user.write_valid_data_in_email_input_field()
        user.remove_all_data_in_email_input_field()
        user.focus_lost()
        user.email_empty_data_validation_hint_appears()
        user.write_valid_data_in_username_input_field()
        user.remove_all_data_in_username_input_field()
        user.focus_lost()
        user.username_is_required_validation_hint_appears()
        user.write_valid_data_in_first_name_input_field()
        user.remove_all_data_in_first_name_input_field()
        user.focus_lost()
        user.first_name_is_required_validation_hint_appears()
        user.write_valid_data_in_last_name_input_field()
        user.remove_all_data_in_last_name_input_field()
        user.focus_lost()
        user.last_name_is_required_validation_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_already_registered_data_step1(self, set_up, page: Page):
        user = DeveloperRegistration(set_up)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer')
        user.click_start_now_button()
        user.step_1_of_4_label_appears()
        user.next_button_is_disabled()
        user.write_already_registered_data_in_email_input_field()
        user.write_already_registered_data_in_username_input_field()
        user.write_valid_data_in_first_name_input_field()
        user.write_valid_data_in_last_name_input_field()
        user.focus_lost()
        user.click_the_next_button()
        user.username_uniqueness_validation_hint_appears()
        user.remove_all_data_in_username_input_field()
        user.write_valid_data_in_username_input_field()
        user.focus_lost()
        user.click_the_next_button()
        user.email_uniqueness_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_cancel_button_in_developer_registration_step1(self, set_up, page: Page):
        user = DeveloperRegistration(set_up)
        user.open_link('https://qa-h360-marketplace.softservetest.com/developer')
        user.click_start_now_button()
        user.step_1_of_4_label_appears()
        user.click_cancel_button()
        user.registration_form_disappears()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_required_data_step2(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step1(set_up, page)
        user = DeveloperRegistration(set_up)
        user.next_button_is_disabled()
        user.write_valid_data_in_password_input_field()
        user.write_valid_data_in_confirm_password_input_field()
        user.focus_lost()
        user.next_button_is_enabled()
        user.click_the_next_button()
        user.step_3_of_4_label_appears()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_min_characters_required_data_step2(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step1(set_up, page)
        user = DeveloperRegistration(set_up)
        user.next_button_is_disabled()
        user.write_min_characters_data_in_password_input_field()
        user.focus_lost()
        user.password_characters_validation_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_data_step2(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step1(set_up, page)
        user = DeveloperRegistration(set_up)
        user.next_button_is_disabled()
        user.write_invali_data_in_password_input_field()
        user.focus_lost()
        user.password_invalid_data_validation_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_invalid_confirm_password_data_step2(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step1(set_up, page)
        user = DeveloperRegistration(set_up)
        user.next_button_is_disabled()
        user.write_valid_data_in_password_input_field()
        user.write_different_data_in_confirm_password_input_field()
        user.focus_lost()
        user.confirm_password_does_not_much_validation_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_previous_button_step2(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step1(set_up, page)
        user = DeveloperRegistration(set_up)
        user.focus_lost()
        user.click_previous_button()
        user.step_1_of_4_label_appears()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_required_valid_data_step3(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step2(set_up, page)
        user = DeveloperRegistration(set_up)
        user.upload_valid_company_logo()
        user.write_valid_data_in_company_website_input_field()
        user.write_valid_data_in_company_name_input_field()
        user.click_categories_drop_down_icon()
        user.select_category()
        user.click_categories_drop_down_icon()
        user.write_valid_data_in_short_description_text_area()
        user.write_valid_data_in_long_description_text_area()
        user.focus_lost()
        user.next_button_is_enabled()
        user.click_the_next_button()
        user.step_4_of_4_label_appears()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_empty_required_data_step3(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step2(set_up, page)
        user = DeveloperRegistration(set_up)
        user.upload_valid_company_logo()
        user.write_valid_data_in_company_website_input_field()
        user.write_valid_data_in_company_name_input_field()
        user.click_categories_drop_down_icon()
        user.select_category()
        user.click_categories_drop_down_icon()
        user.write_valid_data_in_short_description_text_area()
        user.write_valid_data_in_long_description_text_area()
        user.click_remove_app_logo_icon()
        user.remove_data_in_company_website_input_field()
        user.remove_data_in_company_name_input_field()
        user.click_categories_drop_down_icon()
        user.select_category()
        user.click_categories_drop_down_icon()
        user.remove_data_in_short_description_text_area()
        user.remove_data_in_long_description_text_area()
        user.focus_lost()
        user.company_name_is_required_validation_hint_appears()
        user.company_website_is_required_validation_hint_appears()
        user.short_description_is_required_validation_hint_appears()
        user.long_description_is_required_validation_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_min_characters_validation_step3(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step2(set_up, page)
        user = DeveloperRegistration(set_up)
        user.write_min_characters_data_in_short_description_text_area()
        user.write_min_characters_data_in_long_description_text_area()
        user.focus_lost()
        user.short_description_characters_validation_hint_appears()
        user.long_description_is_required_validation_hint_appears()
        user.next_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_max_img_size_step3(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step2(set_up, page)
        user = DeveloperRegistration(set_up)
        user.upload_company_logo_with_more_than_1mb_size()
        user.focus_lost()
        user.app_logo_validation_hint_appears()

    @pytest.mark.developer_registration_regression
    def test_previous_button_step3(self, set_up, page: Page):
        self.test_developer_registration_with_valid_required_data_step2(set_up, page)
        user = DeveloperRegistration(set_up)
        user.click_previous_button()
        user.step_2_of_4_label_appears()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_data_step4(self, set_up, page: Page):
        self.test_developer_registration_with_required_valid_data_step3(set_up, page)
        user = DeveloperRegistration(set_up)
        user.submit_button_is_disabled()
        user.click_the_country_drop_down_icon()
        user.select_valid_country()
        user.add_valid_data_in_city_input_field()
        user.add_valid_data_in_postal_code_input_field()
        user.add_valid_data_in_address_input_field()
        user.accept_policy_check_box()
        user.submit_button_is_enabled()
        user.click_submit_button()
        user.success_message_is_displayed()

    @pytest.mark.developer_registration_regression
    def test_state_label_after_selecting_united_states_country_step4(self, set_up, page: Page):
        self.test_developer_registration_with_required_valid_data_step3(set_up, page)
        user = DeveloperRegistration(set_up)
        user.submit_button_is_disabled()
        user.click_the_country_drop_down_icon()
        user.select_united_states_country()
        user.state_label_appears()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_valid_and_united_states_country_data_step4(self, set_up, page: Page):
        self.test_developer_registration_with_required_valid_data_step3(set_up, page)
        user = DeveloperRegistration(set_up)
        user.submit_button_is_disabled()
        user.click_the_country_drop_down_icon()
        user.select_united_states_country()
        user.state_label_appears()
        user.click_state_drop_down_trigger()
        user.select_state()
        user.add_valid_data_in_city_input_field()
        user.add_valid_data_in_postal_code_input_field()
        user.add_valid_data_in_address_input_field()
        user.accept_policy_check_box()
        user.submit_button_is_enabled()
        user.click_submit_button()
        user.success_message_is_displayed()

    @pytest.mark.developer_registration_regression
    def test_developer_registration_with_empty_required_data_step4(self, set_up, page: Page):
        self.test_developer_registration_with_required_valid_data_step3(set_up, page)
        user = DeveloperRegistration(set_up)
        user.submit_button_is_disabled()
        user.click_the_country_drop_down_icon()
        user.select_valid_country()
        user.add_valid_data_in_city_input_field()
        user.add_valid_data_in_postal_code_input_field()
        user.add_valid_data_in_address_input_field()
        user.accept_policy_check_box()
        user.remove_data_in_city_input_field()
        user.remove_data_in_postal_code_input_field()
        user.remove_data_in_address_input_field()
        user.accept_policy_check_box()
        user.focus_lost()
        user.city_is_required_validation_hint_appears()
        user.postal_code_is_required_validation_hint_appears()
        user.address_is_required_validation_hint_appears()
        user.policy_terms_is_required_validation_hint_appears()
        user.submit_button_is_disabled()

    @pytest.mark.developer_registration_regression
    def test_previous_button_step4(self, set_up, page: Page):
        self.test_developer_registration_with_required_valid_data_step3(set_up, page)
        user = DeveloperRegistration(set_up)
        user.click_previous_button()
        user.step_3_of_4_label_appears()

