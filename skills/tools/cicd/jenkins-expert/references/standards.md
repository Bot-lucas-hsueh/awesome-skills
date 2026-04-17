# Standards & Reference

## 7.1 Official Documentation

- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Pipeline Steps Reference](https://www.jenkins.io/doc/pipeline/steps/)
- [Declarative Pipeline](https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline)
- [Scripted Pipeline](https://www.jenkins.io/doc/book/pipeline/syntax/#scripted-pipeline)
- [Jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/)

## 7.2 Pipeline Syntax

### Declarative Pipeline

```groovy
pipeline {
    agent any
    
    environment {
        JAVA_HOME = '/usr/lib/jvm/java-17'
    }
    
    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
            post {
                success {
                    echo 'Build successful!'
                }
            }
        }
        
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
    
    post {
        always {
            junit '**/target/surefire-reports/*.xml'
        }
    }
}
```

### Scripted Pipeline

```groovy
node {
    stage('Checkout') {
        checkout scm
    }
    
    stage('Build') {
        sh 'mvn clean package'
    }
    
    stage('Test') {
        try {
            sh 'mvn test'
        } finally {
            junit '**/target/surefire-reports/*.xml'
        }
    }
}
```

### Pipeline Directives

| Directive | Description |
|-----------|-------------|
| `agent` | Where to execute |
| `environment` | Environment variables |
| `options` | Pipeline options |
| `stages` | Stage container |
| `steps` | Actual commands |
| `post` | Post-build actions |
| `when` | Conditional execution |

## 7.3 Best Practices

| Practice | Description |
|----------|-------------|
| **Use Declarative** | Prefer declarative over scripted |
| **Shared Libraries** | Reuse code across pipelines |
| **Agent labels** | Target specific executors |
| **Timeout** | Prevent stuck builds |
| **Clean workspace** | Manage disk space |

## 7.4 Credentials & Security

```groovy
pipeline {
    agent any
    
    environment {
        CREDS = credentials('jenkins-credentials-id')
    }
    
    stages {
        stage('Deploy') {
            steps {
                sh "deploy.sh --token ${CREDS}"
            }
        }
    }
}
```

### Security Domains

- Jenkins internal database
- LDAP/Active Directory
- OAuth/GitHub OAuth
- SAML