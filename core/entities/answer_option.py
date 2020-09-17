'''
Entity that compose the options of a Question
'''
from typing import Text
from dataclasses import dataclass
import public # type: ignore
from . import question  # pylint: disable=unused-import


@public.add
@dataclass
class AnswerOption:
    '''
    Entity for options of a question
    '''
    question: 'question.Question'
    display: Text
