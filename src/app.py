import subprocess
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    matched_pages = []
    term = ""  # Set a default value for term

    # Define the items per page and get the current page from the request
    ITEMS_PER_PAGE = 10
    page = request.args.get('page', 1, type=int)

    if request.method == 'POST':
        term = request.form['search_term']
        # Use pdfgrep to search for the term and get page numbers
        result = subprocess.check_output(['pdfgrep', '-n', term, 'static/bigBook.pdf'])
        for line in result.splitlines():
            page_num, _ = line.decode('utf-8').split(':', 1)
            if page_num not in matched_pages:
                matched_pages.append(page_num)

    # Calculate starting and ending indexes for slicing
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    return render_template('index.html', matched_pages=matched_pages[start:end], search_term=term, current_page=page, total_pages=len(matched_pages) // ITEMS_PER_PAGE + 1)

if __name__ == '__main__':
    app.run(debug=True)
