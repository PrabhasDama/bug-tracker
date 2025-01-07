import tkinter as tk
from tkinter import ttk
from database import add_bug_to_db, get_all_bugs_from_db, update_bug_status_in_db, delete_bug_from_db, get_filtered_bugs

def main_window():
    root = tk.Tk()
    root.title("Bug Tracker")
    root.geometry("800x500")

    # Frames for layout
    top_frame = tk.Frame(root)
    top_frame.pack(pady=10)

    bottom_frame = tk.Frame(root)
    bottom_frame.pack(fill="both", expand=True)

    # Bug list
    bug_list = ttk.Treeview(bottom_frame, columns=('ID', 'Title', 'Priority', 'Status'), show='headings')
    bug_list.heading('ID', text='ID')
    bug_list.heading('Title', text='Title')
    bug_list.heading('Priority', text='Priority')
    bug_list.heading('Status', text='Status')
    bug_list.pack(fill="both", expand=True)

    # Populate bugs
    def refresh_bugs():
        for row in bug_list.get_children():
            bug_list.delete(row)
        bugs = get_all_bugs_from_db()
        for bug in bugs:
            bug_list.insert('', 'end', values=bug)

    refresh_bugs()

    # Add new bug
    def add_bug():
        title = title_entry.get()
        description = desc_entry.get()
        priority = priority_entry.get()
        if title and priority:
            add_bug_to_db(title, description, priority)
            refresh_bugs()

    # Update status
    def update_status():
        selected_item = bug_list.selection()
        if selected_item:
            bug_id = bug_list.item(selected_item[0])['values'][0]
            new_status = status_entry.get()
            if new_status:
                update_bug_status_in_db(bug_id, new_status)
                refresh_bugs()

    # Delete bug
    def delete_bug():
        selected_item = bug_list.selection()
        if selected_item:
            bug_id = bug_list.item(selected_item[0])['values'][0]
            delete_bug_from_db(bug_id)
            refresh_bugs()

    # Filter bugs
    def filter_bugs():
        status = status_filter_var.get()
        priority = priority_filter_var.get()
        filtered_bugs = get_filtered_bugs(status, priority)
        for row in bug_list.get_children():
            bug_list.delete(row)
        for bug in filtered_bugs:
            bug_list.insert('', 'end', values=bug)

    # Top frame widgets
    tk.Label(top_frame, text="Title:").grid(row=0, column=0)
    title_entry = tk.Entry(top_frame)
    title_entry.grid(row=0, column=1)

    tk.Label(top_frame, text="Description:").grid(row=1, column=0)
    desc_entry = tk.Entry(top_frame)
    desc_entry.grid(row=1, column=1)

    tk.Label(top_frame, text="Priority:").grid(row=2, column=0)
    priority_entry = ttk.Combobox(top_frame, values=["Low", "Medium", "High"])
    priority_entry.grid(row=2, column=1)

    tk.Button(top_frame, text="Add Bug", command=add_bug).grid(row=3, column=0, columnspan=2, pady=5)

    tk.Label(top_frame, text="New Status:").grid(row=4, column=0)
    status_entry = ttk.Combobox(top_frame, values=["Open", "In Progress", "Closed"])
    status_entry.grid(row=4, column=1)

    tk.Button(top_frame, text="Update Status", command=update_status).grid(row=5, column=0, columnspan=2, pady=5)
    tk.Button(top_frame, text="Delete Bug", command=delete_bug).grid(row=6, column=0, columnspan=2, pady=5)

    # Filters
    tk.Label(top_frame, text="Filter by Status:").grid(row=7, column=0)
    status_filter_var = tk.StringVar(value="All")
    status_filter_menu = ttk.Combobox(top_frame, textvariable=status_filter_var, values=["All", "Open", "In Progress", "Closed"])
    status_filter_menu.grid(row=7, column=1)

    tk.Label(top_frame, text="Filter by Priority:").grid(row=8, column=0)
    priority_filter_var = tk.StringVar(value="All")
    priority_filter_menu = ttk.Combobox(top_frame, textvariable=priority_filter_var, values=["All", "Low", "Medium", "High"])
    priority_filter_menu.grid(row=8, column=1)

    tk.Button(top_frame, text="Apply Filters", command=filter_bugs).grid(row=9, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_window()
