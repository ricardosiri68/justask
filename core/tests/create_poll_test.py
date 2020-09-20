'''
This test case module aims to check the right behavior of the generation of the
differents configurations of a Poll object and its questions
'''
from core.actions import new_poll
from core import entities
from .mocks import payloads


def create_root_poll_test():
    '''
    A root Poll its a survey that not extends of any other previus Poll object
    '''
    poll = new_poll(payloads.MockPollPayload())

    assert isinstance(poll, entities.Poll)


def create_extended_poll_test():
    '''
    A extended Poll its a survey that extends of any other previus Poll object
    and inherits its questions from a kind of composite patter reverse
    '''
    root_poll = new_poll(payloads.MockPollPayload())
    extended_poll = new_poll(payloads.MockPollPayload(parent=root_poll))

    assert isinstance(extended_poll, entities.Poll)
    assert len(extended_poll.get_questions()) == 6
