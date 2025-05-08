import json

def save_json(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def main():
    data = [
        {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
        {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'},
        ]
    save_json(data)

if __name__ == '__main__':
    main()
