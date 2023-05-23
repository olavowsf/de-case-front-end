# DE Case API

This is an sample API created as a demostration for Ginkgo Analytics.


### 1.) Structure


### 2.) How to run this application 
1. Create virtual environment
```python
    python3 -m venv example
    source de_case_env/bin/activate
    pip install -U pip
    pip install -r requirements.txt
```
2. Run tests
```python
    pip install pytest
    pytest tests/
```
3. Run locally


```python
    uvicorn main:app --reload --port 1234      
```
4. Run locally with Docker

Build the image
```
    docker build -t $TAG .
```
Run locally in docker

```python
    docker run -dp $PORT:$PORT -e PORT=$PORT $TAG```
```
5. Deploy it in GCP

Create a repo in Artifact Registry
```
    gcloud artifacts repositories create de-case-repo --repository-format=docker \
    --location=europe-west3
```

Build the image
```
    gcloud builds submit --region=us-west2 --tag europe-west3-docker.pkg.dev/playground-olavo-387508/de-case-repo/image:app   
```
And deploy the new image:
```
    gcloud beta run deploy demo-app --image europe-west3-docker.pkg.dev/playground-olavo-387508/de-case-repo/image:app --region europe-west3 --allow-unauthenticated
```
### 2.) API Documentation

https://documenter.getpostman.com/view/27518917/2s93m1ZjUp

---
Copyright © 2023 Ginkgo Analytics GmbH. All rights reserved.
