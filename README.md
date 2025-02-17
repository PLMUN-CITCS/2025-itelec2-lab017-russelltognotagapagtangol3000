# 2025-ITELEC2-LAB017
Week 05 - Working with Functions

Laboratory # 17 - Guided Coding Exercise: Function with Arguments and Return Statement

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 17 - Guided Coding Exercise: Function with Arguments and Return Statement**

   **Objective:**
   - Learn how to define a function that accepts arguments (parameters).
   - Understand the difference between parameters and arguments.
   - Use the return statement to output a value from a function.
   - Practice using the math module for calculations.

   **Desired Output:**
   ```bash
   The area of a circle with radius 5 is: 78.54
   ```
      
   **Notable Observations (to be discussed after completing the exercise):**
   - Parameters vs. Arguments:
      - A parameter is a variable in the function definition (e.g., radius in def circle_area(radius):). It acts as a placeholder for the value that will be passed to the function.
      - An argument is the actual value passed to the function when it is called (e.g., radius_value in circle_area(radius_value)).
   - return Statement: The return statement sends a value back from the function to the place where it was called. This allows you to use the result of the function's calculation in other parts of your code.

   **Python Best Practices**
   - Descriptive Names: Use clear and descriptive names for functions and parameters.
   - Docstrings: Include a docstring for every function to explain its purpose, parameters, and return value.
   - Formatted Output: Format your output to make it more readable and user-friendly. F-strings provide a concise and expressive way to do this.
   - Modular Code: Break down your code into functions to make it more modular, reusable, and easier to understand.
   - Test Thoroughly: Test your functions with different inputs to ensure they work correctly.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `function_arguments_return.py`
      
   2. Import the math module:
      - Use the import statement to import the math module. This gives you access to mathematical constants and functions, including math.pi for the value of π.
```python
import math
```
      
   3. Define the function (circle_area):
      - Use the def keyword followed by the function name (circle_area).
      - Add parentheses () after the function name and include a parameter name (e.g., radius) inside the parentheses. This defines the input that the function will accept.
      - End the line with a colon :.
```python
def circle_area(radius):
```

   4. Add a docstring:
      - Inside the function definition (indented), add a docstring to explain what the function does.
```python
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
```

   5. Calculate the area:
      - Inside the function definition (indented), calculate the area of the circle using the formula: area = π * radius^2. Use math.pi for π and the ** operator for exponentiation (radius squared).
      - Store the calculated area in a variable named area.
```python
    area = math.pi * (radius ** 2)
```

   6. Return the calculated area:
      - Use the return statement followed by the area variable to return the calculated area from the function.
```python
    return area
```

   7. Call the function and display the result:
      - After the function definition (not indented):
         - Define a variable named radius_value and assign it a specific radius (e.g., 5).
         - Call the circle_area() function, passing radius_value as an argument. Store the returned result in a variable named area_result.
         - Use the print() function with an f-string to display the result, formatting the output to two decimal places using the format specifier {area_result:.2f}.
```python
radius_value = 5
area_result = circle_area(radius_value)

print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
```
   8. Complete Code: Combine the steps above to form the complete program.
   9. Run the code: Execute your Python code.
   10. Observe the output: Verify that the output matches the "Desired Output" shown above.

   **Conclusion**
   This exercise demonstrated how to create a user-defined function that accepts arguments (parameters) and returns a value using the return statement.  You learned the difference between parameters and arguments and practiced using the math module for calculations.  Functions with arguments and return values are essential for writing modular and reusable code, making your programs more organized and efficient.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 04 - Laboratory # 17"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
