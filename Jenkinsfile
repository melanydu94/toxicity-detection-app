pipeline {
    agent any

    stages {
	
        stage('Clear Docker Images') {
            steps {
                sh '''
                docker rmi -f $(docker images -q)
                '''
            }
        }
        stage('Run tests') {
            
            steps {
                sh '''
                pip install -r server/requirements.txt
                python -m pytest test/test_model.py
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
