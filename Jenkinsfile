pipeline {
    agent any

    stages {

        stage('Run tests') {
            
            steps {
                sh '''
                pip3 --install --upgrade pip
                pip3 install numpy pytest
                python3 -m pytest test/test_model.py
                '''
            }

        }

        stage('Build Docker image') {
            
            steps {
                sh '''
                export PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/local/bin/
                docker-compose build
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
