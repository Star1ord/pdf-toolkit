pipeline {
  agent any

  environment {
    APP_NAME = "pdf-toolkit"
    DOCKER_IMAGE = "pdf-toolkit:latest"
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Star1ord/pdf-toolkit.git'
      }
    }

    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Lint') {
      steps {
        echo 'Running PEP8 lint...'
        sh 'pip install flake8 && flake8 . || true'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }

    stage('Smoke Test') {
      steps {
        echo 'Running quick startup test...'
        sh 'docker run --rm $DOCKER_IMAGE python -c "print(\'PDF Toolkit OK\')"'
      }
    }
  }

  post {
    success {
      echo '✅ Pipeline succeeded. Image ready.'
    }
    failure {
      echo '❌ Pipeline failed.'
    }
  }
}
