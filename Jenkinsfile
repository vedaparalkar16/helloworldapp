
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t uat-hello .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm uat-hello'
            }
        }
    }
}
