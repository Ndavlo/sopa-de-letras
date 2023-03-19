from flask import Flask, request, jsonify, render_template
from wordsearch import find_words
from website import create_app

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        matrix = request.form.get('matrix')
        words = request.form.get('words')
        if not matrix or not words:
            return jsonify({'error': 'Matrix and words are required.'})
        matrix = [[c for c in row.strip()] for row in matrix.strip().split('\n')]
        words_list = [word.strip() for word in words.split(',')]
        results = find_words(matrix, words_list)
        response = {'results': {}}
        for word in words_list:
            if word in results:
                 response['results'][word] = {'found': True, 'direction': results[word]['direction'], 'coordinates': results[word]['coordinates']}
            else:
                response['results'][word] = {'found': False, 'direction': None, 'coordinates': []}
        return jsonify(response)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)