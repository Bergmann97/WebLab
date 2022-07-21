from SPARQLWrapper import SPARQLWrapper, JSON
import json


sparql = SPARQLWrapper('http://query.wikidata.org/sparql')

query = '''
PREFIX entity: <http://www.wikidata.org/entity/>
SELECT ?propUrl ?propLabel ?valUrl ?valLabel ?picture
WHERE {
    entity:Q6279 ?propUrl ?valUrl .
    ?property ?ref ?propUrl .
    ?property rdf:type wikibase:Property .
    ?property rdfs:label ?propLabel .
    ?valUrl rdfs:label ?valLabel
    FILTER (LANG(?valLabel) = 'en') .
    OPTIONAL{ ?valUrl wdt:P18 ?picture .}
    FILTER (lang(?propLabel) = 'en' )
}
ORDER BY ?propUrl ?valUrl
'''

sparql.setQuery(query)

sparql.setReturnFormat(JSON)
result = sparql.query().convert()

final_dict = {}

for hit in result['results']['bindings']:
    # print('---------------------------')
    # print(hit['propLabel'])
    # print(hit['valLabel'])
    # print('---------------------------')
    prop = hit['propLabel']['value']
    val = hit['valLabel']['value']
    if prop == 'given name':
        print(prop)
        print(val)
        print(hit)
    if prop not in final_dict.keys():
        final_dict[prop] = val
    else:
        existing_val = final_dict[prop]
        if isinstance(existing_val, list):
            existing_val.append(val)
            final_val = existing_val
        else:
            final_val = [existing_val, val]
        final_dict[prop] = final_val


print(final_dict)
with open('final_dict.json', 'w') as f:
    json.dump(final_dict, f, indent=4)
