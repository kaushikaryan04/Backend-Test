The main api is in the api app 
I have written a small comment on each view to show what each class bassed generic view does
BlogId is used as primary key it is auto incremented
Contect , Title and author are some more field given in the model


To use this project follow following steps -
1 -> git clone this repo
2 -> make a virtual env and activate it
3 -> pip install -r Requirements.txt (This will recursively download all pip packages required)
4 -> make a super user (optional)
5 -> you can use the following paths for testing purpose

To Create a Blog
http://localhost:8000/create

To List all blogs 
http://localhost:8000/all

To list one single blog according to id
http://localhost:8000/list/<id>

To Update one blog according to id
http://localhost:8000/update/<id>