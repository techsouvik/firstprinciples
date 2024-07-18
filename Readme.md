# Blogging Platform

## Overview

This project is a simple blogging platform built using a microservice architecture. It includes three main services:
- Auth Service: Handles user authentication and authorization.
- Blog Service: Manages blog posts (create, read, update, delete).
- Image Service: Handles image uploads and retrieval using AWS S3.

The project uses Docker for containerization, PostgreSQL for the database, and Redis for caching. It also includes an isolated test service for unit testing.

## Services

### Auth Service
- Handles user signup, signin, and authentication.
- Uses SQLite for the database.
- Implements JWT for secure authentication.

### Blog Service
- Manages blog posts (create, read, update, delete).
- Uses PostgreSQL for the database.
- Implements caching with Redis.

### Image Service
- Handles image uploads and retrieval.
- Uses AWS S3 for image storage.
- Implements caching with Redis.

## Architecture

- **Microservices**: Each service runs in its own Docker container.
- **Database**: PostgreSQL for the Blog Service, SQLite for the Auth Service.
- **Caching**: Redis for caching frequently accessed data.
- **Container Orchestration**: Docker Compose to manage multi-container applications.
- **Testing**: Isolated test service using Docker to run unit tests independently.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- AWS account with S3 bucket set up for image storage.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/blogging-platform.git
cd blogging-platform
```

2. Create a .env file in the root directory and set your 

```bash
- environment variables:
- dotenv
```
#### .env
```bash
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_S3_BUCKET_NAME=your_s3_bucket_name
```

3. Build and run the Docker containers:
```bash
docker-compose up --build
```

### Endpoints
##### Auth Service
- POST /signup: Create a new user.
- POST /signin: Authenticate a user and get a token.


##### Blog Service
- POST /posts: Create a new blog post.
- GET /posts: Retrieve a list of all blog posts.
- GET /posts/{id}: Retrieve a single blog post by its ID.
- PUT /posts/{id}: Update an existing blog post.
- DELETE /posts/{id}: Delete a blog post.


##### Image Service
- POST /upload: Upload an image.
- GET /images/{filename}: Retrieve an image by filename.

## Future Prospects for Version-2 

- Adding data validation
- Use AWS Lambda, AWS SQS and API Gateway to link all the services
- Adding Kafka as a throughput for uploading blogs and authenticating users
- feature for uploading videos and download it in a adavtive bit-rate using HLS encoding
- adding OAuth2 as an authentication inplace of JWT tokens

