from ddp import parse_digit_text


def test_some_numbers():
    _5 = "vijf"
    assert parse_digit_text(_5)[0] == "5"

    _55 = "vijf en vijftig"
    assert parse_digit_text(_55)[0] == "55"

    _555 = "vijf honderd vijf en vijftig"
    assert parse_digit_text(_555)[0] == "555"

    _5555 = "vijf duizend vijf en vijftig"
    assert parse_digit_text(_5555)[0] == "5555"


    _55_555 = "vijf en vijftig duizend vijf hondend vijf en vijftig"
    assert parse_digit_text(_55_555)[0] == "55555"

    _555_555 = "vijf honderd vijf en vijftig duizend vijf honderd vijf en vijftig"
    assert parse_digit_text(_555_555)[0] == "555555"

    _5_555_555 = (
        "vijf miljoen vijf honderd vijf en vijftig duizend vijf honderd vijf en vijftig"
    )
    assert parse_digit_text(_5_555_555)[0] == "5555555"

    _1300 = "dertien honderd"
    assert parse_digit_text(_1300)[0] == "1300"

    _1400 = "duizend vier honderd"
    assert parse_digit_text(_1400)[0] == "1400"
