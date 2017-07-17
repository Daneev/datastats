import json

from datastats.datastats import DataStats


test_data = [
    {
        "id": 1,
        "name": "Laith",
        "surname": "Simmons",
        "age": 68,
        "salary": "£27888"
    },
    {
        "id": 2,
        "name": "Mikayla",
        "surname": "Henry",
        "age": 49,
        "salary": "£67137"
    },
    {
        "id": 3,
        "name": "Garth",
        "surname": "Fields",
        "age": 70,
        "salary": "£70472"
    }
]


def test_json():

    ds = DataStats()

    assert ds.stats(test_data, 20, 20000) == json.dumps(
        {
            'avg_age': 62,
            'avg_salary': 55165,
            'avg_yearly_increase': 837,
            'max_salary': [{
                "id": 3,
                "name": "Garth",
                "surname": "Fields",
                "age": 70,
                "salary": "£70472"
            }],
            'min_salary': [{
                "id": 1,
                "name": "Laith",
                "surname": "Simmons",
                "age": 68,
                "salary": "£27888"
            }]
        }
    )


def test__stats():

    ds = DataStats()

    assert ds._stats(test_data, 20, 20000) == {
        'avg_age': 62,
        'avg_salary': 55165,
        'avg_yearly_increase': 837,
        'max_salary': [{
            "id": 3,
            "name": "Garth",
            "surname": "Fields",
            "age": 70,
            "salary": "£70472"
        }],
        'min_salary': [{
            "id": 1,
            "name": "Laith",
            "surname": "Simmons",
            "age": 68,
            "salary": "£27888"
        }]
    }


def test__avg_age():

    ds = DataStats()

    assert ds._avg_age(test_data) == 62


def test__avg_salary():

    ds = DataStats()

    assert ds._avg_salary(test_data) == 55165


def test__avg_yearly_increase():

    ds = DataStats()

    assert ds._avg_yearly_increase(test_data, 20, 20000) == 837


def test__max_salary():

    ds = DataStats()

    assert ds._max_salary(test_data) == [{
        "id": 3,
        "name": "Garth",
        "surname": "Fields",
        "age": 70,
        "salary": "£70472"
    }]


def test__min_salary():

    ds = DataStats()

    assert ds._min_salary(test_data) == [{
        "id": 1,
        "name": "Laith",
        "surname": "Simmons",
        "age": 68,
        "salary": "£27888"
    }]


def test_salaries():

    ds = DataStats()

    assert ds._salaries(test_data) == [27888, 67137, 70472]


def test_ages():

    ds = DataStats()

    assert ds._ages(test_data) == [68, 49, 70]
