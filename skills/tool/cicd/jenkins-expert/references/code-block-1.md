# groovy Example

```
podTemplate(
    label: 'jenkins-agent',
    imagePullPolicy: 'IfNotPresent',
    containers: [
        containerTemplate(
            name: 'jnlp',
            image: 'jenkins/inbound-agent:latest',
            workingDir: '/home/jenkins/agent',
            resourceRequestCpu: '500m',
            resourceLimitCpu: '1000m',
            resourceRequestMemory: '512Mi',
            resourceLimitMemory: '1Gi'
        ),
        containerTemplate(
            name: 'node',
            image: 'node:20-alpine',
            command: 'cat',
            ttyEnabled: true
        ),
        containerTemplate(
            name: 'docker',
            image: 'docker:24-dind',
            command: 'dockerd-entrypoint.sh',
            ttyEnabled: true,
            privileged: true
        )
    ]
) {
    node('jenkins-agent') {
        stage('Build') {
            container('node') {
                sh 'npm ci && npm run build'
            }
        }
        
        stage('Build Docker') {
            container('docker') {
                sh 'docker build -t myapp:latest .'
            }
        }
    }
}
```
