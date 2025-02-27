import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

kivy.require('2.1.0')  # Ensure Kivy version compatibility


class GradePredictorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.courses = []  # Stores course details

    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.create_homepage()
        return self.root

    def create_homepage(self):
        self.clear_widgets()

        title = Label(text="Grade Predictor", font_size=24, bold=True, size_hint=(1, 0.2))
        self.root.add_widget(title)

        button_layout = BoxLayout(orientation='vertical', spacing=10, padding=20, size_hint=(1, 0.6))

        add_course_btn = Button(text="Add Course", size_hint=(1, None), height=50)
        add_course_btn.bind(on_press=self.add_course_page)
        button_layout.add_widget(add_course_btn)

        view_courses_btn = Button(text="View Courses & Calculate Grades", size_hint=(1, None), height=50)
        view_courses_btn.bind(on_press=self.view_courses)
        button_layout.add_widget(view_courses_btn)

        self.root.add_widget(button_layout)

    def clear_widgets(self):
        self.root.clear_widgets()

    def create_form(self, fields, callback):
        form_layout = GridLayout(cols=2, padding=10, spacing=10, size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))

        entries = {}
        for label, default_value in fields:
            label_widget = Label(text=label, size_hint=(None, None), width=200, height=40)
            entry_widget = TextInput(text=default_value, multiline=False, size_hint=(None, None), width=200, height=40)
            form_layout.add_widget(label_widget)
            form_layout.add_widget(entry_widget)
            entries[label] = entry_widget

        form_scroll = ScrollView(size_hint=(1, 0.7))
        form_scroll.add_widget(form_layout)
        self.root.add_widget(form_scroll)

        save_btn = Button(text="Save", size_hint=(1, 0.1))
        save_btn.bind(on_press=lambda instance: callback(entries))
        self.root.add_widget(save_btn)

    def add_course_page(self, instance):
        self.clear_widgets()

        title = Label(text="Add New Course", font_size=18, bold=True, size_hint=(1, 0.1))
        self.root.add_widget(title)

        fields = [
            ("Course Name:", ""),
            ("Course Credits:", "0"),
        ]

        def save_course(entries):
            try:
                name = entries["Course Name:"].text
                credit = float(entries["Course Credits:"].text)

                self.courses.append({
                    "name": name,
                    "credit": credit,
                    "components": [],
                })

                self.show_popup("Success", f"Course '{name}' added successfully!")
                self.create_homepage()
            except ValueError:
                self.show_popup("Error", "Invalid input. Please check your entries.")

        self.create_form(fields, save_course)

    def view_courses(self, instance):
        self.clear_widgets()

        title = Label(text="Courses & Grades", font_size=18, bold=True, size_hint=(1, 0.1))
        self.root.add_widget(title)

        if not self.courses:
            no_course_label = Label(text="No courses added yet.", size_hint=(1, 0.8))
            self.root.add_widget(no_course_label)
            back_btn = Button(text="Back to Home", size_hint=(1, 0.1))
            back_btn.bind(on_press=lambda instance: self.create_homepage())
            self.root.add_widget(back_btn)
            return

        course_layout = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        course_layout.bind(minimum_height=course_layout.setter('height'))

        for course in self.courses:
            course_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            course_label = Label(text=f"{course['name']} (Credits: {course['credit']})", size_hint=(0.7, 1))
            grade_btn = Button(text="Add Grades", size_hint=(0.3, 1))
            grade_btn.bind(on_press=lambda instance, c=course: self.add_grades_page(c))
            course_box.add_widget(course_label)
            course_box.add_widget(grade_btn)
            course_layout.add_widget(course_box)

        course_scroll = ScrollView(size_hint=(1, 0.8))
        course_scroll.add_widget(course_layout)
        self.root.add_widget(course_scroll)

        back_btn = Button(text="Back to Home", size_hint=(1, 0.1))
        back_btn.bind(on_press=lambda instance: self.create_homepage())
        self.root.add_widget(back_btn)

    def add_grades_page(self, course):
        self.clear_widgets()

        title = Label(text=f"Grades for {course['name']}", font_size=18, bold=True, size_hint=(1, 0.1))
        self.root.add_widget(title)

        if course["components"]:
            grade_layout = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
            grade_layout.bind(minimum_height=grade_layout.setter('height'))

            for component in course["components"]:
                component_label = Label(
                    text=f"{component['name']}: {component['weight']}% - Grade: {component['grade']}",
                    size_hint_y=None,
                    height=30,
                )
                grade_layout.add_widget(component_label)

            grade_scroll = ScrollView(size_hint=(1, 0.6))
            grade_scroll.add_widget(grade_layout)
            self.root.add_widget(grade_scroll)

        fields = [
            ("Component Name:", ""),
            ("Weight (%):", "0"),
            ("Grade (%):", "0"),
        ]

        def save_grade(entries):
            try:
                name = entries["Component Name:"].text
                weight = float(entries["Weight (%):"].text)
                grade = float(entries["Grade (%):"].text)

                if weight < 0 or grade < 0 or grade > 100 or weight > 100:
                    raise ValueError

                course["components"].append({
                    "name": name,
                    "weight": weight,
                    "grade": grade,
                })

                self.show_popup("Success", f"Grade component '{name}' added successfully!")
                self.add_grades_page(course)
            except ValueError:
                self.show_popup("Error", "Invalid input. Please check your entries.")

        self.create_form(fields, save_grade)

        back_btn = Button(text="Back to Courses", size_hint=(1, 0.1))
        back_btn.bind(on_press=lambda instance: self.view_courses(None))
        self.root.add_widget(back_btn)

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message, size_hint=(1, 0.8))
        popup_close_btn = Button(text="Close", size_hint=(1, 0.2))
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_close_btn)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        popup_close_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    GradePredictorApp().run()
