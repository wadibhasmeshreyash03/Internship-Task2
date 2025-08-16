import csv
from statistics import mean, median, stdev
from fpdf import FPDF

# Read data from CSV
def read_data(filename):
    names = []
    scores = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names.append(row['Name'])
            scores.append(float(row['Score']))
    return names, scores

# Analyze data
def analyze(scores):
    return {
        'count': len(scores),
        'mean': mean(scores),
        'median': median(scores),
        'stdev': stdev(scores) if len(scores) > 1 else 0,
        'min': min(scores),
        'max': max(scores)
    }

# Generate PDF report
def generate_pdf(names, scores, stats, output_file, end_date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Internship Completion Certificate", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, "This is to certify that the following students have completed their internship. Below is the summary of their performance.\n")
    pdf.ln(5)
    # Table header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Name", 1)
    pdf.cell(40, 10, "Score", 1, ln=True)
    pdf.set_font("Arial", '', 12)
    # Table rows
    for name, score in zip(names, scores):
        pdf.cell(60, 10, name, 1)
        pdf.cell(40, 10, str(score), 1, ln=True)
    pdf.ln(10)
    # Stats
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Statistics", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Total Students: {stats['count']}", ln=True)
    pdf.cell(0, 10, f"Average Score: {stats['mean']:.2f}", ln=True)
    pdf.cell(0, 10, f"Median Score: {stats['median']:.2f}", ln=True)
    pdf.cell(0, 10, f"Standard Deviation: {stats['stdev']:.2f}", ln=True)
    pdf.cell(0, 10, f"Highest Score: {stats['max']}", ln=True)
    pdf.cell(0, 10, f"Lowest Score: {stats['min']}", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, f"Automated Report Generation - Internship End Date: {end_date}", ln=True)
    pdf.output(output_file)

if __name__ == "__main__":
    csv_file = input("Enter the CSV filename (e.g., data.csv): ")
    output_pdf = input("Enter the output PDF filename (e.g., report.pdf): ")
    end_date = input("Enter the internship end date (e.g., 31-07-2025): ")
    names, scores = read_data(csv_file)
    stats = analyze(scores)
    generate_pdf(names, scores, stats, output_pdf, end_date)
    print(f"Report generated: {output_pdf}")
