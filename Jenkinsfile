pipeline {
    agent any

    stages {

        stage('Build Docker image') {
            
            steps {
                sh '''
                export PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/local/bin/
                docker-compose build
                '''
            }

        }
        
        stage('Run tests') {
            
            steps {
                sh '''
                source /path/to/ENV/bin/activate
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
