import sqlite3

class Database():
    """A model of database for work with database"""
    def __init__(self, db_name):
        """make attribute for database file name"""
        self.db_name = db_name
    
    def query(self, query, *params, operation="commit"):
        """Connect to db and execute query"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if operation=="commit":
                try: 
                    cursor.execute(query, params)
                    conn.commit()
                except:
                    return "queryError"
                else:
                    return None
            elif operation=="fetchone":
                try: 
                    cursor.execute(query, params)
                    data = cursor.fetchone()
                except:
                    return "queryError"
                else:
                    return data
            elif operation=="fetchall":
                try: 
                    cursor.execute(query, params)
                    data = cursor.fetchall()
                except:
                    return "queryError"
                else:
                    return data
            else:
                return "No such operation exist"


