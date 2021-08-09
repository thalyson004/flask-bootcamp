from main import db, User

# Create a User
user = User('New user', 33, 180)
#db.session.add(user)
#db.session.commit()

# Read 
users = User.query.all()
print(users)

# Select
#user_one = User.query.get(1)
#print(user_one)

# Filters
thalyson = User.query.filter_by(name='Thalyson')
print(thalyson)
print(thalyson.all())

# Update
user_one = User.query.all()[0]
user_one.name = "Modified"
db.session.add(user_one)
db.session.commit()
users = User.query.all()
print(users)

# Delete 
deleted_user = User.query.all()[0] 
db.session.delete(deleted_user)
db.session.commit()
