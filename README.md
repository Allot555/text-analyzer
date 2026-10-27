# Text Analyzer — Containerized Cloud Application

A simple web application that analyzes text and returns the number of words and characters. Built as a containerization project and deployed to AWS ECS using AWS Fargate.

## Features

- Analyze text through a simple web interface.
- Count words and characters.
- Separate frontend and backend containers.
- Synchronous HTTP communication between frontend and backend.
- JSON API response from the backend.
- Custom Docker images published to Docker Hub.
- Cloud deployment using AWS ECS and AWS Fargate.

## Architecture

```text
User's Browser
      |
      v
Frontend Container (Nginx)
      |
      | HTTP POST /api/analyze
      v
Backend Container (Python + FastAPI)
      |
      | JSON response
      v
Frontend displays the word and character counts
```

The frontend serves the web interface and uses Nginx as a reverse proxy. The backend receives text through a FastAPI endpoint, calculates the word and character counts, and returns the results as JSON.

## Technologies

- **Frontend:** HTML, CSS, JavaScript
- **Web server / reverse proxy:** Nginx
- **Backend:** Python, FastAPI, Uvicorn
- **Containerization:** Docker, Dockerfiles
- **Image registry:** Docker Hub
- **Cloud deployment:** AWS ECS, AWS Fargate

## Project Structure

```text
text-analyzer/
├── Backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── script.js
│   └── nginx.conf
├── .gitignore
└── README.md
```

## Docker Images

The application images are published on Docker Hub:

- [Text Analyzer Frontend](https://hub.docker.com/r/87878799/text-analyzer-frontend)
- [Text Analyzer Backend](https://hub.docker.com/r/87878799/text-analyzer-backend)

## Deployment

The application was deployed to Amazon ECS using AWS Fargate. Both containers ran in the same ECS task, with the frontend communicating synchronously with the backend over HTTP.

The deployment was tested in the cloud, and the application successfully returned text analysis results.

**Note:** The cloud deployment has been stopped to avoid unnecessary resource usage. The source code and Docker images remain available for review.

## What I Learned

- Building custom Docker images from Dockerfiles.
- Running and testing multiple containers.
- Configuring HTTP communication between frontend and backend.
- Using Nginx as a reverse proxy.
- Publishing Docker images to Docker Hub.
- Deploying containerized applications to AWS ECS and Fargate.
- Understanding container separation, stateless application design, and cloud deployment.

## Project Context

Developed as part of a containerization course. The project received a **VG (Pass with Distinction)** grade.
