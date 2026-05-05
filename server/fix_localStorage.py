import glob

for filepath in glob.glob('/Users/akarshaksingh/Desktop/Wellora/client/*.html'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace all incorrect accesses
    content = content.replace("localStorage.getItem('token')", "localStorage.getItem('wellora_token')")
    content = content.replace('localStorage.removeItem("token")', 'localStorage.removeItem("wellora_token")')
    content = content.replace('localStorage.removeItem("user")', 'localStorage.removeItem("wellora_user")')
    content = content.replace("localStorage.removeItem('token')", "localStorage.removeItem('wellora_token')")
    content = content.replace("localStorage.removeItem('user')", "localStorage.removeItem('wellora_user')")
    
    with open(filepath, 'w') as f:
        f.write(content)

