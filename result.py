import tkinter as tk
from tkinter import ttk, messagebox


class StudentResultCompiler:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Result Compilation")

        # Create notebook for class tabs
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        # Define class names and subjects
        self.classes = ["Class IX", "Class X", "Class XI", "Class XII"]
        self.subjects = ["Math", "Physics", "Chemistry", "Biology", "English", "Urdu"]
        self.students = ["Farasat", "S.M. Mehdi", "Alishan Raza", "Yawar", "Baqar Iftikhar",
                         "Nad-e-Ali", "Hussain Raza", "Ammar Abbas", "Ali Abbas Shah", "Measum Abbas"]

        # Initialize marks entries dictionary
        self.marks_entries = {}

        # Create tabs for each class
        for class_name in self.classes:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=class_name)
            self.create_marks_entry_screen(tab, class_name)

    def create_marks_entry_screen(self, tab, class_name):
        """Creates the UI for entering marks for a specific class."""
        title_label = tk.Label(tab, text=f"{class_name} - Enter Marks", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Create table for subjects, students, and marks entry
        table_frame = tk.Frame(tab)
        table_frame.pack(pady=10)

        # Add headers (Subjects and Student Names)
        tk.Label(table_frame, text="Subjects", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=5, pady=5)
        for col, student in enumerate(self.students, start=1):
            tk.Label(table_frame, text=student, font=("Arial", 10), width=12).grid(row=0, column=col, padx=5, pady=5)

        # Create input fields for marks
        for row, subject in enumerate(self.subjects, start=1):
            tk.Label(table_frame, text=subject, font=("Arial", 10), width=15).grid(row=row, column=0, padx=5, pady=5)
            for col, student in enumerate(self.students, start=1):
                entry = tk.Entry(table_frame, width=8, justify="center")
                entry.grid(row=row, column=col, padx=5, pady=5)
                # Store the entry widget in the dictionary using a unique key
                self.marks_entries[(class_name, subject, student)] = entry

        # Add Proceed button
        proceed_button = tk.Button(tab, text="Proceed", command=lambda: self.compile_results(class_name))
        proceed_button.pack(pady=20)

    def compile_results(self, class_name):
        """Compiles the results for a specific class."""
        results = []
        for subject in self.subjects:
            for student in self.students:
                entry = self.marks_entries.get((class_name, subject, student))
                if entry:
                    try:
                        # Validate that marks are numeric
                        marks = int(entry.get())
                        if marks < 0:
                            raise ValueError("Marks cannot be negative")
                        results.append((subject, student, marks))
                    except ValueError:
                        messagebox.showerror("Input Error", "Please enter valid numeric marks for all students.")
                        return

        # If all marks are valid, calculate results
        self.display_results(class_name, results)

    def display_results(self, class_name, results):
        """Displays the compiled results in a new window."""
        result_window = tk.Toplevel(self.master)
        result_window.title(f"{class_name} - Compiled Results")

        # Create a table-like display for results
        tk.Label(result_window, text=f"{class_name} - Results", font=("Arial", 16, "bold")).pack(pady=10)
        table_frame = tk.Frame(result_window)
        table_frame.pack(pady=10)

        # Table headers
        tk.Label(table_frame, text="Student", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(table_frame, text="Total Marks", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=5, pady=5)

        # Calculate and display total marks for each student
        student_totals = {student: 0 for student in self.students}
        for subject, student, marks in results:
            student_totals[student] += marks

        for row, (student, total) in enumerate(student_totals.items(), start=1):
            tk.Label(table_frame, text=student, font=("Arial", 10), width=15).grid(row=row, column=0, padx=5, pady=5)
            tk.Label(table_frame, text=total, font=("Arial", 10), width=15).grid(row=row, column=1, padx=5, pady=5)

        # Close button
        close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
        close_button.pack(pady=10)

    def run(self):
        """Runs the main Tkinter event loop."""
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentResultCompiler(root)
    app.run()
