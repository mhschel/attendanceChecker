import pytest
from check_names import get_last_name_from_attendance, check_attendance


def test_get_last_name_schellekens():
    test_list = ['N.E.  Schellekens (Nadine)']
    actual = get_last_name_from_attendance(test_list)[0]
    expected = 'Schellekens'
    assert actual == expected


def test_get_last_name_korkmaz():
    test_list = ['A.  Korkmaz (Alp)']
    actual = get_last_name_from_attendance(test_list)[0]
    expected = 'Korkmaz'
    assert actual == expected


def test_compare_lists():
    master_list = ['Pien', 'Menno', 'Anna']
    attendance = ['Menno', 'Anna']

    actual = check_attendance(master_list, attendance)[0]
    expected = 'Pien'

    assert actual == expected
