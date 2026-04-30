# yaml Example

```
stages:
  - build
  - test
  - staging
  - production

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/

test:unit:
  stage: test
  script:
    - npm ci
    - npm run test:unit
  coverage: '/Coverage:\s*\d+\.\d+%/'

test:e2e:
  stage: test
  script:
    - npm ci
    - npm run test:e2e
  services:
    - postgres:15
  variables:
    POSTGRES_DB: test
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test

deploy:staging:
  stage: staging
  script:
    - ./deploy.sh staging
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

deploy:production:
  stage: production
  script:
    - ./deploy.sh production
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main
```
