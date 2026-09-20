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
                expression { params.RUN_TESTS == 'true' }
            }
    steps {
        sh '''
            . venv/bin/activate
            python -m pytest
        '''
    }
}

    }
}