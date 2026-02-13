pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/tanvishinde017/CodeAlpha_Jenkins_CICD.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Successful') {
            steps {
                echo 'Build Completed Successfully!'
            }
        }
    }
}
