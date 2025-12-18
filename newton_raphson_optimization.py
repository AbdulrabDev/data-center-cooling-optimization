import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definition of Constants and Functions ---
# k_e: Energy coefficient, k_r: Risk coefficient
k_e = 0.001
k_r = 1000

def total_cost(v):
    """
    Total Cost Function f(v) = Energy Cost + Risk Cost
    f(v) = 0.001 * v^3 + 1000 / v
    """
    return k_e * v**3 + k_r / v

def g(v):
    """
    Derivative of the cost function (set to zero for optimization)
    g(v) = f'(v) = 0.003 * v^2 - 1000 / v^2
    """
    return 3 * k_e * v**2 - k_r / v**2

def g_derivative(v):
    """
    Derivative of g(v) for Newton–Raphson method
    g'(v) = 0.006 * v + 2000 / v^3
    """
    return 6 * k_e * v + 2 * k_r / v**3

# --- 2. Newton–Raphson Algorithm ---
def newton_raphson(v0, tolerance=1e-4, max_iter=100):
    v = v0
    print(f"{'Iteration':<10} | {'v (Speed)':<15} | {'Error':<15}")
    print("-" * 45)
    
    for i in range(max_iter):
        v_old = v
        
        # Newton–Raphson formula: v_new = v - g(v) / g'(v)
        numerator = g(v)
        denominator = g_derivative(v)
        
        if denominator == 0:
            print("Error: Derivative is zero. Division by zero!")
            break
            
        v = v - numerator / denominator
        
        # Error calculation
        error = abs(v - v_old)
        
        print(f"{i+1:<10} | {v:<15.6f} | {error:<15.6f}")
        
        if error < tolerance:
            print("-" * 45)
            print(f"RESULT: Convergence achieved. Optimal Speed (v*) = {v:.4f}")
            return v
            
    print("Maximum number of iterations reached.")
    return v

# --- 3. Main Program ---
print("\n--- Data Center Cooling Optimization Started ---\n")

# Initial guess (v0 = 20)
optimal_v = newton_raphson(20)

# Calculate minimum cost at optimal speed
min_cost = total_cost(optimal_v)
print(f"Minimum Total Cost = {min_cost:.4f}")

# --- 4. Plotting (Visualization) ---
# Plot cost function for fan speeds between 10 and 40
v_values = np.linspace(10, 40, 100)
cost_values = total_cost(v_values)

plt.figure(figsize=(10, 6))
plt.plot(v_values, cost_values, label='Total Cost f(v)', linewidth=2)
plt.plot(optimal_v, min_cost, 'ro', label=f'Optimal Point\nv = {optimal_v:.2f}', markersize=8)
plt.ylim(50, 110)

plt.title('Data Center Cooling Cost Optimization')
plt.xlabel('Fan Speed (v)')
plt.ylabel('Total Cost')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
