from scrapper import address


class ParserTest(address.Address):
    def __init__(self, address: list[str]) -> None:
        super().__init__(address)


def test_address():
    test_list = [
        (
            ParserTest(['1234 rue quelque test', 'Montreal (District)', '']),
            "1234 rue quelque test".upper()
        ),
        (
            ParserTest(['', 'Montreal', '']),
            None
        ),
        (
            ParserTest([]),
            None
        )
    ]
    
    for test in test_list:
        assert test[0].address() == test[1]

def test_city():
    test_list = [
        (
            ParserTest(['1234 rue quelque test', 'Montreal (District)', '']),
            "MONTREAL"
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal', '']),
            "MONTREAL"
        ),
        (
            ParserTest([]),
            None
        )
    ]
    
    for test in test_list:
        assert test[0].city() == test[1]
    

def test_region():
    test_list = [
        (
            ParserTest(['1234 rue quelque test', 'Sainte-Marguerite-du-Lac-Masson', '']),
            "LAURENTIDES"
        ),
        (
            ParserTest(['1234 rue quelque test', "L'ÎLE-CADIEUX (District)", '']),
            "MONTÉRÉGIE"
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal', '']),
            "MONTRÉAL"
        ),
        (
            ParserTest([]),
            None
        )
    ]
    
    for test in test_list:
        assert test[0].region() == test[1]
    
def test_district():
    test_list = [
        (
            ParserTest(['1234 rue quelque test', 'Montreal (District)', '']),
            "DISTRICT"
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal (District1/District2)', '']),
            "DISTRICT1/DISTRICT2"
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal', '']),
            None
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal ()', '']),
            None
        ),
        (
            ParserTest(['1234 rue quelque test']),
            None
        ),
        (
            ParserTest([]),
            None
        ),
    ]
    
    for test in test_list:
        assert test[0].district() == test[1]
        
def test_neighborhood():
    test_list = [
        (
            ParserTest(['1234 rue quelque test', 'Montreal (District)', 'Neighbourhood Just Test']),
            "JUST TEST"
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal (District1/District2)', '']),
            None
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal', None]),
            None
        ),
        (
            ParserTest(['1234 rue quelque test', 'Montreal ()']),
            None
        ),
        (
            ParserTest(['1234 rue quelque test']),
            None
        ),
        (
            ParserTest([]),
            None
        ),
    ]
    
    for test in test_list:
        assert test[0].neighborhood() == test[1]