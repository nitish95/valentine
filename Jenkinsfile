pipeline {
    agent any

    environment {
        IMAGE_NAME = "valentine-site"
        CONTAINER_NAME = "valentine-container"
        PORT = "8082"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d \
                -p $PORT:80 \
                --name $CONTAINER_NAME \
                $IMAGE_NAME
                '''
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building Valentine Site..."
            }
        }
    }
}
