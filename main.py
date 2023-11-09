 
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


html code for index.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Meetings</title>
</head>
<body>
    <h1>Meetings</h1>
    <ul>
        {% for meeting in meetings %}
            <li>{{ meeting }}</li>
        {% endfor %}
    </ul>
    <a href="/add_meeting">Add Meeting</a>
</body>
</html>


html code for add_meeting.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Add Meeting</title>
</head>
<body>
    <h1>Add Meeting</h1>
    <form action="/add_meeting" method="post">
        <input type="text" name="meeting" placeholder="Meeting">
        <input type="submit" value="Add Meeting">
    </form>
</body>
</html>


html code for edit_meeting.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Edit Meeting</title>
</head>
<body>
    <h1>Edit Meeting</h1>
    <form action="/edit_meeting/{{ meeting_id }}" method="post">
        <input type="text" name="meeting" placeholder="Meeting" value="{{ meeting }}">
        <input type="submit" value="Update Meeting">
    </form>
</body>
</html>


html code for delete_meeting.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Delete Meeting</title>
</head>
<body>
    <h1>Delete Meeting</h1>
    <p>Are you sure you want to delete this meeting?</p>
    <form action="/delete_meeting/{{ meeting_id }}" method="post">
        <input type="submit" value="Delete Meeting">
    </form>
</body>
</html>
