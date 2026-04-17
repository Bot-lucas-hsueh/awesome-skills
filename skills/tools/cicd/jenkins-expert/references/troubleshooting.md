# Troubleshooting

## 8.1 Common Failures

### Build Failures

| Error | Cause | Solution |
|-------|-------|----------|
| `Exit code 1` | Script failed | Check shell output, add error handling |
| `java.lang.OutOfMemoryError` | Heap space exhausted | Increase `-Xmx` in Maven/Gradle opts |
| `Connection refused` | Agent offline | Check agent connectivity |
| `No such file or directory` | Wrong workspace | Use relative paths, check `dir()` |
| `Permission denied` | File permissions | Use `sh 'chmod +x'` |

### Agent Issues

| Issue | Fix |
|-------|-----|
| Agent offline | Check Java process, network |
| No executors | Add more executor slots |
| Label not found | Create agent with label |

### Maven/Gradle Issues

```groovy
stage('Build') {
    steps {
        sh 'mvn clean install -DskipTests=false -U'
    }
}

// With retry
sh script: 'mvn clean package', returnStatus: true
```

## 8.2 Debugging

### Enable Debug Logging

1. Go to: Manage Jenkins > System Log > Add new log recorder
2. Add: `jenkins.model.Jenkins`, `org.jenkinsci.plugins.workflow`

### Interactive Debug

```groovy
stage('Debug') {
    steps {
        sh '''
            echo "=== Environment ==="
            env | sort
            echo "=== Java version ==="
            java -version
            echo "=== Workspace ==="
            ls -la
        '''
        script {
            if (params.DEBUG) {
                echo "Debug mode enabled"
            }
        }
    }
}
```

### Pipeline Debug

```groovy
pipeline {
    options {
        // Enable step logs
        timestamps()
    }
    stages {
        stage('Debug') {
            steps {
                echo "Current directory: ${pwd()}"
                echo "Build number: ${env.BUILD_NUMBER}"
            }
        }
    }
}
```

## 8.3 Credentials Troubleshooting

| Problem | Fix |
|---------|-----|
| Credentials not found | Check credential ID matches |
| Secret not masked | Use `mask-passwords` plugin |
| Token expired | Regenerate API token |

### Debug Credentials

```groovy
stage('Test Creds') {
    steps {
        withCredentials([string(credentialsId: 'my-creds', variable: 'TOKEN')]) {
            sh 'echo $TOKEN'
        }
    }
}
```

## 8.4 Shared Library Issues

| Issue | Fix |
|-------|-----|
| Class not found | Add `@Library` annotation |
| Method not defined | Check library version |
| Groovy syntax error | Validate in Jenkins script console |

### Debug Shared Library

```groovy
// In Jenkins script console
library 'my-shared-library'
def myVar = new com.example.MyClass()
echo myVar.hello()
```