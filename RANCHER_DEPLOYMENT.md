# 🚀 Rancher Kubernetes Deployment Guide

## Prerequisites Checklist

✅ **Required:**
- GitHub account with repository
- Access to Rancher at https://rancher.kube.sspu-opava.cz
- Docker image built and pushed to GitHub Container Registry (GHCR)
- kubectl configured (optional, can use Rancher UI)

## Step 1: Prepare GitHub Repository

### 1.1 Initialize Git Repository
```bash
cd /home/impo/Documents/school/grusik
git init
git add .
git commit -m "Initial commit: Flask contact form application"
```

### 1.2 Create GitHub Repository
1. Go to https://github.com/new
2. Create repository named: `contact-form-app`
3. **DON'T** initialize with README (you already have one)

### 1.3 Push to GitHub
```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/contact-form-app.git
git branch -M main
git push -u origin main
```

### 1.4 Enable GitHub Actions
- GitHub Actions will automatically trigger
- It will build and push Docker image to: `ghcr.io/YOUR_USERNAME/contact-form-app:latest`
- Wait for the workflow to complete (check Actions tab)

## Step 2: Update Kubernetes Configuration

### 2.1 Edit kubernetes-deployment.yaml
Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username:

```bash
# Find and replace in kubernetes-deployment.yaml
# Change: ghcr.io/YOUR_GITHUB_USERNAME/contact-form-app:latest
# To: ghcr.io/your-actual-username/contact-form-app:latest
```

### 2.2 Update Ingress Host (Optional)
If you want a custom subdomain, edit the ingress host in `kubernetes-deployment.yaml`:
```yaml
- host: contact-form.kube.sspu-opava.cz  # Change this if needed
```

## Step 3: Deploy to Rancher Kubernetes

### Option A: Using Rancher UI (Recommended for beginners)

#### 3.1 Login to Rancher
1. Navigate to: https://rancher.kube.sspu-opava.cz
2. Login with your credentials
3. Select your cluster

#### 3.2 Create Namespace
1. Click **"Namespaces"** in left menu
2. Click **"Create Namespace"**
3. Name: `contact-form-app`
4. Click **"Create"**

#### 3.3 Create Secrets
1. Go to **"Secrets"** → **"Create"**
2. Namespace: `contact-form-app`
3. Name: `flask-secrets`
4. Type: **Opaque**
5. Add Data:
   - Key: `secret-key` → Value: Generate random string (e.g., `openssl rand -hex 32`)
   - Key: `database-url` → Value: `sqlite:///app.db`
6. Click **"Create"**

#### 3.4 Make GitHub Package Public (Important!)
1. Go to: https://github.com/YOUR_USERNAME?tab=packages
2. Find `contact-form-app` package
3. Click **"Package settings"**
4. Scroll down to **"Danger Zone"**
5. Click **"Change visibility"** → **"Make Public"**
6. Confirm

**OR** Create Image Pull Secret if keeping private:
```bash
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=YOUR_GITHUB_USERNAME \
  --docker-password=YOUR_GITHUB_TOKEN \
  --namespace=contact-form-app
```

Then add to deployment spec:
```yaml
spec:
  imagePullSecrets:
  - name: ghcr-secret
```

#### 3.5 Deploy Application
1. Click **"Workload"** → **"Deployments"**
2. Click **"Import YAML"**
3. Copy and paste entire `kubernetes-deployment.yaml` content
4. Click **"Import"**

#### 3.6 Verify Deployment
1. Go to **"Workload"** → **"Deployments"**
2. Check that `contact-form-app` shows **2/2** pods running
3. If pods are failing, click on pod name → **"View Logs"** to debug

#### 3.7 Access Application
1. Go to **"Service Discovery"** → **"Ingresses"**
2. Find `contact-form-ingress`
3. Click the URL: `https://contact-form.kube.sspu-opava.cz`

### Option B: Using kubectl Command Line

```bash
# Apply the entire configuration
kubectl apply -f kubernetes-deployment.yaml

# Check deployment status
kubectl get pods -n contact-form-app
kubectl get services -n contact-form-app
kubectl get ingress -n contact-form-app

# View logs if needed
kubectl logs -n contact-form-app deployment/contact-form-app

# Check pod details
kubectl describe pod -n contact-form-app <pod-name>
```

## Step 4: Verify Application is Working

### 4.1 Check Pods are Running
```bash
kubectl get pods -n contact-form-app
```

Expected output:
```
NAME                                READY   STATUS    RESTARTS   AGE
contact-form-app-xxxxxxxxxx-xxxxx   1/1     Running   0          2m
contact-form-app-xxxxxxxxxx-xxxxx   1/1     Running   0          2m
```

### 4.2 Check Service
```bash
kubectl get svc -n contact-form-app
```

### 4.3 Check Ingress
```bash
kubectl get ingress -n contact-form-app
```

### 4.4 Test Application
Open browser: `https://contact-form.kube.sspu-opava.cz`

## Troubleshooting

### Problem: Pods are in ImagePullBackOff
**Solution:**
1. Make GitHub package public (see Step 3.4)
2. OR create image pull secret
3. Verify image name is correct: `ghcr.io/YOUR_USERNAME/contact-form-app:latest`

### Problem: Pods are CrashLoopBackOff
**Solution:**
```bash
# View logs
kubectl logs -n contact-form-app deployment/contact-form-app

# Common causes:
# - Missing dependencies (check requirements.txt)
# - Database migration issues
# - Wrong environment variables
```

### Problem: 502 Bad Gateway on Ingress
**Solution:**
1. Check pods are running: `kubectl get pods -n contact-form-app`
2. Check service is created: `kubectl get svc -n contact-form-app`
3. Verify port 5000 is correct
4. Check pod logs for errors

### Problem: Database not persisting
**Solution:**
For production, use PostgreSQL instead of SQLite:

1. Create PostgreSQL database
2. Update secret:
```bash
kubectl create secret generic flask-secrets \
  --from-literal=secret-key="$(openssl rand -hex 32)" \
  --from-literal=database-url="postgresql://user:pass@host:5432/dbname" \
  --namespace=contact-form-app \
  --dry-run=client -o yaml | kubectl apply -f -
```

3. Add persistent volume for SQLite (alternative):
```yaml
volumeMounts:
- name: db-storage
  mountPath: /app/instance
volumes:
- name: db-storage
  persistentVolumeClaim:
    claimName: contact-form-pvc
```

## Production Checklist

Before going to production:

- [ ] Change `SECRET_KEY` to strong random value
- [ ] Use PostgreSQL/MySQL instead of SQLite
- [ ] Set up proper SSL/TLS certificates (Let's Encrypt via cert-manager)
- [ ] Configure proper resource limits
- [ ] Set up monitoring and logging
- [ ] Configure backup strategy for database
- [ ] Test all form validations
- [ ] Review security settings
- [ ] Set up health checks
- [ ] Configure horizontal pod autoscaling (HPA)

## Updating the Application

### Method 1: Push to GitHub (Automatic)
```bash
# Make changes to code
git add .
git commit -m "Update: description of changes"
git push

# GitHub Actions will automatically build new image
# Then update deployment:
kubectl rollout restart deployment/contact-form-app -n contact-form-app
```

### Method 2: Manual Update
```bash
# Edit deployment
kubectl edit deployment contact-form-app -n contact-form-app

# Or apply updated YAML
kubectl apply -f kubernetes-deployment.yaml
```

## Scaling

### Scale replicas:
```bash
kubectl scale deployment contact-form-app --replicas=3 -n contact-form-app
```

### Auto-scaling (HPA):
```bash
kubectl autoscale deployment contact-form-app \
  --cpu-percent=70 \
  --min=2 \
  --max=10 \
  -n contact-form-app
```

## Clean Up / Uninstall

```bash
# Delete entire namespace (removes everything)
kubectl delete namespace contact-form-app

# Or delete specific resources
kubectl delete -f kubernetes-deployment.yaml
```

## Monitoring

### View application logs:
```bash
# All pods
kubectl logs -n contact-form-app -l app=contact-form-app --tail=100 -f

# Specific pod
kubectl logs -n contact-form-app <pod-name> -f
```

### Get into pod shell:
```bash
kubectl exec -it -n contact-form-app <pod-name> -- /bin/bash
```

### Check resource usage:
```bash
kubectl top pods -n contact-form-app
kubectl top nodes
```

## Support

For issues with:
- **Rancher**: Contact school IT admin
- **Application bugs**: Check GitHub Issues
- **Kubernetes**: https://kubernetes.io/docs/

## Summary

Your application is **READY** for Rancher Kubernetes deployment! ✅

The configuration includes:
- ✅ Namespace isolation
- ✅ 2 replica deployment for high availability
- ✅ Service for internal communication
- ✅ Ingress with NGINX for external access
- ✅ TLS/SSL configuration
- ✅ Resource limits and requests
- ✅ Liveness and readiness probes
- ✅ Secrets management
- ✅ Restart policy

Just follow the steps above and your app will be live!
