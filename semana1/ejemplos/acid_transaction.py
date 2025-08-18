try:
    conn.begin()
    cursor.execute("INSERT INTO accounts VALUES (1, 1000)")
    cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE id=1")
    cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE id=2")
    conn.commit()
except:
    conn.rollback()
