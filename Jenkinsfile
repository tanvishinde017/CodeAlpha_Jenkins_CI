pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop flask-container || exit 0'
                bat 'docker rm flask-container || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 8000:8000 --name flask-container flask-app'
            }
        }

        stage('Success') {
            steps {
                echo 'Application Deployed Successfully!'
            }
        }
    }
}
