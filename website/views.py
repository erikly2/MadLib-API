from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        adverb1 = request.form.get('adverb1')
        pluralnoun1 = request.form.get('pluralnoun1')
        verb1 = request.form.get('verb1')
        preposition1 = request.form.get('preposition1')
        preposition2 = request.form.get('preposition2')
        pronoun1 = request.form.get('pronoun1')
        adjective1 = request.form.get('adjective1')
        verb2 = request.form.get('verb2')
        
        session['adverb1']=adverb1
        session['pluralnoun1']=pluralnoun1
        session['verb1']=verb1
        session['preposition1']=preposition1
        session['preposition2']=preposition2
        session['pronoun1']=pronoun1
        session['adjective1']=adjective1
        session['verb2']=verb2

        return redirect(url_for('views.result'))
    return render_template("home.html", user=current_user)

@views.route('/result', methods=['GET', 'POST'])
@login_required
def result():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    adverb1=session.get('adverb1', None)
    verb1=session.get('verb1', None)
    pluralnoun1=session.get('pluralnoun1', None)
    preposition1=session.get('preposition1', None)
    preposition2=session.get('preposition2', None)
    pronoun1=session.get('pronoun1', None)
    adjective1=session.get('adjective1', None)
    verb2=session.get('verb2', None)
    return render_template("result.html", Never=adverb1, give=verb1, strangers=pluralnoun1, you=pronoun1, up=preposition1, down=preposition2, run=verb2, shy=adjective1, user=current_user)