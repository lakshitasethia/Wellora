import re
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Nav links
    content = content.replace('<nav class="nav-links">', '<nav class="nav-links d-none d-md-flex">')
    
    # Sub navbar
    content = content.replace('<div class="sub-navbar">', '<div class="sub-navbar d-none d-md-block">')

    # Hero container
    content = content.replace('<div class="container">\n      <div class="hero-content">', '<div class="container d-flex flex-column flex-lg-row align-items-center gap-4 gap-lg-5">\n      <div class="hero-content">')
    
    # Hero dashboard
    content = content.replace('<div class="hero-dashboard">', '<div class="hero-dashboard w-100 w-lg-auto">')

    # Steps container
    content = content.replace('<div class="steps-container">', '<div class="steps-container d-flex flex-column flex-lg-row gap-4 gap-lg-0">')
    
    # Stats container
    content = content.replace('<div class="container stats-container">', '<div class="container stats-container d-flex flex-wrap flex-lg-nowrap gap-4">')
    
    # Footer content
    content = content.replace('<div class="footer-content">', '<div class="footer-content row">')
    content = content.replace('<div class="footer-brand">', '<div class="footer-brand col-12 col-md-6 col-lg-3 mb-4 mb-lg-0">')
    content = content.replace('<div class="footer-links">', '<div class="footer-links col-12 col-md-6 col-lg-3 mb-4 mb-lg-0">')

    with open(filepath, 'w') as f:
        f.write(content)

for file in glob.glob('/Users/akarshaksingh/Desktop/Wellora/client/*.html'):
    process_file(file)
