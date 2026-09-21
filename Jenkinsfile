pipeline{
    agent {label 'Jenkins-Agent'}

    environment {
        SONARQUBE_SCANNER_HOME = tool 'sonarqube-scanner'
        APP_NAME = "python-app"
        DOCKERHUB_USERNAME = "ohema"
        DOCKERHUB_PASSWORD = "dockerhub"
        BUILD_NUMBER = "${env.BUILD_NUMBER}"
        RELEASE = "1.0.0"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/${APP_NAME}"
        IMAGE_TAG = "${RELEASE}-${BUILD_NUMBER}"
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

        stage("Quality Gate"){
           steps {
               script {
                    waitForQualityGate abortPipeline: false, credentialsId: 'SonarQube'
                }	
            }

        }

        stage("Build & Push Docker Image") {
            steps {
                script {
                    docker.withRegistry('',DOCKERHUB_PASSWORD) {
                        docker_image = docker.build "${IMAGE_NAME}"
                    }
    
                    docker.withRegistry('',DOCKERHUB_PASSWORD) {
                        docker_image.push("${IMAGE_TAG}")
                        docker_image.push('latest')
                    }
                }
            }

       }


    }
}