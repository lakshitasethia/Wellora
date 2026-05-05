import re

with open('/Users/akarshaksingh/Desktop/Wellora/client/css/styles.css', 'r') as f:
    content = f.read()

# Only keep specific non-layout rules inside @media to strip out what bootstrap does
# For font-size and specific transformations

fixed_media = """
/* Responsive Tweaks using raw CSS for non-Bootstrap things */
@media (max-width: 992px) {
  .steps-line {
    display: none;
  }
  .step.active {
    transform: none;
  }
  .stat-item {
    width: 40%;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  .stat-item {
    width: 100%;
  }
}"""

# Remove the old responsive block completely
content = re.sub(r'/\* Responsive \*/\s*@media \(max-width: 992px\) \{.*', fixed_media, content, flags=re.DOTALL)

# Let's also remove flex settings from the classes we gave d-flex to avoiding conflicts
content = re.sub(r'\.hero \.container\s*\{[^}]+\}', '.hero .container {\n  position: relative;\n  z-index: 1;\n}', content)
content = re.sub(r'\.steps-container\s*\{[^}]+\}', '.steps-container {\n  position: relative;\n  max-width: 1000px;\n  margin: 0 auto;\n}', content)
content = re.sub(r'\.stats-container\s*\{[^}]+\}', '.stats-container {\n  justify-content: space-between;\n  align-items: center;\n}', content)
content = re.sub(r'\.footer-content\s*\{[^}]+\}', '.footer-content {\n  gap: 40px;\n  margin-bottom: 60px;\n}', content)

with open('/Users/akarshaksingh/Desktop/Wellora/client/css/styles.css', 'w') as f:
    f.write(content)

