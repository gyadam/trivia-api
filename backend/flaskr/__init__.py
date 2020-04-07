import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  cors = CORS(app, resources={r"/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  @app.route('/categories')
  # return all categories
  def get_categories():
    categories = Category.query.all()
    categories_dict = {category.id:category.type for category in categories}
    return jsonify({
      'categories': categories_dict
    })

  @app.route('/questions', methods=['GET'])
  # return paginated questions
  def get_questions():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
    questions = Question.query.all()
    formatted_questions = [question.format() for question in questions]
    categories = Category.query.all()
    categories_dict = {category.id:category.type for category in categories}
    return jsonify({
      'success': True,
      'questions': formatted_questions[start:end],
      'total_questions': len(formatted_questions),
      'current_category': 'Geography',
      'categories': categories_dict
    })


  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    error = False
    try:
      Question.query.filter_by(id=question_id).one_or_none().delete()
    except:
      error = True
      abort(422)
    success = False if error else True
    return jsonify({
      'success': success
    })


  @app.route('/add')
  def get_form():
    return jsonify({
      'success': True,
    })

  @app.route('/questions', methods=['GET', 'POST'])
  def post_question():
    error = False
    if request.method == 'POST':
      body = request.get_json()
      if 'searchTerm' in body:
        searchterm = body['searchTerm']
        search_results = Question.query.filter(Question.question.ilike('%' + searchterm + '%')).all()
        formatted_results = [result.format() for result in search_results]
        return jsonify({
          'success': True,
          'questions': formatted_results,
          'totalQuestions': len(formatted_results)
        })
      else:
        quest = body['question']
        ans = body['answer']
        cat = body['category']
        diff = body['difficulty']
        try:
          new_question = Question(question=quest, answer=ans, category=cat, difficulty=diff)
          new_question.insert()
        except:
          error = True
          abort(422)
        success = False if error else True
        return jsonify({
          'success': success
        })


  @app.route('/categories/<int:category_id>/questions')
  def get_categorized_questions(category_id):
    categorized_questions = Question.query.filter_by(category=category_id).all()
    formatted_questions = [question.format() for question in categorized_questions]
    return jsonify({
      'success': True,
      'questions': formatted_questions,
      'totalQuestions': len(formatted_questions),
      'currentCategory': category_id
    })

  # TODO: Create a POST endpoint to get questions to play the quiz. 
  '''
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "Unprocessable Entity"
        }), 422


  return app

    