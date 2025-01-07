import sqlite3

def add_bug_to_db(title, description, priority):
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bugs (title, description, priority, status)
        VALUES (?, ?, ?, ?)
    ''', (title, description, priority, 'Open'))
    conn.commit()
    conn.close()

def get_all_bugs_from_db():
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, priority, status FROM bugs')
    bugs = cursor.fetchall()
    conn.close()
    return bugs

def update_bug_status_in_db(bug_id, new_status):
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE bugs SET status = ? WHERE id = ?
    ''', (new_status, bug_id))
    conn.commit()
    conn.close()

def delete_bug_from_db(bug_id):
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM bugs WHERE id = ?
    ''', (bug_id,))
    conn.commit()
    conn.close()

def get_filtered_bugs(status=None, priority=None):
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    query = "SELECT id, title, priority, status FROM bugs WHERE 1=1"
    params = []
    if status and status != "All":
        query += " AND status = ?"
        params.append(status)
    if priority and priority != "All":
        query += " AND priority = ?"
        params.append(priority)

    cursor.execute(query, params)
    bugs = cursor.fetchall()
    conn.close()
    return bugs
