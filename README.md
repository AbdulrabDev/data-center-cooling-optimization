# 🔧 Data Center Cooling Optimization

This project focuses on improving **energy efficiency in data center cooling systems**
by finding the optimal fan speed that minimizes **total cost**.

---

## 🧠 Problem Overview
In data centers, cooling systems face a critical trade-off:

- 🔻 **Low fan speed** → Higher hardware failure risk  
- 🔺 **High fan speed** → Excessive energy consumption  

The goal is to find the **optimal fan speed** that balances these two opposing factors.

---

## 📐 Mathematical Model
The total cost function is modeled as:

- ⚡ Energy Cost ∝ v³  
- 🔥 Risk Cost ∝ 1 / v  

This results in a nonlinear optimization problem.

---

## 🚀 Method Used
To solve the problem numerically, the **Newton–Raphson method** was applied:

- Fast quadratic convergence
- Efficient root-finding for nonlinear equations
- Suitable for engineering optimization problems

---

## 🧪 Results
✅ The algorithm converged in only a few iterations  
✅ The optimal fan speed was found to be approximately:

> **v ≈ 24**

This value represents the most efficient operating point for the system.

---

## 🛠 Tools & Technologies
- 🐍 Python  
- 📊 Numerical Analysis  
- 📈 Optimization Methods  
- 🔢 Newton–Raphson Algorithm  

---

## 📁 Project Files
- `newton_raphson_optimization.py` → Python implementation  
- `project_report.pdf` → Detailed technical report  
- `project_presentation.pptx` → Project presentation slides  

---

## 💡 What I Learned
- Translating real-world engineering problems into mathematical models  
- Applying numerical methods to optimization problems  
- Interpreting convergence behavior and error analysis  

---

📌 *This project was developed as part of a Numerical Analysis course, focusing on real-world engineering applications.*
