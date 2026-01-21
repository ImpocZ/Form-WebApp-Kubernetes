# Kontaktní formulář - Flask Web Aplikace

Jednoduchá webová aplikace s kontaktním formulářem vytvořená pomocí Flask frameworku.

## ✨ Funkce

- 📝 **Kontaktní formulář** s validací všech polí
- ✅ **Validace vstupů**: email, telefonní číslo, PSČ, jméno
- 🛡️ **Bezpečnost**: sanitizace vstupů proti nebezpečným znakům
- 💾 **Dvojí ukládání**: SQL databáze + JSON backup
- 🎨 **Moderní design**: externí CSS, responzivní layout
- 🔧 **Makra**: efektivní templates pomocí Jinja2 maker
- 🗃️ **Databáze**: SQLAlchemy + Flask-Migrate pro verzování
- 🐳 **Docker**: připravený Dockerfile
- 🚀 **CI/CD**: GitHub Actions pro automatické generování Docker images
- ☸️ **Kubernetes**: konfigurace pro deployment

## 📋 Požadavky

- Python 3.11+
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.0.5

## 🚀 Rychlý start

### 1. Instalace závislostí

```bash
pip install -r requirements.txt
```

### 2. Nastavení prostředí

```bash
cp env.example .env
# Upravte .env soubor podle potřeby
```

### 3. Inicializace databáze

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Spuštění aplikace

```bash
python app.py
```

Aplikace poběží na `http://localhost:5000`

## 📁 Struktura projektu

```
grusik/
├── app.py                          # Hlavní Flask aplikace
├── requirements.txt                # Python závislosti
├── Dockerfile                      # Docker konfigurace
├── kubernetes-deployment.yaml      # Kubernetes deployment
├── .gitignore                      # Git ignore soubor
├── env.example                     # Příklad konfigurace
├── templates/                      # HTML šablony
│   ├── base.html                  # Základní layout
│   ├── macros.html                # Jinja2 makra
│   ├── index.html                 # Hlavní stránka s formulářem
│   ├── success.html               # Potvrzení odeslání
│   └── submissions.html           # Zobrazení odeslaných formulářů
├── static/                         # Statické soubory
│   └── css/
│       └── style.css              # Hlavní CSS soubor
├── migrations/                     # Databázové migrace
└── .github/
    └── workflows/
        └── docker-image.yml       # GitHub Actions workflow
```

## 🎯 Validace formuláře

Aplikace validuje:

- **Jméno**: Pouze písmena (včetně diakritiky), mezery a pomlčky, min. 2 znaky
- **Email**: Platný formát emailové adresy
- **Telefon**: České tel. číslo (9 číslic, volitelně +420)
- **PSČ**: 5 číslic (formát: 12345 nebo 123 45)
- **Zpráva**: Volitelné pole, sanitizace nebezpečných znaků

## 🐳 Docker

### Build image:
```bash
docker build -t grusik-app .
```

### Spuštění:
```bash
docker run -p 5000:5000 -e SECRET_KEY=your-secret-key grusik-app
```

## ☸️ Kubernetes Deployment

1. Upravte `kubernetes-deployment.yaml` (nahraďte YOUR_GITHUB_USERNAME)
2. Vytvořte secrets:
```bash
kubectl create secret generic flask-secrets \
  --from-literal=secret-key=your-random-secret-key \
  --from-literal=database-url=sqlite:///app.db \
  -n grusik-app
```
3. Aplikujte deployment:
```bash
kubectl apply -f kubernetes-deployment.yaml
```

## 🔄 GitHub Actions

Workflow automaticky:
- Builduje Docker image při push na main/master
- Pushuje image do GitHub Container Registry
- Taguje verze pomocí SHA a latest

## 🛡️ Bezpečnost

- ✅ Hesla a konfigurace v `.gitignore`
- ✅ Použití environment variables (env.example)
- ✅ Sanitizace všech vstupů
- ✅ SQL injection prevence (SQLAlchemy ORM)
- ✅ XSS prevence (odstranění HTML tagů)

## 📊 Databáze

- **Vývojové prostředí**: SQLite (app.db)
- **Produkce**: PostgreSQL/MySQL (konfigurace v DATABASE_URL)
- **Verzování**: Flask-Migrate pro správu migrací
- **Backup**: Automatické ukládání do JSON

## 🎨 Frontend

- Moderní, responzivní design
- CSS Grid a Flexbox
- Animace a přechody
- Mobilní optimalizace
- Přístupnost (labels, ARIA)

## 📝 Funkce podle požadavků

✅ **Formuláře s validací**  
✅ **Uloženo na GitHubu**  
✅ `.gitignore` pro hesla a konfiguraci  
✅ `env.example` pro environment variables  
✅ **GitHub Actions** pro Docker images  
✅ **Kubernetes deployment** konfigurace  
✅ **Externí CSS** soubor  
✅ **Makra** pro zjednodušení templates  
✅ **Validace** všech polí formuláře  
✅ **Safe characters** - sanitizace vstupů  
✅ **Flask** framework  
✅ **Verzování DB** pomocí Flask-Migrate  
✅ **SQL server** - SQLAlchemy s podporou PostgreSQL/MySQL  
✅ **JSON backup** - ukládání do .json souboru  

## 👨‍💻 Autor

Školní projekt pro SŠPU Opava

## 📄 Licence

Tento projekt je vytvořen pro vzdělávací účely.