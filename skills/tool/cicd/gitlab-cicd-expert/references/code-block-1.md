# yaml Example

```
stages:
  - lint
  - build
  - test
  - security
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"
  NODE_VERSION: "20"

default:
  image: node:${NODE_VERSION}
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
  retry:
    max: 2
    when:
      - runner_system_failure
      - stuck_or_timeout_failure

lint:
  stage: lint
  script:
    - npm ci
    - npm run lint
  allow_failure: false

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 week

test:
  stage: test
  script:
    - npm ci
    - npm run test
  coverage: '/Statements\s*:\s*([^%]+)/'
  artifacts:
    reports:
      junit: junit.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

security:
  stage: security
  script:
    - npm audit --audit-level=high
  allow_failure: true

deploy:
  stage: deploy
  script:
    - echo "Deploying to $CI_ENVIRONMENT_SLUG"
    - ./deploy.sh
  environment:
    name: production
    url: https://example.com
    on_stop: stop_deploy
  only:
    - main
  when: manual

stop_deploy:
  stage: deploy
  script:
    - echo "Stopping deployment"
  environment:
    name: production
    action: stop
  when: manual
```
