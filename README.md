📊 Grade Predictor App
📌 Overview
The Grade Predictor App is a Kivy-based Python application that allows students to manage their courses, add grade components, and estimate their overall grades. The app provides an intuitive user interface for inputting course details, tracking grades, and calculating weighted scores based on individual grade components.

✨ Features
✅ Course Management – Add and view courses with credit details.
✅ Grade Tracking – Input grade components with weights and scores.
✅ Dynamic UI – Uses Kivy's layout system for a modern and responsive interface.
✅ Scroll & Popups – Scrollable views for better navigation and popups for notifications.
✅ User-Friendly – Simple forms and buttons for easy interaction.

🔧 How It Works
1️⃣ Add Courses – Users input course names and credits.
2️⃣ Add Grades – Assign different grade components (e.g., assignments, exams) with weights and scores.
3️⃣ View Courses & Grades – See all stored courses and grade details.
4️⃣ Pop-up Notifications – Success and error messages for better user feedback.

🔧How to Build an APK using Buildozer
To package this app as an APK for Android, follow these steps:

1️⃣Install dependencies (ensure you have Python and Buildozer installed):

sudo apt update && sudo apt install -y python3-pip git zip unzip
pip3 install --user --upgrade Cython virtualenv
pip3 install --user --upgrade buildozer

2️⃣Navigate to the project directory and initialize Buildozer:

buildozer init

3️⃣Edit buildozer.spec to ensure compatibility with Kivy:

Set requirements = python3,kivy==2.1.0
Adjust package details like package.name, package.domain, and permissions if needed.

4️⃣Build the APK:

buildozer -v android debug
This process will take some time and generate an APK in the bin/ directory.

🏗️ Future Improvements
🚀 Backend Integration – Store course and grade data persistently.
📱 Mobile App Version – Convert to a cross-platform mobile app with Flutter or KivyMD.
📊 Grade Visualization – Add graphs and analytics for better insights.
