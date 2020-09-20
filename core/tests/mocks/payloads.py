'''
Here goes all the mocks for the payloads implementations, use this wisely xD
'''
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from core import entities
from core.payloads import PollPayload, QuestionPayload


@dataclass
class MockPollPayload(PollPayload):
    '''emulate a incoming payload on the test case'''

    parent: Optional[entities.Poll] = None

    def poll(self) -> Optional[entities.Poll]:
        return self.parent

    def questions(self) -> List[QuestionPayload]:
        return [
            QuestionPayload('quesiton #1', ['op #1', 'op #2', 'op #3', 'op #4']),
            QuestionPayload('quesiton #2', ['op #5', 'op #6', 'op #7', 'op #8']),
            QuestionPayload('quesiton #3', ['op #9', 'op #10', 'op #11', 'op #12'])
        ]

    def expires_at(self) -> datetime:
        return datetime.now() + timedelta(days=1)
