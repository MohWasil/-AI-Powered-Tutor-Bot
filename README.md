AI-Powered Tutor Bot

AI-Powered Tutor Bot is an interactive web application that acts as a personal tutor. Powered by a Python backend AI agent, it delivers dynamic, structured learning modules that combine lessons, engaging animations, and immediate quizzes to reinforce comprehension and key concepts.

This project showcases a modern approach to education, integrating active learning, formative assessments, and a conversational interface to make learning effective and engaging.

🚀 Features

Dynamic lesson generation using AI

Interactive quizzes for immediate feedback

Simple conversational interface

Modular design with a Python backend and HTML/CSS/JS frontend

📥 Getting Started

Follow these steps to run the application locally.

Step 1: Download Project Files

Ensure you have the following files in the same directory:

main.py (Python backend)

index.html (Frontend UI)

requirements.txt (Python dependencies)

Step 2: Install Dependencies

Open a terminal, navigate to the project directory, and run:

pip install -r requirements.txt


This will install all necessary Python libraries.

Step 3: Start the Python Backend Server

Run the backend server which handles AI logic:

python main.py


You should see output indicating the Flask server is running at:

http://127.0.0.1:5000


Keep this terminal open to keep the backend running.

Step 4: Start the Frontend Web Server

In a new terminal window, navigate to the project directory and start a simple HTTP server:

python -m http.server 8000


This serves your frontend files on port 8000. Keep this terminal open as well.

Step 5: Launch the Application

Open your web browser and navigate to:

http://localhost:8000/index.html


You should see the Tutor Bot interface. Start asking questions about math, science, history, or other subjects in the chat box.

🎉 Enjoy learning with your AI-powered tutor!
📖 Additional Notes

Make sure both backend and frontend servers are running simultaneously.

Do not open index.html directly from the filesystem (i.e., avoid file:// URLs) to prevent browser security issues.

If you want to customize or extend the project, edit main.py for backend logic and index.html for frontend UI.
