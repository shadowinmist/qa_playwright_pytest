pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 20, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    environment {
        CI = 'true'
    }

    stages {
        stage('Przygotowanie Python') {
            steps {
                sh '''
                    set -eu

                    rm -rf reports test-results
                    mkdir -p reports

                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Instalacja Chromium') {
            steps {
                sh '''
                    .venv/bin/python -m playwright install chromium
                '''
            }
        }

        stage('Testy Playwright') {
            steps {
                sh '''
                    .venv/bin/python -m pytest tests/ \
                        --browser chromium \
                        --junitxml=reports/junit.xml \
                        --output=test-results \
                        --tracing=retain-on-failure \
                        --screenshot=only-on-failure
                '''
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('reports/junit.xml')) {
                    junit testResults: 'reports/junit.xml'
                }
            }

            archiveArtifacts(
                artifacts: 'reports/**,test-results/**',
                allowEmptyArchive: true
            )
        }
    }
}