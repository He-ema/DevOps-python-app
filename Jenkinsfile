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

        stage("install dependencies"){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }
    }
}