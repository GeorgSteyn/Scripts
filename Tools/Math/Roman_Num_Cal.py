import re


class RomanNumerals():
    def to_roman(num):
        # Split the num or something. Make it in ruf working state for calculcation
        roman_nums = {'1': 'I',  # Smaller than 4, num + I OR can put in dict 1 = I, 2 = II ect.
                      '4': 'IV',
                      '5': 'V',
                      '9': 'IX',
                      '10': 'X',
                      '50': 'L',
                      '90': 'XC',
                      '100': 'C',
                      '500': 'D',
                      '900': 'CM',
                      '1000': 'M',
                      }

    def from_roman(rome_num):
        # rome_num = MDLVII = 1557
        roman_nums = {'I': '1',
                      'IV': '4',
                      'V': '5',
                      'IX': '9',
                      'X': '10',
                      'L': '50',
                      'XC': '90',
                      'C': '100',
                      'D': '500',
                      'CM': '900',
                      'M': '1000',
                      }

        raw_roman_num = re.split(r'\s(?=(?:CM|XC|IX|IV|M|D|C|L|X|V|I\b)', rome_num)  # raw_roman_num = (M,D,L,V,I,I)
        for num in raw_roman_num:
            if num == CM:
