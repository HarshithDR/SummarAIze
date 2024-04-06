from .db_operations.get_userinterests import *
from .db_operations.get_feeddetails import *

def accessuserfeed(userId):
    user_interests = get_userinterests(userId)
    lst_user_interests = user_interests.split(",")
    return get_feeddetails(lst_user_interests,userId)


