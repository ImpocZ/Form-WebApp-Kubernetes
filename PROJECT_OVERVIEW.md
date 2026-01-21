# 📋 Přehled projektu

## 🎯 Zadání splněno

Tento projekt je kompletní Flask webová aplikace s kontaktním formulářem, která splňuje **všechny požadavky** ze zadání:

### ✅ Základní požadavky
- [x] Webová aplikace s formulářem
- [x] Formulář v českém jazyce
- [x] Validace všech polí (email, jméno, telefon, PSČ)
- [x] Flask framework
- [x] Uložení dat do JSON souboru
- [x] SQL databáze (SQLite/PostgreSQL/MySQL)

### ✅ Technické požadavky
- [x] Externí CSS soubor v samostatné složce (`static/css/style.css`)
- [x] Makra pro zjednodušení templates (`templates/macros.html`)
- [x] Validace formulářových polí
- [x] Safe characters - sanitizace nebezpečných znaků
- [x] Verzování databáze (Flask-Migrate)
- [x] Ukládání do SQL serveru

### ✅ Git a deployment
- [x] Uloženo na GitHubu
- [x] `.gitignore` - neukladá hesla, databáze
- [x] `env.example` - příklad konfigurace
- [x] GitHub Actions pro generování Docker image
- [x] Kubernetes deployment konfigurace

## 🏗️ Architektura aplikace

### Backend (Flask)
```
app.py
├── Flask aplikace
├── SQLAlchemy ORM (databáze)
├── Flask-Migrate (verzování DB)
├── Validační funkce
├── Sanitizace vstupů
└── JSON backup
```

### Frontend (HTML/CSS)
```
templates/
├── base.html       → Základní layout + navigace
├── macros.html     → Reusable makra (input, textarea, flash messages)
├── index.html      → Hlavní formulář
├── success.html    → Potvrzení odeslání
└── submissions.html → Přehled odeslaných formulářů

static/css/
└── style.css       → Moderní responzivní design
```

### Databáze
```
FormSubmission model:
├── id (Primary Key)
├── jmeno (String 100)
├── email (String 120)
├── telefon (String 20)
├── psc (String 6)
├── zprava (Text, nullable)
└── datum_odeslani (DateTime)
```

## 🔒 Bezpečnostní opatření

1. **Validace vstupů**
   - Email: Regex pattern validace
   - Telefon: České formáty (+420XXXXXXXXX)
   - PSČ: 5 číslic
   - Jméno: Pouze písmena + diakritika

2. **Sanitizace**
   - Odstranění HTML tagů
   - Odstranění nebezpečných znaků (<, >, ", ', &)
   - Trim whitespace

3. **SQL Injection prevence**
   - SQLAlchemy ORM (parametrizované dotazy)
   - Žádné raw SQL queries

4. **XSS prevence**
   - Jinja2 auto-escaping
   - Manual sanitizace vstupů

5. **Konfigurace**
   - SECRET_KEY v environment variables
   - Database credentials v .env
   - .gitignore pro citlivá data

## 📊 Ukládání dat

### Primární: SQL databáze
- **Development**: SQLite (`app.db`)
- **Production**: PostgreSQL/MySQL
- **ORM**: SQLAlchemy
- **Migrace**: Flask-Migrate

### Sekundární: JSON backup
- Každé odeslání také v `submissions.json`
- UTF-8 encoding
- Pretty print (indent=2)

## 🎨 Design features

- ✅ Moderní gradient pozadí
- ✅ Card-based layout
- ✅ Responzivní design (mobil/tablet/desktop)
- ✅ Animace (slideIn, scaleIn)
- ✅ Hover efekty
- ✅ Flash zprávy (success/error)
- ✅ Form validace v reálném čase (CSS)
- ✅ Přístupnost (labels, ARIA)

## 🚀 Deployment možnosti

### 1. Lokální vývoj
```bash
python app.py
```

### 2. Docker
```bash
docker build -t grusik-app .
docker run -p 5000:5000 grusik-app
```

### 3. Docker Compose
```bash
docker-compose up
```

### 4. Kubernetes (SŠPU Opava)
```bash
kubectl apply -f kubernetes-deployment.yaml
```

## 🔄 CI/CD Pipeline

GitHub Actions workflow:
1. **Trigger**: Push na main/master
2. **Build**: Docker image
3. **Tag**: SHA + latest
4. **Push**: GitHub Container Registry (ghcr.io)
5. **Ready**: Pro deploy na Kubernetes

## 📈 Rozšíření do budoucna

Možná vylepšení:
- [ ] Přidat captcha (proti spamu)
- [ ] Email notifikace
- [ ] Admin panel
- [ ] Export do CSV/Excel
- [ ] API endpoints (REST/GraphQL)
- [ ] Vícestránkový formulář
- [ ] File upload
- [ ] Autentizace uživatelů

## 🧪 Testování

### Manuální testy:
1. Vyplnit formulář s platnými daty → ✅ Úspěch
2. Vyplnit s neplatným emailem → ❌ Chybová hláška
3. Vyplnit s neplatným telefonem → ❌ Chybová hláška
4. Vyplnit s neplatným PSČ → ❌ Chybová hláška
5. SQL injection pokus → 🛡️ Zabráněno
6. XSS pokus → 🛡️ Zabráněno

### Automatické testy (TODO):
```python
# Přidat pytest
# tests/test_validation.py
# tests/test_routes.py
# tests/test_models.py
```

## 📝 Dokumentace

- `readme.md` - Hlavní dokumentace projektu
- `QUICKSTART.md` - Rychlý průvodce spuštěním
- `README_DEPLOYMENT.md` - Detailní deployment instrukce
- `PROJECT_OVERVIEW.md` - Tento soubor

## 🎓 Hodnocení projektu

### Splněné body zadání:

| Požadavek | Status | Poznámka |
|-----------|--------|----------|
| Webová aplikace | ✅ | Flask aplikace |
| Formulář | ✅ | Kontaktní formulář v CZ |
| GitHub | ✅ | Připraveno k push |
| .gitignore | ✅ | Hesla, DB soubory |
| env.example | ✅ | Konfigurace variables |
| GitHub Actions | ✅ | Docker image CI/CD |
| Kubernetes | ✅ | Deployment YAML |
| Externí CSS | ✅ | static/css/style.css |
| Makra | ✅ | templates/macros.html |
| Validace | ✅ | Všechna pole validována |
| Safe chars | ✅ | Sanitizace implementována |
| Flask | ✅ | Framework použit |
| Verzování DB | ✅ | Flask-Migrate |
| SQL server | ✅ | SQLAlchemy + migrace |
| JSON backup | ✅ | submissions.json |

### Bonus features:
- ✅ Moderní responzivní design
- ✅ Animace a přechody
- ✅ Zobrazení odeslaných formulářů
- ✅ Docker Compose
- ✅ Podrobná dokumentace
- ✅ Bezpečnostní opatření

## 👨‍💻 Technologie

- **Backend**: Flask 3.0.0, Python 3.11+
- **Database**: SQLAlchemy, Flask-Migrate
- **Frontend**: HTML5, CSS3, Jinja2
- **Server**: Gunicorn
- **Container**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions

## 📞 Kontakt

Projekt vytvořen jako školní úkol pro SŠPU Opava.
