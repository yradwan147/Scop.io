import os
import glob
import time
from flask import Flask, request, abort, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from sqlalchemy import desc

import authorparser
import documentparser

from models import setup_db, Author, Document_Year, Log, University

PATH = os.path.dirname(os.path.realpath(__file__))[:-7]
DIRECTORY = PATH + '/Output/'


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
@TODO: Set up CORS.
Allow '*' for origins.
Delete the sample route after completing the TODOs
    '''
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    '''
@TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # def paginate_questions(request):
    #     try:
    #         items_limit = request.args.get('limit', 10, type=int)
    #         selected_page = request.args.get('page', 1, type=int)
    #         current_index = selected_page - 1
    #         questions = Question.query.order_by(Question.id).limit(items_limit).offset(
    #             current_index * items_limit).all()
    #         max_page = len(questions)/10 + 1
    #         # print(page_number, max_page)
    #         if (page_number > max_page):
    #             abort(404)
    #         start = (page_number-1) * QUESTIONS_PER_PAGE
    #         end = start + QUESTIONS_PER_PAGE
    #         formatted_questions = questions[start:end]
    #     except Exception as e:
    #         print(e)
    #         abort(404)
    #     return formatted_questions
    '''
@TODO:
Create an endpoint to handle GET requests
for log entries in database
    '''
    @app.route('/api/log')
    def get_logEntries():
        entries = Log.query.order_by(
            desc(Log.timestamp)).all()
        if entries is None:
            abort(404)
        entries_list = [entry.format() for entry in entries]

        response = {
            'success': True,
            'entries': entries_list,
            'total_entries': len(entries_list)
        }

        LogEntry = Log(timestamp=time.time(), request="GET LOG",
                       response=str(response), status_code=200)
        LogEntry.insert()

        return jsonify(response)

    '''
@TODO:
Create an endpoint to handle GET requests
for authors parsed from database.
    '''
    @app.route('/api/authors')
    def get_authors():
        authors = Author.query.order_by(
            desc(Author.timestamp)).all()
        if authors is None:
            abort(404)
        authors_list_full = [author.format() for author in authors]
        if request.args.get("full") == 'false':
            distinct = []
            for author in authors_list_full:
                if author['name'] not in distinct:
                    distinct.append(author['id'])
                    distinct.append(author['name'])
            authors_list = list(
                filter(lambda i: i['id'] in distinct, authors_list_full))
            authors_list = sorted(
                authors_list, key=lambda i: i['h_index'], reverse=True)
        else:
            authors_list = authors_list_full
        response = {
            'success': True,
            'authors': authors_list,
            'total_authors': len(authors_list)
        }

        LogEntry = Log(timestamp=time.time(), request="GET AUTHORS",
                       response=str(response), status_code=200)
        LogEntry.insert()

        return jsonify(response)

    '''
@TODO:
Create an endpoint to handle GET requests for document entries
parsed from database
    '''
    @app.route('/documents')
    def get_documents():
        documents = Document_Year.query.order_by(desc(Author.timestamp)).all()
        if documents is None:
            abort(404)
        documents_list = [document.format() for document in documents]

        response = {
            'success': True,
            'documents': documents_list,
            'total_documents': len(documents_list)
        }

        LogEntry = Log(timestamp=time.time(), request="GET DOCUMENTS",
                       response=str(response), status_code=200)
        LogEntry.insert()

        return jsonify(response)

    '''
@TODO:
Create an endpoint to run an authors operation with data recieved from
a POST request body.

TEST: test variable limits, correct output,
    '''
    @app.route("/authors", methods=["POST"])
    def run_authors():
        body = request.form
        urlAuthors = body.get('urlAuthors', None)
        delay = body.get('delay', None)
        authorsNo = body.get('authorsNo', None)
        email = body.get('email', None)
        password = body.get('password', None)
        option1 = body.get('option1', True)
        option2 = body.get('option2', True)
        option3 = body.get('option3', True)

        print(urlAuthors, delay, authorsNo, False,
              email, password, option1, option2, option3)

        all_data = authorparser.author_parse(
            urlAuthors, int(delay), int(authorsNo), False, email, password, option1, option2, option3)

        print(all_data)

        for data in all_data:
            try:
                newAuthor = Author(time.time(), data[0], data[1], data[2], data[3], data[4], str(data[5]), data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22],
                                   data[23], data[24], data[25], data[26], data[27], str(data[28:80]), str(data[6]), str(data[80:]))
                newAuthor.insert()
            except Exception as e:
                print(e)
                pass
        #timestamp, name, link, documentsNumber, citationsNumber, h_index, university, topic1, topic2, topic3, topic4, topic5, articleNumber, conferenceNumber, bookchapterNumber,
        #         editorialNumber, reviewNumber, bookNumber, erratumNumber, letterNumber, publicationsStats, publications, coauthor1, coauthor2, coauthor3, coauthor4, coauthor5, citationsStats)
        response = {
            'success': True,
            'author': newAuthor.format(),
            'numberCreated': len(all_data),
        }

        LogEntry = Log(timestamp=time.time(), request=str(body),
                       response=str(response), status_code=200)
        LogEntry.insert()

        return jsonify(response)

    '''
# @TODO:
# Create an endpoint to handle GET requests to authors : retrieve all author instances in the database
# sorted descendingly according to timestamp.

# TEST: test number of instances, correct format 
#     '''
#     @app.route('/authors/<int:id>')
#     def get_author_data(id):
#         author = Author.query.filter_by(id=id).first()
#         name = author.name
#         author_history = Author.query.filter_by(
#             name=name).order_by(desc(Author.timestamp)).all()

#         history_list = [author.format() for author in author_history]

#         response = {
#             'success': True,
#             'history': history_list,
#             'number': len(history_list)
#         }

#         LogEntry = Log(timestamp=time.time(), request="GET AUTHOR",
#                        response=str(response), status_code=200)
#         LogEntry.insert()

#         return jsonify(response)

    @app.route("/api/downloads/authors")
    def send_file():
        list_of_files = glob.glob(DIRECTORY+'/*')
        filename = max(list_of_files, key=os.path.getctime)
        filename = ''.join(filename.split('\\')[-1])
        return send_from_directory(DIRECTORY, filename, as_attachment=True)

        '''
@TODO:
Create error handlers for all expected errors
including 404 and 422.
    '''
    @app.errorhandler(404)
    def not_found(error):

        response = {
            'success': False,
            'message': 'resource not found',
            'code': 404
        }

        LogEntry = Log(timestamp=time.time(), request="ERROR",
                       response=str(response), status_code=404)
        LogEntry.insert()

        return jsonify(response)

    @app.errorhandler(422)
    def unprocessable(error):

        response = {
            'success': False,
            'message': 'request unprocessable',
            'code': 422
        }

        LogEntry = Log(timestamp=time.time(), request="ERROR",
                       response=str(response), status_code=422)
        LogEntry.insert()

        return jsonify(response)

    return app
