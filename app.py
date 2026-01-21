from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import os
from datetime import datetime
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model
class FormSubmission(db.Model):
    __tablename__ = 'form_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    jmeno = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefon = db.Column(db.String(20), nullable=False)
    psc = db.Column(db.String(6), nullable=False)
    zprava = db.Column(db.Text, nullable=True)
    datum_odeslani = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'jmeno': self.jmeno,
            'email': self.email,
            'telefon': self.telefon,
            'psc': self.psc,
            'zprava': self.zprava,
            'datum_odeslani': self.datum_odeslani.isoformat()
        }

# Validation functions
def validate_email(email):
    """Validace emailové adresy"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_name(name):
    """Validace jména - pouze písmena, mezery, pomlčky a diakritika"""
    pattern = r'^[a-zA-ZáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ\s\-]+$'
    return re.match(pattern, name) is not None and len(name) >= 2

def validate_phone(phone):
    """Validace českého telefonního čísla"""
    # Odstranění mezer a pomlček
    clean_phone = phone.replace(' ', '').replace('-', '')
    # Formát: +420XXXXXXXXX nebo XXXXXXXXX (9 číslic)
    pattern = r'^(\+420)?[0-9]{9}$'
    return re.match(pattern, clean_phone) is not None

def validate_psc(psc):
    """Validace českého PSČ - formát XXXXX nebo XXX XX"""
    clean_psc = psc.replace(' ', '')
    pattern = r'^[0-9]{5}$'
    return re.match(pattern, clean_psc) is not None

def sanitize_input(text):
    """Odstranění nebezpečných znaků"""
    if text is None:
        return ""
    # Odstranění HTML tagů a nebezpečných znaků
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'[<>\"\'&]', '', text)
    return text.strip()

def save_to_json(data):
    """Uložení dat do JSON souboru"""
    json_file = 'submissions.json'
    
    # Načtení existujících dat
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            try:
                submissions = json.load(f)
            except json.JSONDecodeError:
                submissions = []
    else:
        submissions = []
    
    # Přidání nového záznamu
    submissions.append(data)
    
    # Uložení zpět do souboru
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(submissions, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Získání dat z formuláře
    jmeno = sanitize_input(request.form.get('jmeno', ''))
    email = sanitize_input(request.form.get('email', ''))
    telefon = sanitize_input(request.form.get('telefon', ''))
    psc = sanitize_input(request.form.get('psc', ''))
    zprava = sanitize_input(request.form.get('zprava', ''))
    
    # Validace
    errors = []
    
    if not jmeno or not validate_name(jmeno):
        errors.append('Jméno musí obsahovat pouze písmena a minimálně 2 znaky.')
    
    if not email or not validate_email(email):
        errors.append('Neplatná emailová adresa.')
    
    if not telefon or not validate_phone(telefon):
        errors.append('Neplatné telefonní číslo. Použijte formát: +420XXXXXXXXX nebo XXXXXXXXX')
    
    if not psc or not validate_psc(psc):
        errors.append('Neplatné PSČ. Použijte formát: XXXXX nebo XXX XX')
    
    if errors:
        for error in errors:
            flash(error, 'error')
        return redirect(url_for('index'))
    
    # Uložení do databáze
    submission = FormSubmission(
        jmeno=jmeno,
        email=email,
        telefon=telefon,
        psc=psc.replace(' ', ''),
        zprava=zprava
    )
    
    try:
        db.session.add(submission)
        db.session.commit()
        
        # Uložení také do JSON souboru
        save_to_json(submission.to_dict())
        
        flash('Formulář byl úspěšně odeslán!', 'success')
        return redirect(url_for('success'))
    except Exception as e:
        db.session.rollback()
        flash('Chyba při ukládání dat. Zkuste to prosím znovu.', 'error')
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submissions')
def view_submissions():
    """Zobrazení všech odeslaných formulářů"""
    submissions = FormSubmission.query.order_by(FormSubmission.datum_odeslani.desc()).all()
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
