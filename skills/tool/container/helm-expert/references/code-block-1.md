# yaml Example

```
# templates/job-migrate.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ include "myapp.fullname" . }}-migrate
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
  annotations:
    # This is what defines this resource as a hook
    "helm.sh/hook": pre-upgrade,pre-rollback
    "helm.sh/hook-weight": "-1"  # Run before other hooks
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          command: ["python", "manage.py", "migrate"]
          env:
            {{- range $key, $value := .Values.config }}
            - name: {{ $key }}
              value: {{ $value | quote }}
            {{- end }}
```
