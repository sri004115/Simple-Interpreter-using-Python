import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import zipfile

def compress_to_zip():
    # Prompt user to select files to compress
    files = filedialog.askopenfilenames(title="Select Files to Compress", filetypes=[("All Files", "*.*")])
    if not files:
        messagebox.showinfo("No Files Selected", "Please select at least one file to compress.")
        return

    # Prompt user to select save location for the zip file
    zip_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Zip files", "*.zip")], title="Save Zip File")
    if not zip_path:
        messagebox.showinfo("No Save Location", "Please specify a location to save the zip file.")
        return

    # Calculate total size of files
    total_size = sum(os.path.getsize(file) for file in files)
    if total_size > 1 * 1024 * 1024 * 1024:  # Warn if files exceed 1GB
        confirm = messagebox.askyesno("Large Files Detected", "The selected files exceed 1GB. Proceed?")
        if not confirm:
            return

    # Create progress bar window
    progress_window = tk.Toplevel()
    progress_window.title("Compressing Files")
    tk.Label(progress_window, text="Compressing, please wait...").pack(pady=10)
    progress_bar = ttk.Progressbar(progress_window, length=400, mode="determinate")
    progress_bar.pack(pady=10)

    # Create the zip file
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for i, file in enumerate(files):
                arcname = os.path.relpath(file, start=os.path.dirname(file))
                zipf.write(file, arcname)
                progress_bar['value'] = (i + 1) / len(files) * 100
                progress_window.update_idletasks()

        progress_window.destroy()
        messagebox.showinfo("Success", f"Files compressed successfully into: {zip_path}")
    except Exception as e:
        progress_window.destroy()
        messagebox.showerror("Error", f"Error compressing files: {str(e)}")

def extract_zip():
    # Prompt user to select a zip file to extract
    zip_path = filedialog.askopenfilename(title="Select Zip File to Extract", filetypes=[("Zip files", "*.zip")])
    if not zip_path:
        messagebox.showinfo("No File Selected", "Please select a zip file to extract.")
        return

    # Prompt user to select extraction folder
    extract_to = filedialog.askdirectory(title="Select Extraction Folder")
    if not extract_to:
        messagebox.showinfo("No Folder Selected", "Please select a folder to extract the zip file.")
        return

    # Create progress bar window
    progress_window = tk.Toplevel()
    progress_window.title("Extracting Files")
    tk.Label(progress_window, text="Extracting, please wait...").pack(pady=10)
    progress_bar = ttk.Progressbar(progress_window, length=400, mode="determinate")
    progress_bar.pack(pady=10)

    # Extract the zip file
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            file_list = zipf.namelist()
            for i, file in enumerate(file_list):
                zipf.extract(file, extract_to)
                progress_bar['value'] = (i + 1) / len(file_list) * 100
                progress_window.update_idletasks()

        progress_window.destroy()
        messagebox.showinfo("Success", f"Files extracted successfully to: {extract_to}")
    except Exception as e:
        progress_window.destroy()
        messagebox.showerror("Error", f"Error extracting files: {str(e)}")

def main():
    root = tk.Tk()
    root.title("Advanced Zip File Utility")

    compress_button = tk.Button(root, text="Compress to Zip", command=compress_to_zip, bg="blue", fg="white", width=20)
    compress_button.pack(pady=10)

    extract_button = tk.Button(root, text="Extract Zip File", command=extract_zip, bg="green", fg="white", width=20)
    extract_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=20)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()