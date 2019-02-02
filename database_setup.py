from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            }


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            }


class Computers(Base):
    __tablename__ = 'computers'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String)
    computer_type = Column(String(250))
    company_id = Column(Integer, ForeignKey('company.id'))
    company_relationship = relationship(Company)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'computer_type': self.computer_type,
            }


engine = create_engine('sqlite:///ComputerCompanieswithusers.db')


Base.metadata.create_all(engine)
