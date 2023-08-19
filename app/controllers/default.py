from app import app, login_manager, db
from flask import render_template, flash, redirect, url_for, request
from app.models.forms import LoginForm, CreateNewPost, CreateNewUser
from app.models.tables import User, Post
from flask_login import login_user, logout_user, current_user, login_required

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/",  methods=["POST", "GET"])
def index():
    user = 0
    new_post = CreateNewPost()
    posts = Post.query.all()
    posts.reverse()
    if current_user.is_authenticated:
        user = int(current_user.get_id())
    return render_template('home.html', new_post=new_post,  posts=posts, user=user)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Email ou Senha incorreto, verifique e tente novamente", "error")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/post', methods=["POST"])
@login_required
def post():
    new_post = CreateNewPost()
    if User.is_authenticated:
        if new_post.validate_on_submit():
            content = new_post.content.data
            title = new_post.title.data
            id_user = current_user.get_id()
            author = User.query.filter_by(id=id_user).first().username
            posted = Post(content, title, id_user, author)
            db.session.add(posted)
            db.session.commit()

    else:
        print("Vai fazer login")
    return redirect(url_for("index"))


@app.route("/sign", methods=["POST", "GET"])
def sing_in():
    form = CreateNewUser()
    if form.validate_on_submit():
        user_name = form.user_name.data
        name = form.name.data
        password = form.password.data
        email = form.email.data
        user = User(user_name, name, password, email)
        if not db.session.execute(db.select(User).filter_by(email=email)).first():
            db.session.add(user)
            db.session.commit()
            flash("Usuario cadastrado com sucesso", "success")
            return redirect(url_for("login"))
        else:
            flash("Email já cadastrado", "error")
    return render_template('sing_in.html', form=form)


@app.route("/delete/<int:id>",  methods=["POST", "GET"])
def delete(id):
    post_id = id
    current_post = db.session.execute(db.select(Post).filter_by(id=post_id)).scalar_one()
    if current_user.is_authenticated:
        db.session.delete(current_post)
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>",  methods=["POST", "GET"])
def update(post_id):
    new_post = CreateNewPost()
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('edit.html', post=post, new_post=new_post)
