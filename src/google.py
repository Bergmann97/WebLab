import json
from io import TextIOWrapper
from firebasehelper import checkDocExist, writeIntoDB

from googleapiclient.discovery import build, Resource
from utils import generateDocID, giveDebugLog, utilizeHTML

from utils import ContentType


f: TextIOWrapper = open('google-credentials.json')
credentials: dict = json.load(f)


def run_search_example():
    '''example search for transscripts of interviews with Joe Biden'''
    result: dict = google_search(
        None,
        'Joe Biden interview transcript',
        credentials['api_key'],
        credentials['google_cs_id'],
        start=1,
        exactTerms='transcript',
        sort=None,
        siteSearch='',
        siteSearchFilter="i",
        hq='',
    )

    print(result)

    with open('tmp/testGCSresult.json', 'w') as file:
        json.dump(result, file)


def run_utilize_example():
    '''tests the utilization of the returned dict from google search'''
    f = open('tmp/testGCSresult.json')
    result = json.load(f)

    utilize_search_result(None, result, {
        'id': 1,
        'labelName': 'Joe Biden',
        'lastName': 'Biden',
    }, 'interview')


def google_search(app, search_term: str, api_key: str, cse_id: str, **kwargs) -> dict:
    '''search for a given term '''
    giveDebugLog(app, f'Crawling {search_term}')
    service: Resource = build('customsearch', 'v1', developerKey=api_key)
    return service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()


def utilize_search_result(app, search_result: dict, politician: dict, content_type: str):
    '''
    turns the google search result to account. Checks if each document is new and saves it or skips it if it exists.
    '''
    COLLECTION: str = 'webpages'

    giveDebugLog(app, 'Utilizing the retrieved information\n')

    total_pages: int = 0  # counts the number of URLs that are newly added to DB

    if search_result.get('items') is not None:
        for item in search_result['items']:  # TODO: remove [:1] when finished
            try:
                url: str = item['link']
                webpage_id: str = generateDocID(url)

                # check uniqueness of webpage in db
                if not checkDocExist(COLLECTION, webpage_id):
                    content_type_value: int = eval(f'ContentType.{content_type.upper()}.value')

                    # parse the document at given url to get title and the content
                    result, title, text = utilizeHTML(app, url)

                    # check if utilization was successfull
                    if result:
                        # create db document
                        webpage: dict = {
                            'webpage_id': webpage_id,
                            'url': url,
                            'domain': item['displayLink'],
                            'content_type': content_type_value,
                            'title': title,
                            'politician': politician,
                            'text': text,
                        }

                        writeIntoDB(COLLECTION, webpage, webpage_id)
                        giveDebugLog(app, f'++ Saved: {title} ++')
                        giveDebugLog(app, f'++ {url} ++\n')
                        total_pages += 1
                else:
                    giveDebugLog(app, f'-- URL: {url} --')
                    giveDebugLog(app, f'-- URL already exists --\n')
            except Exception as e:
                giveDebugLog(app, f'! Doc Skipped due to error: {e} !\n')
                # raise Exception(f'An Error Occured: {e}')
        giveDebugLog(app, '------------------------------')
        giveDebugLog(app, f'## Saved {str(total_pages)} URLs ##\n')
    else:
        giveDebugLog(app, '! No Result !\n')


run_utilize_example()
