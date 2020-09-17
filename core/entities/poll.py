'''
Entity that sets the questions and manage the expiration of the survey
'''
from typing import Optional, List
from dataclasses import dataclass
from datetime import datetime
import public # type: ignore
from . import question # pylint: disable=unused-import

@public.add
@dataclass
class Poll:
    '''
    this its a domain object doesnt need have been attached to any database orm
    or any other persistence system
    '''
    parent: Optional['Poll']
    expires_at: datetime
    questions: List['question.Question']

    def has_expired(self) -> bool:
        '''
        this accessor checks the expiration date with de current datetime

        :return bool
        '''
        return self.expires_at < datetime.now()
