from firebasehelper import getDBCollectionAsDict, getDocFromDB, removeFromDB
from firebasehelper import writeIntoDB
from retrievePoliticians import retrieveWikidata
from utils import giveDebugLog, writeHTMLLog, writeHTMLTable
import json


RETRIEVED_COLLECTION = 'retrieved'
APPROVED_COLLECTION = 'approved'


def onRetrieveClick(app):
    '''
    prototype function to retrieve information from a given webpage using
    Google Custom Search
    '''
    giveDebugLog(app, 'Retrieve Information from Webpage')

    finalStr: str = '<div id="log"><h4>Retrieving information from webpage ...</h4></div>'
    with open('templates/test.html', 'w') as file:
        file.write(finalStr)
    # TODO

    return 'Retrieve Information from Webpage'


def onRetrieveTwitterClick(app):
    '''prototype function to retrieve twitter posts usign the twitter API'''
    giveDebugLog(app, 'Retrieve Information from Twitter')

    finalStr: str = '<div id="log"><h4>Retrieving information from twitter ...</h4></div>'
    with open('templates/test.html', 'w') as file:
        file.write(finalStr)
    # TODO

    return 'Retrieve Information from Twitter'


def onApproveClick(app):
    '''
    prototype function to handle the onClick to approve a single information
    '''
    giveDebugLog(app, 'Approve Information')

    # TODO: change this --> only change value and update doc

    # id of document to approve
    id: str = '123'

    # write given document into approved collection
    old = getDocFromDB(RETRIEVED_COLLECTION, id)
    print(old)
    if old:
        writeIntoDB(APPROVED_COLLECTION, old, id)
        # remove document from retrieved collection
        removeFromDB(RETRIEVED_COLLECTION, id)

        finalStr: str = f'<div id="log"><h4>Information with ID: {id} was approved!</h4></div>'
    else:
        finalStr: str = f'<div id="log"><h4>There is no information with ID: {id}!</h4></div>'

    with open('templates/test.html', 'w') as file:
        file.write(finalStr)


def onListClick(app):
    '''
    the prototype function for handling the onClick for the Button to list all
    retrieved information
    '''
    docs: list[dict] = getDBCollectionAsDict(RETRIEVED_COLLECTION)

    # convert all dicts into lists and put them together to display
    table: list[list[dict]] = []
    for d in docs:
        table.append([str(d['date']), d['title'], d['text']])

    # create html table to add on page
    head: list[str] = ['date', 'title', 'text']
    writeHTMLTable(
        head,
        table,
        'All Retrieved Information'
    )

    giveDebugLog(app, 'List All')


def onListApprovedClick(app):
    '''
    the prototype function for handling the onClick for the Button to list the
    approved information
    '''
    docs: list[dict] = getDBCollectionAsDict(APPROVED_COLLECTION)

    # convert all dicts into lists and put them together to display
    table: list[list[str]] = []
    for d in docs:
        table.append([str(d['date']), d['title'], d['text']])

    # create html table to add on page
    head: list[str] = ['date', 'title', 'text']
    writeHTMLTable(
        head,
        table,
        'All Approved Information'
    )

    giveDebugLog(app, 'List approved')


def onWikidataRetrievalClick(app):
    error, retrievedData = retrieveWikidata(app, 'Q6279')

    if not error:
        head = ['property', 'value']
        lines = []

        for key in retrievedData.keys():
            line = [key, retrievedData[key]]
            lines.append(line)

        writeHTMLTable(head, lines, 'Wikidata of Joe Biden')
    else:
        writeHTMLLog(error)

    giveDebugLog(app, 'Retrieve all information from wikidata for Joe Biden')
