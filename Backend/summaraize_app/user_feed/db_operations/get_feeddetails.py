from .db_setup import *

def get_feeddetails(interests,userId):
    try:
        db = setup_db()
        cursor = db.cursor()
        # Constructing the placeholders for the IN clause
        placeholders = ', '.join(['%s' for _ in range(len(interests))])
        sql = f"SELECT * FROM newsfeedinfo WHERE domain IN ({placeholders}) LIMIT 25;"
        cursor.execute(sql, (interests))
        return {"user" : userId, "newsFeed" : cursor.fetchall()}
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}