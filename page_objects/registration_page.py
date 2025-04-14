import os

from selene import browser, have, be

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
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
        browser.element('#subjectsInput').send_keys(value)

    def check_hobby(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/resources/{value}")

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