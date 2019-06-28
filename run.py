from repoapp import app

if __name__=='__main__':
    app.run(debug=True, port=8000)
    # db.create_all