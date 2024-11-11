from faker import Faker
import faker.providers

faker = Faker()

'''
Documentation to all the methods: https://faker.readthedocs.io/en/stable/providers.html

Default localization US english, ie: en_US
'''

FAKE_DATA = {
    # Person
    'first_name': faker.first_name,
    'last_name': faker.last_name,
    'name': faker.name,
    'name_male': faker.name_male,
    'name_female': faker.name_female,

    # Lorem
    'text': faker.text,

    # Address
    'address': faker.address,
    'building_number': faker.building_number,
    'city': faker.city,
    'country': faker.country,
    'country_code': faker.country_code,
    'postcode': faker.postcode,
    'street_address': faker.street_address,
    'street_name': faker.street_name,

    # Automotive
    'license_plate': faker.license_plate,
    'vin': faker.vin,

    # Bank
    'aba': faker.aba,
    'bank_country': faker.bank_country,
    'bban': faker.bban,
    'iban': faker.iban,
    'swift': faker.swift,

    # Barcode
    'ean': faker.ean,

    # Color
    'color_name': faker.color_name,
    'hex_color': faker.hex_color,
    'rgb_color': faker.rgb_color,

    # Company
    'company': faker.company,
    'bs': faker.bs,
    'catch_phrase': faker.catch_phrase,
    'company_suffix': faker.company_suffix,

    # Credit Card
    'credit_card_full': faker.credit_card_full,
    'credit_card_expire': faker.credit_card_expire,
    'credit_card_number': faker.credit_card_number,
    'credit_card_provider': faker.credit_card_provider,
    'credit_card_security_code': faker.credit_card_security_code,

    # Date Time
    'date': faker.date,

    # Geo
    'location_on_land': faker.location_on_land,

    # Internet
    'company_email': faker.ascii_company_email,
    'email': faker.ascii_free_email,
    'domain_name': faker.domain_name,
    'hostname': faker.hostname,
    'ipv4': faker.ipv4,
    'ipv6': faker.ipv6,
    'mac_address': faker.mac_address,
    'port_number': faker.port_number,
    'slug': faker.slug,
    'uri': faker.uri,
    'url': faker.url,
    'user_name': faker.user_name,

    # Job
    'job': faker.job,

    # Phone Number
    'phone_number': faker.phone_number,

    # User Agent
    'user_agent': faker.user_agent,
}