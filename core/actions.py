'''
This use case action handles the poll creation in all its forms, if something
goes wrong with this operation will throw a domain exception explaining why
'''
from datetime import datetime
import public # type: ignore
from core import entities
from core.payloads.poll_payload import PollPayload

@public.add
def new_poll(payload: PollPayload) -> 'entities.Poll': # type: ignore
    '''
    Build and persist a instance of a Poll object on every way posible. Thats
    its the SRP of this action the only reason for this function will be edited
    its that we find a new way of make a Poll object
    '''

    assert payload.expires_at() > datetime.now()
    assert payload.questions()

    if payload.poll():
        # pylint: disable=no-member
        return entities.Poll( # type: ignore
            parent=payload.poll(),
            expires_at=payload.expires_at(),
            questions=payload.questions()
        )

    # pylint: disable=no-member
    return entities.Poll( # type: ignore
        expires_at=payload.expires_at(),
        questions=payload.questions()
    )
