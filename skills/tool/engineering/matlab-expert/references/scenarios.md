# Scenario Examples

## 9.1 Linear System Solution

**User:** "How do I solve a system of linear equations in MATLAB?"

**MATLAB Expert:**
> **Solution:**
>
> ```matlab
> % Ax = b
> A = [3, 2, 1;
>      1, 3, 2;
>      2, 1, 3];
> b = [10; 14; 14];
>
> % Method 1: Matrix division (preferred)
> x = A \ b;
>
> % Method 2: Inverse (less efficient)
> x = inv(A) * b;
>
> % Method 3: LU decomposition
> [L, U, P] = lu(A);
> y = L \ (P * b);
> x = U \ y;
>
> % Verify solution
> residual = norm(A * x - b);
> ```

## 9.2 FFT Signal Analysis

**User:** "How do I analyze the frequency content of a signal?"

**MATLAB Expert:**
> **FFT Analysis:**
>
> ```matlab
> % Signal parameters
> Fs = 1000;           % Sampling frequency (Hz)
> T = 1/Fs;            % Sampling period
> L = 1500;            % Signal length
> t = (0:L-1)*T;      % Time vector
>
> % Create signal: 50 Hz + 120 Hz + noise
> signal = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t) + 0.5*randn(size(t));
>
> % Compute FFT
> Y = fft(signal);
> P2 = abs(Y/L);
> P1 = P2(1:L/2+1);
> P1(2:end-1) = 2*P1(2:end-1);
>
> % Frequency axis
> f = Fs*(0:(L/2))/L;
>
> % Plot
> plot(f, P1)
> title('Single-Sided Amplitude Spectrum')
> xlabel('Frequency (Hz)')
> ylabel('|P1(f)|')
> ```

## 9.3 Optimization Problem

**User:** "How do I minimize a function with constraints?"

**MATLAB Expert:**
> **Constrained Optimization:**
>
> ```matlab
> % Objective: minimize f(x) = (x1-1)^2 + (x2-2)^2
> fun = @(x) (x(1)-1)^2 + (x(2)-2)^2;
>
> % Constraints
> A = [1, 2];           % Linear inequality: A*x <= b
> b = 2;
> Aeq = [1, 1];         % Linear equality: Aeq*x = beq
> beq = 1;
>
> % Bounds
> lb = [0, 0];          % Lower bounds
> ub = [5, 5];          % Upper bounds
>
> % Initial guess
> x0 = [0.5, 0.5];
>
> % Solve
> options = optimoptions('fmincon', ...
>     'Display', 'iter', ...
>     'Algorithm', 'sqp');
>
> [x, fval, exitflag] = fmincon(fun, x0, A, b, Aeq, beq, lb, ub, [], options);
>
> % Results
> fprintf('Optimal x: [%f, %f]\n', x(1), x(2));
> fprintf('Optimal f(x): %f\n', fval);
> ```
