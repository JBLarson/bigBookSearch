from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open('data.json', 'r') as file:
    data = json.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    matches = []
    if request.method == 'POST':
        term = request.form['search_term']
        for chapter, pages in data.items():
            for page_num, content in pages.items():
                if term.lower() in content.lower():
                    highlighted_content = content.replace(term, f'<span class="highlight">{term}</span>')
                    matches.append({
                        'chapter': chapter,
                        'page': page_num,
                        'content': highlighted_content
                    })
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
