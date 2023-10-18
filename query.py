import json
import re
import requests

def lambda_handler(event, context):
    try:
        
        # CREATE API QUERY PARAMETERS FROM REQUEST
        params = create_query_params(event)
        
        # CALL THE WIKIPEDIA API AND GET SEARCH RESULTS
        results = get_search_results_from_wiki_api(params)
        
        # PARSE THE RESULTS FOR THE INFO WE NEED
        number_of_hits = len(results)
        first_result = get_and_clean_first_result(results)
        
        # PREPARE THE API RESPONSE WITH THE DATA
        api_response = create_api_response(number_of_hits, first_result)

        return api_response
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error: ' + str(e))
        }


def create_query_params(event):
    search_query = json.loads(event['body'])['query']
    return {
        'action': 'query',
        'list': 'search',
        'srsearch': search_query,
        'format': 'json'
    }


def get_search_results_from_wiki_api(params):
    response = requests.get('https://en.wikipedia.org/w/api.php', params=params)
    data = response.json()
    return data['query']['search']


def get_and_clean_first_result(results):
    if (len(results) == 0):
        return "No Results Found!"
    
    # GET THE FIRST SNIPPET
    first_result_snippet = results[0]['snippet']

    # CLEAN THE FIRST RESULT AND REMOVE THE HTML TAGS
    first_result_snippet_cleaned = remove_html_tags(first_result_snippet)
    
    return first_result_snippet_cleaned


def remove_html_tags(result_snippet):
    html_tags_pattern = re.compile(r'<.*?>')
    clean_result_snippet = re.sub(html_tags_pattern, '', result_snippet)
    
    return clean_result_snippet


def create_api_response(number_of_hits, first_result):
    response_body = {
        "numberOfHits": number_of_hits,
        "firstHit": first_result
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }
