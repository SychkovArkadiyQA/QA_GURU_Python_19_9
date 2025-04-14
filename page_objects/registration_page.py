import os
from selene import browser, have, be, by

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector("footer").remove()')
        browser.execute_script('document.querySelector("#fixedban").remove()')
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self
    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self
    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self
    def select_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()
        return self
    def fill_number(self, value):
        browser.element('#userNumber').type(value)
        return self
    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--00{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').click()
        browser.element('#subjectsInput').type(value)
        browser.element(
        by.xpath(f'//div[contains(@class, "subjects-auto-complete__option") and text()="{value}"]')).click()


    def check_hobby(self, value):
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-2]').click()
        browser.element('[for=hobbies-checkbox-3]').click()

    def upload_picture(self, value):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_dir, "resources", value)
        browser.element('#uploadPicture').send_keys(file_path)

    def fill_in_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state #react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#city #react-select-4-input').type(value).press_enter()

    def submit(self):
        browser.element('#submit').execute_script('element.click()')

    def assert_user_data(self, *values):
        browser.all('tbody tr').should(have.exact_texts(values))

    def close_submission_form(self):
        browser.element('#closeLargeModal').click()