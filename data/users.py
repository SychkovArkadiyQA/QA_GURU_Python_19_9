import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: [str]
    subject: str
    hobby: str
    picture_file: str
    address: str
    state: str
    city: str


student = User(
    first_name='Papa',
    last_name='Carlo',
    email='PapaCarlo@example.com',
    gender='Male',
    phone_number='9035645454',
    date_of_birth=['09', 'August', '1997'],
    subject='Maths',
    hobby='Sports',
    picture_file='test.png',
    address='Ekb, Russia',
    state='NCR',
    city='Delhi')