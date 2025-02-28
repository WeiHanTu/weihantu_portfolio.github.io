from flask import Flask, send_from_directory, request, redirect, url_for, render_template_string
import csv
import os
from datetime import datetime

app = Flask(__name__)

CSV_FILE = 'contacts.csv'


def write_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header if file is new
        if not file_exists or os.path.getsize(CSV_FILE) == 0:
            writer.writerow(['Date', 'Name', 'Email', 'Message'])
        writer.writerow(data)


@app.route('/')
def index():
    # Serve your index.html file from the public folder.
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/save_contact', methods=['POST'])
def save_contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save data to CSV
        write_to_csv([date, name, email, message])

        # Redirect to thank-you page after successful submission
        return redirect(url_for('thank_you'))
    else:
        return "405 Method Not Allowed", 405


@app.route('/thankyou')
def thank_you():
    # You can customize this thank-you page as needed.
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Thank You</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 50px; text-align: center; }
        </style>
    </head>
    <body>
        <h1>Thank You!</h1>
        <p>Your message has been received. I will get back to you shortly.</p>
        <a href="/">Return to Home</a>
    </body>
    </html>
    ''')


if __name__ == '__main__':
    app.run(debug=True)
