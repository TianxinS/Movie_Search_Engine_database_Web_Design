from app import db

class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(20), index=True, unique=True)
    FirstName = db.Column(db.String(20))
    LastName = db.Column(db.String(20))
    DateOfBirth = db.Column(db.Date)
    EmailAddress = db.Column(db.String(100), index=True, unique=True)
    PhoneNumber = db.Column(db.String(20))
    Password = db.Column(db.String(18))
    CreatedDate = db.Column(db.Date)
    CreatedBy = db.Column(db.String(100))
    ModifiedDate = db.Column(db.Date)
    ModifiedBy = db.Column(db.String(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)    