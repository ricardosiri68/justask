'''
This module define all the entities of the core domain on a anemic manner
'''
from typing import Optional, List, Text
from dataclasses import dataclass
from datetime import datetime
import public # type: ignore


@public.add
@dataclass
class Poll:
    '''
    this its a domain object doesnt need have been attached to any database orm
    or any other persistence system
    '''
    parent: Optional['Poll']
    expires_at: datetime
    questions: List['Question']
    # TODO: add tags on stage II
    # TODO: add user on stage III

    def has_expired(self) -> bool:
        '''
        this accessor checks the expiration date with de current datetime

        :return bool
        '''
        return self.expires_at < datetime.now()


@public.add
@dataclass
class Question:
    '''
    Poll
       |__Question[] <- you are here xD
    '''
    poll: 'Poll'
    options: List['AnswerOption']
    display: Text


@public.add
@dataclass
class AnswerOption:
    '''
    Entity for options of a question
    '''
    question: 'Question'
    display: Text


@public.add
@dataclass
class Answer:
    '''
    Answer option acts like a bride between the Question, its options and the
    user that answer the question in the poll
    '''
    question: 'Question'
    option_selected: 'AnswerOption'
    # TODO: add user on stage III
