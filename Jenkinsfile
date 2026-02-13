pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat 'python -m unittest discover'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Success Message') {
            steps {
                echo 'Pipeline executed successfully!'
            }
        }
    }
}
