from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML form template
form_html = """
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Web Form</title>
    <style>
      body { font-family: Arial; margin: 50px; }
      form { background: #f9f9f9; padding: 20px; width: 300px; border-radius: 8px; }
      input[type="text"], input[type="email"] { width: 100%; padding: 8px; margin: 5px 0; }
      input[type="submit"] { background: #4CAF50; color: white; border: none; padding: 10px; width: 100%; }
      .result { margin-top: 20px; font-size: 18px; color: green; }
    </style>
  </head>
  <body>
    <h2>Simple Web Form</h2>
    <form method="POST">
      Name: <input type="text" name="name" required><br><br>
      Email: <input type="email" name="email" required><br><br>
      <input type="submit" value="Submit">
    </form>
    {% if name and email %}
      <div class="result">
        <p>Form Submitted!</p>
        <p><strong>Name:</strong> {{ name }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
      </div>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def form():
    name = email = None
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
    return render_template_string(form_html, name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)
