
from flask import Flask, request, session, redirect, render_template_string

app = Flask(__name__)
app.secret_key = "my-secret-key"

correct_password = "admin123"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cinematic Login</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            color: white;
            background:
                radial-gradient(circle at top left, #312e81, transparent 40%),
                radial-gradient(circle at bottom right, #164e63, transparent 40%),
                #070b18;
            overflow: hidden;
        }

        .glow {
            position: absolute;
            width: 280px;
            height: 280px;
            background: #6366f1;
            filter: blur(130px);
            opacity: 0.35;
            border-radius: 50%;
            animation: float 5s infinite alternate;
        }

        @keyframes float {
            from { transform: translate(-50px, -20px); }
            to { transform: translate(60px, 40px); }
        }

        .card {
            position: relative;
            width: 90%;
            max-width: 400px;
            padding: 40px 32px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 24px;
            background: rgba(255,255,255,0.07);
            backdrop-filter: blur(18px);
            box-shadow: 0 25px 80px rgba(0,0,0,0.5);
        }

        .icon {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .tag {
            color: #a5b4fc;
            letter-spacing: 4px;
            font-size: 11px;
            font-weight: bold;
        }

        h1 {
            margin: 12px 0;
            font-size: 32px;
        }

        .subtitle {
            color: #aab3c5;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 28px;
        }

        label {
            display: block;
            text-align: left;
            margin-bottom: 9px;
            font-size: 13px;
            color: #dbeafe;
        }

        input {
            width: 100%;
            padding: 15px;
            color: white;
            background: rgba(255,255,255,0.06);
            border: 1px solid #414b68;
            border-radius: 12px;
            outline: none;
            font-size: 15px;
        }

        input:focus {
            border-color: #818cf8;
            box-shadow: 0 0 15px #6366f144;
        }

        input::placeholder {
            color: #7c879e;
        }

        button {
            width: 100%;
            padding: 15px;
            margin-top: 18px;
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            background: linear-gradient(100deg, #6366f1, #06b6d4);
            transition: 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px #6366f155;
        }

        .message {
            margin-top: 20px;
            padding: 13px;
            border-radius: 10px;
            font-size: 14px;
        }

        .success {
            color: #86efac;
            background: #14532d55;
            border: 1px solid #22c55e66;
        }

        .error {
            color: #fca5a5;
            background: #7f1d1d55;
            border: 1px solid #ef444466;
        }

        .locked {
            color: #fca5a5;
            background: #450a0a88;
            border: 1px solid #ef4444;
        }

        .attempts {
            margin-top: 20px;
            font-size: 12px;
            color: #94a3b8;
        }

        .footer {
            margin-top: 28px;
            color: #64748b;
            font-size: 11px;
            letter-spacing: 1px;
        }
    </style>
</head>

<body>
    <div class="glow"></div>

    <div class="card">
        <div class="icon">🔐</div>
        <div class="tag">SECURE ACCESS</div>

        <h1>Welcome Back</h1>
        <p class="subtitle">
            Enter your password to continue.<br>
            You have a maximum of 3 attempts.
        </p>

        <form method="POST">
            <label for="password">Password</label>

            <input
                type="password"
                id="password"
                name="password"
                placeholder="Enter your password"
                required
                {% if locked or success %}disabled{% endif %}
            >

            <button type="submit"
                {% if locked or success %}disabled{% endif %}>
                LOGIN SECURELY
            </button>
        </form>

        {% if message %}
            <div class="message {{ status }}">
                {{ message }}
            </div>
        {% endif %}

        <p class="attempts">
            Attempts used: {{ attempts }} / 3
        </p>

        {% if locked or success %}
            <form method="POST" action="/reset">
                <button type="submit">START AGAIN</button>
            </form>
        {% endif %}

        <div class="footer">ENCRYPTED EXPERIENCE · FLASK</div>
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    attempts = session.get("attempts", 0)
    success = session.get("success", False)
    locked = attempts >= 3 and not success

    message = ""
    status = ""

    if request.method == "POST" and not locked and not success:
        password = request.form.get("password", "")
        attempts += 1
        session["attempts"] = attempts

        if password == correct_password:
            message = "Login successful! Welcome."
            status = "success"
            session["success"] = True
            success = True

        else:
            if attempt_is_last(attempts):
                message = "Account locked! Maximum attempts reached."
                status = "locked"
                locked = True
            else:
                message = "Wrong password! Please try again."
                status = "error"

    return render_template_string(
        HTML,
        message=message,
        status=status,
        attempts=attempts,
        locked=locked,
        success=success
    )


def attempt_is_last(attempt):
    return attempt == 3


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
