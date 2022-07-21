# Meeting 2

## Questions for database

* What should be stored in firebase for:
  * Politicians $\rightarrow$ example Kamila Harris $\rightarrow$ all information from wikidata?
    * **!!retrieve all information from wikidata available but only for one specific person!!**
    * NINL ist full name?
    * firstname
    * lastname
    * labelName?
    * images
    * twitter
      * needs a bit more for us: twitter username property from wikidata to get twitter usernames
  * Websites/corpus $\rightarrow$ name texts
    * **! only texts !**
    * politician_id
    * what means validity? $\rightarrow$ approved or use extra collection
    * text **are the probably p, etc., elements?**
    * all other points clear
  * Tweets
    * conv_id
    * create date
    * extraction date $\rightarrow$ **date where I retrieved it**
    * language
    * entities $\rightarrow$ **complete explanation $\rightarrow$ we need later**
    * concerning politician
    * politician name
    * message
    * tweet_id
    * twitter_id $\rightarrow$ **id of twitter user**
      * maybe also twitter username
    * issues

## Persons to focus on now

[Link to retrieve help](https://stackoverflow.com/questions/47472274/how-to-get-information-of-a-specific-wikidata-id-using-sparql-query)

* Joe Biden
* Kamala Harris
* Alexandria Ocasio-Cortez
* Bernie Sanders
* Ted Cruz
* Barack Obama
* Jimmy Carter
* Madeleine Albright
* Hillary Clinton
* Elizabeth Warren

## Other questions

[utils.py | utilizeHTML() | title](https://colab.research.google.com/drive/1h6stbzZAet8WUtR5iHuwsMdT45ghvXqf#scrollTo=hlwBY82Nj8Fu&line=64&uniqifier=1)

$\hookrightarrow$ explained: remove blank whitespaces
