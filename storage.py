import json


def save_json(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def get_highest_id():
    ids = []
    data = load_json('data.json')
    for post in data:
        ids.append(post['id'])
    return max(ids)


def delete_post(id):
    data = load_json('data.json')
    for post in data:
        if post['id'] == id:
            data.remove(post)
            save_json(data)


def update_post(post_id, author, title, content):
    data = load_json('data.json')
    for post in data:
        if post['id'] == post_id:
            post['author'] = author
            post['title'] = title
            post['content'] = content
    save_json(data)


def main():
    data = [
        {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.', 'likes': 0},
        {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.', 'likes': 0}
        ]
    save_json(data)
    get_highest_id()

if __name__ == '__main__':
    main()
