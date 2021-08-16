# Code Created by Rayhan Biju 2021 #

from Website import create_app
from flask import render_template
import python_jwt

app = create_app()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(401)
def restricted_access(e):
    return render_template('401.html'), 401


if __name__ == '__main__':
    app.run(debug=True)
