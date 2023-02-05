## Doorman - Meeting 2 (2/4)

## New Idea
* Have application scrape information from social media websites (Twitter, Instagram, Facebook, etc.) to obtain information and photos of close friends to auto generate for Doorman
    * From Danny, good for a reach goal so we don't underdeliver for overpromising

## Work
* Made AWS account and started discussing how to store all the information
    * Consensus: Use an S3 bucket (5 GB free) to store information and code.
    * Does not make sense to use DynamoDB since we are not fully leveraging the key-value database (may change if our implementation changes)
* Wrote `facial.py` based on the library found online for facial recognition, made the work fairly trivial. Can use the model in our results and write up
    * [face-recognition](https://pypi.org/project/face-recognition/)

## Other
* Waiting to hear back from Mars on refinements and recommendations for project to fix scope and/or make improvements to it