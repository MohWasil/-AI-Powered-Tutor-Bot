# main.py
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app and enable CORS for the frontend
app = Flask(__name__)
CORS(app)

# A more complex dictionary of pre-programmed learning modules.
# Each module now contains a lesson AND a quiz.
LESSONS_AND_QUIZZES = {
    "math": {
        "lesson": {
            "title": "What is the Pythagorean Theorem?",
            "explanation": "The Pythagorean Theorem is a fundamental principle in geometry that describes the relationship between the three sides of a right-angled triangle. It states that the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. The formula is written as $a^2 + b^2 = c^2$, where $c$ is the hypotenuse and $a$ and $b$ are the other two sides.",
            "imageUrl": "https://placehold.co/600x400/22C55E/FFFFFF?text=a%C2%B2+%2B+b%C2%B2+%3D+c%C2%B2",
            "animation": "pulse",
            "animationReason": "The pulse animation is chosen to represent the rhythmic, foundational nature of a mathematical theorem."
        },
        "quiz": {
            "question": "If the two shorter sides of a right triangle are 3 and 4, what is the length of the hypotenuse?",
            "options": ["5", "6", "7", "8"],
            "correctAnswer": "5",
            "explanation": "Using the Pythagorean Theorem, $3^2 + 4^2 = 9 + 16 = 25$. The hypotenuse is the square root of 25, which is 5."
        }
    },
    "science": {
        "lesson": {
            "title": "How Does Photosynthesis Work?",
            "explanation": "Photosynthesis is the process that plants and other organisms use to convert light energy into chemical energy. During this process, they use sunlight to synthesize nutrients from carbon dioxide and water. Photosynthesis is responsible for producing most of the oxygen in the Earth's atmosphere, making it a critical process for life on our planet.",
            "imageUrl": "https://placehold.co/600x400/FACC15/FFFFFF?text=Sunlight+%2B+CO%E2%82%82+%2B+H%E2%82%82O",
            "animation": "glow",
            "animationReason": "The glow animation is chosen to represent the energy from the sun being absorbed by the plant's leaves."
        },
        "quiz": {
            "question": "What two things do plants use to create nutrients?",
            "options": ["Water and Oxygen", "Carbon Dioxide and Water", "Sunlight and Oxygen", "Carbon Dioxide and Soil"],
            "correctAnswer": "Carbon Dioxide and Water",
            "explanation": "Plants use sunlight, carbon dioxide ($CO_2$), and water ($H_2O$) to create their own food through photosynthesis."
        }
    },
    "history": {
        "lesson": {
            "title": "What was the Renaissance?",
            "explanation": "The Renaissance was a period in European history from the 14th to the 17th century that marked a major cultural shift from the Middle Ages to modernity. It was a time of great artistic, political, scientific, and cultural rebirth. Think of it as a time when people rediscovered the ideas and art of ancient Greece and Rome, leading to incredible works by figures like Leonardo da Vinci and Michelangelo.",
            "imageUrl": "https://placehold.co/600x400/EF4444/FFFFFF?text=Da+Vinci's+Sketch",
            "animation": "rotate",
            "animationReason": "The rotate animation symbolizes the turning point in history and the revolving nature of ideas during the Renaissance period."
        },
        "quiz": {
            "question": "The Renaissance marked a transition from which historical period?",
            "options": ["The Iron Age", "The Enlightenment", "The Middle Ages", "The Roman Empire"],
            "correctAnswer": "The Middle Ages",
            "explanation": "The Renaissance is widely considered a bridge between the Middle Ages and the modern era."
        }
    },
}

@app.route('/generate_lesson', methods=['POST'])
def generate_lesson():
    """
    This endpoint takes a user query and returns a full lesson module with a quiz.
    """
    try:
        data = request.json
        user_input = data.get('query', '').lower()

        if not user_input:
            return jsonify({"error": "No query provided."}), 400

        # Simple logic to find the correct module
        lesson_data = None
        for key in LESSONS_AND_QUIZZES:
            if key in user_input:
                lesson_data = LESSONS_AND_QUIZZES[key]
                break

        if not lesson_data:
            # A default response if no specific keyword is found
            lesson_data = {
                "lesson": {
                    "title": "Welcome to Tutor Bot!",
                    "explanation": "I can help with lessons in Math, Science, and History. Try asking about one of these topics!",
                    "imageUrl": "https://placehold.co/600x400/6B7280/FFFFFF?text=Tutor+Bot",
                    "animation": "none",
                    "animationReason": "No specific animation is needed for this welcome message."
                },
                "quiz": None
            }
        
        return jsonify(lesson_data), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
