"""
P1. Validate that every passport"  # (splited by empty line) has all required fields

P2. Additional validation
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

"""
import re

REQUIRED_FIELDS = {
    r'byr:(?:(?:19[2-9]\d))|(?:200[0-2])',
    r'iyr:(?:20(?:1\d|20))',
    r'eyr:(?:20(?:2\d|30))',
    r'hgt:(?:(?:(?:1(?:(?:[5-8]\d)|9[0-3]))cm)|(?:59|6\d|7[0-6])in)',
    r'hcl:(?:\#[0-9a-f]{6})',
    r'ecl:(?:amb|blu|brn|gry|grn|hzl|oth)',
    r'pid:(?:\d{9})',
}

with open('input') as f:
    current_passport = ''
    counter = 0
    for line in f:
        if line == '\n':
            for field in REQUIRED_FIELDS:
                field = r'\b{}\b'.format(field)
                if re.search(field, current_passport) is None:
                    break
            else:
                counter += 1
            current_passport = ''
        else:
            current_passport += line

print(counter)
