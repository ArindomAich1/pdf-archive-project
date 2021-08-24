import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from archive import database as _database

class User(_database.Base):
    __tablename__ = "user"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    full_name = _sql.Column(_sql.String, nullable=False)
    agnee_mail = _sql.Column(_sql.String, nullable=False, unique=True, index=True)
    roll_no= _sql.Column(_sql.String, nullable=False, unique=True, index=True)
    password_hash = _sql.Column(_sql.String, nullable=False)

    def __repr__(self):
        return f"fullname : {self.full_name}\nmail_address : {agnee_mail}\nrollno : {roll_no}"