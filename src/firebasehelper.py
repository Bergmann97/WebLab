import json
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils import extract_domain, generateDocID


'''
load Firebase data
- read credentials
- initialize app
- get the db to write and read
'''
f = open('informationextraction-service-account.json')
credential = json.load(f)
cred = credentials.Certificate(credential)
firebase_admin.initialize_app(cred)
db = firestore.client()


def getDBCollectionAsDict(collection: str) -> list[str]:
    '''returns list of dicts from given collection'''
    coll = db.collection(collection)
    p_docs = coll.stream()
    return [d.to_dict() for d in p_docs]


def writeIntoDB(collection: str, data: dict, id: str):
    '''writes the given dict into collection with automatic or given id'''
    coll = db.collection(collection)
    if not id:
        coll.add(data)
    else:
        coll.document(id).set(data)


def removeFromDB(collection: str, id: str):
    '''removes the document with given id from given collection'''
    coll = db.collection(collection)
    coll.document(id).delete()


def getDocFromDB(collection: str, id: str):
    '''returns the dict of the document with given id from given collection'''
    coll = db.collection(collection)
    return coll.document(id).get().to_dict()


def getDocFromDBwithAttr(collection: str, attr: str, value: str) -> list[dict]:
    '''return the documents of a specified collection where the given attribute satisifies the given value'''
    coll = db.collection(collection)
    s_docs: list = coll.where(attr, '==', value).stream()
    docs: list[dict] = [d.to_dict() for d in s_docs]

    return docs


def saveTemplate(root_url: str, pagination_slug: str, links_parser: str):
    '''saves the template into the db and generates id and domain'''
    domain: str = extract_domain(root_url)
    template_id: str = generateDocID(root_url)

    data: dict = {
        'id': template_id,
        'root_url': root_url,
        'domain': domain,
        'pagination_slug': pagination_slug,
        'links_parser': links_parser,
    }

    db.collection('templates').document(template_id).set(data)  # write final dict into db


def test_templateSave():
    saveTemplate(
        'https://www.rev.com/blog/transcript-category/donald-trump-transcripts/',
        'page/{page}/',
        'soup.find("div", attrs={"class":"fl-post-grid"}).findAll("a", href=True)'
    )


def checkDocExist(collection: str, id: str):
    '''checks if a document with given id already exists in collection'''
    doc = db.collection(collection).document(id).get()  # Documentsnapshot
    return doc.exists
