from dataclasses import dataclass



@dataclass
class Member:

    member_id: int
    first_name: str
    last_name: str
    person_nr: str
    email: str
    phone_nr: str
    member_rank: str


@dataclass
class Transaction:
    transaction_id: int
    date: str 
    product_name: str
    product_price: float
    unit: int
    kg: float
    total: float 
    store_name_id: str
    creditor: str

@dataclass
class Participant:
    participant_id: int
    first_name :str
    last_name :str
    person_nr :str
    telephone :str
    participated :bool
    sex: bool
    role :str

@dataclass
class Query: # query what ever you wish
    query: str


