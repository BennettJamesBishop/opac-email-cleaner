import tkinter as tk
from tkinter import ttk, messagebox
from htmlParser import get_clean_html_body
from apiCall import generate_link_names
from promptArgs.monthlyEventEmail import MonthlyEventEmail
from promptArgs.UCSBNewsletter import UCSBNewsletter
from promptArgs.seniorNewsletter import SeniorNewsletter

# Function to process input and generate meaningful link names
def process_links():
    email_type = email_type_var.get()
    url = url_entry.get().strip()
    link_names = link_entry.get().strip()

    # Validate inputs
    if not url:
        messagebox.showerror("Input Error", "Please enter a valid email URL.")
        return
    if not link_names:
        messagebox.showerror("Input Error", "Please enter at least one link name.")
        return

    # Select the correct email type
    email_args = UCSBNewsletter if email_type == "UCSB Newsletter" else MonthlyEventEmail

    # Fetch and clean HTML
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Fetching email content...\n")
    root.update_idletasks()

    html_body = get_clean_html_body(url)
    if "Error" in html_body:
        messagebox.showerror("URL Error", html_body)
        return

    # Process links
    link_array = [link.strip() for link in link_names.split(",")]

    # Call OpenAI API to generate link names
    result_text.insert(tk.END, "Generating link names...\n")
    root.update_idletasks()
    
    try:
        result = generate_link_names(email_args, html_body, link_array)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("API Error", f"Failed to generate link names: {str(e)}")

    result_text.config(state=tk.DISABLED)

# Create Tkinter Window
root = tk.Tk()
root.title("Link Naming App")
root.geometry("650x500")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Link Naming App", font=("Arial", 16, "bold")).pack(pady=10)

# Email Type Selection
tk.Label(root, text="Select Email Type:").pack(pady=5)
email_type_var = tk.StringVar(value="UCSB Newsletter")
email_dropdown = ttk.Combobox(root, textvariable=email_type_var, values=["UCSB Newsletter", "Monthly Event Newsletter"], state="readonly")
email_dropdown.pack(pady=5)

# URL Input
tk.Label(root, text="Enter Email URL:").pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

# Link Names Input
tk.Label(root, text="Enter Links (comma-separated):").pack(pady=5)
link_entry = tk.Entry(root, width=60)
link_entry.pack(pady=5)

# Process Button
process_button = tk.Button(root, text="Generate Link Names", command=process_links, bg="#007bff", fg="white", font=("Arial", 12, "bold"))
process_button.pack(pady=10)

# Results Display
tk.Label(root, text="Generated Link Names:").pack(pady=5)
result_text = tk.Text(root, height=10, width=75, state=tk.DISABLED)
result_text.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
