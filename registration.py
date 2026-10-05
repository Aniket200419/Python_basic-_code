from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        password = request.form.get("password")
        gender = request.form.get("gender")

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Registration Success</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #74ebd5 0%, #9face6 100%);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .card {{
                    background: #fff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
                    width: 400px;
                    text-align: center;
                }}
                h2 {{
                    color: #4CAF50;
                }}
                a {{
                    display: inline-block;
                    margin-top: 15px;
                    text-decoration: none;
                    color: #fff;
                    background: #4CAF50;
                    padding: 10px 20px;
                    border-radius: 5px;
                }}
                a:hover {{
                    background: #45a049;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Registration Successful!</h2>
                <p><b>Name:</b> {fullname}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Password:</b> {password}</p>
                <p><b>Gender:</b> {gender}</p>
                <a href="/">Go Back</a>
            </div>
        </body>
        </html>
        """

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Registration</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                width: 400px;
                background: #fff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
            }
            h2 {
                text-align: center;
                margin-bottom: 20px;
                color: #333;
            }
            label {
                font-weight: bold;
                margin-top: 10px;
                display: block;
            }
            input[type=text], input[type=email], input[type=password], select {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            input[type=submit] {
                width: 100%;
                background-color: #4CAF50;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            input[type=submit]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Registration Form</h2>
            <form method="POST">
                <label for="fullname">Full Name</label>
                <input type="text" id="fullname" name="fullname" required>

                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>

                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>

                <label for="gender">Gender</label>
                <select id="gender" name="gender" required>
                    <option value="">Select gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>

                <input type="submit" value="Register">
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
