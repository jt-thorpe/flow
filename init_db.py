"""
A utility script to initialise the database.

This script is used to initialise the database and add test data to it.

This script can be run from the command line with the following command:
    python -m flow.utils.init_db
"""
import uuid

from sqlalchemy import create_engine, insert
from sqlalchemy_utils import database_exists

from models.db_table_models import (metadata_obj, password_table,
                                        income_table, expense_table, user_table)

# create engine to connect to database
engine = create_engine(
    "postgresql://flow_db_master:1pdSftvvtiP0GVQ4eytmMWQL4d0JpFHU@dpg-ci1gki67avjfjanekg50-a.frankfurt-postgres.render.com/flow_test_db_jz1j", echo=True)


def init_db():
    """Initialise the database."""
    print("===== INITIALISING DATABASE =====")
    print("Checking database exists...")
    print("WARNING: ALL TABLE DATA WILL BE LOST.")
    cont = input("Enter [y/n] to re-init database... ")
    if (cont == "y" or cont == "Y") and database_exists(engine.url):
        print("Dropping all tables... ")
        metadata_obj.drop_all(engine)
        print("All tables dropped.")
    else:
        print("Exiting.")
        return

    print("Creating tables...")
    metadata_obj.create_all(engine)  # create all tables from metadata_obj

    print("Adding test data...")
    with engine.connect() as conn:
        random_uuid = uuid.uuid4()

        test_user = insert(user_table).values(
            id=random_uuid,
            # a hash of "test@test.com"
            email="2a0761fca1583c463a83e896684483034cff2603f15d164371f42107a06137be")
        conn.execute(test_user)

        test_pword = insert(password_table).values(
            user_id=random_uuid,
            # a hash of "test"
            password="292c79310884cedb2b80bd8696b05f58fff1e1b753b21404f45d1aea4958311c")
        conn.execute(test_pword)

        test_income_transaction = insert(income_table).values(
            user_id=random_uuid,
            amount=1000,
            description="Test income")
        conn.execute(test_income_transaction)
        conn.commit()

        test_expense_transaction = insert(expense_table).values(
            user_id=random_uuid,
            amount=500,
            description="Test expense")
        conn.execute(test_expense_transaction)
        conn.commit()
    print("DONE.")


if __name__ == "__main__":
    init_db()
