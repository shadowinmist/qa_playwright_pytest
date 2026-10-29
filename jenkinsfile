pipeline {
    agent any

    stages {
        stage('Sprawdzenie repozytorium') {
            steps {
                echo 'Jenkins pobrał projekt z GitHuba!'
                sh '''
                    pwd
                    ls -la
                    git log -1 --oneline
                '''
            }
        }
    }
}