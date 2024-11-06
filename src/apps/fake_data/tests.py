from django.test import TestCase

from src.apps.fake_data.utils import FAKE_DATA


def get_fake_person_name():
    return FAKE_DATA['name_name_male']()


def get_fake_internet_ipv4():
    return FAKE_DATA['internet_ipv4']()


def get_fake_bank_bban():
    return FAKE_DATA['bank_bban']()


if __name__ == '__main__':
    print(get_fake_person_name())
    print(get_fake_internet_ipv4())
    print(get_fake_bank_bban())
