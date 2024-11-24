from table_classes import Member, Participant, Transaction, Query
from database import Connect
from fastapi import FastAPI
from sqlalchemy import text



app = FastAPI()


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 


connector = Connect('test.db')

# If not database file exists:
# connector.create_tables() 
# connector.populate_db()


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 


@app.get("/")      #127.0.0.0.1:8000/
def test_endpoint():
    return {"test":"Server"}


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 



# ######### CREATE MEMBER
@app.post("/new_member")
def new_member(member: Member):    
    
    query = """
    INSERT INTO Members (first_name, last_name, person_nr, email, phone_nr, member_rank) 
    
        VALUES (:first_name, :last_name, :person_nr, :email, :phone_nr, :member_rank)

    """
    
    params = ({
              "first_name":member.first_name, 
              "last_name": member.last_name, 
              "person_nr": member.person_nr, 
              "email": member.email, 
              "phone_nr": member.phone_nr, 
              "member_rank": member.member_rank
              }
            )



    connector.push_data(text(query), params)


# ######### READ MEMBER
@app.get("/all_members")
def get_all_members():
    try:
        query = 'SELECT * FROM Members'     #selectar allt från tabellen Members
        resp = connector.fetch_data(query)

        return resp

    except Exception as e:
        return {"error": str(e)}


@app.get("/member/{id}")
def get_member(id: int):

    query = f"SELECT * FROM Members where member_id = {id}"
    resp = connector.fetch_data(query)
    
    return resp


# ######### UPDATE MEMBER
@app.put("/update_member/{member_id}")
def update_member(member_id: int, member: Member):  
    print("API SIDE >>>>>>>>>", member)

    query = """
    UPDATE Members
    SET first_name = :first_name, last_name = :last_name, person_nr = :person_nr, 
        email = :email, phone_nr = :phone_nr, member_rank = :member_rank
    WHERE member_id = :member_id
    """

    params = {
        "first_name": member.first_name,
        "last_name": member.last_name,
        "person_nr": member.person_nr,
        "email": member.email,
        "phone_nr": member.phone_nr,
        "member_rank": member.member_rank,
        "member_id": member_id
    }

    connector.push_data(text(query), params)
    print("Updated:", member)


# ######### DELETE MEMBER
@app.delete("/delete_member/{member_id}")
def delete_sale(member_id):

    query = "DELETE FROM Members WHERE member_id = :member_id"
    params = { "member_id": member_id }

    success = connector.push_data(text(query), params)

    if success:
        return {"message": "Participant deleted successfully."}
    else:
        return {"error": "Failed to delete participant."}



## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 



# ######### CREATE TRANSACTION
@app.post("/new_transaction")
def new_transaction(transaction: Transaction):  
    
    query = """
    INSERT INTO Transactions (date, product_name, product_price, unit, kg, total, store_name_id, creditor) 
    
        VALUES (:date, :product_name, :product_price, :unit, :kg, :total, :store_name_id, :creditor)

    """
    
    params = ({
              "date":transaction.date, 
              "product_name": transaction.product_name, 
              "product_price": transaction.product_price, 
              "unit": transaction.unit, 
              "kg": transaction.kg, 
              "total": transaction.total,
              "store_name_id": transaction.store_name_id,
              "creditor": transaction.creditor
              }
            )


    connector.push_data(text(query), params)


# ######### READ TRANSACTION
@app.get("/all_transactions")
def get_all_transactions():
    try:
        query = 'SELECT * FROM Transactions'
        resp = connector.fetch_data(query)
        
        return resp

    except Exception as e:
        return {"error": str(e)}



@app.get("/transaction/{id}")
def get_transaction(id: int):

    query = f"SELECT * FROM Transactions where transaction_id = {id}"
    resp = connector.fetch_data(query)
    
    return resp


# ######### UPDATE TRANSACTION
@app.put("/update_transaction/{transaction_id}")
def update_transaction(transaction_id: int, transaction: Transaction):  

    query = """
    UPDATE Transactions
    SET date = :date, product_name = :product_name, product_price = :product_price,
        unit = :unit, kg = :kg, total = :total, store_name_id = :store_name_id, creditor = :creditor
    WHERE transaction_id = :transaction_id
    """

    params = {
        "date": transaction.date,
        "product_name": transaction.product_name,
        "product_price": transaction.product_price,
        "unit": transaction.unit,
        "kg": transaction.kg,
        "total": transaction.total,
        "store_name_id": transaction.store_name_id,
        "creditor": transaction.creditor,
        "transaction_id": transaction_id
    }

    connector.push_data(text(query), params)
    print("Updated:", transaction)


# ######### DELETE TRANSACTION
@app.delete("/delete_transaction/{transaction_id}")
def delete_transaction(transaction_id: int):
    query = "DELETE FROM Transactions WHERE transaction_id = :transaction_id"
    params = {"transaction_id": transaction_id}
    
    success = connector.push_data(text(query), params)
    
    if success:
        return {"message": "Transaction deleted successfully."}
    else:
        return {"error": "Failed to delete transaction."}



## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 



# ######### CREATE PARTICIPANT
@app.post("/new_participant")
def new_participant(participant: Participant):
    
    query = """
    INSERT INTO Participants (first_name, last_name, person_nr, telephone, participated, sex, role) 
    VALUES (:first_name, :last_name, :person_nr, :telephone, :participated, :sex, :role)
    """
    
    params = {
        "first_name": participant.first_name,
        "last_name": participant.last_name,
        "person_nr": participant.person_nr,
        "telephone": participant.telephone,
        "participated": participant.participated,
        "sex": participant.sex,
        "role": participant.role,
    }

    connector.push_data(text(query), params)


# ######### READ PARTICIPANT
@app.get("/all_participants")
def get_all_members():
    try:
        query = 'SELECT * FROM Participants'
        resp = connector.fetch_data(query)

        return resp

    except Exception as e:
        return {"error": str(e)}


@app.get("/participant/{id}")
def get_transaction(id: int):

    query = f"SELECT * FROM Participants where participant_id = {id}"
    resp = connector.fetch_data(query)
    
    return resp


# ######### UPDATE PARTICIPANT
@app.put("/update_participant/{participant_id}")
def update_participant(participant_id: int, participant: Participant):  

    query = """
    UPDATE Participants
    SET first_name = :first_name, last_name = :last_name, person_nr = :person_nr, 
        telephone = :telephone, participated = :participated, sex = :sex, role = :role
    WHERE participant_id = :participant_id
    """

    params = {
        "first_name": participant.first_name,
        "last_name": participant.last_name,
        "person_nr": participant.person_nr,
        "telephone": participant.telephone,
        "participated": participant.participated,
        "sex": participant.sex,
        "role": participant.role,
        "participant_id": participant_id
    }

    connector.push_data(text(query), params)
    print("Updated:", participant)


# ######### DELETE PARTICIPANT
@app.delete("/delete_participant/{participant_id}")
def delete_participant(participant_id: int):
    query = "DELETE FROM Participants WHERE participant_id = :participant_id"
    params = {"participant_id": participant_id}
    
    success = connector.push_data(text(query), params)
    
    if success:
        return {"message": "Participant deleted successfully."}
    else:
        return {"error": "Failed to delete participant."}



## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 

@app.post("/optional_query")
def optional_query(request: Query):

    query = request.query

    query_result = connector.fetch_data(query)

    return query_result


