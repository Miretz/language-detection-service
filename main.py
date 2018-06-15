import os

from flask import (
    Flask,
    render_template 
)

import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')
port = int(os.getenv("PORT", 5000))

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='localhost', port=port, debug=False, use_reloader=False)
