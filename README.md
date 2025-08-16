Name : Shreyash Rajendra Wadibhasme 
Company : Codtech IT solutions
Id : CT08DG1782 
Domain : Python programming
Duration : june to august 2025
Mentor : Neela Santosh Kumar

## **Project Overview: Automated Report Generation**
![task2photo](https://github.com/user-attachments/assets/3bd77af3-43f1-4df3-a044-246773b7a143)

### **Objective**

The project automates the process of generating an **Internship Completion Certificate Report** in PDF format. It reads student performance data from a CSV file, analyzes the scores, and creates a professional report that includes both individual results and overall statistics.


### **Key Components**

1. **Data Input (CSV Handling)**
   * Reads student data from a `.csv` file (e.g., `data.csv`).
   * Columns:
     * **Name** – Student’s name.
     * **Score** – Performance score.

2. **Data Analysis**
   * Uses Python’s `statistics` module to calculate:
     * Total number of students
     * Average score (Mean)
     * Median score
     * Standard deviation
     * Minimum and maximum score

3. **Report Generation (PDF Creation)**
   * Utilizes the **FPDF** library to create a formatted PDF.
   * Report includes:
     * Title: *Internship Completion Certificate*
     * Table of student names and scores
     * Statistical summary of performance
     * Internship end date (entered by user)

4. **User Interaction**
   * Asks the user for:
     * CSV file name (e.g., `data.csv`)
     * Output PDF file name (e.g., `report.pdf`)
     * Internship end date (e.g., `31-07-2025`)
   * Generates a PDF automatically with all details.

### **Technologies Used**
* **Python**
* **CSV module** → Read student data
* **Statistics module** → Calculate mean, median, stdev
* **FPDF** → Generate PDF report

### **Applications**

* Automates **internship performance reporting**.
* Can be adapted for **academic certificates**, **exam reports**, or **employee performance reviews**.
* Reduces manual work in preparing structured reports.
