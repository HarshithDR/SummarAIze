from db_setup import *

def set_userinterest(useremail,interests):
    mydb = setup_db()
    cursor = mydb.cursor()
    sql = "INSERT INTO interests (useremailid, interests) VALUES (%s, %s, %s)"
    val = (useremail, interests)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")