pipeline {
    agent any

    stages {
        stage('start') {
          agent any
            steps {
              script {
                def attachments = [
                  [
                    text: 'start',
                    fallback: 'Hey, Vader seems to be mad at you.',
                    color: '#ff0000'
                  ]
                ]

                slackSend(channel: "#cicd", attachments: attachments)
              }
            }
        }
        stage('ci') {
            steps {
              sh '''
              python3 -m venv venv
              . venv/bin/activate
              pip install -r requirements.txt
              pylint $(git ls-files 'hello.py') 
              pytest
              coverage run -m pytest
              coverage report
              coverage html
              '''
            }
        }
        stage('deploy') {
            steps {
              sshagent (credentials: ['cicd-pem-username']){
                sh '''
                ssh -o "StrictHostKeyChecking no" ec2-user@43.200.70.100 "cd cicd && git pull"
                '''
              }
            }
        }
        stage('end') {
          agent any
            steps {
              script {
                def attachments = [
                  [
                    text: 'end',
                    fallback: 'Hey, Vader seems to be mad at you.',
                    color: '#ff0000'
                  ]
                ]

                slackSend(channel: "#cicd", attachments: attachments)
              }
            }
        }
    }
}