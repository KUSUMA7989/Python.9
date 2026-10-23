
from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capital Quiz</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            background:
                linear-gradient(135deg, #080c20, #182848, #4b134f);
            color: white;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 520px;
            padding: 35px;
            border-radius: 22px;
            background: rgba(255, 255, 255, 0.09);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(15px);
        }

        h1 {
            text-align: center;
            font-size: 32px;
            margin-bottom: 10px;
            color: #70e1f5;
        }

        .subtitle {
            text-align: center;
            color: #d5d9e8;
            margin-bottom: 30px;
        }

        .question {
            margin-bottom: 24px;
        }

        label {
            display: block;
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 12px;
        }

        input {
            width: 100%;
            padding: 14px;
            border-radius: 10px;
            border: 1px solid #667799;
            outline: none;
            background: rgba(255, 255, 255, 0.95);
            color: #172033;
            font-size: 16px;
        }

        input:focus {
            border: 2px solid #70e1f5;
            box-shadow: 0 0 12px rgba(112, 225, 245, 0.4);
        }

        button {
            width: 100%;
            padding: 15px;
            margin-top: 5px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(90deg, #70e1f5, #a78bfa);
            color: #10162a;
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(112, 225, 245, 0.3);
        }

        .result {
            margin-top: 24px;
            padding: 18px;
            border-radius: 12px;
            background: rgba(0, 0, 0, 0.2);
            line-height: 2;
        }

        .correct {
            color: #6fffb0;
        }

        .wrong {
            color: #ff9999;
        }

        .score {
            margin-top: 12px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #70e1f5;
        }

        @media (max-width: 480px) {
            .container {
                padding: 24px;
            }

            h1 {
                font-size: 27px;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>🇮🇳 Capital Quiz</h1>
        <p class="subtitle">Test your knowledge of Indian capitals</p>

        <form method="POST">
            <div class="question">
                <label for="q1">1. What is the capital of India?</label>
                <input
                    type="text"
                    id="q1"
                    name="q1"
                    placeholder="Enter your answer"
                    value="{{ q1 }}"
                    required
                >
            </div>

            <div class="question">
                <label for="q2">2. What is the capital of Telangana?</label>
                <input
                    type="text"
                    id="q2"
                    name="q2"
                    placeholder="Enter your answer"
                    value="{{ q2 }}"
                    required
                >
            </div>

            <button type="submit">Submit Answers →</button>
        </form>

        {% if submitted %}
        <div class="result">
            <p>
                <strong>Question 1:</strong>
                <span class="{{ 'correct' if result1 else 'wrong' }}">
                    {{ '✓ Correct answer!' if result1 else '✗ Wrong answer. Correct answer: New Delhi.' }}
                </span>
            </p>

            <p>
                <strong>Question 2:</strong>
                <span class="{{ 'correct' if result2 else 'wrong' }}">
                    {{ '✓ Correct answer!' if result2 else '✗ Wrong answer. Correct answer: Hyderabad.' }}
                </span>
            </p>

            <div class="score">
                Your Score: {{ score }}/2
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def quiz():
    q1 = ""
    q2 = ""
    result1 = False
    result2 = False
    score = 0
    submitted = False

    if request.method == "POST":
        q1 = request.form.get("q1", "").strip().lower()
        q2 = request.form.get("q2", "").strip().lower()

        result1 = q1 in ["delhi", "new delhi"]
        result2 = q2 == "hyderabad"

        score = int(result1) + int(result2)
        submitted = True

    return render_template_string(
        html,
        q1=q1,
        q2=q2,
        result1=result1,
        result2=result2,
        score=score,
        submitted=submitted
    )


if __name__ == "__main__":
    app.run(debug=True)
