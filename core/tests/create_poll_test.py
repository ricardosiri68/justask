'''
This test case module aims to check the right behavior of the generation of the
differents configurations of a Poll object and its questions
'''
from typing import List, Optional
from core.payloads.poll_payload import PollPayload
from core.actions import new_poll
from core import entities

class MockPollPayload(PollPayload):

    # pylint: disable=no-member
    def poll(self) -> Optional[entities.Poll]: # type: ignore
        return None

    def questions(self) -> List[entities.Question]: # type: ignore
        # TODO: check a way of retrive a Poll object and display string
        return [
            entities.Question(), # type: ignore
            entities.Question() # type: ignore
        ]

def create_root_poll_test():
    '''
    A root Poll its a survey that not extends of any other previus Poll object
    '''
    assert False

def create_extended_poll_test():
    '''
    A extended Poll its a survey that extends of any other previus Poll object
    and inherits its questions from a kind of composite patter reverse
    '''
    assert False
