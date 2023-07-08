import sqlite3
from popup import Popup
from datetime import datetime

class SQLiteDB():
    
    def connect_db(self):
        today = datetime.today().strftime("%m-%d-%Y") 
        db_filename = "data/database_" + today
        self.conn = sqlite3.connect(db_filename)
        self.cursor = self.conn.cursor()
    
    def close_db(self):
        self.conn.commit()
        self.conn.close()
        
        
    def initialize(self):
        self.connect_db()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS team (
                name TEXT PRIMARY KEY,
                location TEXT,
                description Text
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS agenda (
                category TEXT,
                task TEXT PRIMARY KEY,
                summary TEXT,
                status INTEGER
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS next_day (
                category TEXT,
                task TEXT PRIMARY KEY
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                time INTEGER PRIMARY KEY,
                desc TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS issues (
                id INTEGER PRIMARY KEY,
                description TEXT
            )
        ''')        
        self.initial_team()
        self.close_db()
    
        
    """ TEAM QUERIES
        - Initalize
    """
    def initial_team(self):
        # Members Table
        data = [
            ('Thanh', 'location1', None),
            ('Person1', 'location1', None),
            ('Person2', 'location1', None),
            ('Person3', 'location1', None),
            ('Person4', 'location1', None),
            ('Person5', 'location1', None),
            ('Person6', 'location1', None),
            ('Person7', 'location1', None),
            ('Person8', 'location1', None),
            ('Person9', 'location1', None),
            ('Person10', 'location1', None),
            ('Person11', 'location1', None),
            ('Person12', 'location1', None),
            ('Person13', 'location1', None),

        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO team (name, location, description) "
            "VALUES (?, ?, ?)", data
        )
    
    def get_team(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM team
            ORDER BY name
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_at_location1(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM team
            WHERE location = 'location1'
            ORDER BY name
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_not_at_location1(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM team
            WHERE location != 'location1'
            ORDER BY name
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data

    def get_member_info(self, name):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM team
            WHERE name = ?
        ''', (name,) )
        data = self.cursor.fetchall()
        self.close_db()
        return data
        
    def update_member(self, name, location, desc):    
        # Update Info
        self.connect_db()
        self.cursor.execute('''
            UPDATE team
            SET location = ?,
            description = ?
            WHERE name = ?
        ''', (location, desc, name ))
        self.close_db()
        Popup().show_popup()

    def add_member(self, name, location, desc):
        self.connect_db()
        self.cursor.execute('''
            INSERT OR IGNORE INTO team (name, location, description) 
            VALUES (?, ?, ?) 
        ''', (name, location, desc))
        self.close_db()
        Popup().show_popup()

    def delete_member(self, name):
        self.connect_db()
        self.cursor.execute('''
            DELETE FROM team
            WHERE name = ? 
       ''', (name,))
        self.close_db()
        Popup().show_popup()
    
        
    """ Agenda
        - Category TEXT
        - Task TEXT PRIMARY KEY
        - Summary TEXT
        - Status INTEGER
    """
    def get_agenda(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM agenda
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_cat1_agenda(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM agenda
            WHERE category = 'CAT1'
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_cat2_agenda(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM agenda
            WHERE category = 'CAT2'
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_cat3_agenda(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM agenda
            WHERE category = 'CAT3'
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_task_info(self, task):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM agenda
            WHERE task = ?
        ''', (task,) )
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def add_agenda(self, category, task, summary):
        self.connect_db()
        self.cursor.execute('''
            INSERT OR IGNORE INTO agenda (category, task, summary, status) 
            VALUES (?, ?, ?, ?) 
        ''', (category, task, "Not yet set", 0))
        self.close_db()
        Popup().show_popup()
    
    def update_agenda(self, category, task, summary, status):
        self.connect_db()
        self.cursor.execute('''
            UPDATE agenda
            SET category = ?,
                summary = ?,
                status = ?
            WHERE task = ? 
        ''', (category, summary, status, task))
        self.close_db()
        Popup().show_popup()
    
    def delete_agenda(self, task):
        self.connect_db()
        self.cursor.execute('''
            DELETE FROM agenda 
            WHERE task = ?
        ''', (task,))
        self.close_db()
        Popup().show_popup()
        
    def update_status(self, task, status):
        self.connect_db()
        self.cursor.execute('''
            UPDATE agenda 
            SET status = ? 
            WHERE task = ? 
        ''', (status, task))
        self.close_db()
        Popup().show_popup() 
    
     # -- Next Day Agenda -- #
    def get_nextday(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT category, task FROM next_day
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data

    def get_next_cat1_agenda(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM next_day
            WHERE category = 'CAT1'
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_next_cat2_agenda(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM next_day
            WHERE category = 'CAT2'
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def get_next_cat3_agenda(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM next_day
            WHERE category = 'CAT3'
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def add_nextday(self, category, task):
        self.connect_db()
        self.cursor.execute('''
            INSERT OR IGNORE INTO next_day (category, task) 
            VALUES (?, ?) 
        ''', (category, task))
        self.close_db()
        Popup().show_popup()

    def delete_nextday(self, task):
        self.connect_db()
        self.cursor.execute('''
            DELETE FROM next_day 
            WHERE task = ?
        ''', (task,))
        self.close_db()
        Popup().show_popup()
        
    def update_nextday(self, category, task):
        self.connect_db()
        self.cursor.execute('''
            UPDATE next_day
            SET category = ?
            WHERE task = ? 
        ''', (category, task))
        self.close_db()
        Popup().show_popup()
    
    def get_nextday_info(self, task):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM next_day
            WHERE task = ?
        ''', (task,) )
        data = self.cursor.fetchall()
        self.close_db()
        return data
        
    # -- EVENTS -- #
    def get_events(self):
        self.connect_db()
        self.cursor.execute(
            "SELECT * FROM events"
        )
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def add_event(self, time, desc):
        self.connect_db()
        self.cursor.execute(
            "INSERT OR IGNORE INTO events (time, desc) "
            "VALUES (?, ?)", 
            (time, desc)
        )
        self.close_db()
        Popup().show_popup()
        
    def delete_event(self, time):
        self.connect_db()
        self.cursor.execute('''
            DELETE FROM events 
            WHERE time = ?
        ''', (time,))
        self.close_db()
        Popup().show_popup()
        
    def update_event(self, time, desc):
        self.connect_db()
        self.cursor.execute('''
            UPDATE events
            SET desc = ? 
            WHERE time = ?
        ''', (desc, time))
        self.close_db()
        Popup().show_popup()
        
    # -- Issues -- #
    def get_issues(self):
        self.connect_db()
        self.cursor.execute('''
            SELECT * FROM issues
            ORDER BY id
        ''')
        data = self.cursor.fetchall()
        self.close_db()
        return data
    
    def add_issue(self, issue_num, issue_desc):
        self.connect_db()
        self.cursor.execute('''
            INSERT OR IGNORE INTO issues (id, description)
            VALUES (?, ?)
        ''', (issue_num, issue_desc))
        self.close_db()
        Popup().show_popup()
        
    def delete_issue(self, id):
        self.connect_db()
        self.cursor.execute('''
            DELETE FROM issues 
            WHERE id = ?
        ''', (id,))
        self.close_db()
        Popup().show_popup()