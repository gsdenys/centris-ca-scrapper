from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pandas as pd

ENGINE = create_engine("sqlite:///quebec-houses.db", echo=True)

columns = [
    'PRICE',
    'TYPE',
    'CATEGORY',
    'BEDROOM',
    'BATHROOM',
    'REGION',
    'CITY',
    'NEIGHBORHOOD',
    'DISTRICT',
    'DATE',
    'PAGE'
]

def save(data: list):
    df = pd.DataFrame(data=data, columns=columns)

    df.to_sql('items', ENGINE, if_exists='append')