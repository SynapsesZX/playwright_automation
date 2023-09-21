from page_object.base_page import BasePage
from playwright.sync_api import expect


class DeveloperRegistration(BasePage):

    def click_start_now_button(self):
        self.page.get_by_text('Start Now!').click()

    def step_1_of_4_label_appears(self):
        self.page.wait_for_timeout(timeout=1000)
        self.page.get_by_text('Create your account 1 of 4 steps').is_visible()

    def write_valid_data_in_email_input_field(self):
        self.page.locator('#email').type(self.randomWord_mails(value=5))

    def remove_all_data_in_email_input_field(self):
        self.page.locator('#email').clear()

    def write_invalid_data_in_email_input_field(self):
        self.page.locator('#email').type('gfhgfhfgfgfgmail.com')

    def write_already_registered_data_in_email_input_field(self):
        self.page.locator('#email').type('igorzyabrov2050@gmail.com')

    def email_data_validation_hint_appears(self):
        expect(self.page.get_by_text('E-mail address should be contain a valid email address')).to_be_visible()

    def email_empty_data_validation_hint_appears(self):
        expect(self.page.get_by_text('E-mail address is required')).to_be_visible()

    def email_uniqueness_hint_appears(self):
        email = self.page.locator(
            "[class*='text-field_root__367aZ contact-information-form_emailField__z1-19'] [class='text-field_error__1kbJu'] span").text_content()
        assert email == 'We found a user with this e-mail address. If this is you, please log in.'

    def write_valid_data_in_username_input_field(self):
        self.page.locator('#userName').type(self.randomWord(value=5))

    def write_already_registered_data_in_username_input_field(self):
        self.page.locator('#userName').type('igor')

    def remove_all_data_in_username_input_field(self):
        self.page.locator('#userName').clear()

    def username_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('Username is required')).to_be_visible()

    def write_valid_data_in_first_name_input_field(self):
        self.page.locator('#firstName').type(self.randomWord(value=5))

    def remove_all_data_in_first_name_input_field(self):
        self.page.locator('#firstName').clear()

    def first_name_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('First name is required')).to_be_visible()

    def write_valid_data_in_last_name_input_field(self):
        self.page.locator('#lastName').type(self.randomWord(value=5))

    def remove_all_data_in_last_name_input_field(self):
        self.page.locator('#lastName').clear()

    def username_uniqueness_validation_hint_appears(self):
        username = self.page.locator(
            "[class*='contact-information-form_userNameField__HZQhu'] [class='text-field_error__1kbJu']").text_content()
        assert username == 'This Username is already exists'

    def last_name_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('Last name is required')).to_be_visible()

    def focus_lost(self):
        self.page.locator('.p-dialog-header').click()

    def next_button_is_disabled(self):
        expect(self.page.locator('#registration-form-submit-button')).to_be_disabled()

    def next_button_is_enabled(self):
        self.page.locator('#registration-form-submit-button').is_enabled()

    def click_the_next_button(self):
        self.page.locator('#registration-form-submit-button').click()

    def step_2_of_4_label_appears(self):
        self.page.wait_for_timeout(timeout=1000)
        self.page.get_by_text('Create your account 2 of 4 steps').is_visible()

    def phone_number_not_marked_as_required(self):
        self.page.get_by_text('Mobile phone is required').is_hidden()

    def click_cancel_button(self):
        self.page.locator('#registration-form-cancel-button').click()

    def registration_form_disappears(self):
        self.page.locator('.p-dialog-header').is_hidden()

    def write_valid_data_in_password_input_field(self):
        self.page.locator('#password').type('Ighjgh5656561!')

    def write_min_characters_data_in_password_input_field(self):
        self.page.locator('#password').type('Ig')

    def write_invali_data_in_password_input_field(self):
        self.page.locator('#password').type('I771948741iggf')

    def password_invalid_data_validation_hint_appears(self):
        expect(self.page.get_by_text('Password should be contain at least 1 symbol(s)')).to_be_visible()

    def password_characters_validation_hint_appears(self):
        expect(self.page.get_by_text('Password range should be 14-200 characters')).to_be_visible()

    def write_valid_data_in_confirm_password_input_field(self):
        self.page.locator('#confirmPassword').type('Ighjgh5656561!')

    def write_different_data_in_confirm_password_input_field(self):
        self.page.locator('#confirmPassword').type('Ighjgh5656561!ghg')

    def confirm_password_does_not_much_validation_hint_appears(self):
        expect(self.page.get_by_text('Confirm password does not match')).to_be_visible()

    def step_3_of_4_label_appears(self):
        self.page.wait_for_timeout(timeout=1000)
        self.page.get_by_text('Create your account 3 of 4 steps').is_visible()

    def upload_valid_company_logo(self):
        self.page.locator('#icon-file').set_input_files('D:/playwright_auto/img/app_logo.png')

    def upload_company_logo_with_more_than_1mb_size(self):
        self.page.locator('#icon-file').set_input_files('D:/playwright_auto/img/2mb.jpg')

    def write_valid_data_in_company_website_input_field(self):
        self.page.locator('#website').type('https://www.google.com/')

    def app_logo_validation_hint_appears(self):
        expect(self.page.get_by_text('Max size 1MB')).to_be_visible()

    def remove_data_in_company_website_input_field(self):
        self.page.locator('#website').clear()

    def write_valid_data_in_company_name_input_field(self):
        self.page.locator('#companyName').type('QA')

    def remove_data_in_company_name_input_field(self):
        self.page.locator('#companyName').clear()

    def click_previous_button(self):
        self.page.locator('#registration-form-back-button').click()

    def click_categories_drop_down_icon(self):
        self.page.locator(
            '[class*="company-information-form_categoryRoot__3bbfg"] [class="p-multiselect-trigger"]').click()

    def select_category(self):
        self.page.locator('[class*="p-multiselect-items"][class*="p-component"] li:first-child').click()

    def write_valid_data_in_short_description_text_area(self):
        self.page.locator('#short_description').type('sdfsdffsdfsdsdfsdsdfdsdfsdfsdfddfdsfsdf')
        element = self.page.locator('#short_description').text_content()
        assert element == 'sdfsdffsdfsdsdfsdsdfdsdfsdfsdfddfdsfsdf'

    def write_min_characters_data_in_short_description_text_area(self):
        self.page.locator('#short_description').type('s')

    def remove_data_in_short_description_text_area(self):
        self.page.locator('#short_description').clear()

    def write_valid_data_in_long_description_text_area(self):
        self.page.locator('.ql-blank').type('dfgfgfggfgfgfgfgfgffgfgfhghgjhgjkh')
        element = self.page.locator('.ql-editor p').text_content()
        assert element == 'dfgfgfggfgfgfgfgfgffgfgfhghgjhgjkh'

    def write_min_characters_data_in_long_description_text_area(self):
        self.page.locator('.ql-blank').type('d')

    def remove_data_in_long_description_text_area(self):
        self.page.locator('[class="ql-editor"] p').clear()

    def step_4_of_4_label_appears(self):
        self.page.wait_for_timeout(timeout=1000)
        self.page.get_by_text('Create your account 4 of 4 steps').is_visible()

    def click_remove_app_logo_icon(self):
        self.page.locator('.icon_icon__36an4').click()

    def company_website_is_required_validation_hint_appears(self):
        self.page.get_by_text('Company Website is required').is_visible()

    def company_name_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('Company Name is required')).to_be_visible()

    def short_description_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('Short Description is required')).to_be_visible()

    def short_description_characters_validation_hint_appears(self):
        expect(self.page.get_by_text('Short Description range should be 30-300 characters')).to_be_visible()

    def long_description_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('Long Description range should be 3-1000 characters')).to_be_visible()

    def click_the_country_drop_down_icon(self):
        self.page.locator('.p-dropdown-trigger').click()

    def select_valid_country(self):
        self.page.locator('.p-dropdown-items li:first-child').click()

    def select_united_states_country(self):
        self.page.locator("[class='p-dropdown-items'] li[aria-label='United States']").click()

    def click_state_drop_down_trigger(self):
        self.page.locator('[class*="location-form_stateField__2zkI0"] [class="p-dropdown-trigger"]').click()

    def select_state(self):
        self.page.locator('[class*="p-dropdown-panel"] ul li:first-child').click()

    def add_valid_data_in_city_input_field(self):
        self.page.locator('#city').type('QA')

    def remove_data_in_city_input_field(self):
        self.page.locator('#city').clear()

    def state_label_appears(self):
        expect(self.page.locator('label[for="state"]')).to_be_visible()

    def city_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('City is required')).to_be_visible()

    def postal_code_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('Postal Code is required')).to_be_visible()

    def address_is_required_validation_hint_appears(self):
        expect(self.page.get_by_text('Address is required')).to_be_visible()

    def policy_terms_is_required_validation_hint_appears(self):
        # expect(self.page.get_by_text('is required')).to_be_visible()
        element = self.page.locator('.checkbox_error__3i3sx').text_content()
        assert element == ' is required'

    def add_valid_data_in_postal_code_input_field(self):
        self.page.locator('#postalCode').type('QA')

    def remove_data_in_postal_code_input_field(self):
        self.page.locator('#postalCode').clear()

    def add_valid_data_in_address_input_field(self):
        self.page.locator('#address').type('QA')

    def remove_data_in_address_input_field(self):
        self.page.locator('#address').clear()

    def accept_policy_check_box(self):
        self.page.locator('.p-checkbox.p-component').click()

    def click_submit_button(self):
        self.page.locator('#registration-form-submit-button').click()

    def submit_button_is_disabled(self):
        expect(self.page.locator('#registration-form-submit-button')).to_be_disabled()

    def submit_button_is_enabled(self):
        self.page.locator('#registration-form-submit-button').is_enabled()

    def success_message_is_displayed(self):
        expect(self.page.get_by_text("Success")).to_be_visible()

    def success_message_not_displayed(self):
        expect(self.page.get_by_text("Success")).to_be_hidden()
