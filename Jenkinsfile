pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Linting') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 main.py calculadora_estatistica.py calculadora_mediana.py'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pip install -r requirements.txt'  // Instale as dependências de teste, se necessário
                sh 'python -m unittest discover -s tests'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/nosetests.xml', allowEmptyArchive: true
            junit '**/nosetests.xml'
        }
    }
}
