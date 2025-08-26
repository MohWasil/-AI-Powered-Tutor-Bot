# -AI-Powered-Tutor-Bot
Tutor Bot is a simple, interactive web application that acts as a personal tutor. Instead of being a static website, it uses a Python backend as a powerful AI agent to deliver dynamic, structured learning modules. Each module includes a lesson, an engaging animation, and an immediate quiz to test comprehension and reinforce key concepts.

This project demonstrates a modern approach to education, combining active learning, formative assessment, and a conversational interface to make learning more effective and engaging.

🚀 How to Use the Application
The application is split into two parts: a Python backend (the "brain" of the tutor) and a simple HTML/CSS/JS frontend (the user interface). Both must be running at the same time for the application to work correctly.

Here's the step-by-step guide on how to get it running on your local machine.

Step 1: Set Up the Project
Download the project files. Make sure you have the following three files in the same folder:

main.py (the Python backend)

index.html (the frontend)

requirements.txt (the list of Python libraries)

Open your terminal or command prompt and navigate to the folder where you saved these files. You can do this with the cd command.

Step 2: Install Dependencies
This project requires a few Python libraries. The requirements.txt file makes this process easy.

In your terminal, run the following command:

Bash

pip install -r requirements.txt
This will automatically install all the necessary libraries.

Step 3: Start the Backend Server
The Python backend handles the logic for generating lessons and quizzes. You need to get it running first.

In your terminal, run this command:

Bash

python main.py
You will see output indicating that the Flask server is running on http://127.0.0.1:5000. Do not close this terminal window.

Step 4: Start the Frontend Web Server
Now, you need to serve the index.html file so your browser can load the application correctly. Opening it directly from your file system (file://...) won't work due to browser security policies.

Open a second, new terminal window and run this command:

Bash

python -m http.server 8000
This will start a simple web server on port 8000. Keep this window open as well.

Step 5: Launch the Application
With both servers running, you can now launch the application in your browser.

Open your web browser and go to this address:

http://localhost:8000/index.html
The application will load in your browser, and you can start asking questions about math, science, or history in the chat box. Enjoy!
