from pyargon2 import hash
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models.db_table_models import (password_table, transaction_table,
                                    user_table)
from models.transaction_data import TransactionData


class FlowModel(QObject):
    """Flow model.

    Handles authentication, database queries, and other data-related tasks.
    Stores the authentication status of the user.

    Attributes:
        model_auth_signal (pyqtSignal): sent to controller
    """

    model_auth_signal = pyqtSignal(bool)  # sent to controller
    load_pie_chart_signal = pyqtSignal(list)  # sent to controller
    update_labels_signal = pyqtSignal(float, float)  # sent to controller

    def __init__(self):
        """Initialize Flow model."""
        super().__init__()

        self._engine = create_engine(
            "postgresql://flow_db_master:1pdSftvvtiP0GVQ4eytmMWQL4d0JpFHU@dpg-ci1gki67avjfjanekg50-a.frankfurt-postgres.render.com/flow_test_db_jz1j", echo=True)

        self._is_authenticated = False
        self._user_email_id = None
        self._income_transaction_data = TransactionData(is_income=True)
        self._income_total = 0
        self._expense_transaction_data = TransactionData(is_income=False)
        self._expense_total = 0

    @property
    def engine(self):
        """Return the database engine.

        Returns:
            sqlalchemy.engine.Engine: the database engine
        """
        return self._engine

    @property
    def user_email(self):
        """Return the user's email.

        Returns:
            str: the user's email or None if not authenticated
        """
        return self._user_email_id

    @property
    def is_authenticated(self):
        """Return whether the user is authenticated.

        Returns:
            bool: True if authenticated, False otherwise
        """
        return self._is_authenticated

    @property
    def user_transactions(self):
        """Return the user's transactions.

        Returns:
            list: the user's transactions
        """
        return self._user_transactions
    
    @property
    def income_total(self):
        """Return the user's total income.

        Returns:
            float: the user's total income
        """
        return self._income_total
    
    @property
    def expense_total(self):
        """Return the user's total expenses.

        Returns:
            float: the user's total expenses
        """
        return self._expense_total

    @pyqtSlot(tuple)
    def authenticate_user(self, login_request_details):
        """Authenticate the user.

        If the user is authenticated, emit True signal to controller.
        Otherwise, emit False signal to controller.

        Args:
            login_request_details (tuple): the user's email and password

        TODO:
            - implement proper query
            - don't hardcode salt
        """
        salt = "some_salt"
        hashed_email = hash(login_request_details[0], salt=salt)
        hashed_password = hash(login_request_details[1], salt=salt)

        with Session(self._engine) as session, session.begin():
            # get email and password from database
            # TODO: not properly implemented
            get_email_query = select(user_table).where(
                user_table.c.email == hashed_email)
            email_query_res = session.execute(get_email_query).all()

            get_pword_query = select(password_table).where(
                password_table.c.password == hashed_password)
            pword_query_res = session.execute(get_pword_query).all()

        try:
            # authentication successful
            if (hashed_email == email_query_res[0][1]
                    and hashed_password == pword_query_res[0][1]):
                self._user_email_id = email_query_res[0][0]
                self._is_authenticated = True
                self.model_auth_signal.emit(True)
            else:
                # authentication failed
                self._user_email_id = None
                self._is_authenticated = False
                self.model_auth_signal.emit(False)
        except IndexError:
            # query returned no results i.e. user not found
            self._user_email_id = None
            self._is_authenticated = False
            self.model_auth_signal.emit(False)

    def get_all_transactions_from_db(self):
        """Get all transactions from the database.

        Return a list of RowMapping objects for each transaction which behaves
        as a dict.

        Returns:
            list: all transactions from the database
        """
        with Session(self._engine) as session, session.begin():
            # get income and expenses from database
            get_transactions = select(transaction_table).where(
                transaction_table.c.user_id == self._user_email_id)
            return session.execute(get_transactions).mappings().all()

    @pyqtSlot(bool)
    def initialise_user_transactions(self):
        """Initialise the user's transactions.

        Populate both the income and expense transaction data models with the user's transactions
        when the app first loads. Provides an initial total for both income and expenses.

        Args:
            is_authenticated (bool): whether the user is authenticated

        Returns:
            None
        """
        db_transactions = self.get_all_transactions_from_db()
        if db_transactions is None:
            return

        for transaction in db_transactions:
            if transaction["is_income"]:
                self._income_transaction_data.add_transaction(transaction)
                self._income_total += float(transaction["amount"])
            else:
                self._expense_transaction_data.add_transaction(transaction)
                self._expense_total += float(transaction["amount"])

        self.update_labels_signal.emit(self._income_total, self._expense_total)
        
        # load data to pie chart
        self.load_pie_chart_signal.emit(db_transactions)

    def add_transaction_to_db(self, transaction):
        """Add a transaction to the database.

        As the database handles the primary key, we need to return the
        transaction that was added to the database so that we can
        add it to the transaction data models.

        Args:
            transaction (dict): the transaction to add to the database

        Returns:
            dict: the transaction that was added to the database
                  containing the value of the primary key (id)
        """
        self._income_total += float(transaction["amount"]) if transaction["is_income"] else 0
        self._expense_total += float(transaction["amount"]) if not transaction["is_income"] else 0
        result = None
        with Session(self._engine) as session, session.begin():
            add_transaction_query = transaction_table.insert().values(
                user_id=self._user_email_id,
                amount=transaction["amount"],
                date=transaction["date"],
                description=transaction["description"],
                is_income=transaction["is_income"]
            )
            result = session.execute(add_transaction_query)
        self.update_labels_signal.emit(self._income_total, self._expense_total)
        return result.last_inserted_params()
