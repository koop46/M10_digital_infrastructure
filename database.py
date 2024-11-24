from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Boolean, Date
import pandas as pd
import numpy as np


class Connect:


    def __init__(self, db_file):
        self.db_file = db_file
        connection_url = f"sqlite:///{self.db_file}"  #sqlite:///M10.db
        self.engine = create_engine(connection_url, echo=False)         # skapar en connection till databas / skapar en databas den connectar till
        self.db_connection = self.engine.connect()


    def fetch_data(self, query):
        df = pd.read_sql(query, con=self.db_connection)

        df = df.replace(np.nan, '', regex=True)
        df = df.to_dict(orient='records')

        return df


    def insert_table(self, df, tablename): #inserta table
        df.to_sql(tablename, if_exists = 'append', index = False, con = self.db_connection)


    def disconnect(self):
        try:
            self.db_connection.close()
            print("Disconnected")
        except Exception as e:
            print(f"Error closing connection: {e}")


    def __del__(self):
        try:
            self.db_connection.close()
        except:
            pass


    def push_data(self, query, *args):

        try:
            self.db_connection.execute(query, args)
            self.db_connection.commit() 

            print("Query executed successfully.")
            return True  # Return success status
        
        except Exception as e:
            print(f"Error executing query: {e}")
            return False


    def create_tables(self):
        metadata = MetaData()
        members = Table(
            'Members', metadata,
            Column('member_id', Integer, primary_key=True, autoincrement=True),
            Column('first_name', String, nullable=False),
            Column('last_name', String, nullable=False),
            Column('person_nr', String, unique=True, nullable=False),
            Column('email', String, unique=True, nullable=False),
            Column('phone_nr', String, nullable=False),
            Column('member_rank', String, nullable=False)
        )

        transactions = Table(
            'Transactions', metadata,
            Column('transaction_id', Integer, primary_key=True, autoincrement=True),
            Column('date', Date, nullable=False),
            Column('product_name', String, nullable=False),
            Column('product_price', Float, nullable=False),
            Column('unit', String, nullable=True),
            Column('kg', Float, nullable=True),
            Column('total', Float, nullable=False),
            Column('store_name_id', String, nullable=False),
            Column('creditor', String, nullable=False)
        )

        participants = Table(
            'Participants', metadata,
            Column('participant_id', Integer, primary_key=True, autoincrement=True),
            Column('first_name', String, nullable=False),
            Column('last_name', String, nullable=False),
            Column('person_nr', String, unique=True, nullable=False),
            Column('telephone', String, nullable=False),
            Column('participated', Boolean, nullable=False),
            Column('sex', Boolean, nullable=False),
            Column('role', String, nullable=False)
        )

        metadata.create_all(self.engine)

    def populate_db(self):

        members_df = pd.DataFrame(
            {
                'first_name': ['Alejandro', 'Shariq', 'Qasim'],
                'last_name': ['Martinez', 'Ali', 'Ali'],
                'person_nr': ['19850101-1234', '19800315-5678', '19921201-2345'],
                'email': ['shariq@email.com', 'john.doe@email.com', 'jane.smith@email.com'],
                'phone_nr': ['1234567890', '0987654321', '1122334455'],
                'member_rank': ['CEO', 'CTO', 'COO']
            }
        )   
        self.insert_table(members_df, 'Members')

        transactions_df = pd.DataFrame( 
            {
                'date': pd.to_datetime(['2024-11-16', '2024-11-16', '2024-11-16', '2024-11-16']).date,
                'product_name': ['BANANER EKO', 'CHOKLADFLARN', 'PÄRON CONFERENCE XT', 'ÄPPLE GRANY SMITH'],
                'product_price': [29.95, 44.95, 24.95, 35.95],
                'unit': [None, 1.0, 1.0, None],
                'kg': [1.242, None, None, 1.206],
                'total': [37.198, 44.95, 24.95, 43.36],
                'store_name_id': ['Coop Landala_1', 'Coop Landala_1', 'Coop Landala_1', 'Coop Landala_1'],
                'creditor': ['Shariq Ali', 'Shariq Ali', 'Shariq Ali', 'Shariq Ali']
            }
        )
        self.insert_table(transactions_df, 'Transactions')

        participants_df = pd.DataFrame(
            {
                'first_name': ['Alice', 'Maria', 'John', 'Emma', 'James'],
                'last_name': ['Johnson', 'Gonzalez', 'Doe', 'Davis', 'Taylor'],
                'person_nr': ['19900824-1122', '19950709-3344', '19851231-5567', '19930321-7788', '19961210-8899'],
                'telephone': ['6677889900', '3344556677', '9988776655', '2233445566', '5566778899'],
                'participated': [True, False, True, True, True],
                'sex': [False, False, True, False, True],
                'role': ['Manager', 'Developer', 'Developer', 'HR Specialist', 'Designer']
            }
        )

        self.insert_table(participants_df, 'Participants')
        print("Database successfully populated.")


