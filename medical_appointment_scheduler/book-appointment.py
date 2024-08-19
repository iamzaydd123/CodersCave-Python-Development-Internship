import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import requests
import csv
from datetime import datetime, timedelta

BASE_URL = 'http://127.0.0.1:5000/appointments'

def on_phone_number_key_press(event):
    # Allow backspace key
    if event.keysym == 'BackSpace':
        return
    # Validate if the pressed key is a digit
    if not event.char.isdigit():
        return "break"  # Do not allow the input

def select_all(event):
    phone_entry.select_range(0, tk.END)

def validate_phone_number():
    phone_number = phone_entry.get()
    if not phone_number.isdigit() or len(phone_number) != 10:
        messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
        return False
    return True

def create_appointment():
    patient_name = name_entry.get().title()
    phone_number = phone_entry.get()
    selected_date = date_var.get()
    selected_time = time_combobox.get()

    if not (patient_name and validate_phone_number() and selected_date != 'Select Date' and selected_time and selected_time != 'Select Time'):
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    data = {
        'patient_name': patient_name,
        'phone_number': phone_number,
        'date': selected_date,
        'time': selected_time
    }

    response = requests.post(BASE_URL, json=data)
    
    if response.status_code == 201:
        messagebox.showinfo("Success", "Appointment created successfully.")
        clear_fields()
    else:
        messagebox.showerror("Error", "Failed to create appointment. Please try again.")

def save_to_csv():
    appointments = requests.get(BASE_URL).json()

    if not appointments:
        messagebox.showinfo("Info", "No appointments to save.")
        return

    with open('appointments.csv', 'w', newline='') as csvfile:
        fieldnames = ['patient_name', 'phone_number', 'date', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for appointment in appointments:
            writer.writerow(appointment)

        messagebox.showinfo("Success", "Appointments saved to appointments.csv.")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    date_var.set('Select Date')
    time_combobox.set('Select Time')

# Create main application window
app = tk.Tk()
app.title("Medical Appointment Scheduler")
app.geometry("400x300")
app.configure(bg='#000000')

# Define fonts
font_style = ('Arial', 12)
bold_font_style = ('Arial', 12, 'bold')

# Name label and entry
tk.Label(app, text="Name:", font=bold_font_style, bg='#000000', fg='white').grid(row=0, column=0, pady=10, padx=10, sticky='e')
name_entry = tk.Entry(app, font=font_style, width=25, bg='#333333', fg='white', insertbackground='white')
name_entry.grid(row=0, column=1, pady=10, padx=10)

# Phone Number label and entry
tk.Label(app, text="Phone Number:", font=bold_font_style, bg='#000000', fg='white').grid(row=1, column=0, pady=10, padx=10, sticky='e')
phone_entry = tk.Entry(app, font=font_style, width=25, bg='#333333', fg='white', insertbackground='white')
phone_entry.grid(row=1, column=1, pady=10, padx=10)
phone_entry.bind("<KeyPress>", on_phone_number_key_press)
phone_entry.bind("<Control-a>", select_all)

# Date label and entry
tk.Label(app, text="Date:", font=bold_font_style).grid(row=2, column=0, pady=10, padx=10, sticky='e')
date_var = tk.StringVar()
date_entry = DateEntry(app, width=22, borderwidth=2, textvariable=date_var, date_pattern='dd-mm-yyyy', font=font_style, state='normal')
date_var.set('Select Date')
date_entry.grid(row=2, column=1, pady=10, padx=10)

# Time label and combobox
tk.Label(app, text="Time:", font=bold_font_style, bg='#000000', fg='white').grid(row=3, column=0, pady=10, padx=10, sticky='e')
start_time = datetime.strptime('08:00', '%H:%M')
end_time = datetime.strptime('18:00', '%H:%M')
time_slots = [(start_time + timedelta(minutes=i*30)).strftime('%I:%M %p') for i in range(int((end_time - start_time).total_seconds() / 60 / 30)) if (start_time + timedelta(minutes=i*30)).strftime('%I:%M %p') not in ['12:00 PM', '12:30 PM']]
time_combobox = ttk.Combobox(app, values=time_slots, font=font_style, state='normal', width=23)
time_combobox.set('Select Time')
time_combobox.grid(row=3, column=1, pady=10, padx=10)

# Create button
create_button = tk.Button(app, text="Create Appointment", command=create_appointment, font=bold_font_style, bg='#4CAF50', fg='white', width=20)
create_button.grid(row=4, column=0, columnspan=2, pady=10)

# Save button
save_button = tk.Button(app, text="Save to CSV", command=save_to_csv, font=bold_font_style, bg='#2196F3', fg='white', width=20)
save_button.grid(row=5, column=0, columnspan=2, pady=10)

# Center align all widgets
for child in app.winfo_children():
    child.grid_configure(padx=10, pady=5)

app.mainloop()
