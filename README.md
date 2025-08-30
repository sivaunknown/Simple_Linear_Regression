# Simple_Linear_Regression
A Mathematical implementation of Simple_Linear_Regression using Python

Here's a **simple and clean explanation** you can use in your `README.md` file for your code:

---

# 📊 Simple Linear Regression (Salary Prediction)

This Python script implements **Simple Linear Regression** from scratch using `NumPy`, `Pandas`, and `Matplotlib`.

It predicts the **salary** of an employee based on their **years of experience**.

---

## ✅ Features

* 📥 Reads salary data from a CSV file
* 📈 Calculates regression line using the **least squares method**
* 📍 Predicts salary for a custom input value
* 📊 Plots:

  * Data points (scatter plot)
  * Best-fit regression line
  * Predicted point with dashed lines to x/y axes
* 📐 Displays model accuracy using **R² Score**

---

## 📁 Data Format

The dataset (`Salary_dataset.csv`) should contain two columns:

| YearsExperience | Salary  |
| --------------- | ------- |
| 1.2             | 39344.0 |
| 2.3             | 39892.0 |
| ...             | ...     |

---

## 🧮 How It Works

1. **Load Data**
   Loads the dataset and splits it into independent variable `x` (Years of Experience) and dependent variable `y` (Salary).

2. **Calculate Parameters**

   * `slope` is calculated using the least squares formula
   * `y_intercept` is computed using mean values

3. **Predict Values**
   Uses the formula:
   **y = mx + c**

   where:

   * `m` = slope
   * `c` = y-intercept

4. **Plot Results**

   * Plots original data and regression line
   * Highlights a predicted salary for a given experience value with a green `X` and dashed guide lines

5. **Evaluate Accuracy**

   * Calculates **R² Score** (model accuracy)

---

## 📷 Example Output

* **Red line** → Regression line
* **Blue dots** → Actual data points
* **Green X** → Predicted point (with dashed lines to x and y axes)
Let me know if you want me to generate a complete `README.md` file or also include setup instructions like required libraries.

