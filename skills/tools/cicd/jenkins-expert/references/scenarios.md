# Examples

## 10.1 Declarative Pipeline

```groovy
pipeline {
    agent {
        docker {
            image 'maven:3.9-eclipse-temurin-17'
            args '-v /root/.m2:/root/.m2'
        }
    }
    
    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }
    
    environment {
        MAVEN_OPTS = '-Xmx1024m'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'mvn clean package -DskipTests'
            }
        }
        
        stage('Test') {
            steps {
                sh 'mvn test'
            }
            post {
                always {
                    junit '**/target/surefire-reports/*.xml'
                    publishHTML(target: [
                        reportDir: 'target/site/jacoco',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'mvn deploy'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            emailext(
                subject: "Build Success: ${env.JOB_NAME}",
                body: "Build ${env.BUILD_NUMBER} succeeded",
                to: 'team@example.com'
            )
        }
        failure {
            emailext(
                subject: "Build Failed: ${env.JOB_NAME}",
                body: "Build ${env.BUILD_NUMBER} failed",
                to: 'team@example.com'
            )
        }
    }
}
```

## 10.2 Parallel Stages with Shared Library

```groovy
@Library('shared-library') _

pipeline {
    agent any
    
    stages {
        stage('Build') {
            parallel {
                stage('Frontend') {
                    steps {
                        script {
                            common.node('20') {
                                sh 'cd frontend && npm install && npm run build'
                            }
                        }
                    }
                }
                stage('Backend') {
                    steps {
                        script {
                            common.node('17') {
                                sh 'cd backend && mvn clean package'
                            }
                        }
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm run test:integration'
            }
        }
        
        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```

## 10.3 Docker Build and Push

```groovy
pipeline {
    agent any
    
    environment {
        REGISTRY = 'docker.io'
        IMAGE_NAME = 'myapp'
        CREDENTIALS = credentials('docker-hub')
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker run -d --name test-app $IMAGE_NAME:$BUILD_NUMBER'
                sh 'sleep 5 && curl http://localhost:8080/health'
                sh 'docker stop test-app'
            }
        }
        
        stage('Push') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    echo $CREDENTIALS_PSW | docker login -u $CREDENTIALS_USR --password-stdin $REGISTRY
                    docker tag $IMAGE_NAME:$BUILD_NUMBER $REGISTRY/$IMAGE_NAME:latest
                    docker push $REGISTRY/$IMAGE_NAME:latest
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker rmi $IMAGE_NAME:$BUILD_NUMBER || true'
        }
    }
}
```

## 10.4 Matrix Build

```groovy
multiJob('matrix-build') {
    axes {
        axis('JDK_VERSION', ['11', '17', '21'])
        axis('OS', ['linux', 'windows'])
    }
    
    steps {
        conditionalSteps {
            condition {
                expression { return OS == 'linux' }
            }
            steps {
                shell('build.sh')
            }
        }
        conditionalSteps {
            condition {
                expression { return OS == 'windows' }
            }
            steps {
                batchFile('build.bat')
            }
        }
    }
}
```

## 10.5 Shared Library

```groovy
// vars/common.groovy
def node(String version, Closure body) {
    node("jdk-${version}") {
        body()
    }
}

def mavenBuild(String goals) {
    sh "mvn ${goals} -B"
}

return this
```

```groovy
// Jenkinsfile using shared library
@Library('my-shared-library') _

pipeline {
    agent any
    
    stages {
        stage('Build with JDK 17') {
            steps {
                script {
                    common.node('17') {
                        common.mavenBuild('clean package')
                    }
                }
            }
        }
    }
}
```

## 10.6 Kubernetes Deployment

```groovy
pipeline {
    agent any
    
    environment {
        KUBECONFIG = credentials('kubeconfig')
    }
    
    stages {
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                sh 'kubectl apply -f k8s/staging/ -n staging'
                sh 'kubectl rollout status deployment/app -n staging'
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            input {
                message "Deploy to production?"
                ok "Deploy"
            }
            steps {
                sh 'kubectl apply -f k8s/production/ -n production'
                sh 'kubectl rollout status deployment/app -n production'
            }
        }
    }
}
```