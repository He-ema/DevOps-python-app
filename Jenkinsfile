pipeline{
    agent {label 'Jenkins-Agent'}
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

        stage('SonarQube Analysis'){
      steps{
        script{
          withSonarQubeEnv(credentialsId: 'SonarQube') {
    sh 'mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar'
}
        }
      }
    }


    }
}