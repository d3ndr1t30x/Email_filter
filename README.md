# Country-Specific Domain Reference

This README provides a list of common country-specific top-level domains (TLDs) and secondary domains. You can use these to customize the filtering criteria in the `email_filter.py` Python script.

## How to Use
In `email_filter.py`, you can modify the `country_domains` list to include or exclude specific domains based on the countries you want to filter out. Simply add or remove domains from this list as needed.

### Example
```python
# Modify this list in email_filter.py
country_domains = [
    ".co.uk", ".com.au", ".co.nz",  # Add or remove as needed
    # Add more domains below
]
```

Europe

    .co.uk - United Kingdom
    .fr - France
    .de - Germany
    .it - Italy
    .nl - Netherlands
    .es - Spain
    .se - Sweden
    .pl - Poland
    .ch - Switzerland
    .be - Belgium
    .dk - Denmark

Asia

    .in - India
    .jp - Japan
    .cn - China
    .sg - Singapore
    .hk - Hong Kong
    .kr - South Korea
    .my - Malaysia
    .ph - Philippines
    .th - Thailand
    .vn - Vietnam
    .pk - Pakistan

Middle East & Africa

    .ae - United Arab Emirates
    .sa - Saudi Arabia
    .za - South Africa
    .ng - Nigeria
    .eg - Egypt
    .ma - Morocco
    .il - Israel
    .tr - Turkey

Americas (non-U.S.)

    .ca - Canada
    .mx - Mexico
    .br - Brazil
    .ar - Argentina
    .cl - Chile
    .pe - Peru
    .co - Colombia
    .ve - Venezuela

Oceania

    .au - Australia
    .nz - New Zealand
    .pg - Papua New Guinea
    .fj - Fiji

Other General International Domains

    .eu - European Union
    .asia - Asia-Pacific region
    .lat - Latin America
    .africa - Africa
