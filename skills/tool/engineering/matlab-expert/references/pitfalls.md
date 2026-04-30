# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | Not preallocating arrays | 🔴 High | Initialize with `zeros`, `NaN`, `cell` |
| 2 | Using loops instead of vectorization | 🟡 Medium | Use `.` operators, `arrayfun` |
| 3 | Comparing floats with `==` | 🔴 High | Use tolerance: `abs(a-b) < eps` |
| 4 | Not clearing variables in loops | 🟡 Medium | Use `clear` or unique names |
| 5 | Magic numbers in code | 🟡 Medium | Use constants |
| 6 | No input validation | 🟡 Medium | Use `arguments` block |

## 10.2 Anti-Patterns

### Loop vs Vectorization

```matlab
% BAD: Slow loop
result = zeros(1, 10000);
for i = 1:10000
    result(i) = sin(i * 0.1);
end

% GOOD: Vectorized
result = sin(0.1:0.1:1000);

% GOOD: arrayfun for complex operations
result = arrayfun(@(x) complexFunc(x), input);
```

### Variable Naming

```matlab
% BAD: Unclear names
x = 5;
y = 10;
z = x * y;

% GOOD: Descriptive names
width = 5;
height = 10;
area = width * height;
```

## 10.3 Performance Tips

| Technique | Use Case | Command |
|-----------|----------|---------|
| Preallocation | Loop-heavy code | `zeros`, `NaN`, `cell` |
| Vectorization | Loop replacements | `.^`, `.*`, `./` |
| GPU arrays | Large matrix ops | `gpuArray`, `gather` |
| Parallel | Embarrassingly parallel | `parfor`, `spmd` |

## 10.4 Best Practices

```
Code Organization:
□ Use functions for reusable code
□ Group related code in scripts
□ Use meaningful variable names
□ Add header comments

Performance:
□ Preallocate all arrays
□ Vectorize when possible
□ Use appropriate data types
□ Clear unused variables

Error Handling:
□ Validate inputs
□ Use try-catch for risky operations
□ Provide meaningful error messages
□ Log errors for debugging
```
