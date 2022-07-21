# Structure Plan

This explains when what part should be finished and what exactly should be finished

## **1. Firebase Setup**

### **1.1 Collections for entities**

* [X] politicians
* [X] templates (*src_templates*)
* [X] tweets
* [X] webpages (*corpus*)

### **1.2 Specify entity attributes**

* [ ] politicians
* [ ] templates
* [ ] tweets
* [ ] webpages

### **1.3 make CRUD possible**

for each collection it should be possible to write, read, update and delete a document

**Note:** *tasks that are in progress are marked with $\leftarrow$*

* [ ] **Politicians**
  * [ ] create
  * [ ] read
  * [ ] update
  * [ ] delete
* [ ] **templates**
  * [ ] create
  * [ ] read
  * [ ] update
  * [ ] delete
* [ ] **tweets**
  * [ ] create
  * [ ] read
  * [ ] update
  * [ ] delete
* [ ] **webpages**
  * [ ] create
  * [ ] read
  * [ ] update
  * [ ] delete

## **2. Twitter Retrieval**

make it possible to retrieve posts from Twitter

* [X] make Twitter API usable
* [ ] create function to retrieve tweets by specifications
* [ ] select the needed information and create dict
* [ ] check for uinqueness

## **3. Webpage Retrieval**

make it possible to retrieve content from webpages

* [X] make google custom search executable
* [ ] aplly templates for search
* [ ] create function for adaptive search with specifications
* [ ] make index page template for better representation
* [X] check webpage for uniqueness
* [X] search for content in page
