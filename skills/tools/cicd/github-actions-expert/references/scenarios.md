# Examples

## 10.1 Full CI Pipeline

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linter
        run: npm run lint
      
      - name: Check formatting
        run: npm run format:check

  test:
    runs-on: ubuntu-latest
    needs: lint
    strategy:
      matrix:
        node: [18, 20]
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test -- --coverage
        env:
          NODE_ENV: test
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info

  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      
      - name: Build application
        run: npm run build
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-artifacts
          path: dist/
          retention-days: 7

  build-image:
    runs-on: ubuntu-latest
    needs: build
    if: github.event_name == 'push' && (github.ref == 'refs/heads/main')
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      
      - name: Download artifacts
        uses: actions/download-artifact@v4
        with:
          name: build-artifacts
          path: dist/
      
      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

## 10.2 Deployment Pipeline

```yaml
name: Deploy

on:
  workflow_dispatch:
    inputs:
      environment:
        type: choice
        options: [staging, production]
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment }}
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy application
        env:
          API_URL: ${{ secrets.API_URL }}
          API_KEY: ${{ secrets.API_KEY }}
        run: |
          echo "Deploying to ${{ github.event.inputs.environment }}"
          ./deploy.sh ${{ github.event.inputs.environment }}

      - name: Verify deployment
        run: |
          curl -f $API_URL/health || exit 1

  notify:
    runs-on: ubuntu-latest
    needs: deploy
    if: always()
    steps:
      - name: Send notification
        if: needs.deploy.result == 'failure'
        run: echo "Deployment failed"
```

## 10.3 Scheduled Maintenance

```yaml
name: Scheduled Dependency Update

on:
  schedule:
    - cron: '0 8 * * 1'
  workflow_dispatch:

jobs:
  dependency-update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Check for updates
        run: |
          npm outdated || true
          pip list --outdated || true
      
      - name: Create PR
        run: |
          gh pr create --title "Update dependencies" --body "Automated dependency check"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  cleanup-artifacts:
    runs-on: ubuntu-latest
    steps:
      - name: Clean old artifacts
        uses: actions/github-script@v7
        with:
          script: |
            const { owner, repo } = context.repo;
            const artifacts = await github.rest.actions.listArtifacts({
              owner, repo,
              per_page: 100
            });
            for (const art of artifacts.data) {
              if (art.expired) {
                await github.rest.actions.deleteArtifact({
                  owner, repo,
                  artifact_id: art.id
                });
              }
            }
```

## 10.4 Parallel Job Configuration

```yaml
jobs:
  test-unit:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        test: [unit1, unit2, unit3, unit4]
    steps:
      - run: npm test -- --testPathPattern=${{ matrix.test }}

  test-integration:
    runs-on: ubuntu-latest
    needs: test-unit
    steps:
      - run: npm test -- --testPathPattern=integration

  lint:
    runs-on: ubuntu-latest
    steps:
      - run: npm run lint

  lint-and-test:
    runs-on: ubuntu-latest
    needs: [lint, test-integration]
    if: always()
    steps:
      - run: echo "All checks passed"