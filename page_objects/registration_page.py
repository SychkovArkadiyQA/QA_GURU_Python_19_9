import os
from data.users import User
from selene import browser, have, be, by
from tests.constant import THANKS_FOR_SUBMITTING_TEXT


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

    @property
    def date_of_birth(self):
        return browser.element('#dateOfBirthInput')

    def fill_in_date_of_birth(self, date_of_birth):
        day, month, year = date_of_birth
        self.date_of_birth.click()
        browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
        self.date_of_birth.send_keys(f'{day} {month} {year}').press_enter()

    def fill_subject(self, value):
        browser.element('#subjectsInput').click()
        browser.element('#subjectsInput').type(value)
        browser.element(
        by.xpath(f'//div[contains(@class, "subjects-auto-complete__option") and text()="{value}"]')).click()

    def check_hobby(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).click()

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

    def assert_form_submission_text(self, expected_text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(expected_text))

    def assert_user_data(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        full_birthday = f'{student.date_of_birth[0]} {student.date_of_birth[1]},{student.date_of_birth[2]}'
        expected_values = [
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.phone_number}',
            f'Date of Birth {full_birthday}',
            f'Subjects {student.subject}',
            f'Hobbies {student.hobby}',
            f'Picture {student.picture_file}',
            f'Address {student.address}',
            f'State and City {student.state} {student.city}'
        ]
        browser.all("tbody tr").should(have.exact_texts(*expected_values))

    def close_submission_form(self):
        browser.element('#closeLargeModal').click()

    def register(self, student: User):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.fill_email(student.email)
        self.select_gender(student.gender)
        self.fill_number(student.phone_number)
        self.fill_in_date_of_birth(student.date_of_birth)
        self.fill_subject(student.subject)
        self.check_hobby(student.hobby)
        self.upload_picture(student.picture_file)
        self.fill_in_address(student.address)
        self.select_state(student.state)
        self.select_city(student.city)
        self.submit()
        self.assert_form_submission_text(THANKS_FOR_SUBMITTING_TEXT)

    def should_have_registered(self, student: User):
        self.assert_user_data(student)
        self.close_submission_form()