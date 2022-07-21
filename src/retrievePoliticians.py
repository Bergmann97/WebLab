import json
import datetime

from typing import Tuple, Union
from firebasehelper import writeIntoDB
from SPARQLWrapper import SPARQLWrapper, JSON


COLLECTION: str = 'politicians'


def getValueQuery(id: str, prop: str):
    return f'''
        SELECT ?vLabel
        WHERE
        {{
        wd:{id} p:{prop} ?statement1.
        ?statement1 ps:{prop} ?v.
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        }}
    '''


def retrieveWikidata(app, id: str) -> Tuple[str, dict]:
    '''
    retrieves all available information of an entity based on the given id from wikidata and writes them into the
    firebase id.
    It also adds as attribute the retrievalDate
    '''
    sparql: SPARQLWrapper = SPARQLWrapper('http://query.wikidata.org/sparql')

    propQuery: str = f'''
        SELECT ?p ?propLabel
        WHERE
        {{
        wd:{id} ?p ?v .
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        ?prop wikibase:directClaim ?p
        }}
    '''

    # the query to use for retrieving all entities from wikidata
    query: str = f'''
        SELECT ?p ?propLabel ?v ?vLabel
        WHERE {{
        wd:{id} ?p ?v .
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        ?prop wikibase:directClaim ?p
        }}
    '''

    # setting the query for receiving all property ids
    sparql.setQuery(propQuery)
    sparql.setReturnFormat(JSON)
    try:
        propResult: dict = sparql.query().convert()
    except Exception as e:
        return e, None

    final_dict: dict = {}  # will include the final data from the result dict
    final_dict['id'] = id  # set the given id into the dict

    prop_ids: list = []  # saves all property ids
    prop_labels = []  # saves the labels of the properties

    # iterate thru properties
    for hit in propResult['results']['bindings']:
        p: str = hit['p']['value'].split('/')[-1]
        label: str = hit['propLabel']['value']
        prop_ids.append(p)
        prop_labels.append(label)

    for p in prop_ids:
        label = prop_labels[prop_ids.index(p)]
        sparql: SPARQLWrapper = SPARQLWrapper('http://query.wikidata.org/sparql')
        sparql.setQuery(getValueQuery(id, p))
        sparql.setReturnFormat(JSON)
        try:
            result: dict = sparql.query().convert()
        except Exception as e:
            return e, None

        values = []

        # iterate thru all retrieved values and add them to list
        for hit in result['results']['bindings']:
            val: str = hit['vLabel']['value']      # the value, like "Joe"
            values.append(val)

        # check if the property already exists, if so add value to existing value, otherwise create property
        if label not in final_dict.keys():
            if len(values) == 1:
                final_dict[label] = values[0]
            else:
                final_dict[label] = values
        else:
            existing_val: Union[str, list] = final_dict[label]
            # convert properties existing value to list, if not happend yet
            if isinstance(existing_val, list):
                existing_val.extend(values)
                final_val = existing_val
            else:
                final_val: list = values.append(existing_val)
            final_dict[label] = final_val

    # save the date and time of this retrieving process
    final_dict['retrievalDate'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    # write the data into firebase db
    writeIntoDB(COLLECTION, final_dict, id)

    # with open('final_dict.json', 'w') as f:
    #     f.write(json.dumps(final_dict, indent=4))

    return None, final_dict


# retrieveWikidata(None, 'Q6279')
