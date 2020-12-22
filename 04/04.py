#!/usr/bin/python3

import re

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class PassportValidator():
    @staticmethod
    def validate(passport):
        raise NotImplementedError()


class SimplePassportValidator():
    @staticmethod
    def validate(passport):
        return all(passport.fields.values())


class ComplexPassportValidator():
    year_re = re.compile(r'^\d{4}$')
    hgt_re = re.compile(r'^(\d+)(in|cm)$')
    hcl_re = re.compile(r'^#[a-f0-9]{6}$')
    ecl_re = re.compile(r'^(?:amb|blu|brn|gry|grn|hzl|oth)$')
    pid_re = re.compile(r'^\d{9}$')

    @classmethod
    def validate(cls, passport):
        try:
            valid = all(passport.fields.values())
            if not valid: return False

            byr = int(cls.year_re.match(passport.fields['byr']).group(0))
            valid = (1920 <= byr and byr <= 2002)
            if not valid: return False

            iyr = int(cls.year_re.match(passport.fields['iyr']).group(0))
            valid = (2010 <= iyr and iyr <= 2020)
            if not valid: return False

            eyr = int(cls.year_re.match(passport.fields['eyr']).group(0))
            valid = (2020 <= eyr and eyr <= 2030)
            if not valid: return False

            hgt, hgt_unit = cls.hgt_re.match(passport.fields['hgt']).groups()
            hgt = int(hgt)
            valid1 = (hgt_unit == 'cm' and 150 <= hgt and hgt <= 193)
            valid2 = (hgt_unit == 'in' and 59 <= hgt and hgt <= 76)
            if not (valid1 or valid2) : return False

            hcl = cls.hcl_re.match(passport.fields['hcl'])
            valid = hcl
            if not valid: return False

            ecl = cls.ecl_re.match(passport.fields['ecl'])
            valid = ecl
            if not valid: return False

            pid = cls.pid_re.match(passport.fields['pid'])
            valid = pid
            if not valid: return False
        except Exception:
            return False

        print(passport.fields)
        return True


class Passport:
    def __init__(self):
        self.resetFields()

    def resetFields(self):
        self.fields = {name: None for name in FIELDS}

    def isValid(self, validator):
        return validator.validate(self)

    def setField(self, field, value):
        if field in self.fields:
            self.fields[field] = value

if __name__ == '__main__':
    n_valid_simple = 0
    n_valid_complex = 0
    with open('input') as f:
        passport = Passport()
        for line in f:
            line = line.rstrip()
            if line == '':
                if passport.isValid(SimplePassportValidator):
                    n_valid_simple += 1
                if passport.isValid(ComplexPassportValidator):
                    n_valid_complex += 1
                passport.resetFields()
            else:
                for kv in line.split(' '):
                    field, value = kv.split(':')
                    passport.setField(field, value)
        print("{} valid passports with simple method".format(n_valid_simple))
        print("{} valid passports with complex method".format(n_valid_complex))
