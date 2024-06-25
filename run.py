import datetime
from flask import Flask, jsonify, request
from appconfig import app
from appconfig import mysql

@app.route('/blogs', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM blogs''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/blogs', methods=['GET'])
def get_blogs():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM blogs''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/blogs', methods=['POST'])
def add_blog():
    cur = mysql.connection.cursor()
    author = request.json['author']
    content = request.json['content']
    print(author,content)
    now = datetime.datetime.now()
    date_created = now.strftime('%Y-%m-%d %H-%M-%S')
    cur.execute("INSERT INTO blogs (author, content,created_at,updated_at) VALUES (%s, %s,%s,%s)", (author,content,date_created,date_created))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Blog Post added successfully'})

@app.route('/blogs/<int:id>', methods=['DELETE'])
def delete_data(id):
    cur = mysql.connection.cursor()
    cur.execute('''DELETE FROM blogs WHERE id = %s''', (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Blog Post deleted successfully'})

@app.route('/blogs/<int:id>', methods=['PUT'])
def update_data(id):
    cur = mysql.connection.cursor()
    content = request.json['content']
    author = request.json['author']
    now = datetime.datetime.now()
    date_updated = now.strftime('%Y-%m-%d %H-%M-%S')
    cur.execute('''UPDATE blogs SET author = %s, content = %s, updated_at = %s WHERE id = %s''', (author, content,date_updated,id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Blog Post updated successfully'})

if __name__ == '__main__':
  app.run(debug=True)

from app import routes
