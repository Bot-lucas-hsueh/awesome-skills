# Glossary

## Core Concepts

### Chart
A package of Kubernetes resources that can be deployed as a unit. Contains templates, values, and metadata.

### Release
A specific instance of a chart deployed to a Kubernetes cluster. Multiple releases of the same chart can coexist.

### Repository
A collection of charts that can be downloaded. Default repository is https://charts.helm.sh.

### Values
Configuration values that customize chart behavior. Specified in values.yaml or via --set.

### Template
A Kubernetes manifest with Go template syntax that generates actual YAML based on values.

### Hook
A resource that executes at specific points in the release lifecycle (pre-install, post-install, etc.).

## Chart Components

### Chart.yaml
Metadata file containing chart name, version, description, and maintainer information.

### values.yaml
Default configuration values. These are merged with user-provided values during installation.

### values.schema.json
JSON schema that validates values.yaml structure and types.

### _helpers.tpl
Template file containing reusable named templates (functions) used across the chart.

### NOTES.txt
Instructions displayed after successful installation. Located in templates/ directory.

### requirements.yaml (deprecated)
Old format for declaring chart dependencies. Replaced by Chart.yaml dependencies.

## Template Syntax

### Dot Notation
Access to chart metadata: `.Chart.Name`, `.Release.Name`, `.Values.image`

### Pipeline
Chain of functions: `{{ .Values.tag | default "latest" | quote }}`

### Named Templates
Reusable template blocks defined with `{{- define "name" }}...{{- end }}`

### Include Function
Includes a named template: `{{ include "mychart.labels" . }}`

### Tpl Function
Renders a string as a template: `{{ .Values.templateString | tpl . }}`

## Lifecycle

### Install
Creating a new release from a chart.

### Upgrade
Updating an existing release to a new chart version or values.

### Rollback
Reverting a release to a previous revision.

### Uninstall
Removing a release and its resources.

### History
List of all revisions (versions) of a release.

### Hook Lifecycle
pre-install → install → post-install → pre-upgrade → upgrade → post-upgrade → pre-rollback → rollback → post-rollback → pre-uninstall → uninstall → post-uninstall

## Dependencies

### Subchart
A chart that is included as a dependency in another chart.

### Parent Chart
The main chart that includes dependencies.

### Lock File
requirements.lock - locks dependency versions to ensure reproducible builds.

### Repository Index
index.yaml - index of all charts in a repository.

## Release Management

### Revision
A numbered version of a release. Increment on each upgrade.

### Dry Run
Simulates an install/upgrade without making changes. Used for testing.

### Rollback Strategy
Policy for handling rollbacks (automatic, manual).

### Release Name
Identifier for a release. Must be unique within a namespace.

## Testing

### Lint
Static analysis of chart for errors and best practices.

### Test
Hook-based tests that run against deployed resources.

### Dry-run
Server-side rendering check without applying.

### Show values
Display merged values for debugging.

## Security

### Secrets
Sensitive data that should not be stored in values files.

### Hook Deletion Policy
Controls when hooks are deleted (before-hook-creation, hook-succeeded, hook-failed, hook-crashed).

### RBAC
Role-based access control for Helm operations.

## Distribution

### Chart Museum
Open-source Helm chart repository server.

### Artifact Hub
Public registry for Helm charts and other packages.

### OCI Registry
Support for storing charts in OCI registries (Docker Hub, GCR, etc.).

## Advanced

### Library Chart
Type of chart that provides utilities without deploying resources directly.

### Crds
Custom Resource Definitions that should be installed before the chart.

### Post Rendering
Extension point for modifying rendered manifests before applying.

### Plugin
Extension to Helm functionality (e.g., diff, secrets, unittest).

## Commands

### create
Creates a new chart with directory structure.

### install
Installs a chart as a release.

### upgrade
Upgrades a release with a new chart version or values.

### rollback
Reverts a release to a previous revision.

### list
Lists all releases in a namespace.

### status
Shows status of a release.

### get
Gets extended information about a release (manifest, values, hooks).

### template
Renders chart templates locally.

### lint
Validates chart syntax and best practices.

### package
Packages a chart into a tarball.

### dependency
Manages chart dependencies (update, build, list).

### repo
Manages chart repositories (add, list, remove, update).