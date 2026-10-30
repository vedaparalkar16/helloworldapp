
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\veda\\AppData\\Local\\Programs\\Python\\Python310\\python.exe'
        DOCKER_IMAGE = 'uat-hello'
    }

    stages {

        stage('1. GitHub Checkout') {
            steps {
                echo 'Pulling project from GitHub'
                checkout scm
            }
        }

        stage('2. Check Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('3. Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install pytest evidently pandas scikit-learn'
            }
        }

        stage('4. Run Application') {
            steps {
                bat '"%PYTHON%" hello.py'
            }
        }

        stage('5. Run Pytest') {
            steps {
                bat '"%PYTHON%" -m pytest -v -s'
            }
        }

        stage('6. Evidently Monitoring') {
            steps {
                bat '"%PYTHON%" monitor.py'
            }
        }

        stage('7. Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('8. Run Docker Container') {
            steps {
                bat 'docker run --rm %DOCKER_IMAGE%'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'monitoring_report.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'UAT PIPELINE COMPLETED SUCCESSFULLY!'
        }

        failure {
            echo 'UAT PIPELINE FAILED. CHECK CONSOLE OUTPUT.'
        }
    }
}
