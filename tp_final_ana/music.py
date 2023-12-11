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
        """SELECT name as nombre
         FROM tracks
         ORDER BY name DESC"""
    ).fetchall()
    return render_template('canciones/index.html', musica=musica)


@bp.route('/<int:id>/datalle', methods=('GET', 'POST'))
def detalle(id):
    db = get_db()
    music = db.execute(
        """SELECT name as nombre
         FROM tracks
         ORDER BY name DESC"""
    ).fetchone()

    artistas = db.execute(
        """SELECT ArtistId, name
            FROM artists
                ORDER BY ArtistId;"""
    ).fetchall()

    return render_template('canciones/detalle.html', music=music, artistas=artistas)