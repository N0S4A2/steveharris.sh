from __future__ import unicode_literals
from flask import Flask, render_template
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(APP_ROOT, 'static')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gigography')
def gigography():
    return render_template('gigography.html')

@app.route('/moshington')
def moshington():
    with open(os.path.join(STATIC_ROOT, 'moshington.ics')) as shows_file:
        shows = []
        for line in shows_file:
            # Parsing iCalendar file, hence the syntax
            if line.startswith('DTSTART'):
                date = line.split(':')[1]
                date = date[4:6] + '/' + date[6:]
                show = {'date': date}
            elif line.startswith('SUMMARY'):
                # TODO Support band names with ':' or '@' characters
                lineup, venue = line.split(':')[1].split('@')
                show['lineup'] = lineup
                show['venue'] = venue
                shows.append(show)
    return render_template('moshington.html', shows=shows)

@app.route('/moshington.ics')
def moshington_ics():
    # TODO Configure the web server to serve the file
    return app.send_static_file('moshington.ics')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run()
