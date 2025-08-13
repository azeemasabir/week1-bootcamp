import csv

def read_grades(file_path):
    """Reads student grades from a CSV file and returns a list of (name, grade) tuples."""
    grades = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append((row['name'], float(row['grade'])))
    return grades

def calculate_average(grades):
    """Calculates the average grade from a list of (name, grade) tuples."""
    if not grades:
        return 0
    total = sum(grade for _, grade in grades)
    return total / len(grades)

def write_results(grades, output_path, pass_mark=60):
    """Writes Pass/Fail results to a new CSV file."""
    with open(output_path, mode='w', newline='') as file:
        fieldnames = ['name', 'grade', 'result']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for name, grade in grades:
            result = 'Pass' if grade >= pass_mark else 'Fail'
            writer.writerow({'name': name, 'grade': grade, 'result': result})

if __name__ == "__main__":
    input_file = "grades.csv"
    output_file = "results.csv"
    grades_list = read_grades(input_file)
    avg = calculate_average(grades_list)
    print(f"Average grade: {avg:.2f}")
    write_results(grades_list, output_file)
    print(f"Results saved to {output_file}")
