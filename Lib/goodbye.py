import praw
from prawcore import ResponseException


def get_authentication_details():
    user_details = []

    username = input("Please enter your reddit username: ")
    user_details.append(username)
    password = input("Please enter the password for the above reddit account: ")
    user_details.append(password)
    client_id = input("Please enter your client id: ")
    user_details.append(client_id)
    client_secret = input("Please enter your secret key: ")
    user_details.append(client_secret)
    return user_details


def checkpoint():
    return input("Modifying your post history is final, please type yes to confirm you wish to proceed. ")


if __name__ == "__main__":
    my_statement = "This comment has been edited prior to deletion to protest Reddit's outrageous API changes that " \
                 "are effective 7/1/2023 and I encourage users who wish to delete their accounts " \
                 "do the same to prevent Reddit from further monetizing the content and data you produced that they " \
                 "rely on. \n \n " \
                 "Fuck u/spez, fuck Reddit, and fuck corporate greed."

    while True:
        try:
            details = get_authentication_details()
            reddit = praw.Reddit(
                client_id=details[2],
                client_secret=details[3],
                password=details[1],
                user_agent="Goodbye Reddit",
                username=details[0]
            )

            if details[0] == reddit.user.me():
                print("Log in successful")
                break
        except ResponseException:
            print("Invalid credentials\n"
                  "Please check you log in details and try again")

    sure = False
    while not sure:
        if checkpoint() == "yes":
            sure = True
    reddit.validate_on_submit = True
    user = reddit.redditor(details[0])

    for comment in user.comments.new(limit=None):
        comment.edit(my_statement)
    for submission in user.submissions.new(limit=None):
        submission.delete()
    
    print("Account scrubbing complete, remember to delete your Reddit account")
