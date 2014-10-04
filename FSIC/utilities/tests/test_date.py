# -*- coding: utf-8 -*-


from FSIC.utilities.date import DateParser


def test_parse():
    test_cases = {
        '2000': [2000, 1, 1, 'A'],
        '2000A1': [2000, 1, 1, 'A'],
        '2000A01': [2000, 1, 1, 'A'],

        '2005Q2': [2005, 2, 4, 'Q'],
        '2005Q02': [2005, 2, 4, 'Q'],

        '2010M9': [2010, 9, 12, 'M'],
        '2010M09': [2010, 9, 12, 'M'],
    }
    for case, expected in test_cases.items():
        parser = DateParser(case)
        result = [parser.year,
                  parser.period,
                  parser.freq,
                  parser.freq_id]
        assert result == expected


if __name__ == '__main__':
    import nose
    nose.runmodule()
