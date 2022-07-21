import re
from typing import Tuple
import requests

from enum import Enum
from bs4 import BeautifulSoup, ResultSet, Tag
from requests import Response


# Enum that gives the different content types
class ContentType(Enum):
    INTERVIEW = 1
    SPEECH = 2
    REMARK = 3
    TWEETS = 4


def giveDebugLog(app, msg: str):
    '''if app is given, prints an app debug message, else an basic python output'''
    if app:
        app.logger.debug(msg)
    else:
        print(msg)


def writeHTMLLog(log: str):
    finalStr = f'<p>{log}</p>'
    # write html to display the created elements
    with open('templates/test.html', 'w') as file:
        file.write(finalStr)


def writeHTMLTable(header: list[str], table: list[list[str]], headline: str):
    '''
    creates an html table with a given headline based on a table with string
    content
    '''
    # TODO: find cell with urls and make them links
    # create arround element with headline
    finalStr = '<div id="log">\n'
    finalStr += '  <h4>' + headline + ':</h4>\n'

    # create html table
    tableStr = '<table>\n'

    # create top row
    tableStr += '  <tr>\n'
    for item in header:
        tableStr += '    <th>' + item + '</th>\n'
    tableStr += '  </tr>\n'

    # add rows
    for line in table:
        tableStr += '  <tr>\n'
        for item in line:
            if isinstance(item, list):
                tableStr += '<td><ul>'
                for i in item:
                    tableStr += '<li>' + i + '</li>'
                tableStr += '</ul></td>'
            else:
                tableStr += '    <td>' + item + '</td>\n'
        tableStr += '  </tr>\n'

    tableStr += '</table>'
    finalStr += tableStr

    finalStr += '</div>'

    # write html to display the created elements
    with open('templates/test.html', 'w') as file:
        file.write(finalStr)


def extract_domain(url) -> str:
    '''extracts the domain of a given url'''
    m: re.Match = re.search('https?://([A-Za-z_0-9.-]+).*', url)
    return m.group(1)


def generateDocID(url: str) -> str:
    '''generates the db id by removing http, www and all symbols from url'''
    doc_id: re.Match = re.search('https?://', url)
    doc_id: str = url.replace(doc_id.group(), '').replace('www', '')  # remove "https://" and "www"
    doc_id: str = ''.join(e for e in doc_id if e.isalnum())  # remove all symbols and special chars

    return doc_id


def utilizeHTML(app, url: str) -> Tuple[bool, str, list]:
    '''
    based on the given url the document gets requested and title and content of the document are separated from
    the HTML document. If the url is no HTML document, the utilization gets stopped
    '''

    # request the document of the given url
    try:
        page: Response = requests.get(url, timeout=30)
        # check if document is not HTML
        if 'text/html' not in page.headers['Content-Type']:
            return False, None, None

        soup: BeautifulSoup = BeautifulSoup(page.content, 'html.parser')  # parse HTML with BeautifulSoup

        # find the headline/title in document
        h1: Tag = soup.find('h1')
        if h1 is None:
            return False, None, None

        # TODO: found multiple h1's?

        title: str = ' '.join(h1.text.split())

        # find all paragraph elements in document (should have at least 8)
        p_elems: ResultSet = soup.find_all('p')  # ResultSet
        if p_elems is None or len(p_elems) <= 8:
            return False, None, None
        content: list[str] = [p.text for p in p_elems]

        return True, title, content
    except Exception as e:
        giveDebugLog(app, f'! Doc Skipped due to error: {e} !')
        return False, None, None
