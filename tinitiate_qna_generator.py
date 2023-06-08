from flask import Flask, render_template
import markdown
import os
import re

app = Flask(__name__)

"""
# ###################################################################################
# Render Styles Start
# ###################################################################################
def render_header_detail_html():
    




# ###################################################################################
# Main Program
# ###################################################################################
def 
"""

@app.route('/')
def index():
    # List all Markdown files in the 'content' folder
    files = os.listdir('E:/TinitiateIntervewQnAService/content')
    md_files = [f for f in files if f.endswith('.md')]

    # Generate menu from file names
    menu = [{'title': f.replace('.md', ''), 'url': f.replace('.md', '')} for f in md_files]

    # Convert Markdown files to HTML
    html_files = []
    for md_file in md_files:
        with open(os.path.join('E:/TinitiateIntervewQnAService/content', md_file), 'r') as f:
            html = '<a id="' + md_file.replace('.md', '') + '"><b>' + md_file.replace('.md', '').upper() + '</b></a> <hr>'
            html = html + '\n' + markdown.markdown(f.read())
        html_files.append(html.replace('<h1>', '<ul><li style="background-color:PowderBlue;"><b>').replace('</h1>', '</b></li></ul>'))

    # Render HTML files and menu using template
    return render_template('index.html', files=html_files, menu=menu)

@app.route('/sidebar')
def sidebar():

    l_h1_tag_replace = """<a href=\"#\" class=\"list-group-item list-group-item-action active\" aria-current=\"true\">
          <div class=\"d-flex w-100 justify-content-between\"><h5 class=\"mb-1\">"""

    l_h1_tag_replace = """<a href=\"#\" class=\"list-group-item list-group-item-action active\" aria-current=\"true\">
          <div class=\"d-flex w-100 justify-content-between\"><h5 class=\"mb-1\">"""

    # List all Markdown files in the 'content' folder
    files = os.listdir('E:/TinitiateIntervewQnAService/content')
    md_files = [f for f in files if f.endswith('.md')]

    # Convert Markdown files to HTML
    html_files = []
    html_content = []
    # html_content = [{"Tab":,"Topic":,"Content":]
    l_file_data = {}
    html = ""
    for md_file in md_files:
        l_file_data["Tab"]   = md_file.replace('.md', '')+"_tab"
        l_file_data["Topic"] = md_file.replace('.md', '')
        l_file_data["Main"] = md_file.replace('.md', '')+"_main"
        html = ""
        with open(os.path.join('E:/TinitiateIntervewQnAService/content', md_file), 'r') as f:
            html = markdown.markdown(f.read())
            l_file_data["QuesCount"] = html.count('<h1>')
            html = html.replace('<h1>',l_h1_tag_replace).replace('</h1>', '</h5></div>')
            html = html.replace('<ul><li>','<p class="mb-1">').replace('</ul></li>', '</p></a>')
            l_file_data["Content"] = html
            
            
        print(l_file_data)
        html_content.append(l_file_data)
        l_file_data = {}
        html = ""
        
    # Render HTML files and menu using template
    return render_template('prod_bt5_side_bar.html', data=html_content)

if __name__ == '__main__':
    app.run(debug=True)


