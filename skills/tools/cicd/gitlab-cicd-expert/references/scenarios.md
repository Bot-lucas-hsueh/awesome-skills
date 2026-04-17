# Examples

## 10.1 Basic CI Pipeline

```yaml
stages:
  - build
  - test
  - deploy

variables:
  NODE_VERSION: "20"
  GIT_DEPTH: 10

build:
  stage: build
  image: node:$NODE_VERSION
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour
  cache:
    key: npm-${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/

test:unit:
  stage: test
  image: node:$NODE_VERSION
  script:
    - npm ci
    - npm run test:unit
  coverage: '/Statements\s*:\s*([^%]+)/'
  cache:
    key: npm-${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/

test:integration:
  stage: test
  image: node:$NODE_VERSION
  script:
    - npm ci
    - npm run test:integration
  needs:
    - build

deploy:
  stage: deploy
  script:
    - ./deploy.sh production
  environment:
    name: production
    url: https://example.com
  only:
    - main
```

## 10.2 Multi-Stage Pipeline with DAG

```yaml
stages:
  - build
  - test
  - security
  - deploy

build:app:
  stage: build
  script:
    - npm ci && npm run build

build:image:
  stage: build
  script:
    - docker build -t $IMAGE_TAG .
  needs: []

test:unit:
  stage: test
  script: npm run test:unit
  needs: [build:app]

test:e2e:
  stage: test
  script: npm run test:e2e
  needs: [build:app]

scan:SAST:
  stage: security
  script: npm run security:scan
  needs: [build:app]

scan:container:
  stage: security
  script: check-container-scan
  needs: [build:image]

deploy:staging:
  stage: deploy
  script: ./deploy.sh staging
  environment:
    name: staging
  needs: [test:unit, test:e2e]

deploy:prod:
  stage: deploy
  script: ./deploy.sh production
  environment:
    name: production
  needs: [deploy:staging, scan:SAST, scan:container]
  when: manual
```

## 10.3 Parallel Matrix Build

```yaml
test:matrix:
  stage: test
  script: npm run test:$TEST_SUITE
  parallel:
    matrix:
      - TEST_SUITE: [unit, integration, e2e]
        NODE_VERSION: "18"
      - TEST_SUITE: [unit, integration]
        NODE_VERSION: "20"
  cache:
    key: npm-$NODE_VERSION
    paths:
      - node_modules/

lint:
  stage: test
  script: npm run lint
  cache:
    key: npm
    paths:
      - node_modules/
```

## 10.4 Review Apps

```yaml
review:
  stage: deploy
  script:
    - kubectl set image deployment/review-$CI_MERGE_REQUEST_IID app=$IMAGE_TAG
    - echo "Review app deployed"
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    url: https://review-$CI_MERGE_REQUEST_IID.example.com
    on_stop: stop_review
  only:
    - merge_requests

stop_review:
  stage: deploy
  script:
    - kubectl delete deployment/review-$CI_MERGE_REQUEST_IID
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    action: stop
  when: manual
  needs: [review]
```

## 10.5 Template with Include

```yaml
# .gitlab-ci.yml
include:
  - local: /.gitlab/ci/templates/node.yml

stages:
  - build
  - test
  - deploy

deploy:
  extends: .deploy
  environment:
    name: production
```

```yaml
# .gitlab/ci/templates/node.yml
.build:
  image: node:20
  cache:
    key: node_modules
    paths:
      - node_modules/

.build_script:
  script:
    - npm ci
    - npm run build
```