from table_classes import Transaction, Participant, Member
from dataclasses import asdict
import requests



URL = "http://127.0.0.1:8000"



def create_member(member_details): # måste vara rätt datatype som Member klassen bestämt

    new_member = Member(*member_details)
    response = requests.post(f'{URL}/new_member', json=asdict(new_member))

    return response


def read_all_members():
    response = requests.get(f'{URL}/all_members')
    print("Raw response content:", response.text)  # Debugging output
    
    response.raise_for_status()  
    
    return response.json() #omvandlar till dictionary


def read_member(id):
     
    res = requests.get(f'{URL}/member/{id}') # Member class for updating purposes

    member = res.json()
    try:
        member = Member(**member[0])
        
    except Exception as e:
        return {"error": str(e)}
    
    return member


def update_member(member_id: int, member_details):

    current = read_member(member_id)
    updated = current

    for key, value in member_details.items():
        setattr(updated, key, value)
    
    response = requests.put(f'{URL}/update_member/{member_id}', json=asdict(updated))
    
    return response


def delete_member(member_id):

    response = requests.delete(f'{URL}/delete_member/{member_id}')

    return response



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



def create_participant(participant_details):

    new_participant = Participant(*participant_details)

    response = requests.post(f'{URL}/new_participant', json=asdict(new_participant))

    return response


def read_all_participants():
    response = requests.get(f'{URL}/all_participants')
    print("Raw response content:", response.text)  
    
    response.raise_for_status()  
    
    return response.json()


def read_participant(id):
     
    res = requests.get(f'{URL}/participant/{id}') # Member class for updating purposes

    participant = res.json()
    
    try:
        participant = Participant(**participant[0]) #unpack into class

    except Exception as e:
        return {"error": str(e)}

    
    return participant


def update_participant(participant_id: int, participant_details):

    current = read_participant(participant_id)
    updated = current


    for key, value in participant_details.items():
        setattr(updated, key, value)

    response = requests.put(f'{URL}/update_participant/{participant_id}', json=asdict(updated))
    
    return response


def delete_participant(participant_id: int):

    response = requests.delete(f'{URL}/delete_participant/{participant_id}')
    
    return response



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def create_transaction(transaction_details): # måste vara rätt datatype som Member klassen bestämt

    new_transaction = Transaction(*transaction_details)
    response = requests.post(f'{URL}/new_transaction', json=asdict(new_transaction))

    return response



def update_transaction(transaction_id: int, transaction_details):

    current = read_transaction(transaction_id)
    updated = current


    for key, value in transaction_details.items():
        setattr(updated, key, value)

    response = requests.put(f'{URL}/update_transaction/{transaction_id}', json=asdict(updated))
    
    return response



def read_all_transactions():
    response = requests.get(f'{URL}/all_transactions')
    print("Raw response content:", response.text)  
    
    response.raise_for_status()  
    
    return response.json()



def read_transaction(id):
     
    res = requests.get(f'{URL}/transaction/{id}') # Member class for updating purposes

    transaction = res.json()
    
    try:
        transaction = Transaction(**transaction[0])

    except Exception as e:
        return {"error": str(e)}

    
    return transaction



def delete_transaction(transaction_id: int):

    response = requests.delete(f'{URL}/delete_transaction/{transaction_id}')

    return response


