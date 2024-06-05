from pyargon2 import hash
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models.db_table_models import (expense_table, income_table,
                                    password_table, user_table)
from models.pyqt_transaction_model import PyQtTransactionTableModel
from models.transaction_model import Expense, Income, Transaction


class FlowModel(QObject):
    """Flow model.

    Handles authentication, database queries, and other data-related tasks.
    Stores the authentication status of the user.

    Attributes:
        model_auth_signal (pyqtSignal): sent to controller
    """

    # Signals: model -> controller
    model_auth_signal = pyqtSignal(bool)
    model_totals_changed_signal = pyqtSignal(float, float)

    def __init__(self):
        """Initialize Flow model."""
        super().__init__()

        self._engine = create_engine(
            "postgresql://flow_db_user:3n29Y1Rw8gyqy7mJGvIIz4Yz66LwXW23@dpg-cpg27l8l5elc738lp8a0-a.frankfurt-postgres.render.com/flow_db", echo=True)

        self._is_authenticated = False
        self._user_email_id = None
        self._income_data = PyQtTransactionTableModel()
        self._expense_data = PyQtTransactionTableModel()

    @property
    def engine(self):
        """Return the database engine.

        Returns:
            sqlalchemy.engine.Engine: the database engine
        """
        return self._engine

    @property
    def user_email_id(self):
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

    def get_income_from_db(self):
        try:
            with Session(self._engine) as session, session.begin():
                # get income and expenses from database
                income_query = select(income_table).where(
                    income_table.c.user_id == self._user_email_id)
                return session.execute(income_query).mappings().all()
        except Exception:
            print("Error getting income from db")

    def get_expenses_from_db(self):
        try:
            with Session(self._engine) as session, session.begin():
                # get income and expenses from database
                expense_query = select(expense_table).where(
                    expense_table.c.user_id == self._user_email_id)
                return session.execute(expense_query).mappings().all()
        except Exception:
            print("Error getting expenses from db")

    @pyqtSlot(bool)
    def initialise_user_transactions(self):
        """Initialise the user's transactions.

        Get the user's transactions from the database and add them to the model.
        Once complete, signal to the controller to initialise the labels and pie chart.
        """
        db_incomes = self.get_income_from_db()
        db_expenses = self.get_expenses_from_db()
        if db_incomes and db_expenses is None:
            return

        for item in db_incomes:
            income = Income(item["id"],
                            item["user_id"],
                            item["amount"],
                            item["date"].strftime("%d/%m/%Y"),
                            item["description"])
            self._income_data.add_transaction(income)

        for item in db_expenses:
            expense = Expense(item["id"],
                              item["user_id"],
                              item["amount"],
                              item["date"].strftime("%d/%m/%Y"),
                              item["description"])
            self._expense_data.add_transaction(expense)

        self.model_totals_changed_signal.emit(self._income_data.get_total_amount(),
                                              self._expense_data.get_total_amount())

    @pyqtSlot(Transaction)
    def add_transaction(self, transaction):
        """Add a transaction to the model.

        As the id (uuid) and user_id (uuid) are generated by the database, the
        transaction is added to the database first. The transaction returned from
        the database is then added to the model.

        Args:
            transaction (Transaction): the transaction to add

        Returns:
            None
        """
        if type(transaction) is Expense:
            self._expense_data.add_transaction(
                self.add_transaction_to_db(transaction)
            )
        else:
            self._income_data.add_transaction(
                self.add_transaction_to_db(transaction)
            )

    def add_transaction_to_db(self, transaction):
        """Add transaction to database.

        Add the transaction to the database and return the transaction. The attributes
        transaction.id and transaction.user_id are set to the values generated by the
        datebase.

        Args:
            transaction (Income or Expense): the transaction to add

        Returns:
            Income or Expense: the transaction with the id and user_id set
        """
        table = None
        if type(transaction) is Expense:
            self._expense_data.total_amount += float(transaction.get_amount())
            table = expense_table
        else:
            self._income_data.total_amount += float(transaction.get_amount())
            table = income_table

        result = None
        with Session(self._engine) as session, session.begin():
            add_transaction_query = table.insert().values(
                user_id=self._user_email_id,
                amount=transaction.get_amount(),
                date=transaction.get_date(),
                description=transaction.get_description()
            )
            result = session.execute(add_transaction_query)

        self.model_totals_changed_signal.emit(self._income_data.get_total_amount(),
                                              self._expense_data.get_total_amount())

        transaction._id = result.last_inserted_params()["id"]
        transaction._user_id = result.last_inserted_params()["user_id"]
        transaction._date = transaction.get_date().strftime("%d/%m/%Y")  # covnert to dd/mm/yyyy string for display

        return transaction
