import gspread
import pandas as pd


class Data():
    _gc = gspread.service_account(filename='lunchtime-311916-12d6f5d4e57a.json')

    _sh = _gc.open('Lunch')

    _data = _sh.sheet1.get()

    df = pd.DataFrame()
    df['id'] = [int(_value[0]) for _value in _data]
    df['name'] = [_value[1] for _value in _data]
    df['lunch type'] = [_value[2] for _value in _data]
