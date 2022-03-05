pipeline {
    agent any

    stages {

        stage('Build Docker image') {
            
            steps {
                sh '''
                docker-compose build
                '''
            }

        }
        
        stage('Run tests') {
            
            steps {
                sh '''
                python -m pytest test/test_model.py
                '''
            }

        }
        
        stage('Run Docker image') {
            
            steps {
                sh '''
                docker-compose up
                '''
            }

        }
        
    }
}
