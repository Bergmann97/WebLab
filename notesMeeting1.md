# Kickoff Meeting

## Questions

1) just focusing on named persons or can I select the focused people?

2) **Flask Server**
    * locally or should it run on Google Cloud Platform?
    * mentioned example code?

3) JSON-Files are stored in **Firebase**
     * Authentication ?
        * Login-Screen?

4) **User-Interface**:
    * Management Tasks:
      * Create/Add targeted website (with parsing template)
        * Needs form etc.
        * Needs check of template is ok?
          * how should these templates work?
      * Receive/Retrieve new articles etc.
        * Form with dates or just a button to start?
        * after retrieving a list with found results?
        * also mentioned periodic requests for Twitter $\rightarrow$ should be automated?
      * Manage? $\rightarrow$ Delete retrieved articles
        * also manual adding of content?

## Notes

1) we are just focusing on the 10 listed person

2) should of course run locally but also on Google Cloud Platform
Course/Hints: TBD

3) we are just saving text documents. The JSON-Files will include all tweets of a month of a single person $\rightarrow$ no authentication needed

4) concerning manage: everything should be retrieved and then we need to manage which tweets/docs are correct and can be approved $\rightarrow$ list separately
First make manual receiving possible after that having a look at automated receiving

## Additional Notes

email concerning firebase and google credentials

### Helpful Links (from Meeting)

[Deploy on Google Cloud Platform](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)

[Example page from rev.com](https://www.rev.com/blog/transcripts/donald-trump-phoenix-arizona-rally-speech-transcript-july-24)

[person_IDs](https://www.wikidata.org/wiki/Q6279) $\rightarrow$ crawl ID automatically?
