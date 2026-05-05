import re

with open('/Users/akarshaksingh/Desktop/Wellora/client/css/styles.css', 'r') as f:
    content = f.read()

# Remove .hero .container
content = re.sub(r'\.hero \.container\s*\{[^}]+\}', '', content)

# Remove .sub-navbar .container
content = re.sub(r'\.sub-navbar \.container\s*\{[^}]+\}', '', content)

# stats-container
content = re.sub(r'\.stats-container\s*\{[^}]+\}', '', content)

# footer-content
content = re.sub(r'\.footer-content\s*\{[^}]+\}', '', content)

with open('/Users/akarshaksingh/Desktop/Wellora/client/css/styles.css', 'w') as f:
    f.write(content)
