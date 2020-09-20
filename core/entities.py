'''
This module define all the entities of the core domain on a anemic manner
'''
from typing import Optional, List, Text
from dataclasses import dataclass, field
from datetime import datetime
import public # type: ignore


@public.add
@dataclass
class Poll:
    '''
    this its a domain object doesnt need have been attached to any database orm
    or any other persistence system
    '''
    expires_at: datetime
    parent: Optional['Poll'] = None
    questions: List['Question'] = field(default_factory=list)
    # TODO: add tags on stage II
    # TODO: add user on stage III

    def has_expired(self) -> bool:
        '''
        this accessor checks the expiration date with de current datetime

        :return bool
        '''
        return self.expires_at < datetime.now()

    def set_questions(self, questions = List['Question']) -> 'Poll':
        '''
        we use a chain method here becouse its more useful for object
        building
        '''
        self.questions = questions

        return self

    def get_questions(self) -> List['Question']:
        '''
        inverse composite of the full question list. local + inherited
        '''
        if self.parent is not None:
            return self.questions + self.parent.get_questions()

        return self.questions


@public.add
@dataclass
class Question:
    '''
    Poll
       |__Question[] <- you are here xD
    '''
    poll: 'Poll'
    display: Text
    options: List['AnswerOption'] = field(default_factory=list)

    def set_options(self, options: List['AnswerOption']) -> 'Question':
        '''
        we use a chain method instead of a dinamic property here becouse its
        more useful for object building operations
        '''
        self.options = options

        return self

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
