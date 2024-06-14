# import heapq
# import json
import json

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
#### MAKE IT WORK
import multiprocessing
import re
import time

# import os
import pandas.errors
# import requests
# import yfinance
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yfinance as yf
# from bs4 import BeautifulSoup
all_distances = []
import pandas as pd
import numpy as np
import openai
from newspaper import Article


# from sklearn.metrics.pairwise import cosine_similarity
# from scipy.spatial.distance import cosine as cosine_similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


openai.api_key = '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'
from openai import OpenAI

client = OpenAI(api_key='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')


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=text, model=model).data[0].embedding  # ['data']#[0]['embedding']


# print(get_embedding("Hi"))

def save_to_csv(list):
    df = pd.DataFrame(list)

    df.to_csv('/Users/davidlevgabbay/Desktop/AlpacaBot-py11/Openai/dist_obj.csv', index=False)


# def scrape_google_articles(search, page):
#     """Scrapes a list of articles and their links from Google."""
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#     url = f"https://www.google.com/search?q={search}&sca_esv=563626424&biw=1440&bih=814&start={(page - 1) * 10}&tbs=qdr%3Ad&tbm=nws&sxsrf=AB5stBilPJzFMJ-R4mtJxmz2w-nx9jc_bg%3A1694593091648&ei=Q3ABZcCRJ86dkdUP9KeTqA4&ved=0ahUKEwiAv5Cak6eBAxXOTqQEHfTTBOUQ4dUDCA0&uact=5&oq=Enters+into+Agreement+to+&gs_lp=Egxnd3Mtd2l6LW5ld3MiGUVudGVycyBpbnRvIEFncmVlbWVudCB0byAyBRAhGKABMggQIRgWGB4YHTIIECEYFhgeGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB1Iww1QyQJYrgpwAHgAkAEAmAHMAaAB1gmqAQUwLjYuMbgBA8gBAPgBAcICBhAAGBYYHsICCBAAGIoFGIYDwgIHECEYoAEYCogGAQ&sclient=gws-wiz-news"
#     # url = f"https://www.google.com/search?q=`{search}&sca_esv=563626424&tbs=qdr:h&tbm=nws&sxsrf=AB5stBi3tC3D9FEFkm9ClDGgqCjV1En66A:1694178050522&ei=Ahv7ZK-fH9KrkdUP_aSrsA4&start=0&sa=N&ved=2ahUKEwivqIyHiZuBAxXSVaQEHX3SCuY4HhDy0wN6BAgBEAQ&biw=1440&bih=814&dpr=2"
#     # url = "https://www.google.coxfm/search?q=beats+earnings+estimate&sca_esv=562751389&tbm=nws&sxsrf=AB5stBjR1qWDNx_xjyRJT9SgKU5-xn3cNg:1693924038973&source=lnt&sa=X&ved=2ahUKEwjk__nk1pOBAxWrdaQEHdQTAdMQpwV6BAgBEBM&tbas=0&biw=1351&bih=727&dpr=2"
#     response = requests.get(url)#, headers=headers)
#     # titles = []
#     # links = []
#     full = []
#     soup = BeautifulSoup(response.content, "html.parser")
#     print(soup.text)
#     articles = soup.find_all('div', {"class": "Gx5Zad fP1Qef xpd EtOod pkphOe"})
#     # print(soup.text)
#     for article in articles:
#         current_time = datetime.datetime.now()
#
#         # Define the target time (10:30 PM)
#         target_time = current_time.replace(hour=20, minute=0, second=0,
#                                            microsecond=0)  # todo change if not finding enough stocks
#         target_btime = current_time.replace(hour=15, minute=30, second=0, microsecond=0)
#
#         # Calculate the time difference
#         time_difference = current_time - target_time
#         time_bdifference = current_time - target_btime
#
#         # Extract the number of hours and minutes
#         hours = time_difference.days * 24 + time_difference.seconds // 3600
#         accurate_hours = 24 + hours
#
#         bhours = time_bdifference.days * 24 + time_bdifference.seconds // 3600
#         accurate_bhours = bhours
#         time_label = article.find('span', {"class": "r0bn4c rQMQod"}).text
#
#         pattern = r'\d+'  # This pattern matches one or more digits
#
#         # Use the findall() function from the re module to find all matches in the string
#         matches = re.findall(pattern, time_label)
#
#         # Check if any matches were found
#         if matches:
#             # Since findall() returns a list, we'll assume the first match is the integer you want
#             first_integer = int(matches[0])
#             time_pub = first_integer
#         else:
#             time_pub = 1
#
#         print(accurate_bhours)
#         if time_pub < accurate_hours and time_pub >= accurate_bhours:  # can change
#
#             title = article.find("span", {"dir": "ltr"}).text
#             a = article.find("a")["href"][7:]
#             desired_string = a.split("&sa")[0]
#             full1 = {"title": title, "link": desired_string}
#             full.append(full1)
#             # titles.append(title)
#             # links.append(desired_string)
#             print("Time published: ", time_pub, accurate_hours, " For ", title)
#
#     return full
def scrape_google_articles(search, page):
    """Scrapes a list of articles and their links from Google."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # url = f"https://www.google.com/search?q={search}&sca_esv=563626424&biw=1440&bih=814&start={(page - 1) * 10}&tbs=qdr%3Ad&tbm=nws&sxsrf=AB5stBilPJzFMJ-R4mtJxmz2w-nx9jc_bg%3A1694593091648&ei=Q3ABZcCRJ86dkdUP9KeTqA4&ved=0ahUKEwiAv5Cak6eBAxXOTqQEHfTTBOUQ4dUDCA0&uact=5&oq=Enters+into+Agreement+to+&gs_lp=Egxnd3Mtd2l6LW5ld3MiGUVudGVycyBpbnRvIEFncmVlbWVudCB0byAyBRAhGKABMggQIRgWGB4YHTIIECEYFhgeGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB1Iww1QyQJYrgpwAHgAkAEAmAHMAaAB1gmqAQUwLjYuMbgBA8gBAPgBAcICBhAAGBYYHsICCBAAGIoFGIYDwgIHECEYoAEYCogGAQ&sclient=gws-wiz-news"
    # # url = f"https://www.google.com/search?q=`{search}&sca_esv=563626424&tbs=qdr:h&tbm=nws&sxsrf=AB5stBi3tC3D9FEFkm9ClDGgqCjV1En66A:1694178050522&ei=Ahv7ZK-fH9KrkdUP_aSrsA4&start=0&sa=N&ved=2ahUKEwivqIyHiZuBAxXSVaQEHX3SCuY4HhDy0wN6BAgBEAQ&biw=1440&bih=814&dpr=2"
    # # url = "https://www.google.coxfm/search?q=beats+earnings+estimate&sca_esv=562751389&tbm=nws&sxsrf=AB5stBjR1qWDNx_xjyRJT9SgKU5-xn3cNg:1693924038973&source=lnt&sa=X&ved=2ahUKEwjk__nk1pOBAxWrdaQEHdQTAdMQpwV6BAgBEBM&tbas=0&biw=1351&bih=727&dpr=2"
    # response = requests.get(url)#, headers=headers)
    # # titles = []
    # # links = []
    full = []
    # soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.text)
    # articles = soup.find_all('div', {"class": "Gx5Zad fP1Qef xpd EtOod pkphOe"})
    # print(soup.text)
    url = f"https://www.google.com/search?q={search}&sca_esv=563626424&biw=1440&bih=814&start={(page - 1) * 10}&tbs=qdr%3Ad&tbm=nws&sxsrf=AB5stBilPJzFMJ-R4mtJxmz2w-nx9jc_bg%3A1694593091648&ei=Q3ABZcCRJ86dkdUP9KeTqA4&ved=0ahUKEwiAv5Cak6eBAxXOTqQEHfTTBOUQ4dUDCA0&uact=5&oq=Enters+into+Agreement+to+&gs_lp=Egxnd3Mtd2l6LW5ld3MiGUVudGVycyBpbnRvIEFncmVlbWVudCB0byAyBRAhGKABMggQIRgWGB4YHTIIECEYFhgeGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB0yChAhGBYYHhgPGB1Iww1QyQJYrgpwAHgAkAEAmAHMAaAB1gmqAQUwLjYuMbgBA8gBAPgBAcICBhAAGBYYHsICCBAAGIoFGIYDwgIHECEYoAEYCogGAQ&sclient=gws-wiz-news"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode

    # Use the headless Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options) # You may need to specify the path to your chromedriver
    driver.get(url)

    # Get the page source after Selenium has rendered the JavaScript content
    html = driver.page_source

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    driver.quit()

    # Now you can proceed with scraping the content as before
    articles = soup.find_all('div', {"class": "SoaBEf"})
    # print(articles[0])
    for article in articles:
        current_time = datetime.datetime.now()

        # Define the target time (10:30 PM)
        target_time = current_time.replace(hour=16, minute=30, second=0,
                                           microsecond=0)  # todo change if not finding enough stocks
        target_btime = current_time.replace(hour=15, minute=30, second=0, microsecond=0)

        # Calculate the time difference
        time_difference = current_time - target_time
        time_bdifference = current_time - target_btime

        # Extract the number of hours and minutes
        hours = time_difference.days * 24 + time_difference.seconds // 3600
        accurate_hours = 24 + hours

        bhours = time_bdifference.days * 24 + time_bdifference.seconds // 3600
        accurate_bhours = bhours
        time_label_parent = article.find('div', {"class": "OSrXXb rbYSKb LfVVr"})
        time_label = time_label_parent.find('span').text
        # print(time_label)

        pattern = r'\d+'  # This pattern matches one or more digits

        # Use the findall() function from the re module to find all matches in the string
        matches = re.findall(pattern, time_label)

        # Check if any matches were found
        if matches:
            # Since findall() returns a list, we'll assume the first match is the integer you want
            first_integer = int(matches[0])
            time_pub = first_integer
        else:
            time_pub = 1

        print(accurate_bhours)
        if time_pub < accurate_hours and time_pub >= accurate_bhours:  # can change

            title = article.find("div", {"class": "n0jPhd ynAwRc MBeuO nDgy9d"}).text
            a = article.find("a")["href"][7:]
            desired_string = a.split("&sa")[0]
            full1 = {"title": title, "link": desired_string}
            full.append(full1)
            # titles.append(title)
            # links.append(desired_string)
            print("Time published: ", time_pub, accurate_hours, " For ", title)

    return full

def get_company_procedure(search):
    print("Running procedure")
    items1 = scrape_google_articles(search, 1)
    items2 = scrape_google_articles(search, 2)
    items3 = scrape_google_articles(search, 3)
    items4 = scrape_google_articles(search, 4)
    items5 = scrape_google_articles(search, 5)
    items6 = scrape_google_articles(search, 6)
    items7 = scrape_google_articles(search, 7)

    items = items1 + items2 + items3 + items4 + items5 + items6 + items7
    print("Items: ", items)
    count = 0
    # Retrieve and print the three most recent articles
    for item in items:
        # print("Starting to read...")
        if count < 5:

            # article = i
            title = item["title"]
            link = item["link"]
            # print(title)

            question = f"{title}. give me the company name(write nothing else and if nasdaq is in the text so dont say nadaq say the company name)"

            chat = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            noc = chat.choices[0].message.content.strip()
            print("GPT ANSWER: ", noc)
            symbol = get_symbol(noc)
            print("Symbol: ", symbol, noc)
            exchange_name = 'None'
            try:
                url = f"https://www.google.com/search?q={symbol}+google+finance&sca_esv=4b723428e1eceb0a&sca_upv=1&sxsrf=ACQVn0_yizbh04WVxYQ8xhw9u5OHFxwBHw%3A1712840135706&ei=x90XZq3bKraDi-gP_reWsAs&oq=brainstorm+cell+therapeutics+stock+gogl&gs_lp=Egxnd3Mtd2l6LXNlcnAiJ2JyYWluc3Rvcm0gY2VsbCB0aGVyYXBldXRpY3Mgc3RvY2sgZ29nbCoCCAAyBxAhGAoYoAEyBxAhGAoYoAEyBxAhGAoYoAEyBxAhGAoYoAFI-g5QggJY8gdwAXgBkAEAmAG1AaABuQaqAQMwLjW4AQHIAQD4AQGYAgagAssGwgIKEAAYRxjWBBiwA8ICBRAAGIAEwgIGEAAYFhgewgILEAAYgAQYigUYhgPCAgUQIRigAcICBBAhGBWYAwCIBgGQBgiSBwMxLjWgB-Mb&sclient=gws-wiz-serp"

                chrome_options = Options()
                chrome_options.add_argument("--headless")  # Runs Chrome in headless mode

                # Use the headless Chrome WebDriver
                driver = webdriver.Chrome(
                    options=chrome_options)  # You may need to specify the path to your chromedriver
                driver.get(url)

                # Get the page source after Selenium has rendered the JavaScript content
                html = driver.page_source

                # Use BeautifulSoup to parse the HTML
                soup = BeautifulSoup(html, "html.parser")

                div_exchange = soup.find("div", {"class": "iAIpCb PZPZlf"})
                exchange_text = div_exchange.find("span").get_text()
                driver.quit()
                exchange_text = exchange_text.split(":")[0]

                print("Exchange text:", symbol, exchange_text)
                if "NASDAQ" == exchange_text or "NYSE" == exchange_text:
                    exchange_name = "good"

                else:
                    exchangxe_name = "None"
                    continue
            except Exception:
                exchange_name = 'None'
                # continue
            if exchange_name == "good":
                print("Getting result")
                result = str(first_par(link, title, noc=noc))
                print("Result: ", result)

                if not result == "None":
                    print("Result: ", result)
                    # losvector = get_embedding(result, engine="text-embedding-ada-002")
                    winvector = get_embedding(result)

                    win_df["similarities"] = win_df['embedding'].apply(lambda x: cosine_similarity(x, winvector))
                    winsimilarities.append(win_df["similarities"].iloc[-1])

                    win2_df["similarities"] = win2_df['embedding'].apply(lambda x: cosine_similarity(x, winvector))
                    lossimilarities.append(win2_df["similarities"].iloc[-1])

                    win3_df["similarities"] = win3_df['embedding'].apply(lambda x: cosine_similarity(x, winvector))
                    lossimilarities.append(win3_df["similarities"].iloc[-1])

                    distobj = {
                        "dist": (win_df["similarities"].iloc[-1] + win2_df["similarities"].iloc[-1] + win3_df["similarities"].iloc[-1]) / 3,
                        "noc": noc,
                        "symbol": symbol
                    }
                    print(distobj)
                    lock = multiprocessing.Lock()
                    lock.acquire()
                    try:
                        df = pd.read_csv('/Users/davidlevgabbay/Desktop/AlpacaBot-py11/Openai/dist_obj.csv')
                        # df = df_read.append(distobj, ignore_index=True)
                        df.loc[len(df.index)] = [distobj["dist"], distobj["noc"], distobj["symbol"]]
                    except pandas.errors.EmptyDataError as e:
                        print(e)
                        df = pd.DataFrame(columns=["dist", "noc", "symbol"])
                        df.loc[len(df.index)] = [distobj["dist"], distobj["noc"], distobj["symbol"]]
                        # df = []
                        # df.append(distobj)

                    save_to_csv(df)
                    lock.release()

                    count += 1
                    print(count)
                    print("Finished article")
                else:
                    print('Failed to extract article information.')
            else:
                print(symbol, "not a exchange")

    print("Done")


def get_symbol(company_name):
    try:
        url = f"https://www.nyse.com/site-search?q={company_name}&page=1"
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Runs Chrome in headless mode

        # Use the headless Chrome WebDriver
        driver = webdriver.Chrome(options=chrome_options)  # You may need to specify the path to your chromedriver
        driver.get(url)

        # Wait for the specific element to appear
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3.m-0.font-headings.border-0.pb-0.mers\\:border-b-2.mers\\:border-solid.mers\\:border-secondary.mers\\:pb-2\\.5.print\\:orphans-3.print\\:widows-3.font-medium.normal-case.leading-none.print\\:break-after-avoid.text-2xl.md\\:text-4xl")))

        # Get the page source after Selenium has rendered the JavaScript content
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("p", {"class": "overflow-hidden text-ellipsis"})#.text
        symbol = None
        # print(links)
        for link in links:
            if "quote" in link.text:
                symbol = link.text
                # print(link)
                break
        # print(symbol)
        symbol = symbol.split(":")[2]

        driver.quit()
    except Exception as e:
        print("Failed to get symbol", e)
        symbol = "NOT A COMPANY"
    return symbol




# import pandas as pd #TODO fix if does not work

winningtext = """Migdal Insurance & Financial Holdings Ltd. Sells 750,000 Shares of Talkspace, Inc. (NASDAQ:TALK)
Migdal Insurance & Financial Holdings Ltd. cut its stake in shares of Talkspace, Inc. (NASDAQ:TALK - Free Report) by 37.5% in the fourth quarter, according to the company in its most recent disclosure with the Securities and Exchange Commission (SEC). The fund owned 1,250,000 shares of the company's stock after selling 750,000 shares during the period. Migdal Insurance & Financial Holdings Ltd. owned approximately 0.75% of Talkspace worth $3,175,000 as of its most recent SEC filing.


Other institutional investors and hedge funds have also made changes to their positions in the company. NVP Associates LLC purchased a new position in shares of Talkspace in the fourth quarter valued at approximately $8,973,000. Vanguard Group Inc. boosted its holdings in Talkspace by 29.5% in the third quarter. Vanguard Group Inc. now owns 5,740,353 shares of the company's stock valued at $11,194,000 after purchasing an additional 1,307,834 shares during the period. Goldman Sachs Group Inc. grew its stake in Talkspace by 44.8% during the 1st quarter. Goldman Sachs Group Inc. now owns 5,081,589 shares of the company's stock worth $8,842,000 after purchasing an additional 1,571,383 shares in the last quarter. AWM Investment Company Inc. increased its holdings in Talkspace by 94.2% during the 3rd quarter. AWM Investment Company Inc. now owns 2,287,724 shares of the company's stock worth $4,461,000 after purchasing an additional 1,109,876 shares during the period. Finally, Alyeska Investment Group L.P. raised its position in Talkspace by 87.6% in the 4th quarter. Alyeska Investment Group L.P. now owns 1,594,800 shares of the company's stock valued at $973,000 after purchasing an additional 744,800 shares in the last quarter. 57.37% of the stock is owned by hedge funds and other institutional investors.


A shocking leak has revealed tech giant Microsoft's plans to add crypto support to future products. If the plans in these leaked internal documents pan out, we could see prices skyrocket for Bitcoin, Ethereum, XRP and MORE… The coupling of gaming and cryptocurrency could absolutely transform digital finance as we know it in 2024.
Claim your free seat by clicking here now.

Talkspace Stock Down 3.0 %
TALK stock traded down $0.09 during trading on Wednesday, hitting $2.94. The company had a trading volume of 916,795 shares, compared to its average volume of 1,258,979. The firm has a 50-day moving average price of $3.09 and a 200-day moving average price of $2.47. The firm has a market cap of $496.58 million, a PE ratio of -25.08 and a beta of 1.26. Talkspace, Inc. has a 1-year low of $0.74 and a 1-year high of $3.92.
Talkspace (NASDAQ:TALK - Get Free Report) last announced its quarterly earnings data on Thursday, February 22nd. The company reported ($0.01) EPS for the quarter, topping analysts' consensus estimates of ($0.04) by $0.03. Talkspace had a negative net margin of 12.78% and a negative return on equity of 16.06%. The company had revenue of $42.42 million during the quarter, compared to the consensus estimate of $38.30 million. During the same quarter in the prior year, the firm earned ($0.08) EPS. Sell-side analysts anticipate that Talkspace, Inc. will post -0.03 earnings per share for the current year.
Wall Street Analysts Forecast Growth
A number of research analysts recently issued reports on TALK shares. TheStreet upgraded shares of Talkspace from a "d" rating to a "c-" rating in a research note on Thursday, February 22nd. Barclays raised their price objective on shares of Talkspace from $2.50 to $3.00 and gave the stock an "equal weight" rating in a report on Friday, February 23rd.
Check Out Our Latest Research Report on TALK
Talkspace Company Profile (Free Report)
Talkspace, Inc operates as a virtual behavioral healthcare company in the United States. The company offers psychotherapy and psychiatry services through its platform to individuals, enterprises, and health plans and employee assistance programs. It provides text, audio, and video-based psychotherapy from licensed therapists.
Iris Energy Limited development of green energy-driven data centres in Canada

Our Vancouver office is working alongside the firm’s Calgary office to advise Australia-based Iris Energy Limited on the development of green energy-driven data centres in Canada. Iris Energy is a bitcoin mining business powered by renewable energy, with multiple data centre sites in British Columbia powered by renewable hydroelectric electricity. Iris Energy has a portfolio of development projects across Canada, the United States and APAC. 


Our work includes advising on all aspects of real estate (e.g., land purchases, leases, contaminated site remediation advice, and management of environmental liabilities), business agreements (e.g., equipment leases, equipment finance, equipment procurement agreements, engineering agreements), other land and power arrangements (e.g., utility interconnection and power supply agreements, regulatory requirements) and IPO support. 


This mandate reflects a significant footprint across British Columbia, with 3 existing projects totalling 160MW and major growth across North America. The development of data centres is a fast-growing area for Canadian real estate groups, not least because the British Columbia government has taken major steps to attract investment. Such developments present unique challenges and requirements. With bitcoin mining often being criticised for its substantial energy use, it is noteworthy that our client is focusing on developing data centres powered by renewables.
 
Stock Traders Buy High Volume of Iris Energy Call Options (NASDAQ:IREN)
Iris Energy Stock Performance
IREN opened at $4.35 on Wednesday. The company’s 50-day simple moving average is $5.67 and its two-hundred day simple moving average is $4.94. Iris Energy has a 52-week low of $2.79 and a 52-week high of $9.69.
Iris Energy (NASDAQ:IREN – Get Free Report) last issued its quarterly earnings data on Thursday, February 15th. The company reported ($0.07) earnings per share for the quarter. The company had revenue of $42.57 million for the quarter, compared to the consensus estimate of $37.58 million. On average, sell-side analysts predict that Iris Energy will post 0.08 earnings per share for the current fiscal year.
Hedge Funds Weigh In On Iris Energy
A number of institutional investors and hedge funds have recently modified their holdings of the company. Mirae Asset Global Investments Co. Ltd. boosted its holdings in shares of Iris Energy by 52.4% in the fourth quarter. Mirae Asset Global Investments Co. Ltd. now owns 1,037,420 shares of the company’s stock worth $7,418,000 after buying an additional 356,752 shares during the last quarter. Vontobel Holding Ltd. bought a new position in Iris Energy in the third quarter worth approximately $104,000. Van ECK Associates Corp boosted its stake in shares of Iris Energy by 19.7% during the 3rd quarter. Van ECK Associates Corp now owns 1,117,769 shares of the company’s stock worth $4,147,000 after acquiring an additional 184,039 shares during the last quarter. Tucker Asset Management LLC purchased a new position in shares of Iris Energy during the 3rd quarter worth $47,000. Finally, Exchange Traded Concepts LLC grew its position in shares of Iris Energy by 47.1% during the 4th quarter. Exchange Traded Concepts LLC now owns 613,818 shares of the company’s stock valued at $4,389,000 after acquiring an additional 196,635 shares during the period. 41.08% of the stock is currently owned by hedge funds and other institutional investors.
Analyst Ratings Changes
A number of analysts have recently commented on the company. B. Riley dropped their price target on Iris Energy from $10.00 to $9.50 and set a “buy” rating on the stock in a research report on Friday, March 15th. Canaccord Genuity Group reiterated a “buy” rating and set a $9.00 price objective on shares of Iris Energy in a research note on Thursday, March 28th. Cantor Fitzgerald reissued an “overweight” rating and issued a $10.00 target price on shares of Iris Energy in a research note on Thursday, March 28th. Finally, HC Wainwright reaffirmed a “buy” rating and issued a $10.00 price target on shares of Iris Energy in a research report on Tuesday, April 2nd. Five analysts have rated the stock with a buy rating, According to data from MarketBeat, Iris Energy currently has a consensus rating of “Buy” and an average target price of $12.00.
Check Out Our Latest Research Report on Iris Energy
About Iris Energy
(Get Free Report)
Iris Energy Limited owns and operates bitcoin mining data centers. The company was incorporated in 2018 and is headquartered in Sydney, Australia.
Fifth Third stock gains after strong quarterly guidance, Q1 earnings beat
Fifth Third Bancorp (NASDAQ:FITB) stock advanced 4% in Friday morning trading after delivering strong guidance for Q2 and better-than-forecast Q1 earnings.
The Cincinnati, Ohio-based lender expects Q2 2024 total revenue rising about 1% sequentially from $2.18B in Q1, implying Q2 revenue of ~$2.20B (vs. $2.13B consensus). Net interest income is seen stable to up 1% in Q2 from $1.39B in Q1, implying $1.39B-$1.40B (vs. $1.39B Visible Alpha consensus).
Q2 noninterest income is anticipated to rise 2%-4% from $717M in Q1, implying $731.3M-$745.7M. Noninterest expense is projected to retreat about 6% from Q1's $1.30B, implying $1.22B.
For Q1 2024, the company turned in adjusted EPS of $0.76 (excluding a negative $0.06 impact from certain items), surpassing the $0.72 average analyst estimate. The latest figure compares with GAAP EPS of $0.72 in Q4 2023 and $0.78 in the year-earlier period.
Net interest income (fully taxable equivalent) was $1.39B (vs. $1.38B Visible Alpha consensus), down from $1.42B in the prior quarter and $1.52B a year before.
Noninterest income fell to $710M from $744M in Q4 2023 and rose from $696M in Q1 2023.
Provision for credit losses of $94M climbed from $55M in Q4 2023 and slid from $164M a year ago.
Total noninterest expense of $1.34B decreased 8% Q/Q and gained 1% Y/Y.
Average portfolio loans and leases of $117.3B slipped 1% Q/Q; average deposits of $168.1B also edged down 1% sequentially.
American Express (AXP) Earnings Announcement - Will Credit Card Giant Surpass Expectations?
American Express Company (AXP - Get Rating) will unveil its first-quarter results on April 19. Wall Street anticipates the credit card giant to post higher revenue and earnings in the first quarter. With AXP’s earnings expected shortly, I have discussed why waiting for an opportune entry point in the stock could be wise.
For the first quarter, AXP’s EPS and revenue are expected to increase 24.2% and 10.5% year-over-year to $2.98 and $15.79 billion, respectively. The company achieved record revenues and profits in 2023 and added 12.2 million new proprietary cards last year, bringing the total number of cards-in-force issued on its global network to over 140 million.
For fiscal 2024, AXP has guided revenue growth of 9% to 11% and expects EPS of between $12.65 and $13.15. The company aims to continue achieving revenue growth of 10% plus and mid-teens EPS growth in the future. AXP’s stock has gained 41% over the past six months and 33% over the past year, closing the last trading session at $217.67.
Here’s what you might want to consider ahead of its upcoming earnings release:
Robust Financials
AXP’s total revenues net of interest expense for the fiscal fourth quarter ended December 31, 2023, rose 11.4% year-over-year to $15.80 billion. Its net interest income rose 30.7% over the prior-year quarter to $3.60 billion. The company’s net income attributable to common shareholders increased 23.2% year-over-year to $1.90 billion. Also, its EPS came in at $2.62, representing an increase of 26.6% year-over-year.
For the fiscal year ended December 31, 2023, AXP’s total revenues net of interest expense increased 14.5% year-over-year to $60.52 billion. Its net interest income rose 32.7% over the prior-year period to $13.13 billion. The company’s net income attributable to common shareholders increased 11.5% year-over-year to $8.25 billion. Also, its EPS came in at $11.21, representing an increase of 13.8% year-over-year.
Favorable Analyst Estimates
2024 STOCK MARKET OUTLOOK
Analysts expect AXP’s fiscal 2024 EPS and revenue to increase 14.2% and 9.4% year-over-year to $12.81 and $66.22 billion, respectively. Its fiscal 2025 EPS and revenue are expected to increase 15% and 8.6% year-over-year to $14.73 and $71.92 billion, respectively.
Similarly, analysts expect AXP’s EPS and revenue for the quarter ending June 30, 2024, to increase 12% and 9.8% year-over-year to $3.24 and $16.53 billion, respectively.
Mixed Profitability
AXP’s 15.06% trailing-12-month net income margin is 36% lower than the 23.52% industry average. Its 55.04% trailing-12-month gross profit margin is 7.7% lower than the 59.66% industry average.
On the other hand, AXP’s 31.28% trailing-12-month Return on Common Equity is 187.7% higher than the 10.87% industry average. Furthermore, the stock’s 3.21% trailing-12-month Return on Total Assets is 195.3% higher than the industry average of 1.09%. Also, its 0.23x trailing-12-month asset turnover ratio is 7.5% higher than the industry average of 0.21x.
Mixed Valuation
In terms of forward non-GAAP PEG, AXP’s 1.29x is 6.1% higher than the 1.21x industry average. Its 17x forward non-GAAP P/E is 72.1% higher than the 9.88x industry average. Likewise, its 5.04x forward Price/Book is 406.8% higher than the 0.99x industry average.
On the other hand, in terms of forward Price/Sales, AXP’s 2.37x is 0.8% lower than the 2.39x industry average.
POWR Ratings Reflect Uncertainty
AXP has an overall rating of C, equating to a Neutral in our POWR Ratings system. The POWR Ratings are calculated by considering 118 different factors, each weighted to an optimal degree.
Our proprietary rating system also evaluates each stock based on eight distinct categories. AXP has a C grade for Value, which is consistent with its mixed valuation. It has a C grade for Stability, in sync with its 1.23 beta.
AXP’s mixed profitability justifies its C grade for Quality.
AXP is ranked #19 out of 45 stocks in the Consumer Financial Services industry. Click here to access AXP’s Growth, Momentum, and Sentiment ratings.
Bottom Line
After ending fiscal 2023 on a solid note, AXP remains firmly positioned to achieve its long-term annual revenue growth of more than 10% and mid-teens EPS growth. As consumer spending continues to remain robust, the company is expected to see strong growth in billings, new account acquisitions, and processed volumes in the first quarter.
However, loans and cardmember receivables are expected to moderate through the rest of the year. Net interest income growth is also expected to moderate in fiscal 2024. Moreover, as credit card delinquencies continue to rise, write-offs are expected to increase along with higher reserve build-ups.
Given its mixed profitability, valuation, and stability, it could be wise to wait for a better entry point in the stock.
How Does American Express Company (AXP) Stack Up Against Its Peers?
AXP has an overall POWR Rating of C, equating to a Neutral rating. You may check out these A and B-rated stocks within the Consumer Financial Services industry: Qifu Technology, Inc. (QFIN - Get Rating), Atlanticus Holdings Corporation (ATLC - Get Rating), and EZCORP, Inc. (EZPW - Get Rating). For exploring more Buy-rated Comsumer Financial Services stocks, click here.
What To Do Next?
Discover 10 widely held stocks that our proprietary model shows have tremendous downside potential. Please make sure none of these “death trap” stocks are lurking in your portfolio:
"""

winningtext2 = """SG Americas Securities LLC acquired a new stake in shares of ModivCare Inc. (NASDAQ:MODV – Free Report) in the fourth quarter, according to the company in its most recent 13F filing with the Securities and Exchange Commission. The firm acquired 4,257 shares of the company’s stock, valued at approximately $187,000.
Get ModivCare alerts: 
A number of other hedge funds have also recently bought and sold shares of MODV. T. Rowe Price Investment Management Inc. grew its stake in ModivCare by 35.0% during the 4th quarter. T. Rowe Price Investment Management Inc. now owns 1,134,756 shares of the company’s stock valued at $101,822,000 after purchasing an additional 294,108 shares in the last quarter. Neuberger Berman Group LLC grew its stake in ModivCare by 81.4% during the 1st quarter. Neuberger Berman Group LLC now owns 330,136 shares of the company’s stock valued at $38,094,000 after purchasing an additional 148,191 shares in the last quarter. FMR LLC grew its stake in ModivCare by 222.4% during the 1st quarter. FMR LLC now owns 182,889 shares of the company’s stock valued at $15,377,000 after purchasing an additional 126,170 shares in the last quarter. Citadel Advisors LLC grew its stake in ModivCare by 365.7% during the 2nd quarter. Citadel Advisors LLC now owns 81,770 shares of the company’s stock valued at $6,909,000 after purchasing an additional 64,210 shares in the last quarter. Finally, Penn Capital Management Company LLC grew its position in shares of ModivCare by 65.1% in the 1st quarter. Penn Capital Management Company LLC now owns 154,050 shares of the company’s stock worth $12,982,000 after acquiring an additional 60,757 shares in the last quarter.
Analyst Ratings Changes
Several brokerages have recently commented on MODV. Deutsche Bank Aktiengesellschaft lowered ModivCare from a “buy” rating to a “hold” rating and decreased their target price for the stock from $60.00 to $40.00 in a research report on Friday, February 23rd. Jefferies Financial Group lowered ModivCare from a “buy” rating to a “hold” rating and decreased their target price for the stock from $60.00 to $39.00 in a research report on Friday, February 23rd. Finally, Barrington Research lowered ModivCare from an “outperform” rating to a “market perform” rating in a research report on Monday, February 26th.
Read Our Latest Stock Analysis on MODV
ModivCare Trading Down 0.2 %
Shares of NASDAQ MODV opened at $22.48 on Friday. The company has a market cap of $319.22 million, a price-to-earnings ratio of -1.56, a price-to-earnings-growth ratio of 0.61 and a beta of 0.44. ModivCare Inc. has a 12-month low of $20.30 and a 12-month high of $83.19. The company has a current ratio of 0.78, a quick ratio of 0.78 and a debt-to-equity ratio of 6.30. The stock’s 50 day simple moving average is $32.02 and its 200 day simple moving average is $36.95.
ModivCare (NASDAQ:MODV – Get Free Report) last announced its quarterly earnings results on Thursday, February 22nd. The company reported $1.18 earnings per share (EPS) for the quarter, topping the consensus estimate of $1.13 by $0.05. The business had revenue of $703.22 million for the quarter, compared to the consensus estimate of $699.34 million. ModivCare had a positive return on equity of 36.50% and a negative net margin of 7.42%. Equities research analysts expect that ModivCare Inc. will post 4.22 EPS for the current year.
About ModivCare
(Free Report)
ModivCare Inc, a technology-enabled healthcare services company, provides a suite of integrated supportive care solutions for public and private payors and their members. The company operates through four segments: Non-Emergency Medical Transportation (NEMT), Personal Care, Remote Patient Monitoring (RPM), and Corporate and Other.

Key Insights
Significantly high institutional ownership implies Valley National Bancorp's stock price is sensitive to their trading actions
51% of the business is held by the top 7 shareholders
Insiders have sold recently
Every investor in Valley National Bancorp (NASDAQ:VLY) should be aware of the most powerful shareholder groups. We can see that institutions own the lion's share in the company with 75% ownership. That is, the group stands to benefit the most if the stock rises (or lose the most if there is a downturn).
Because institutional owners have a huge pool of resources and liquidity, their investing decisions tend to carry a great deal of weight, especially with individual investors. Hence, having a considerable amount of institutional money invested in a company is often regarded as a desirable trait.
Let's take a closer look to see what the different types of shareholders can tell us about Valley National Bancorp.



ownership-breakdown
What Does The Institutional Ownership Tell Us About Valley National Bancorp?
Many institutions measure their performance against an index that approximates the local market. So they usually pay more attention to companies that are included in major indices.
As you can see, institutional investors have a fair amount of stake in Valley National Bancorp. This suggests some credibility amongst professional investors. But we can't rely on that fact alone since institutions make bad investments sometimes, just like everyone does. When multiple institutions own a stock, there's always a risk that they are in a 'crowded trade'. When such a trade goes wrong, multiple parties may compete to sell stock fast. This risk is higher in a company without a history of growth. You can see Valley National Bancorp's historic earnings and revenue below, but keep in mind there's always more to the story.

earnings-and-revenue-growth
Investors should note that institutions actually own more than half the company, so they can collectively wield significant power. Valley National Bancorp is not owned by hedge funds. Bank Leumi Le-Israel BM, Asset Management Arm is currently the company's largest shareholder with 14% of shares outstanding. BlackRock, Inc. is the second largest shareholder owning 13% of common stock, and The Vanguard Group, Inc. holds about 9.0% of the company stock.
On further inspection, we found that more than half the company's shares are owned by the top 7 shareholders, suggesting that the interests of the larger shareholders are balanced out to an extent by the smaller ones.
While studying institutional ownership for a company can add value to your research, it is also a good practice to research analyst recommendations to get a deeper understand of a stock's expected performance. Quite a few analysts cover the stock, so you could look into forecast growth quite easily.
Insider Ownership Of Valley National Bancorp
The definition of an insider can differ slightly between different countries, but members of the board of directors always count. Management ultimately answers to the board. However, it is not uncommon for managers to be executive board members, especially if they are a founder or the CEO.
Most consider insider ownership a positive because it can indicate the board is well aligned with other shareholders. However, on some occasions too much power is concentrated within this group.
We can see that insiders own shares in Valley National Bancorp. This is a big company, so it is good to see this level of alignment. Insiders own US$53m worth of shares (at current prices). It is good to see this level of investment by insiders. You can check here to see if those insiders have been buying recently.
General Public Ownership
With a 23% ownership, the general public, mostly comprising of individual investors, have some degree of sway over Valley National Bancorp. While this group can't necessarily call the shots, it can certainly have a real influence on how the company is run.
Next Steps:
It's always worth thinking about the different groups who own shares in a company. But to understand Valley National Bancorp better, we need to consider many other factors. Case in point: We've spotted 2 warning signs for Valley National Bancorp you should be aware of.
But ultimately it is the future, not the past, that will determine how well the owners of this business will do. Therefore we think it advisable to take a look at this free report showing whether analysts are predicting a brighter future."""

winningtext3 = """Root, Inc.: Promising Embedded Strategy With Potential Nationwide Expansion
May 06, 2024 8:05 AM ETRoot, Inc. (ROOT) Stock12 Comments

Tech and Growth
3.16K Followers
Follow
Summary
Root, Inc. is a leading auto insurtech company, leveraging data science and technology to improve underwriting performance.
Despite weak overall share performance since going public, Root has seen significant growth over the past year, with its stock price increasing almost 10x.
Root's strong financial performance, including revenue growth and narrowing net losses, suggests potential for continued growth and profitability.

Luis Alvarez/DigitalVision via Getty Images
Root, Inc. (NASDAQ:ROOT) is an auto insurtech company, leveraging data science and tech platform to drive underwriting performance. ROOT also claims to be the largest auto insurtech player by premium.
Overall share performance since going public in 2020 has been weak, with ROOT currently trading at $56, down almost -87% since then. ROOT could have been performing much worse, had it not seen strong momentum over the past year. Just May last year, ROOT was still trading at $5 price level, meaning that it is now up almost 10x today over the past year.
I rate ROOT stock a buy. My 1-year price target of $74.7 per share projects a 32% upside. I believe ROOT may continue to see strong tailwinds into FY 2024, driven by its embedded platform distribution strategy that should also allow it to unlock further growth through nationwide expansion in the future.
Financial Reviews

ycharts
Fundamentals had been weak in the last two years, when ROOT saw overall decline in business growth and also profitability. However, ROOT appears to have been on a rebound since FY 2023, when it posted a revenue growth of over 46% YoY. It maintained this trend in the most recent quarter, Q1 2024. In Q1, ROOT delivered a revenue of almost $255 million, which was already a staggering 263% YoY growth. Though this was primarily due to the easier comparison, considering the considerable downturn last year, when policies in force trended lower because ROOT reduced marketing expense.
Net losses have also continued to narrow as of Q1, with ROOT realizing a GAAP net loss margin of -2.4%, closing in the gap to breakeven. In fact, this has been the closest ROOT has been to achieving breakeven over the past five years on a quarterly basis. The improved bottom-line performance seems to have helped improve operating cash flow (OCF) generation as well. ROOT has consistently delivered positive OCF since two quarters ago, and it continued to maintain such a trend in Q1, when it delivered over $14 million in OCF. This seems to also have helped create a slight uptick in liquidity. ROOT ended Q1 with over $856 million of cash and short-term investments, up over 1% since last quarter.
Out of that $856 million of liquidity, cash and cash equivalents actually declined slightly to $640 million. Yet, ROOT also invested $59 million of its cash into investments. As such, AFS (Available-For Sale) securities, short-term investments, and other investments ended up increasing to $220 million for the quarter, up by over 28% YoY, driving up overall liquidity position.
Catalyst
I believe ROOT is well positioned to maintain a decent growth performance and also a positive trend in profitability.

company presentation
I think that the key catalyst here would be the increased effort to diversify its distribution through embedding its technology-driven products into car-buying platforms such as Carvana, which already possess a large client base. Effectively, this allows for more effective GWP (Gross Written Premium) growth through seamlessly adding insurance-buying activity into a typical car-buying journey, in my opinion. Given the success so far in driving sustainable growth in Q1, as demonstrated by the steep downtrend in gross loss ratio and also 68% YoY growth in new writings from partnerships, I believe ROOT is in a good position to scale up further.

company presentation
In my view, one of the key growth levers here would be nationwide expansion. Today, as commented by the management, ROOT has only been operating in 34 states, suggesting that there is significant room for expansion:
And we believe that we’ve got ample growth levers that we can pull. Currently, we’re only in 34 states. We would like to be national at some point and we’re continuing to invest in our differentiated distribution. So, our partnership channel does continue to grow.
Source: Q1 earnings call.
Risk
As anticipated by the management, GWP will decline in Q2 relative to Q1, driven by seasonality and also changes in the competitive environment. GWP remains a key driver for growth for ROOT, and declining GWP could signal potential top-line growth slowdown that may trigger sell-offs.
Nonetheless, in my view, this may also suggest that the market’s expectation of ROOT achieving a net profit breakeven will consequently increase, especially given the fact that ROOT will not be spending aggressively just to grow its GWP. As a result, ROOT will also need to deliver stronger profitability profile in Q2 and beyond to somehow offset the lower growth. Otherwise, share performance could potentially suffer, in my view.
In fact, I would also expect ROOT to take the opportunity here to aim for a breakeven, since it is typical for ROOT to also spend higher on marketing in Q1, relative to other quarters:
I’d say we are always looking at the competitive environment and monitoring the competitive environment, as well as seasonality and we do know that the first quarter, you see more auto insurance shopping and so you should expect that to accelerate sales and marketing spend in the first quarter relative to other quarters.
Source: Q1 earnings call.
In my view, stronger profitability performance in Q2 should also help reduce concerns regarding competition, which is expected to become more intense in the FY. The online auto insurtech space has gotten crowded, with players like Metromile, Branch, or Clearcover competing for market share.
Valuation / Pricing
My target price for ROOT is driven by the following assumptions for the bull vs bear scenarios of the FY 2024 projection:
Bull scenario (50% probability) assumptions - I expect revenue to grow 119% YoY to $1 billion, in line with the market’s consensus. I assume forward P/S to expand slightly to 1.4x, implying a share price appreciation to $93.
Bear scenario (50% probability) assumptions - ROOT to deliver FY 2024 revenue of $700 million, a 53% YoY growth, but is still way lower than the market’s consensus low-end target of $997 million. I assign ROOT a forward P/S of 1.2x, where it is trading today, projecting a sideways price action within $56 price level.

own analysis
Consolidating all the information above into my model, I arrived at an FY 2024 weighted target price of $74.7 per share, projecting an over 32% upside. I would assign the stock a buy rating.
My assumption of 50-50 for bull and bear scenarios is based on my belief that the competitive environment still presents a bit of uncertainty despite the relatively strong tailwinds today. Though the management has not issued a FY guidance, the market’s consensus seems to expect a very strong outperformance continuing on in FY 2024. I believe the $74.7 price target is also realistic, since ROOT also already saw that level this year. In fact, ROOT’s YTD high was $83 per share, which it last saw in early April.
Conclusion
ROOT is an insurtech company that has been on a rebound since seeing decline in business in the past two years. I think that the embedded platform distribution strategy should allow ROOT to unlock efficient growth opportunities through providing better insurance-buying experience. Moreover, given the strong unit economics today, ROOT is in a good position to scale up nationwide, where there is still plenty of room for growth there. My price target of $74.7 projects a 32% 1-year upside. I rate the stock a buy.
LX Oncology Appoints Allison Dillon as Chief Business Officer
May 07, 2024 09:00 ET| Source: ALX Oncology
Follow

Share













SOUTH SAN FRANCISCO, Calif., May 07, 2024 (GLOBE NEWSWIRE) -- ALX Oncology Holdings Inc., (“ALX Oncology” or “the Company”) (Nasdaq: ALXO), an immuno-oncology company developing therapies that block the CD47 immune checkpoint pathway, today announced the appointment of Allison Dillon, Ph.D., as Chief Business Officer (“CBO”).
“We are excited to welcome Allison to our leadership team in the midst of this promising growth period for our Company,” said Jason Lettmann, Chief Executive Officer of ALX Oncology. “For over 15 years, Allison has worked to develop and deliver novel oncology products to patients with cancer. With multiple clinical study readouts over the next 12 months, Allison’s deep oncology market expertise and impressive track record in executing portfolio, development, and commercial strategy will be vital in our endeavor to propel evorpacept to its full potential as a first-in-class, universal combination agent with anti-cancer antibodies, antibody-drug conjugates, and checkpoint inhibitors.”
“Evorpacept has immense potential to positively impact the lives of people with cancer,” said Dr. Dillon, CBO of ALX Oncology. “With near-term clinical trial readouts and a strong balance sheet, ALX Oncology is well positioned for greater success. I am thrilled to begin working with this impressive team as we continue elevating our science and value through this exciting next chapter.”
Dr. Dillon joined ALX Oncology from Calithera Biosciences, where she most recently served as Senior Vice President of Commercial and Portfolio Strategy until 2023. During her time at Calithera, Dr. Dillon spearheaded commercial planning across a pipeline of hematology, solid tumors, and cystic fibrosis molecules. As Senior Vice President, Dr. Dillon also led corporate communications, including public and investor relations functions. Dr. Dillon helped oversee successful fundraising activities and acquisition of drugs such as mivavotinib and sapansertib from Takeda. Prior to joining Calithera in 2017, Dr. Dillon’s expertise on pre- and post-launch commercialization strategy grew during her time at Genentech. Dr. Dillon drove the commercial launch plan for the initial launch of TECENTRIQ® (atezolizumab) in the US, and multiple subsequent launches, later serving as the Marketing Lead for GU indications. Additionally, she was the U.S. commercial representative on various Roche global business teams that informed investments. She served in marketing and sales roles for AVASTIN® (bevacizumab), TARCEVA® (erlotinib), ZELBORAF® (vemurafenib), and TECENTRIQ. Prior to Genentech, Dr. Dillon was a Senior Consultant at the management consulting firm Campbell Alliance, working across pharma and biotech clients. Prior to consulting, she was a Postdoctoral Fellow at the University of California San Francisco, Howard Hughes Medical Institute studying genetic pathways involved in medulloblastoma. Dr. Dillon holds a Ph.D. and M.S. in Neuroscience from Albert Einstein College of Medicine and a B.A. in Psychology from the University of Richmond.
About ALX Oncology
ALX Oncology is a publicly traded, clinical-stage immuno-oncology company focused on helping patients fight cancer by developing therapies that block the CD47 immune checkpoint inhibitor and bridge the innate and adaptive immune system. ALX Oncology’s lead product candidate, evorpacept, is a next generation CD47 blocking therapeutic that combines a high-affinity CD47 binding domain with an inactivated, proprietary Fc domain. To date, evorpacept has been dosed in over 500 subjects and has demonstrated promising activity and favorable tolerability profile across a range of hematologic and solid malignancies in combination with various leading anti-cancer antibodies. ALX Oncology is currently focusing on combining evorpacept with anti-cancer antibodies, antibody-drug conjugates (“ADCs”), and PD-1/PD-L1 immune checkpoint inhibitors.
Cautionary Note Regarding Forward-Looking Statements
This press release contains forward-looking statements that involve substantial risks and uncertainties. Forward-looking statements include statements regarding future results of operations and financial position, business strategy, product candidates, planned preclinical studies and clinical trials, results of clinical trials, research and development costs, regulatory approvals, timing and likelihood of success, plans and objects of management for future operations, as well as statements regarding industry trends. Such forward-looking statements are based on ALX Oncology’s beliefs and assumptions and on information currently available to it on the date of this press release. Forward-looking statements may involve known and unknown risks, uncertainties and other factors that may cause ALX Oncology’s actual results, performance or achievements to be materially different from those expressed or implied by the forward-looking statements. These and other risks are described more fully in ALX Oncology’s filings with the Securities and Exchange Commission (“SEC”), including ALX Oncology’s Annual Reports on Form 10-K, Quarterly Reports on Form 10-Q and other documents ALX Oncology files with the SEC from time to time. Except to the extent required by law, ALX Oncology undertakes no obligation to update such statements to reflect events that occur or circumstances that exist after the date on which they were made.
First quarter revenue of $85.8 million, up 21% year-over-year
ARR of $354.2 million, up 21% year-over-year
First quarter net cash provided by operating activities of $14.8 million
First quarter free cash flow of $12.0 million, free cash flow margin of 14.0%
New Enterprise SEO Platform now Generally Available (GA)
May 06, 2024 04:30 PM Eastern Daylight Time
BOSTON--(BUSINESS WIRE)--Semrush Holdings, Inc. (NYSE: SEMR), a leading online visibility management SaaS platform, today reported financial results for the first quarter ended March 31, 2024.
“We had a strong start to 2024, achieving first quarter revenue and ARR growth of 21% year-over-year. Importantly, we reported strong profitability exceeding our guidance, with income from operations of $1.5 million and non-GAAP income from operations of $9.7 million. In the first quarter, we reported nearly 112,000 paying customers and added several new products and features to our platform. Looking ahead, we are very optimistic about our potential. We continue to succeed in executing on our core growth pillars by onboarding more customers, cross-selling and up-selling to existing customers and leveraging AI in our platform to ensure businesses of any size have the most valuable digital marketing software suite. And now with our Enterprise SEO product generally available, we expect to drive momentum by moving up-market to larger accounts,” said Oleg Shchegolev, CEO and Co-Founder of Semrush.
First Quarter 2024 Financial Highlights
First quarter revenue of $85.8 million, up 21% year-over-year.
Income from operations of $1.5 million for the first quarter, compared to a loss from operations of $10.8 million in the prior year period.
Operating margin of 1.7% for the first quarter, compared to operating margin of (15.2)% in the prior year period.
Non-GAAP income from operations of $9.7 million for the first quarter, compared to a non-GAAP loss from operations of $6.5 million in the prior year period.
Non-GAAP operating margin of 11.3% for the first quarter, compared to non-GAAP operating margin of (9.1)% in the prior year period.
Q1 free cash flow of $12.0 million and free cash flow margin of 14.0%.
ARR of $354.2 million as of March 31, 2024, up 21% year-over-year.
Nearly 112,000 paying customers as of March 31, 2024, up 10% from a year ago.
Dollar-based net revenue retention of 107% as of March 31, 2024, consistent with the previous quarter.
See “Non-GAAP Financial Measures & Definitions of Key Metrics” below for how Semrush defines ARR, dollar-based net revenue retention, non-GAAP income (loss) from operations, non-GAAP operating margin, free cash flow, and free cash flow margin, and the financial tables that accompany this release for reconciliations of each non-GAAP financial measure to its closest comparable GAAP financial measure.
First Quarter 2024 Business Highlights
We are committed to empowering our customers with the best-in-class platform needed to boost their online presence and gain an edge in the market. In the first quarter, we advanced and expanded many of our offerings:
Continued investments in Generative AI to provide enhanced, more efficient content creation capabilities through Semrush’s platform and App Center:
Introduced Semrush Copilot, a feature that provides AI-powered SEO alerts and recommendations based on machine learning algorithms that reference data from several Semrush tools at once.
Launched AdCreative.ai, an AI-powered app that generates ad creatives, product photoshoots, and texts for any social media or display platform.
We are pleased to announce our new Enterprise SEO Platform is now generally available following a soft launch in October 2023. We see strong demand for the product and it is now being used by large, multinational corporations.
We have upgraded .Trends, one of our Competitive Intelligence (CI) products with daily and weekly competitor website traffic data. Previously the data was tracked monthly. We believe the added granularity will help businesses gain deeper insights on their competitors’ content performance, shifts in strategy, website and individual page traffic, special events, and seasonal variations.
Semrush customers who pay more than $10,000 annually grew by 32% year-over-year.
Ended the quarter with more than 1,125,000 registered free active customers, up 27% year-over-year.
Business Outlook
“We delivered a strong first quarter across the board, exceeding our revenue and Non-GAAP operating margin guidance,” said Brian Mulroy, CFO of Semrush. “Growth this quarter was driven by new customer additions and expansion of our average revenue per customer as we continue to execute on our cross-sell and up-sell strategy. We continue to drive cost efficiencies, invest in the business, and expand profitability. Looking ahead, we are raising our full year 2024 guidance and are confident in our ability to grow and scale our business. We expect to make incremental investments to strengthen our position while also driving further operating leverage in the business and delivering long-term value to our shareholders.”
Based on information as of today, May 6, 2024, we are issuing the following financial guidance:
Second Quarter 2024 Financial Outlook
For the second quarter, we expect revenue in a range of $89.1 to $90.1 million, which at the mid-point would represent growth of approximately 20% year-over-year.
We expect second quarter non-GAAP operating margin to be approximately 11.0%.
Full-Year 2024 Financial Outlook
For the full year, we expect revenue in a range of $366 to $369 million, which represents growth of 19% to 20% year-over-year.
We expect full year non-GAAP operating margin of 10.5% to 11.5%.
We expect full year free cash flow margin to be approximately 8.0%.
As indicated in our fourth quarter 2023 and full year 2023 Financial Results, we are no longer providing guidance for non-GAAP net income, and instead are guiding both non-GAAP operating margin and free cash flow margin. We have also updated our definitions of non-GAAP income (loss) from operations to exclude Amortization of Acquired Intangible Assets, Acquisition Related Costs, Restructuring Costs and other one-time expenses outside the ordinary course of business (for example, our Exit Costs incurred primarily in 2022) in addition to the prior exclusion of Stock Based Compensation. Our guidance for the second quarter 2024 and full year 2024, as well as actual results presented herein, reflect this change.
Reconciliations of non-GAAP operating margin and free cash flow margin guidance to the most directly comparable GAAP measures are not available without unreasonable efforts on a forward-looking basis due to the high variability, complexity and low visibility with respect to the charges excluded from these non-GAAP measures, in particular the measures and effects of share-based compensation expense, employer taxes and tax deductions specific to equity compensation awards that are directly impacted by future hiring, turnover and retention needs. We expect the variability of the above charges to have a significant, and potentially unpredictable, impact on our future GAAP financial results.
Conference Call Details
Semrush will host a conference call and webcast to discuss its financial results, business highlights, outlook and other matters, the details for which are provided below.
Date: Tuesday, May 7, 2024
Time: 8:30 a.m. ET
Hosts: Oleg Shchegolev, CEO, Eugene Levin, President, and Brian Mulroy, CFO
Conference ID: 283299
Participant Toll Free Dial-In Number: +1 833 470 1428
Participant International Dial-In Number: +1 929 526 1599
Registration:
The live webcast of the conference call as well as the replay can be accessed for a limited time from the Semrush investor relations website at http://investors.semrush.com/.
About Semrush
Semrush is a leading online visibility management SaaS platform that enables businesses globally to run search engine optimization, pay-per-click, content, social media and competitive research campaigns and get measurable results from online marketing. Semrush offers insights and solutions for companies to build, manage, and measure campaigns across various marketing channels. Semrush, with nearly 112,000 paying customers, is headquartered in Boston and has offices in Philadelphia, Trevose, Austin, Dallas, Florida, Amsterdam, Barcelona, Belgrade, Berlin, Limassol, Prague, Warsaw, and Yerevan.
Forward-looking Statements
This press release contains forward-looking statements within the meaning of the federal securities laws, which are statements that involve substantial risks and uncertainties. Forward-looking statements generally relate to future events or our future financial or operating performance. In some cases, you can identify forward-looking statements because they contain words such as “may,” “will,” “shall,” “should,” “expects,” “plans,” “anticipates,” “could,” “intends,” “target,” “projects,” “contemplates,” “believes,” “estimates,” “predicts,” “potential” or “continue” or the negative of these words or other similar terms or expressions that concern our expectations, strategy, plans or intentions. Forward-looking statements include, but are not limited to, guidance on financial results for the second quarter and full year of 2024 (including revenue, non-GAAP operating margin, and free cash flow margin); statements regarding the expectations of demand for our products, including the .Trends product, onboarding new customers, adoption of and demand for new products and features; statements about expansion of our platform, and launching new products; statements about future operating results, growth opportunities, future spending and incremental investments, business trends, capability to deliver profits, and growth and value for shareholders.
The forward-looking statements contained in this release are also subject to other risks and uncertainties, including those more fully described in our filings with the Securities and Exchange Commission (“SEC”), including in the sections entitled “Risk Factors” and “Management’s Discussion and Analysis of Financial Condition and Results of Operations'' in our filings with the Securities and Exchange Commission ("SEC"), including our most recent annual report on form 10-K, and our subsequently filed quarterly reports and other SEC filings. Although we believe that our plans, intentions, expectations, strategies and prospects as reflected in or suggested by those forward-looking statements are reasonable, we can give no assurance that the plans, intentions, expectations or strategies will be attained or achieved. The forward-looking statements in this release are based on information available to us as of the date hereof, and we disclaim any obligation to update any forward-looking statements, except as required by law. These forward-looking statements should not be relied upon as representing our views as of any date subsequent to the date of this press release.
Additional information regarding these and other factors that could affect our results is included in our SEC filings, which may be obtained by visiting our Investor Relations page on its website at investors.semrush.com or the SEC's website at www.sec.gov.
Non-GAAP Financial Measures & Definitions of Key Metrics
We believe that providing non-GAAP information to investors, in addition to the GAAP presentation, allows investors to view the financial results in the way management views the operating results. We further believe that providing this information allows investors to not only better understand our financial performance, but also to evaluate the efficacy of the methodology and information used by management to evaluate and measure such performance. We also believe that the use of non-GAAP financial measures provides an additional tool for investors to use in evaluating ongoing operating results and trends and in comparing our financial results with other companies in our industry, many of which present similar non-GAAP financial measures to investors. We also believe free cash flow margin is useful to investors as we monitor it as a measure of our overall business performance, which enables us to analyze our future performance without the effects of non-cash items and allows us to better understand the cash needs of our business. The non-GAAP information included in this press release should not be considered superior to, or a substitute for, financial statements prepared in accordance with GAAP and may be different from non-GAAP financial measures presented by other companies. Investors are encouraged to review the reconciliation of non-GAAP measures to their most directly comparable GAAP financial measures provided in the financial statement tables included below in this press release.
Annual Recurring Revenue (ARR) is defined as of a given date as the monthly recurring revenue that we expect to contractually receive from all paid subscription agreements that are actively generating revenue as of that date multiplied by 12. We include both monthly recurring paid subscriptions, which renew automatically unless canceled, as well as the annual recurring paid subscriptions so long as we do not have any indication that a customer has canceled or intends to cancel its subscription and we continue to generate revenue from them.
Dollar-based net revenue retention is defined as (a) the revenue from our customers during the twelve-month period ending one year prior to such period as the denominator and (b) the revenue from those same customers during the twelve months ending as of the end of such period as the numerator. This calculation excludes revenue from new customers and any non-recurring revenue.
Free cash flow and free cash flow margin. We define free cash flow, a non-GAAP financial measure, as net cash provided by (used in) operating activities less purchases of property and equipment and capitalized software development costs. We define free cash flow margin as free cash flow divided by GAAP revenue.
Non-GAAP income (loss) from operations, and non-GAAP operating margin. As described above, we have updated our definitions for non-GAAP income (loss) from operations and have introduced non-GAAP operating margin; the updated definitions, which apply to our guidance for the second quarter and full year 2024, are as follows. We define non-GAAP income (loss) from operations as GAAP income (loss) from operations, excluding Stock Based Compensation, Amortization of Acquired Intangible Assets, Acquisition Related Costs, Restructuring Costs and other one-time expenses outside the ordinary course of business (for example, our Exit Costs incurred primarily in 2022). We define non-GAAP operating margin as non-GAAP income (loss) from operations divided by GAAP revenue. We believe investors may want to consider our results with and without the effects of these items in order to compare our financial performance with that of other companies that exclude such items and to compare our results to prior periods.
Stock-based compensation. Stock-based compensation is a non-cash expense accounted for in accordance with FASB ASC Topic 718. We believe that the exclusion of stock-based compensation expense allows for financial results that are more indicative of our operational performance and provide for a useful comparison of our operating results to prior periods and to our peer companies because stock-based compensation expense varies from period to period and company to company due to such things as differing valuation methodologies, timing of awards and changes in stock price.
Amortization of acquired intangible assets. Excluding amortization of acquired intangible assets from non-GAAP expense and income measures allows management and investors to evaluate results “as-if” the acquired intangible assets had been developed internally rather than acquired and, therefore, provides a supplemental measure of performance in which our acquired intellectual property is treated in a comparable manner to our internally developed intellectual property. These amounts are inconsistent in amount and frequency and are significantly impacted by the timing and size of acquisitions. Although we exclude amortization of acquired intangible assets from our non-GAAP expenses, we believe that it is important for investors to understand that such intangible assets contribute to revenue generation.
Restructuring and other costs. Restructuring and other costs include restructuring expenses as well as other charges that are unusual in nature, are the result of unplanned events, and arise outside the ordinary course of our business. Restructuring expenses consist of employee severance costs, charges for the closure of excess facilities and other contract termination costs. Other costs include litigation contingency reserves, asset impairment charges, relocation expenses associated with the migration of employees in 2022 that occurred throughout 2022 and early 2023, and gains or losses on the sale or disposition of certain non-strategic assets or product lines.
Acquisition-related costs, net. In recent years, we have completed a number of acquisitions, which result in transition, integration and other acquisition-related expense which would not otherwise have been incurred, are unpredictable and dependent on a significant number of factors that are deal-specific or outside of our control, are not indicative of our operational performance (or that of the acquired businesses or assets) and are likely to fluctuate as our acquisition activity increases or decreases in future periods. By excluding acquisition-related costs and adjustments from our non-GAAP measures, management is better able to evaluate our ability to utilize our existing assets and estimate the long-term value that acquired assets will generate for us.

EARNINGS
Addus HomeCare Expects 2024 Acquisitions
By Jim Parker | May 7, 2024
 Pixabay
Share
Facebook
Twitter
LinkedIn
Send email
Addus HomeCare Corp. (NASDAQ: ADUS) is poised for further acquisitions, potentially including some hospice deals.
The company is seeking to pair its clinical services with its personal business in its existing markets. This is a cornerstone of its acquisition strategy. But Addus Chairman and CEO Dirk Allison does not rule out the possibility of moving into new markets if circumstances are right.
“As we see potential acquisitions come to mark, it remains our primary focus to use our financial capacity to acquire strategic operations that align with our overall growth strategy of adding clinical services where we have strong personal care presence, enhancing our existing personal care markets and adding new personal care markets where we can enter at scale,” Allison said in a Q1 earnings call. “We also believe this acquisition strategy will continue to strengthen our ability to participate in value-based contracts with our payers and to adapt to potential reimbursement changes.”
When examining new markets, Addus focuses on regions where they can quickly become the largest or second-largest provider by market share, according to CFO Brian Poff.
Fueling its acquisition aspirations is more than $77 million in dry powder as well as existing lines of credit.
Addus’ roughly 33,000 employees provide hospice, home health and private duty nursing services across more than 200 locations in 22 states.
The company saw 11.6% year-over-year revenue growth in Q1, reaching $280.7 million in net service revenue. The company’s hospice segment, which represents about 20% of the business, earned nearly $56 million in the first quarter. Hospice revenue per day was up 3.7% from the prior year’s quarter.
The personal care, hospice and home health provider is no stranger to acquisitions. Addus purchased Illinois-based hospice provider JourneyCare Inc. for $85 million in October 2022 and picked up Chicago-based  Home Health Ltd. for an undisclosed sum the following month. Last summer, Addus acquired Tennessee Quality Care for $106 million.
In addition to deals, Addus is seeing results when it comes to same-store hospice growth.
“We were pleased to see consistent positive year over year trends in our hospice business in the first quarter inclusive of our Tennessee Quality Care acquisition. Our hospice same-store revenue growth of 5.8% was our third consecutive quarter of sequential increase and the highest percentage increase we have seen prior to the COVID pandemic,” Poff said during the earnings call. “We continue to see favorable admission trends as we have experienced three consecutive quarters of sequential same store admission growth.”



"""

winsimilarities = []
lossimilarities = []

beforew_df = [{"text": winningtext}]
beforew2_df = [{"text": winningtext2}]
beforew3_df = [{"text": winningtext3}]

#

win_df = pd.DataFrame(beforew_df)
win2_df = pd.DataFrame(beforew2_df)
win3_df = pd.DataFrame(beforew3_df)
# search_term = "Rockwell Medical: New Course Amid Market Challenges. Rockwell Medical Inc, a microcap company, is gaining attention due to a compelling turnaround plan. The company is pivoting back to its core business, ceasing commercialization spending on Triferic. Despite this shift away from costly Triferic development, Rockwell's core business faces challenges; thin margins, and strong competition."


win_df['embedding'] = win_df['text'].apply(lambda x: get_embedding(x))
win2_df['embedding'] = win2_df['text'].apply(lambda x: get_embedding(x))
win3_df['embedding'] = win3_df['text'].apply(lambda x: get_embedding(x))


# win_df['embedding'] = get_embedding(win_df['text'])
# win_df2['embedding'] = get_embedding(win_df2['text'])


def scrape_website(url, timeout=15):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        # Send a GET request to the specified URL with a timeout
        response = requests.get(url, timeout=timeout, headers=headers)
        # Raise an exception for unsuccessful HTTP status codes (e.g., 404, 500, etc.)
        response.raise_for_status()

        # Create a BeautifulSoup object from the response content
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup)

        # Extract the text from the BeautifulSoup object
        text = soup.get_text(separator='\n\n')

        # Remove extra whitespace and newlines
        text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())

        return text
    except requests.exceptions.Timeout:
        print("Request to the URL timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)

        return None


# TODO if first_par does not return enough replace


def error_first_par(url, title, noc):
    extracted_text = scrape_website(url)
    print(extracted_text)
    if extracted_text != None:
        lines = extracted_text.split('\n')
        paragraph = []
        title = title

        def find_first_paragraph(text):
            lines = text.split("\n")
            paragraph_lines = []
            for line in lines:
                # Check if line is empty or indented (contains whitespace at the beginning)
                if not line or line.startswith(" "):
                    # If paragraph_lines is not empty, it means we've found the start of a new paragraph
                    if paragraph_lines:
                        break
                else:
                    # Check if line has more than 4 words
                    words = line.split()
                    if len(words) > 7:
                        paragraph_lines.append(line)
            return paragraph_lines

        for line in lines:
            if len(line.split()) > 7 and title not in line and noc in line:
                paragraph.append(line)

            else:
                continue

        # print(paragraph)

        find_first_paragraph(extracted_text)
        # print(paragraph)
        try:
            return_var = title + " " + paragraph[1] + " " + paragraph[2] + " " + paragraph[3]
            if return_var != "None":
                return return_var
        except Exception:
            return None
    else:
        return None


def first_par(url, title, noc):
    url = url[1:]
    url = "https://" + url
    try:
        print(url)
        article = Article(url)
        article.download()
        article.parse()

        article_text = article.text

        if len(article_text) != 0:
            return title + ' ' + article_text
        else:
            return "None"
    except Exception:
        print("Moving to 2 way")
        error_result = error_first_par(url, title, noc)
        return error_result


import requests
from bs4 import BeautifulSoup

# from datetime import datetime
# import asyncio
current_datetime = datetime.datetime.now()
dists = []
# Convert the current date and time to a timestamp
timestamp = current_datetime.timestamp()
search = 'Announces+share+price'  # Replace with your desired search query


def get_companies(arg, extension):
    searches = ["Beats+earnings+estimate", "Beats+quarterly+estimate", "Enters+into+Agreement+to",
                "What+is+Wall+Street's+Target+Price", "fda+approval", "Announces+Expanded+Retail",
                "Announces+CEO+Transition", "Fiscal+Q+Earnings", "Announces+Positive+Pre-Clinical+Results",
                "to+acquire+for+million$",
                "Secures+Groundbreaking+Deal", "Reports+%+Increase+in+Q+Net+income",
                "Announces+positive+initial+phase",
                "Announces+succesful+phase", "nasdaq Rally Continues", "to buy for $ targeted push",
                "(NASDAQ: skyrockets",
                "Closes Business Combination with", "stock more than doubles after deal to sell its",
                "succeeds in pivotal study", "Drug Succeeds in Trial",
                "Announce Its New Generative AI Platform and Technology Partner"]
    print(f"starting process {extension}")

    get_company_procedure(searches[arg])
    get_company_procedure(searches[arg + 1])
    #ADD 4 more searches
    print("Done with process")


# TODO when defining embed texts replace by code all company names to "oogaboogatralala"
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
    sorted_df = df.sort_values(by="dist", ascending=False)
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


#['AAPL', 'AIZ', 'FTDR', 'LUV', 'FSLY', 'NOVA', 'ZS', 'LYV', 'RDDT', 'PCTY', 'ITCI', 'RIVN', 'OXY', 'NKLA', 'CZR', 'GPRO', 'DIS', 'UL']



