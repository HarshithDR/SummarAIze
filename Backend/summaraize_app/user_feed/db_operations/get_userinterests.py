from .db_setup import *

def get_userinterests(userid):
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "SELECT interests FROM summaraize.interests where id = %s"
        cursor.execute(sql, (userid))
        return cursor.fetchall()
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}