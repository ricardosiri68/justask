'''
Entity that represent the user answer to a multiple choice (AnswerOption)
question
'''
from dataclasses import dataclass
import public # type: ignore
from . import question
from . import answer_option

@public.add
@dataclass
class Answer:
    '''
    Answer option acts like a bride between the Question, its options and the
    user that answer the question in the poll
    '''
    question: 'question.Question'
    option_selected: 'answer_option.AnswerOption'
    # TODO: add user on stage III
