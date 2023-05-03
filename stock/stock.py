import datetime
import apimoex
import matplotlib.pyplot as plt
import pandas as pd
import requests


def get_ticker_data(ticker: str) -> pd.DataFrame:
    with requests.Session() as session:
        data = apimoex.get_board_history(
            session=session,
            security=ticker,
            start=str((datetime.datetime.now() - datetime.timedelta(days=30)).date()),
            end=str(datetime.datetime.now().date())
        )
        data = pd.DataFrame(data)
        return data


def make_plot(ticker: str) -> str:
    data = get_ticker_data(ticker)

    if data.empty:
        raise ValueError('Wrong ticker')

    close = data['CLOSE'].values
    date = [x[5:] for x in data['TRADEDATE'].values]
    plt.figure(figsize=(12, 6))
    plt.xlabel('Дата (месяц-день)')
    plt.ylabel('Цена')
    plt.grid(visible=True)
    plt.plot(
        date,
        close,
        linewidth=3,
    )
    filepath = str(hash(datetime.datetime.now())) + '.jpg'
    plt.savefig(filepath)
    return filepath
