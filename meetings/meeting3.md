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
