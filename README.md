 ### Problem

You want to store the meetings of your friends in a database and be able to access them from anywhere.

### Solution

Create a Flask application that allows you to store and view the meetings of your friends.

### Design

The application will consist of the following HTML files:

* `index.html`: The home page of the application. This page will display a list of all the meetings in the database.
* `add_meeting.html`: A page that allows you to add a new meeting to the database.
* `edit_meeting.html`: A page that allows you to edit an existing meeting in the database.
* `delete_meeting.html`: A page that allows you to delete a meeting from the database.

The application will also have the following routes:

* `/`: The home page of the application.
* `/add_meeting`: A route that handles the addition of a new meeting to the database.
* `/edit_meeting/<int:meeting_id>`: A route that handles the editing of an existing meeting in the database.
* `/delete_meeting/<int:meeting_id>`: A route that handles the deletion of a meeting from the database.

### Implementation

The following code shows the implementation of the Flask application:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

meetings = []

@app.route('/')
def index():
    return render_template('index.html', meetings=meetings)

@app.route('/add_meeting', methods=['GET', 'POST'])
def add_meeting():
    if request.method == 'POST':
        meeting = request.form.get('meeting')
        meetings.append(meeting)
        return redirect(url_for('index'))
    return render_template('add_meeting.html')

@app.route('/edit_meeting/<int:meeting_id>', methods=['GET', 'POST'])
def edit_meeting(meeting_id):
    if request.method == 'POST':
        meeting = request.form.get('meeting')
        meetings[meeting_id] = meeting
        return redirect(url_for('index'))
    return render_template('edit_meeting.html', meeting_id=meeting_id, meeting=meetings[meeting_id])

@app.route('/delete_meeting/<int:meeting_id>')
def delete_meeting(meeting_id):
    meetings.pop(meeting_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Usage

To use the application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the application.
4. Open your web browser and go to `http://localhost:5000`.
5. Click on the "Add Meeting" link to add a new meeting to the database.
6. Enter the details of the meeting and click on the "Add Meeting" button.
7. The meeting will be added to the database and you will be redirected to the home page.
8. To edit a meeting, click on the "Edit" link next to the meeting.
9. Enter the new details of the meeting and click on the "Update Meeting" button.
10. The meeting will be updated in the database and you will be redirected to the home page.
11. To delete a meeting, click on the "Delete" link next to the meeting.
12. The meeting will be deleted from the database and you will be redirected to the home page.