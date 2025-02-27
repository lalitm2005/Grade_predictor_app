import tkinter as tk
from tkinter import messagebox
from plyer import notification
from datetime import datetime, timedelta
import random

# Sample data for class schedule and important dates
class_schedule = {
    'Monday': ['Math', 'Physics', 'Chemistry'],
    'Tuesday': ['Biology', 'Computer Science'],
    'Wednesday': ['Math', 'English'],
    'Thursday': ['Physics', 'Chemistry'],
    'Friday': ['Computer Science', 'Biology']
}

important_dates = {
    'Quiz 1': '2024-12-20',
    'Major Exam': '2024-12-25',
    'Minor Exam': '2024-12-30'
}

# Sample motivational quotes
quotes = [
    "The only way to do great work is to love what you do.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "The best time to plant a tree was 20 years ago. The second best time is now."
]

# Function to get a random motivational quote
def get_motivational_quote():
    return random.choice(quotes)

# Function to calculate study time before exams (for the forgetting curve)
def get_study_time(exam_date):
    today = datetime.now().date()
    days_left = (exam_date - today).days
    if days_left < 5:
        return "Start revising now!"
    elif days_left < 10:
        return "Start studying soon!"
    else:
        return "You have plenty of time, plan your study schedule!"

# Function to show a notification
def show_notification(message):
    notification.notify(
        title="Reminder",
        message=message,
        timeout=10
    )

# Function to create a modern UI window
def create_main_window():
    window = tk.Tk()
    window.title("B.Tech Schedule App")
    window.geometry("400x500")

    # Label for app title
    title_label = tk.Label(window, text="B.Tech Schedule & Motivation", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=20)

    # Create a frame for the class schedule
    schedule_frame = tk.Frame(window)
    schedule_frame.pack(pady=10)

    # Label for class schedule
    schedule_label = tk.Label(schedule_frame, text="Class Schedule", font=("Helvetica", 12, "bold"))
    schedule_label.grid(row=0, column=0, columnspan=2)

    # Display the class schedule
    row = 1
    for day, subjects in class_schedule.items():
        day_label = tk.Label(schedule_frame, text=f"{day}:", font=("Helvetica", 10))
        day_label.grid(row=row, column=0, sticky="w")
        subjects_label = tk.Label(schedule_frame, text=", ".join(subjects), font=("Helvetica", 10))
        subjects_label.grid(row=row, column=1, sticky="w")
        row += 1

    # Section for reminders
    reminder_frame = tk.Frame(window)
    reminder_frame.pack(pady=10)

    # Label for reminders
    reminder_label = tk.Label(reminder_frame, text="Important Dates", font=("Helvetica", 12, "bold"))
    reminder_label.grid(row=0, column=0, columnspan=2)

    # Display the important dates
    row = 1
    for event, date in important_dates.items():
        event_label = tk.Label(reminder_frame, text=f"{event}: {date}", font=("Helvetica", 10))
        event_label.grid(row=row, column=0, sticky="w")
        study_button = tk.Button(reminder_frame, text="Study Time", font=("Helvetica", 10),
                                 command=lambda date=date: show_study_time(date))
        study_button.grid(row=row, column=1)
        row += 1

    # Section for motivational quotes
    motivation_frame = tk.Frame(window)
    motivation_frame.pack(pady=10)

    # Button to show a motivational quote
    motivation_button = tk.Button(motivation_frame, text="Show Motivation", font=("Helvetica", 12),
                                  command=lambda: show_motivational_quote())
    motivation_button.pack()

    # Section for notifications
    notification_button = tk.Button(window, text="Set Study Notification", font=("Helvetica", 12),
                                    command=lambda: set_study_notification())
    notification_button.pack(pady=20)

    # Main loop
    window.mainloop()

# Function to show study time based on the exam date
def show_study_time(exam_date_str):
    exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d').date()
    study_message = get_study_time(exam_date)
    messagebox.showinfo("Study Time", study_message)

# Function to show a random motivational quote
def show_motivational_quote():
    quote = get_motivational_quote()
    messagebox.showinfo("Motivational Quote", quote)

# Function to set a study notification
def set_study_notification():
    upcoming_event = random.choice(list(important_dates.keys()))
    event_date = important_dates[upcoming_event]
    study_message = get_study_time(datetime.strptime(event_date, '%Y-%m-%d').date())
    show_notification(f"Reminder: {upcoming_event} is approaching! {study_message}")

# Run the app
create_main_window()
