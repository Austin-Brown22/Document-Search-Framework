pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'python -m pip install paver'
                sh 'python -m paver --version'
                sh 'paver default'
            }
        }
    }
}
