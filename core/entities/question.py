'''
Entity that represents the question itself, have a set of AnswerOption and
Answer
'''
from typing import Text, List
from dataclasses import dataclass
import public # type: ignore
from . import poll # pylint: disable=unused-import
from . import answer_option # pylint: disable=unused-import

@public.add
@dataclass
class Question:
    '''
    Poll
       |__Question[] <- you are here xD
    '''
    poll: 'poll.Poll'
    options: List['answer_option.AnswerOption']
    display: Text
