<<<<<<< HEAD
## Meeting 3: Update project scope

### Do we want to use local storage or AWS

USE RDS
https://www.rojotek.com/blog/2017/08/07/accessing-rds-from-aws-lambda/
https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html



## Determination: Use relational database

### What are we storing?

+ Name
+ Images (feature vector encoding)
+ Birthday
+ Social Media URLS <REACH>
+ Relation to you
This could be a value of a set of possible values, maybe {friend, family, etc.}
+ When were they last here?
+ Lock the door



## Architecture
+ RDS (database)
+ AWS Alexa SDK (dialogue and NLP)
+ Lambda (Alexa SDK triggers a lambda which can access the RDS)






Problem (describe how it evolved as)
Zach
Refined user story for your usecase, how it has evolved and why
MAX
Changes in product feature set, how it was scoped down (or up perhaps)
Ruhaan
Estimate on what reach goals might be achieved and how it changed.
Miguel
More specific plan on tools you plan to use
Jason
Revised diagram the system architecture, Show prior version and new version
Sophia
What have you built so far, what APIs did you tinker with, what did you learn or find interesting
Jason
DEMO (or show and tell)
Max
Key milestones you plan to meet moving forward
Danny
Conclusion
Anything else you want to share with us!
=======
2/18 
How “production ready” do we want our product? 
  Scalability concerns 
Does Alexa abstract away too much from us? 
IntentSchema / SampleUtterances  
Where are we storing the “face database” and the “information database”?
  Are these even different? 
Clarifying scope of the project more clearly 
  How much do we want Alexa to do for us?
  What tools are we using?
  What do we want Alexa to do? 
    Who is at the door?
    How many people are at the door?
    Information about the person (people?) at the door? 
    Add this face to the database
    What information do we want it to know about?
    Confirmation conversation
    Open/Lock the door
    Communicate with the person outside directly (Reach) 



>>>>>>> 7ebfbe887255c2c79356cd249113575e4e7545d8
