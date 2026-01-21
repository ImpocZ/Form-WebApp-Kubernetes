# Deployment Instructions

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env file with your configuration
   ```

3. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## Docker Deployment

1. **Build Docker image:**
   ```bash
   docker build -t grusik-app .
   ```

2. **Run Docker container:**
   ```bash
   docker run -p 5000:5000 -e SECRET_KEY=your-secret-key grusik-app
   ```

## Kubernetes Deployment

1. **Update the image in kubernetes-deployment.yaml:**
   Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username

2. **Create secrets:**
   ```bash
   kubectl create secret generic flask-secrets \
     --from-literal=secret-key=your-random-secret-key \
     --from-literal=database-url=sqlite:///app.db \
     -n grusik-app
   ```

3. **Apply the deployment:**
   ```bash
   kubectl apply -f kubernetes-deployment.yaml
   ```

4. **Check deployment status:**
   ```bash
   kubectl get pods -n grusik-app
   kubectl get services -n grusik-app
   ```

## GitHub Actions

The GitHub Actions workflow automatically builds and pushes Docker images to GitHub Container Registry when you push to the main/master branch.

1. **Enable GitHub Actions** in your repository settings
2. **Push your code** to the main branch
3. **The workflow will automatically:**
   - Build the Docker image
   - Push it to ghcr.io
   - Tag it with the commit SHA and latest

## Features

- ✅ Form validation (email, phone, PSČ, name)
- ✅ Safe character handling
- ✅ External CSS file
- ✅ Template macros for efficiency
- ✅ SQL database with Flask-SQLAlchemy
- ✅ Database migrations with Flask-Migrate
- ✅ JSON file backup
- ✅ Docker support
- ✅ GitHub Actions CI/CD
- ✅ Kubernetes deployment configuration
- ✅ Environment variable configuration
- ✅ .gitignore for sensitive data

## Security Notes

- Never commit `.env` file or database files
- Always use strong SECRET_KEY in production
- Keep database credentials secure
- Use environment variables for sensitive configuration
