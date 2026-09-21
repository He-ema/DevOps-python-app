pipeline{
    agent {label 'Jenkins-Agent'}

    environment {
        SONARQUBE_SCANNER_HOME = tool 'sonarqube-scanner'
    }

    stages{


        stage('Cleanup Workspace'){
      steps{
        cleanWs()
      }
        } 

        stage("Checkout the code from GitHub"){
            steps{
                git branch: 'main', url: 'https://github.com/He-ema/DevOps-python-app' , credentialsId: 'github'
            }
        }

        stage('Install Dependencies') {
    steps {
        sh '''
            python3 -m venv venv
            . venv/bin/activate
            python -m pip install --upgrade pip
            python -m pip install -r requirements.txt
        '''
    }
}

        stage('Run Tests') {
            when {
                expression { return params.RUN_TESTS  }
            }
    steps {
        sh '''
            . venv/bin/activate
            python -m pytest
        '''
    }
}

        stage('SonarQube Analysis') {
    steps {
        script {
            

            withSonarQubeEnv(credentialsId: 'SonarQube') {
                sh """
                    ${SONARQUBE_SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=python-app \
                        -Dsonar.sources=. \
                        -Dsonar.python.version=3.14
                """
            }
        }
    }
}


    }
}