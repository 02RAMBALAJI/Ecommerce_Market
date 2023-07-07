from market import app,db
#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5000)