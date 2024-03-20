# How to run

## Clone the repository
```bash
git clone https://github.com/PImpliesQ/DjangoBackend.git
```

## Build with Docker
```bash
docker build -t django-backend .
```

## Run the container
```bash
docker run -p 8000:8000 django-backend
```

# Team Member Contributions
- The code for models and API endpoints was written by Hector Gittos, as well as the overall project
structure.
- The GitHub actions workflows, Dockerfile, deployment + hosting, and external database support code was done by Will Favier-Parsons.
- Integration and validation testing was done by Kaylum Smith, Callum Hynes, and Will Favier-Parsons.
- Build testing was done by Hector Gittos and Will Favier-Parsons.