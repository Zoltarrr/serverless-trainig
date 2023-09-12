pipeline {
  agent any
  stages {
    stage('Stage_1') {
      steps {
        echo 'This is $BUILD_NUMBER of demo $DEMO'
        sh 'echo "This is $BUILD_NUMBER of demo $DEMO"'
      }
    }

  }
  environment {
    DEMO = '1'
  }
}