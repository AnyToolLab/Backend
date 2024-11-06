from faker import Faker
import faker.providers

faker = Faker()

'''
Documentation to all the methods: https://faker.readthedocs.io/en/stable/providers.html

Default localization US english, ie: en_US
'''

FAKE_DATA = {
    # Person
    'name_name_male': faker.name_male,
    'name_name_female': faker.name_female,

    # Lorem
    'text': faker.text,

    # Address
    'address_address': faker.address,
    'address_building_number': faker.building_number,
    'address_city': faker.city,
    'address_country': faker.country,
    'address_country_code': faker.country_code,
    'address_postcode': faker.postcode,
    'address_street_address': faker.street_address,
    'address_street_name': faker.street_name,

    # Automotive
    'automotive_license_plate': faker.license_plate,
    'automotive_vin': faker.vin,

    # Bank
    'bank_aba': faker.aba,
    'bank_bank_country': faker.bank_country,
    'bank_bban': faker.bban,
    'bank_iban': faker.iban,
    'bank_swift': faker.swift,

    # Barcode
    'barcode_ean': faker.ean,

    # Color
    'color_color_name': faker.color_name,
    'color_hex_color': faker.hex_color,
    'color_rgb_color': faker.rgb_color,

    # Company
    'company_company': faker.company,
    'company_bs': faker.bs,
    'company_catch_phrase': faker.catch_phrase,
    'company_company_suffix': faker.company_suffix,

    # Credit Card
    'credit_card_credit_card_full': faker.credit_card_full,
    'credit_card_credit_card_expire': faker.credit_card_expire,
    'credit_card_credit_card_number': faker.credit_card_number,
    'credit_card_credit_card_provider': faker.credit_card_provider,
    'credit_card_credit_card_security_code': faker.credit_card_security_code,

    # Date Time
    'date_time_date': faker.date,

    # Geo
    'geo_location_on_land': faker.location_on_land,

    # Internet
    'internet_company_email': faker.ascii_company_email,
    'internet_email': faker.ascii_free_email,
    'internet_domain_name': faker.domain_name,
    'internet_hostname': faker.hostname,
    'internet_ipv4': faker.ipv4,
    'internet_ipv6': faker.ipv6,
    'internet_mac_address': faker.mac_address,
    'internet_port_name': faker.port_number,
    'internet_slug': faker.slug,
    'internet_uri': faker.uri,
    'internet_url': faker.url,
    'internet_user_name': faker.user_name,

    # Job
    'job_job': faker.job,

    # Phone Number
    'phone_number_phone_number': faker.phone_number,

    # User Agent
    'user_agent_user_agent': faker.user_agent,
}
