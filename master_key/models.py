from sqlalchemy import Column, ForeignKey, Integer, String

# from sqlalchemy.orm import relationship
from database import Base


class Master_Password(Base):
    id = Column(Integer(), primary_key=True)
    mp = Column(String(), unique=True, nullable=False)
    hint = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"<Master_Password {self.mp} - {self.hint}>"

    # def is_active(self):
    #     return True

    # def is_authenticated(self):
    #     return True

    # def get_id(self):
    #     return self.id


class Passwords(Base):
    id = Column(Integer(), primary_key=True)
    services = Column(String(255), unique=True, nullable=False)

    passwords = Column(String(), unique=True, nullable=False)

    def __repr__(self):
        return f"<Passwords {self.services}:{self.passwords}>"
