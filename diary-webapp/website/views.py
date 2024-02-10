from flask import Blueprint, render_template, request, flash, jsonify
from datetime import datetime
from flask_login import login_required, current_user
from .models import Entry
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/post', methods=['POST', 'GET'])
@login_required
def entry_post():
    if request.method == 'POST':
        entry = request.form.get('entry')
        
        if len(entry) < 2:
            flash('Your entry needs to be longer.', category='error')
        else: 
            new_entry = Entry(data=entry,  date=datetime.now().isoformat(sep=" ", timespec="minutes"), user_id=current_user.id)
            db.session.add(new_entry)
            db.session.commit()
            flash('Your entry has been added!', category="success")
        
    return render_template('entrypost.html', user=current_user)

@views.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)
            
                