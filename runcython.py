from faststocks import *

if __name__ == '__main__':

    print("start")
    ######MAKE IT ONLY WORK ON STOCK WITH CAP 1-150 MILLION NOT MORE NOT LESS

    e = True
    thread1 = multiprocessing.Process(target=get_companies, args=(0, 1))
    thread2 = multiprocessing.Process(target=get_companies, args=(2, 2))
    thread3 = multiprocessing.Process(target=get_companies, args=(4, 3))
    thread4 = multiprocessing.Process(target=get_companies, args=(6, 4))
    thread5 = multiprocessing.Process(target=get_companies, args=(8, 5))
    thread6 = multiprocessing.Process(target=get_companies, args=(10, 6))
    thread7 = multiprocessing.Process(target=get_companies, args=(12, 7))
    thread8 = multiprocessing.Process(target=get_companies, args=(14, 8))
    thread9 = multiprocessing.Process(target=get_companies, args=(16, 9))
    thread10 = multiprocessing.Process(target=get_companies, args=(18, 10))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()

    import yfinance as yf

    sorted_dist_obj = None
    file_path = '/Users/davidlevgabbay/Desktop/AlpacaBot-py11/Openai/dist_obj.csv'  # Replace with your file path
    df = pd.read_csv("/Users/davidlevgabbay/Desktop/AlpacaBot-py11/Openai/dist_obj.csv")
    print("Non sorted", df)
    sorted_df = df.sort_values(by="dist", ascending = False)
    print("Sorted", sorted_df.tail(50))
    stocks_full = sorted_df["symbol"].tolist()
    stocks_good = []
    print(stocks_full, stocks_full[0])
    for stock in stocks_full:
        if stock != "nan":
            df = yf.download(stock, interval="1m", period="2d")
            print(df)
            print(f" {stock} length: ", len(df))
            if len(df) > 300 and df["Close"].iloc[-1] < 200 and stock not in stocks_good:
                stocks_good.append(stock)
                print("Appended")
    # stocks = stocks_good[:12]

    print(stocks_good)
    print(stocks_good[:18])
    stocks = stocks_good[:12]


"""

['NDAQ', 'WELL', 'NVAX', 'CPB', 'FLS', 'BMY', 'HPE', 'GRMN', 'STM', 'CORZZ', 'NYT', 'WMT', 'INTC', 'SNGX', 'DCI', 'TIGR', 'SAP', 'BBIO']

"""