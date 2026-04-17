# Glossary

## Container Basics

### Container
A lightweight, standalone, executable package that includes everything needed to run a piece of software: code, runtime, system tools, libraries, and settings.

### Image
A read-only template used to create containers. Images are built from a Dockerfile and can contain multiple layers.

### Layer
A modification to an image, represented as an instruction in a Dockerfile. Layers are stacked to create the final image.

### Tag
A label applied to an image version, typically in the format `name:version` (e.g., `nginx:1.25`).

### Registry
A storage and distribution system for Docker images. Examples: Docker Hub, Google Container Registry (GCR), Amazon ECR.

### Digest
A unique identifier for an image content, formatted as `sha256:...`. Used for immutable image references.

## Dockerfile Instructions

### FROM
Defines the base image for the build. Must be the first instruction.

### RUN
Executes commands in a new layer and commits the results. Used for installing packages.

### COPY
Copies files from the build context into the container.

### ADD
Similar to COPY but with additional features (remote URLs, auto-extraction of tar files). Prefer COPY.

### CMD
Specifies the default command to run when a container starts. Only the last CMD is effective.

### ENTRYPOINT
Configures a container to run as an executable. Arguments from CMD or CLI are appended.

### WORKDIR
Sets the working directory for subsequent instructions.

### ENV
Sets environment variables that persist when a container runs.

### EXPOSE
Documents which ports the container listens on at runtime.

### LABEL
Adds metadata to an image as key-value pairs.

### USER
Sets the user (or UID) for running commands in the container.

### VOLUME
Creates a mount point for external storage.

### ARG
Defines variables that users can pass to the builder with `docker build --build-arg`.

## Docker Compose

### Service
A container definition in docker-compose, representing a single component of the application.

### Volume
A persistent data storage mechanism, defined at the top level and mounted into services.

### Network
A communication layer between services, defined at the top level.

### Build
Configuration for building an image from a Dockerfile, used instead of `image` in services.

### Depends_on
Defines startup order between services. Container waits for dependencies to start.

### Healthcheck
Defines a command to verify service health, used by `depends_on` condition.

## BuildKit

### Cache Mount
A BuildKit feature that caches package manager data between builds for faster rebuilds.

### Secret
A BuildKit feature for passing sensitive data during build without baking into image.

### Multi-platform Build
Building images for multiple architectures (amd64, arm64) in a single command.

### Build Context
The set of files sent to the Docker daemon for building an image.

### Squash
Combining all layers into a single layer to reduce image size (deprecated in favor of cache).

## Networking

### Bridge Network
The default network driver. Creates a software bridge on the host.

### Host Network
Removes network isolation between container and host.

### Overlay Network
Connects containers across multiple Docker hosts (used with Swarm).

### Macvlan Network
Assigns a MAC address to containers, allowing them to appear as physical devices.

## Security

### Non-root User
Running containers as a non-privileged user to reduce security risk.

### Read-only Root Filesystem
Mounting container root filesystem as read-only to prevent modifications.

### Capabilities
Linux kernel capabilities that can be granted to containers. Should drop ALL and add only what's needed.

### Seccomp
Linux kernel feature that filters system calls. Docker provides a default profile.

### AppArmor
Linux security module for restricting program capabilities.

### SELinux
Security-enhanced Linux - mandatory access control system.

## Storage

### Bind Mount
Mounts a host file or directory into the container.

### Named Volume
Docker-managed storage that persists independently of containers.

### tmpfs Mount
Stores data in memory, useful for sensitive data that shouldn't persist.

## Orchestration

### Docker Swarm
Docker's native clustering and orchestration solution.

### Compose
Docker's tool for defining multi-container applications.

### Service
In Swarm, a definition of the desired state for a task.

### Task
A single container running in Swarm.

### Node
A Docker engine participating in a Swarm cluster.

## Troubleshooting Terms

### OOMKilled
Container terminated due to out-of-memory (OOM) killer.

### Exit Code
Numeric value returned when a container exits. 0=success, non-zero=error.

### Log Driver
Mechanism for capturing container logs (json-file, syslog, journald).

### Daemon
The background Docker service (dockerd) that manages containers.

### Build Context
Files and directories available during image build.

### Layer Cache
Docker's mechanism for reusing layers between builds.

## Advanced

### Distroless Image
Minimal images containing only the application and runtime dependencies, no shell or package managers.

### Scratch Image
Empty base image, used for statically compiled binaries.

### Multi-stage Build
Using multiple FROM statements to separate build and runtime environments.

### Sidecar Pattern
Container that runs alongside the main container to provide auxiliary functionality.

### Init Container
Container that runs before main containers to perform setup tasks.

### Health Check
Command that determines if container is healthy.

### Liveness Probe
Kubernetes concept - checks if container needs to be restarted.

### Readiness Probe
Kubernetes concept - checks if container can receive traffic.

### Startup Probe
Kubernetes concept - checks if container has started (for slow-starting apps).