import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '1234')
DB_NAME = os.getenv('DB_NAME', 'scopus')
DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    migrate = Migrate(app, db)


'''
Author

'''


class Author(db.Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer)
    name = Column(String)
    link = Column(String)
    documentsNumber = Column(Integer)
    citationsNumber = Column(Integer)
    h_index = Column(Integer)
    university = Column(String)
    topic1 = Column(String)
    topic2 = Column(String)
    topic3 = Column(String)
    topic4 = Column(String)
    topic5 = Column(String)
    articleNumber = Column(Integer)
    conferenceNumber = Column(Integer)
    bookchapterNumber = Column(Integer)
    editorialNumber = Column(Integer)
    reviewNumber = Column(Integer)
    bookNumber = Column(Integer)
    erratumNumber = Column(Integer)
    letterNumber = Column(Integer)
    publicationsStats = Column(String)
    publications = Column(String)
    coauthor1 = Column(String)
    coauthor2 = Column(String)
    coauthor3 = Column(String)
    coauthor4 = Column(String)
    coauthor5 = Column(String)
    coauthor6 = Column(String)
    coauthor7 = Column(String)
    coauthor8 = Column(String)
    citationsStats = Column(String)

    def __init__(self, timestamp, name, link, documentsNumber, citationsNumber, h_index, university, coauthor1, coauthor2, coauthor3, coauthor4, coauthor5, coauthor6, coauthor7, coauthor8, topic1, topic2, topic3, topic4, topic5, articleNumber, conferenceNumber, bookchapterNumber,
                 editorialNumber, reviewNumber, bookNumber, erratumNumber, letterNumber, publicationsStats, publications, citationsStats):
        self.timestamp = timestamp
        self.name = name
        self.link = link
        self.documentsNumber = documentsNumber
        self.citationsNumber = citationsNumber
        self.h_index = h_index
        self.university = university,
        self.topic1 = topic1
        self.topic2 = topic2
        self.topic3 = topic3
        self.topic4 = topic4
        self.topic5 = topic5
        self.articleNumber = articleNumber
        self.conferenceNumber = conferenceNumber
        self.bookchapterNumber = bookchapterNumber
        self.editorialNumber = editorialNumber
        self.reviewNumber = reviewNumber
        self.bookNumber = bookNumber
        self.erratumNumber = erratumNumber
        self.letterNumber = letterNumber
        self.publicationsStats = publicationsStats
        self.publications = publications
        self.coauthor1 = coauthor1
        self.coauthor2 = coauthor2
        self.coauthor3 = coauthor3
        self.coauthor4 = coauthor4
        self.coauthor5 = coauthor5
        self.coauthor6 = coauthor6
        self.coauthor7 = coauthor7
        self.coauthor8 = coauthor8
        self.citationsStats = citationsStats

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'name': self.name,
            'link': self.link,
            'documentsNumber': self.documentsNumber,
            'citationsNumber': self.citationsNumber,
            'h_index': self.h_index,
            'university': self.university,
            'topic1': self.topic1,
            'topic2': self.topic2,
            'topic3': self.topic3,
            'topic4': self.topic4,
            'topic5': self.topic5,
            'articleNumber': self.articleNumber,
            'conferenceNumber': self.conferenceNumber,
            'bookchapterNumber': self.bookchapterNumber,
            'editorialNumber': self.editorialNumber,
            'reviewNumber': self.reviewNumber,
            'bookNumber': self.bookNumber,
            'erratumNumber': self.erratumNumber,
            'letterNumber': self.letterNumber,
            'publicationsStats': self.publicationsStats,
            'publications': self.publications,
            'coauthor1': self.coauthor1,
            'coauthor2': self.coauthor2,
            'coauthor3': self.coauthor3,
            'coauthor4': self.coauthor4,
            'coauthor5': self.coauthor5,
            'coauthor6': self.coauthor6,
            'coauthor7': self.coauthor7,
            'coauthor8': self.coauthor8,
            'citationsStats': self.citationsStats
        }


'''
Document Year

'''


class Document_Year(db.Model):
    __tablename__ = 'document_years'

    id = Column(Integer, primary_key=True)
    year = Column(String)
    number = Column(Integer)
    authors = Column(String)
    subjects = Column(String)
    types = Column(String)
    keywords = Column(String)
    funding = Column(String)
    countries = Column(String)

    def __init__(self, year, number, authors, subjects, types, keywords, funding, countries):
        self.year = year
        self.number = number
        self.authors = authors
        self.subjects = subjects
        self.types = types
        self.keywords = keywords
        self.funding = funding
        self.countries = countries

    def format(self):
        return {
            'id': self.id,
            'year': self.year,
            'number': self.number,
            'authors': self.authors,
            'subjects': self.subjects,
            'types': self.types,
            'keywords': self.keywords,
            'funding': self.funding,
            'countries': self.countries
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


'''
Log

'''


class Log(db.Model):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    request = Column(String)
    response = Column(String)
    status_code = Column(Integer)

    def __init__(self, timestamp, request, response, status_code):
        self.timestamp = timestamp
        self.request = request
        self.response = response
        self.status_code = status_code

    def format(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'request': self.request,
            'response': self.response[:200],
            'status_code': self.status_code,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


'''
University

'''


class University(db.Model):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    link = Column(String)

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
