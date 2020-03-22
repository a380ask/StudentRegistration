from flask import Flask, request, render_template, redirect
from flask_pymongo import PyMongo

#initialize
#this function initializes any application
app = Flask(__name__)
app.debug = True

#config
app.config["MONGO_URI"] = "mongodb://studentReg:bwIP9FWOqjsozzUU@cluster0-shard-00-00-n27aa.mongodb.net:27017,cluster0-shard-00-01-n27aa.mongodb.net:27017,cluster0-shard-00-02-n27aa.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority" #"mongodb+srv://studentReg:bwIP9FWOqjsozzUU@cluster0-n27aa.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
print(mongo.db)

#Route to my page
@app.route("/studentReg", methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("StReg.html")
    else:
        return redirect("/studentList")

@app.route("/studentList", methods = ['GET', 'POST'])
def studentList():
    if request.method == 'GET':
        return render_template("tables.html")

#run
if __name__ == "__main__":
    app.run()