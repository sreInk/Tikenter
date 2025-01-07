import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import subprocess
import os


class CodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Editor")
        self.root.geometry("800x600")

        # Create a Text widget (the area where text will be typed)
        self.text_area = tk.Text(self.root, wrap="word", undo=True, font=("Courier", 12))
        self.text_area.pack(expand=True, fill="both")

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo_action)
        self.edit_menu.add_command(label="Redo", command=self.redo_action)

        # Run menu
        self.run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Run Code", command=self.run_code)

        self.file_name = None

        # Highlight the code with Python syntax
        self.highlight_code()

    def open_file(self):
        """Open a file"""
        file_path = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            self.file_name = file_path
            self.root.title(f"Code Editor - {file_path}")
            self.highlight_code()

    def save_file(self):
        """Save the current file"""
        if self.file_name:
            with open(self.file_name, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
        else:
            self.save_as()

    def save_as(self):
        """Save the current text as a new file"""
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            self.file_name = file_path
            self.root.title(f"Code Editor - {file_path}")

    def exit_editor(self):
        """Exit the editor"""
        if messagebox.askyesno("Quit", "Do you want to save before quitting?"):
            self.save_file()
        self.root.quit()

    def undo_action(self):
        """Undo the last action"""
        try:
            self.text_area.edit_undo()
        except Exception as e:
            print(f"Error undoing: {e}")

    def redo_action(self):
        """Redo the last undone action"""
        try:
            self.text_area.edit_redo()
        except Exception as e:
            print(f"Error redoing: {e}")

    def highlight_code(self):
        """Apply syntax highlighting to the code"""
        code = self.text_area.get(1.0, tk.END)
        lexer = PythonLexer()  # For Python code highlighting
        formatter = HtmlFormatter(style='monokai', full=True, noclasses=True)
        highlighted_code = highlight(code, lexer, formatter)

        # We now need to inject the highlighted code back into the text widget
        # This can be done by formatting and inserting individual lines of the highlighted code.
        self.text_area.delete(1.0, tk.END)  # Clear previous content

        # Insert the highlighted content line by line
        self.text_area.insert(tk.END, highlighted_code)

    def run_code(self):
        """Run the code inside the editor"""
        code = self.text_area.get(1.0, tk.END)
        try:
            # Save the code to a temporary file and run it
            temp_file = "temp_script.py"
            with open(temp_file, "w") as f:
                f.write(code)

            result = subprocess.run(["python3", temp_file], capture_output=True, text=True)
            output = result.stdout + result.stderr

            # Show output in a dialog box
            simpledialog.messagebox.showinfo("Code Output", output)

            # Clean up the temporary file
            os.remove(temp_file)

        except Exception as e:
            messagebox.showerror("Error", f"Error running code: {e}")


# Create the main window
root = tk.Tk()

# Create the CodeEditor instance
editor = CodeEditor(root)

# Start the Tkinter event loop
root.mainloop()
