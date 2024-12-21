import tkinter as tk
from tkinter import scrolledtext
import sys
import io

class PythonInterpreter:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Interpreter")

        # Input Area
        self.input_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=80)
        self.input_area.pack(pady=10)

        # Run Button
        self.run_button = tk.Button(root, text="Run", command=self.run_code, bg="green", fg="white")
        self.run_button.pack(pady=5)

        # Output Area
        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=80, state=tk.DISABLED, fg="white", bg="black")
        self.output_area.pack(pady=10)

    def run_code(self):
        # Get the code from the input area
        code = self.input_area.get("1.0", tk.END)

        # Clear previous output
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)

        # Redirect stdout and stderr
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        sys.stderr = redirected_output

        try:
            # Execute the code and capture the output
            exec_globals = {}
            exec_locals = {}
            exec(code, exec_globals, exec_locals)
        except Exception as e:
            self.output_area.insert(tk.END, f"Error:\n{redirected_output.getvalue()}{str(e)}\n")
        else:
            output = redirected_output.getvalue()
            self.output_area.insert(tk.END, output if output else "Code executed successfully.\n")
        finally:
            # Reset stdout and stderr
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        # Disable editing of the output area
        self.output_area.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    interpreter = PythonInterpreter(root)
    root.mainloop()
    #python interpreter.py env\Scripts\activate
