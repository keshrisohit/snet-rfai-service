from enum import Enum


class ApprovedRequestStatus(Enum):
    ACTIVE = "APPROVED/ACTIVE"
    SOLUTION_VOTE = "APPROVED/SOLUTION_VOTE"
    COMPLETED = "APPROVED/COMPLETED"
    EXPIRED = "APPROVED/EXPIRED"


class OpenRequestStatus(Enum):
    ACTIVE = "OPEN/ACTIVE"
    EXPIRED = "OPEN/EXPIRED"


class RFAIStatus(Enum):
    OPEN = OpenRequestStatus
    APPROVED = ApprovedRequestStatus


class RFAIStatusCodes(Enum):
    OPEN = 0
    OPEN_ACTIVE = 1000
    OPEN_EXPIRED = 1010
    APPROVED = 1
    APPROVED_ACTIVE = 1110
    APPROVED_SOLUTION_VOTE = 1120
    APPROVED_COMPLETED = 1130
    APPROVED_EXPIRED = 1140
    REJECTED = 2
    CLOSED = 4
