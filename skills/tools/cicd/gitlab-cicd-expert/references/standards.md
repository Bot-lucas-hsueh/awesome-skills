# Standards & Reference

## 7.1 Official Documentation

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [CI/CD YAML Syntax](https://docs.gitlab.com/ee/ci/yaml/)
- [Pipeline Architecture](https://docs.gitlab.com/ee/ci/pipelines/)
- [GitLab Runner](https://docs.gitlab.com/runner/)
- [Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/)
- [CI/CD Examples](https://gitlab.com/explore/categories/continuous-integration/)

## 7.2 Pipeline Syntax

### Basic Structure

```yaml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  GIT_DEPTH: 10

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

test:
  stage: test
  script:
    - npm test
  coverage: '/Coverage: \d+\.\d+%/'
```

### Pipeline Triggers

```yaml
workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
    - if: $CI_COMMIT_TAG

include:
  - local: /.gitlab/ci/template.yml
  - remote: 'https://example.com/remote-template.yml'
```

### DAG Jobs

```yaml
build:
  stage: build
  script: echo "Building..."

test:parallel:
  stage: test
  script: echo "Testing..."
  parallel:
    matrix:
      - TEST_SUITE: unit
      - TEST_SUITE: integration
      - TEST_SUITE: e2e

deploy:
  stage: deploy
  script: echo "Deploying"
  needs:
    - job: test:parallel
      optional: true
```

## 7.3 Best Practices

| Practice | Description |
|----------|-------------|
| **Use DAG** | Use `needs:` for parallel execution |
| **Cache dependencies** | Use `cache: key:` for reuse |
| **Artifacts wisely** | Set expire_in, don't include unnecessary files |
| **Fail fast** | Run unit tests before integration tests |
| **Use templates** | DRY with `include:` for shared configs |

## 7.4 Runner Configuration

```yaml
deploy:
  tags:
    - docker
  only:
    - main
  environment:
    name: production
    url: https://example.com
    on_stop: stop_deploy

stop_deploy:
  stage: deploy
  script: echo "Stopping..."
  environment:
    name: production
    action: stop
  when: manual
```