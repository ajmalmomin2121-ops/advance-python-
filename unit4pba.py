import pandas as pd
import matplotlib.pyplot as plt

# Read employee data from CSV file
df = pd.read_csv("employee.csv")

# Display employee details
print("Employee Details:")
print(df)

# Calculate average salary for each department
avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(avg_salary)

# Plot a bar chart
avg_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


