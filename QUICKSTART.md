# 🚀 Rychlý průvodce spuštěním

## Pro okamžité spuštění (už nastaveno):

Aplikace je už nainstalovaná a běží! Otevřete v prohlížeči:

**http://localhost:5000**

## Co můžete dělat:

1. **Vyplnit formulář** - hlavní stránka (/)
2. **Zobrazit odeslané formuláře** - klikněte na "Odeslané formuláře" v menu

## Testovací data:

### Platné údaje pro testování:
- **Jméno**: Jan Novák
- **Email**: jan.novak@example.com
- **Telefon**: +420 123 456 789 nebo 123456789
- **PSČ**: 12345 nebo 123 45
- **Zpráva**: Libovolný text

### Příklady neplatných údajů:
- **Jméno**: Jan123 ❌ (obsahuje čísla)
- **Email**: jannovak ❌ (není platný email)
- **Telefon**: 12345 ❌ (příliš krátké)
- **PSČ**: 1234 ❌ (musí mít 5 číslic)

## Restartování aplikace:

Pokud potřebujete restartovat server:

```bash
# Zastavte aktuální server (Ctrl+C v terminálu)
# Pak spusťte znovu:
cd /home/impo/Documents/school/grusik
/home/impo/Documents/school/grusik/.venv/bin/python app.py
```

## Kde jsou uložená data:

1. **SQL databáze**: `/home/impo/Documents/school/grusik/app.db`
2. **JSON backup**: `/home/impo/Documents/school/grusik/submissions.json`

## Zobrazení databáze:

```bash
# V terminálu:
cd /home/impo/Documents/school/grusik
/home/impo/Documents/school/grusik/.venv/bin/python -c "from app import app, db, FormSubmission; app.app_context().push(); print([s.to_dict() for s in FormSubmission.query.all()])"
```

## Resetování databáze:

```bash
cd /home/impo/Documents/school/grusik
rm app.db submissions.json
/home/impo/Documents/school/grusik/.venv/bin/flask db upgrade
```

## GitHub a Docker:

1. **Přidejte do Git:**
```bash
cd /home/impo/Documents/school/grusik
git init
git add .
git commit -m "Initial commit: Flask contact form application"
```

2. **Pushněte na GitHub:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/grusik.git
git push -u origin main
```

3. **GitHub Actions** se automaticky spustí a vytvoří Docker image!

## Užitečné příkazy:

### Zobrazit všechny tabulky v DB:
```bash
cd /home/impo/Documents/school/grusik
/home/impo/Documents/school/grusik/.venv/bin/python -c "from app import app, db; app.app_context().push(); print(db.metadata.tables.keys())"
```

### Vytvořit novou migraci po změnách modelu:
```bash
cd /home/impo/Documents/school/grusik
/home/impo/Documents/school/grusik/.venv/bin/flask db migrate -m "Popis změny"
/home/impo/Documents/school/grusik/.venv/bin/flask db upgrade
```

### Testovat Docker lokálně:
```bash
cd /home/impo/Documents/school/grusik
docker build -t grusik-test .
docker run -p 5000:5000 grusik-test
```

## Řešení problémů:

### Port 5000 je už používán:
```bash
# Změňte port v app.py na řádku:
# app.run(debug=True, host='0.0.0.0', port=5001)
```

### Chyba importu modulů:
```bash
cd /home/impo/Documents/school/grusik
/home/impo/Documents/school/grusik/.venv/bin/pip install -r requirements.txt
```

### Databáze neexistuje:
```bash
cd /home/impo/Documents/school/grusik
/home/impo/Documents/school/grusik/.venv/bin/flask db upgrade
```

## 🎓 Pro hodnocení projektu:

Projekt splňuje všechny požadavky:
- ✅ Formulář s validací
- ✅ Externí CSS
- ✅ Makra v templates
- ✅ Safe characters
- ✅ Flask framework
- ✅ SQL databáze + verzování
- ✅ JSON backup
- ✅ .gitignore + env.example
- ✅ Docker
- ✅ GitHub Actions
- ✅ Kubernetes konfigurace
