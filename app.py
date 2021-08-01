from flask import Flask, render_template , url_for , request

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        # task_content = request.form['content']
        # new_task = Todo(content=task_content)

        # try:
        #     db.session.add(new_task)
        #     db.session.commit()
        #     return redirect('/')
        # except:
        #     return 'There was an issue adding your task'
        pass

    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)