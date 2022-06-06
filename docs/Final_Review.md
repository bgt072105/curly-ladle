{% include navigation.html %}

## Major Commits:

[Local Storage for Notepad](https://github.com/kamryns/curlycupboard3.0/commit/394a2ee1f6392e11a596890e4e36a89d980eecd4)

* Notes can be stored using local storage
* Notes stay even when page is left or reloaded
* Delete functionality has also been added

```
    if(localStorage.getItem("noteText")===null){
        localStorage.setItem("noteText",'');
    }
    var noteArray = [];
    if(localStorage.getItem("noteText") != ""){
        noteArray = JSON.parse(localStorage.getItem("noteText"));
    }
```

[Implement Reviews Database](https://github.com/kamryns/curlycupboard3.0/commit/11aa05dee07b068e7494d826a06d1846ab215694)

* Database stores books reviews
* Uses Create, Read, Update, and Delete
* Has search functionality to searchy by keyword

```
@app_database.route('/')
def database():
    """obtains all Users from table and loads Admin Form"""
    return render_template("database.html", table=books_all())


# CRUD create/add
@app_database.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Books(
            request.form.get("name"),
            request.form.get("book"),
            request.form.get("review"),
        )
        po.create()
    return redirect(url_for('database.database'))


# CRUD read
@app_database.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        bookid = request.form.get("bookid")
        po = book_by_id(bookid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("database.html", table=table)


# CRUD update
@app_database.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        bookid = request.form.get("bookid")
        review = request.form.get("review")
        po = book_by_id(bookid)
        print("here")
        print(po)
        if po is not None:
            po.update(review)
    return redirect(url_for('database.database'))


# CRUD delete
@app_database.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        bookid = request.form.get("bookid")
        po = book_by_id(bookid)
        if po is not None:
            po.delete()
    return redirect(url_for('database.database'))
```

[Create Discussion Board](https://github.com/kamryns/curlycupboard3.0/commit/5d3e390ed4c8f479795dba06921fbaa038b221bf)

* Allows users to post comments
* Uses POST method
* Has delete function to delete the last comment added

```
@app.route('/beginnerforum/')
def beginnerforum():
    return render_template("beginnerforum.html")


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.form:
        thought = request.form.get("thought")
        thisList.append(thought)
        if len(thought) != 0:
            return render_template("beginnerforum.html", nickname=thisList)
    return render_template("beginnerforum.html")


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if len(thisList) > 0:
        thisList.pop(len(thisList) - 1)
    return render_template("beginnerforum.html", nickname=thisList)
```

[Add Dictionary](https://github.com/kamryns/curlycupboard3.0/commit/0af8e229e7f3691a0f32b9fddc499afee2a107ce)

* Uses an API to find defintions
* Provides noun, verb, adjective, and adverb definitions of words
* Splits definitions up based on their part of speech

```
@app.route('/dictionary/', methods=['GET','POST'])
def dictionary():
    try:
        keyword = request.form['keyword']
    except:
        keyword = "study"
    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/definition/"
    querystring = {"entry":keyword}
    headers = {
        'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code<400:
        results = json.loads(response.content.decode("utf-8"))
        return render_template("dictionary.html", results=results, word=keyword)
    else:
        return render_template("dictionary.html", word=keyword)
    # print(response.text)
```
