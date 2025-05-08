from readline import set_completer

from flask import Flask, render_template, request, redirect, url_for
import storage
app = Flask(__name__)


@app.route('/')
def index():
    data = storage.load_json('data.json')
    return render_template('index.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form.get('content','Lorem Ipsum')
        id = storage.get_highest_id() + 1
        data = storage.load_json('data.json')
        data.append({'id': id, 'author': author, 'title': title, 'content': content})
        storage.save_json(data)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    storage.delete_post(post_id)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    data = storage.load_json('data.json')
    for post in data:
        if post['id'] == post_id:
            if request.method == 'POST':
                author = request.form['author']
                title = request.form['title']
                content = request.form.get('content', 'Lorem Ipsum')
                storage.update_post(post_id, author, title, content)
                return redirect(url_for('index'))
            return render_template('update.html', post=post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
