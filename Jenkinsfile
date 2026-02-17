pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-ci-app"
        CONTAINER_NAME = "flask-ci-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out source code from GitHub..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                bat "pip install -r requirements.txt"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Stop Old Container') {
            steps {
                echo "Stopping old container if running..."
                bat """
                docker stop %CONTAINER_NAME% || exit 0
                docker rm %CONTAINER_NAME% || exit 0
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Running new container..."
                bat "docker run -d -p 5000:8000 --name %CONTAINER_NAME% %IMAGE_NAME%"
            }
        }

        stage('Verify Running Container') {
            steps {
                echo "Listing running containers..."
                bat "docker ps"
            }
        }

        stage('Success') {
            steps {
                echo "CI/CD Pipeline Executed Successfully!"
                echo "Application deployed at: http://localhost:5000"
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace..."
            cleanWs()
        }
    }
}
