# Goodbye Reddit
This is a simple script to delete all posts and edit all your comments in protest of the upcoming API changes to reddit. In it's present state you must supply your own client id and secret key to access the Reddit API which can be done here: https://www.reddit.com/wiki/api.

## Functions
This script will go through all a users comments and replace them with a custom message to prevent Reddit from being able to use the contents of the comment for future monetization or data to train large language models. This script will then delete all submissions for the same purpose. This is the nuclear option to scrub your account before deletion and since the other recent API change is irreversible so there is a checkpoint in the code that the user must acknowledge to proceed to scrubbing.

## Todo
If I have the time before the API changes go into effect I do plan on cleaning up the code a bit and modifying it to use my API token, but I have a busy week or so coming up and did not want to let perfect be the enemey of good in a case like this where time is of the essence.


