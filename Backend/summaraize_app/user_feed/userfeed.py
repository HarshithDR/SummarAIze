from .db_operations.get_userinterests import *
from .db_operations.get_feeddetails import *

def accessuserfeed(userId):
    user_interests = get_userinterests(userId)
    print("here I am",user_interests)
    #lst_user_interests = user_interests.split(",")
    #get_feeddetails(lst_user_interests,userId)
    return {'userId': userId, 'message': 'Im still under build'}


