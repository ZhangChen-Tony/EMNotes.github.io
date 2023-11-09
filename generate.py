import os

# Function to get all html files
def get_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

# Create a new index.html file
with open('index.html', 'w') as index_file:
    # Set the title and style of the HTML file
    index_file.write('''
    <html>
    <head>
    <title>EM notes from Chen Zhang</title>
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    a {
        display: block;
        margin: 10px 0;
    }
    </style>
    </head>
    <body>
    <h1>EM notes from Chen Zhang</h1>
    ''')

    # Create a link with a title for each html file
    for html_file in get_html_files('.'):  # replace '.' with your directory
        title = os.path.basename(html_file)
        index_file.write(f'<a href="{html_file}">{title}</a>\n')

    # Close the HTML tags
    index_file.write('</body>\n</html>')