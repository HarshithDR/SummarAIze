from ...db_setup import *

def set_userinterest(useremail,interests):
    print(useremail,interests)
    try:
        db = setup_db()
        cursor = db.cursor()
        sql = "INSERT INTO interests (useremailid, interests) VALUES (%s, %s)"
        val = (useremail, interests)
        cursor.execute(sql, val)
        # Retrieve the last inserted ID
        last_insert_id = cursor.lastrowid
        db.commit()
        db.close()
        print(cursor.rowcount, "record inserted.")
        return {"success" : True, "record_id" : last_insert_id}
    except Exception as e:
        return {"success" : False, "error_message" : str(e)}