from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('music', __name__,url_prefix='/music/')

@bp.route('/')
def index():
    db = get_db()
    musica = db.execute(
        """SELECT SELECT Title as titulo
         FROM albums
         ORDER BY Title DESC"""
    ).fetchall()
    return render_template('canciones/index.html', musica=musica)