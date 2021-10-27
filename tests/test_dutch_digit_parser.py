from ddp import parse_digit_text


def test_some_numbers():
    _5 = "vijf"
    assert parse_digit_text(_5)[0] == "5"

    _55 = "vijf en vijftig"
    _555 = "vijf honderd vijf en vijftig"
    _5555 = "vijf duizend vijf en vijftig"
    _55_555 = "vijf en vijftig duizend vijf hondend en vijf en vijftig"
    _555_555 = "vijf hondend duizend vijf honderd vijf en vijftig"
    _5_555_555 = (
        "vijf miljoen vijf honderd vijf en vijftig duizend vijf honderd vijf en vijftig"
    )

    _1300 = "dertien honderd"
    _1400 = "duizend vier honderd"
