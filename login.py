from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>3D Login Page</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            min-height: 100vh;
            overflow: hidden;
        }

        /* ===== BACKGROUND ===== */

        .background {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;

            background:
                radial-gradient(circle at 15% 20%, #4f46e5, transparent 30%),
                radial-gradient(circle at 85% 80%, #9333ea, transparent 30%),
                linear-gradient(135deg, #020617, #111827);

            position: relative;
            overflow: hidden;
        }

        /* ===== 3D OBJECTS ===== */

        .cube {
            position: absolute;

            width: 100px;
            height: 100px;

            border: 1px solid rgba(255,255,255,0.25);

            background: rgba(255,255,255,0.05);

            backdrop-filter: blur(5px);

            transform: rotate(45deg);

            box-shadow:
                0 0 40px rgba(99,102,241,0.35);

            animation: floating 8s infinite ease-in-out;
        }

        .cube1 {
            top: 10%;
            left: 12%;
        }

        .cube2 {
            bottom: 10%;
            right: 12%;

            width: 150px;
            height: 150px;

            animation-delay: 2s;
        }

        .cube3 {
            top: 65%;
            left: 20%;

            width: 60px;
            height: 60px;

            animation-delay: 4s;
        }

        @keyframes floating {

            0%, 100% {
                transform: rotate(45deg) translateY(0);
            }

            50% {
                transform: rotate(135deg) translateY(-40px);
            }
        }

        /* ===== LOGIN CARD ===== */

        .login-container {
            perspective: 1200px;
            z-index: 10;
        }

        .login-card {
            width: 390px;

            padding: 40px;

            border-radius: 25px;

            background: rgba(255,255,255,0.10);

            border: 1px solid rgba(255,255,255,0.25);

            backdrop-filter: blur(20px);

            box-shadow:
                0 30px 70px rgba(0,0,0,0.6),
                inset 0 1px 1px rgba(255,255,255,0.2);

            color: white;

            text-align: center;

            transform:
                rotateX(5deg)
                rotateY(-5deg);

            transition: 0.5s;
        }

        .login-card:hover {
            transform:
                rotateX(0deg)
                rotateY(0deg)
                translateY(-10px);
        }

        /* ===== ICON ===== */

        .icon {
            width: 70px;
            height: 70px;

            margin: auto;
            margin-bottom: 20px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 20px;

            background:
                linear-gradient(
                    135deg,
                    #6366f1,
                    #a855f7
                );

            font-size: 32px;

            box-shadow:
                0 15px 35px rgba(99,102,241,0.5);

            transform: translateZ(40px);
        }

        /* ===== TEXT ===== */

        h1 {
            font-size: 30px;
            margin-bottom: 8px;
        }

        .subtitle {
            color: #cbd5e1;
            margin-bottom: 30px;
        }

        /* ===== INPUT ===== */

        .input-box {
            position: relative;
            margin-bottom: 25px;
        }

        .input-box input {
            width: 100%;

            padding: 15px;

            border-radius: 12px;

            border: 1px solid rgba(255,255,255,0.2);

            outline: none;

            background: rgba(0,0,0,0.25);

            color: white;

            font-size: 15px;
        }

        .input-box label {
            position: absolute;

            left: 15px;
            top: 15px;

            color: #94a3b8;

            pointer-events: none;

            transition: 0.3s;
        }

        .input-box input:focus {
            border-color: #818cf8;

            box-shadow:
                0 0 15px rgba(99,102,241,0.5);
        }

        .input-box input:focus + label,
        .input-box input:not(:placeholder-shown) + label {

            top: -9px;
            left: 12px;

            padding: 0 5px;

            font-size: 12px;

            color: #a5b4fc;

            background: #111827;
        }

        /* ===== OPTIONS ===== */

        .options {
            display: flex;

            justify-content: space-between;

            font-size: 12px;

            margin-bottom: 25px;

            color: #cbd5e1;
        }

        .options a {
            color: #a5b4fc;
            text-decoration: none;
        }

        /* ===== BUTTON ===== */

        button {
            width: 100%;

            padding: 15px;

            border: none;

            border-radius: 12px;

            background:
                linear-gradient(
                    135deg,
                    #6366f1,
                    #a855f7
                );

            color: white;

            font-size: 16px;

            font-weight: bold;

            cursor: pointer;

            transition: 0.3s;

            box-shadow:
                0 10px 25px rgba(99,102,241,0.4);
        }

        button:hover {
            transform: translateY(-3px);

            box-shadow:
                0 15px 35px rgba(168,85,247,0.6);
        }

        /* ===== MESSAGE ===== */

        .message {
            margin-top: 20px;

            padding: 10px;

            border-radius: 10px;

            background: rgba(255,255,255,0.1);

            color: #c4b5fd;
        }

        /* ===== REGISTER ===== */

        .register {
            margin-top: 25px;

            color: #94a3b8;

            font-size: 13px;
        }

        .register a {
            color: #a5b4fc;

            text-decoration: none;

            font-weight: bold;
        }

        /* ===== MOBILE ===== */

        @media (max-width: 500px) {

            .login-card {
                width: 90vw;
                padding: 30px 25px;
            }

            .cube {
                opacity: 0.4;
            }
        }

    </style>
</head>

<body>

<div class="background">

    <!-- 3D Floating Objects -->
    <div class="cube cube1"></div>
    <div class="cube cube2"></div>
    <div class="cube cube3"></div>


    <!-- Login -->
    <div class="login-container">

        <div class="login-card">

            <div class="icon">
                🔐
            </div>

            <h1>Welcome Back</h1>

            <p class="subtitle">
                Login to your account
            </p>


            <form method="POST">

                <div class="input-box">

                    <input
                        type="text"
                        name="username"
                        placeholder=" "
                        required
                    >

                    <label>
                        Username
                    </label>

                </div>


                <div class="input-box">

                    <input
                        type="password"
                        name="password"
                        placeholder=" "
                        required
                    >

                    <label>
                        Password
                    </label>

                </div>


                <div class="options">

                    <label>
                        <input type="checkbox">
                        Remember me
                    </label>

                    <a href="#">
                        Forgot Password?
                    </a>

                </div>


                <button type="submit">
                    Login
                </button>

            </form>


            {% if message %}

                <div class="message">
                    {{ message }}
                </div>

            {% endif %}


            <p class="register">

                Don't have an account?

                <a href="#">
                    Create Account
                </a>

            </p>

        </div>

    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Demo Login
        if username == "admin" and password == "1234":

            message = "✅ Login Successful!"

        else:

            message = "❌ Invalid Username or Password"

    return render_template_string(
        HTML,
        message=message
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )