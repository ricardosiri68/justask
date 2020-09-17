'''
This payload its an abstraction of any kind of DTO that attempt to provide the
object dependency for core.actions.new_poll action
'''
from typing import List, Optional
from abc import ABCMeta, abstractmethod
from datetime import datetime
from core import entities # pylint: disable=unused-import

class PollPayload(metaclass=ABCMeta):
    '''
    This ddd port enable the application layer to provide a common interface to
    comunicate with the core.actions.new_poll action in stricted way
    '''
    @abstractmethod
    def poll(self) -> Optional['entities.Poll']: # type: ignore
        '''
        returns the parent Poll entity possibly retrived from the persistence
        systeme but could come from any source of solution
        '''
        return NotImplemented

    @abstractmethod
    def expires_at(self) -> datetime: # type: ignore
        '''
        implemnts the datetime object for the expiration moment of the poll,
        after the date here described the poll can not be anwsered any more for
        anybody
        '''
        return NotImplemented

    @abstractmethod
    def questions(self) -> List['entities.Question']: # type: ignore
        '''
        this iterable returns all the question that compose the poll, if this
        method returns a empty list the action should produce an exception,
        this its also a requirement for a http request validation by example
        '''
        return NotImplemented
