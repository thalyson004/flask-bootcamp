from main import db, User

db.create_all()


thalyson = User('Thalyson', 20)
gomes = User('Gomes', 15)

db.session.add_all([thalyson, gomes])
db.session.commit()

print( thalyson, gomes, sep='\n' )

