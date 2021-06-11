from flask import Flask, render_template, request
import comment_db

app = Flask('app')
comment_db.clear()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment_db.add(request.form['comment'])

    search_query = request.args.get('q')

    comments = comment_db.get(search_query)

    return render_template('index.html',
                           comments=comments,
                           search_query=search_query)
app.run(host='0.0.0.0',port=8080)