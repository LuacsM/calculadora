pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Verifique o código do repositório
                checkout scm
            }
        }
        stage('Lint e Testes') {
            steps {
                // Execute o script para lint
                bat 'flake8 main.py calculadora_estatistica.py calculadora_mediana.py'
                // Execute os testes
                bat 'python -m unittest discover -s tests'
            }
        }
    }
    post {
        always {
            // Publique resultados dos testes JUnit
            step([$class: 'JUnitResultArchiver', testResults: 'test-reports/**/*.xml'])
        }
    }
}
