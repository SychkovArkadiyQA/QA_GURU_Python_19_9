from page_objects.registration_page import RegistrationPage

def test_complete_form():
    registration_page = RegistrationPage()
    registration_page.open()
    #WHEN
    registration_page.fill_first_name('Papa')
    registration_page.fill_last_name('Carlo')
    registration_page.fill_email('PapaCarlo@example.com')
    registration_page.select_gender('Male')
    registration_page.fill_number('9035645454')
    registration_page.fill_birthday('1997', 'August', '9')
    registration_page.fill_subject('Maths')
    registration_page.check_hobby('Sports')
    registration_page.check_hobby('Reading')
    registration_page.check_hobby('Music')
    registration_page.upload_picture('test.png')
    registration_page.fill_in_address('Ekb, Russia')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit()
    #THEN
    registration_page.assert_user_data(
        'Student Name Papa Carlo', 'Student Email PapaCarlo@example.com',
        'Gender Male', 'Mobile 9035645454', 'Date of Birth 09 August,1997',
        'Subjects Maths', 'Hobbies Sports, Reading, Music',
        'Picture test.png', 'Address Ekb, Russia',
        'State and City NCR Delhi'
    )
    registration_page.close_submission_form()