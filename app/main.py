from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/admin')
def admin():
    return render_template('admin/index.html')