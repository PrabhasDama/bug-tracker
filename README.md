# Bug Tracker

A Python-based Bug Tracker application that uses **SQLite** for data storage and **Tkinter** for a graphical user interface (GUI). This project helps manage and track software bugs by allowing users to add, view, update, and delete bugs efficiently.

## Features

- **Add Bugs**: Input details like title, description, and priority.
- **View Bugs**: See all bugs displayed in a table format.
- **Update Bugs**: Modify the status of a bug (e.g., Open, In Progress, Closed).
- **Delete Bugs**: Remove bugs from the list when they are no longer needed.
- **Filters**: Apply filters to view bugs by status or priority.

## Technologies Used

- **Python**: Programming language used for the entire application.
- **SQLite**: Database for persistent storage of bug data.
- **Tkinter**: GUI framework for creating the application interface.

## Requirements

```bash
Python 3.x
sqlite3 (built-in with Python)
tkinter (built-in with Python)
```

# Installation and Setup
```bash
# Clone the Repository
git clone https://github.com/PrabhasDama/bug-tracker.git
cd bug-tracker

# Initialize the Database
python init_db.py

# Run the Application
python main.py
```

# How to Use
## Adding a Bug:
- Enter the bug title, description, and priority in the input fields.
- Click the "Add Bug" button to save the bug.

## Viewing Bugs:
- All bugs are displayed in a table with columns for ID, Title, Priority, and Status.

## Updating a Bug:
- Select a bug from the table.
- Enter the new status (e.g., "In Progress" or "Closed") and click the "Update Status" button.

## Deleting a Bug:
- Select a bug from the table and click the "Delete Bug" button to remove it.

## Filtering Bugs:
- Use the dropdown menus to filter bugs by status or priority.
- Click the "Apply Filters" button to view the filtered list.

# Future Enhancements
- Add a search feature to find bugs quickly.
- Export bug data to a file (e.g., CSV).
- Add user authentication for multi-user support.

# Author
- **Prabhas Dama**  
  An aspiring developer passionate about creating practical tools and learning new technologies.
