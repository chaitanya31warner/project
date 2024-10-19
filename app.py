from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get server name
    name = " Y CHAITANYA SHIVA SRINIVAS"  

    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get IST time
    ist_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time() + 5.5 * 3600))

    # Get top command output
    top_output = subprocess.getoutput("top -bn1")

    # Format the data
    return f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {ist_time}</p>
        <pre><b>Top Output:</b><br>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
