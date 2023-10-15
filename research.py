import json
import requests

def lambda_handler(event, context):
    try:
        # CALL HOUSE STOCK WATCHER API AND FORMAT DATA
        stock_watcher_api_data = call_house_stock_watcher_api()
        list_of_stocks = format_stock_watcher_data_into_list(stock_watcher_api_data)
        
        # CALL REDDIT STOCK API AND FORMAT DATA
        reddit_stock_api_data = call_reddit_stock_api()
        formatted_reddit_stock_data = format_reddit_stock_data_into_map(reddit_stock_api_data)
        
        # GET THE TICKER SYMBOLS THAT ARE IN BOTH API RESPONSES
        stocks_in_both_datasets = [ticker for ticker in list_of_stocks if ticker in formatted_reddit_stock_data.keys()]
        
        # FILTER REDDIT MAP BASED ON COMMON STOCKS
        filtered_reddit_stock_data = {ticker: sentiment for ticker, sentiment in formatted_reddit_stock_data.items() if ticker in stocks_in_both_datasets}

        return {
            'statusCode': 200,
            'body': json.dumps(filtered_reddit_stock_data)
        }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error: ' + str(e))
        }


def call_house_stock_watcher_api():
    response = requests.get('https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json')
    return response.json()


def format_stock_watcher_data_into_list(stock_watcher_api_data):
    stock_list = []
    for datapoint in stock_watcher_api_data:
        ticker = datapoint['ticker']
        stock_list.append(ticker)
    return stock_list


def call_reddit_stock_api():
    response = requests.get('https://tradestie.com/api/v1/apps/reddit')
    return response.json()


def format_reddit_stock_data_into_map(data):
    formatted_data = {}
    for datapoint in data:
        ticker = datapoint['ticker']
        sentiment = datapoint['sentiment']
        formatted_data[ticker] = sentiment
    return formatted_data
