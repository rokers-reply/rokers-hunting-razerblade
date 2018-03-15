pipeline {
  agent {
    docker {
      image 'python:3.6.4-alpine3.6'
    }
    
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building output files'
        sh 'python3 libs.py'
        sh 'python3 parsing.py'
        archiveArtifacts '*.py'
      }
    }
  }
}
