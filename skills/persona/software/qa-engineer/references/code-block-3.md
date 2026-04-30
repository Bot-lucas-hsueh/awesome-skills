# bash Example

```
# --- Jest ---
npx jest --coverage --watch                          # Dev: watch + coverage
npx jest --onlyChanged                               # Test only changed files
npx jest tests/unit/pricing.test.ts --verbose        # Run single test file
npx jest --updateSnapshot                            # Update snapshots

# --- Playwright ---
npx playwright test                                  # Run all E2E tests
npx playwright test --ui                             # Debug mode with UI
npx playwright test --grep "@smoke"                  # Run tagged tests only
npx playwright test checkout.spec.ts --debug         # Debug specific test
npx playwright codegen https://example.com           # Record test from browser

# --- pytest ---
pytest tests/ -v --tb=short                          # Verbose with short tracebacks
pytest tests/ -m "smoke and not slow"                # Run by markers
pytest tests/ --cov=src --cov-report=html --cov-fail-under=80
pytest tests/ -n auto                                # Parallel (requires pytest-xdist)
pytest tests/ --durations=10                         # Show 10 slowest tests

# --- k6 ---
k6 run tests/load/load.js                            # Local load test
k6 run -e BASE_URL=https://staging.example.com tests/load/load.js
k6 run --out cloud tests/load/load.js                # Grafana Cloud output

# --- Mutation Testing ---
npx stryker run                                      # JS/TS mutation score
mutmut run && mutmut results                         # Python mutation score

# --- Flakiness Detection ---
npx playwright test --repeat-each=5 --reporter=json  # Run each test 5x
```
