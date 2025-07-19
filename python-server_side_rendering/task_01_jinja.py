from flask import Flask, render_template_string

app = Flask(__name__)

# Header ve footer ortak template'leri
header_html = """
<header>
    <h1>My Flask App</h1>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/contact">Contact</a>
    </nav>
    <hr>
</header>
"""

footer_html = """
<hr>
<footer>
    <p>&copy; 2024 My Flask App</p>
</footer>
"""

# Ana şablonlar — içerik burada değişiyor, header ve footer dahil ediliyor
base_template = """
<!doctype html>
<html lang="en">
<head>
    <title>{{ title }}</title>
</head>
<body>
    {{ header|safe }}

    <main>
        {{ content|safe }}
    </main>

    {{ footer|safe }}
</body>
</html>
"""

@app.route('/')
def home():
    content = """
    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask application.</p>
    <ul>
        <li>Flask</li>
        <li>HTML</li>
        <li>Templates</li>
    </ul>
    """
    return render_template_string(base_template, title="Home",
                                  header=header_html,
                                  footer=footer_html,
                                  content=content)

@app.route('/about')
def about():
    content = """
    <h1>About Us</h1>
    <p>This page gives information about our Flask application.</p>
    """
    return render_template_string(base_template, title="About",
                                  header=header_html,
                                  footer=footer_html,
                                  content=content)

@app.route('/contact')
def contact():
    content = """
    <h1>Contact Us</h1>
    <p>You can contact us via email at contact@example.com.</p>
    """
    return render_template_string(base_template, title="Contact",
                                  header=header_html,
                                  footer=footer_html,
                                  content=content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
