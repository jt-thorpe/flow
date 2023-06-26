from pyargon2 import hash
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models.db_table_models import password_table, user_table


class FlowModel(QObject):
    """Flow model.

    Handles authentication, database queries, and other data-related tasks.
    Stores the authentication status of the user. Emits signals to the
    controller and receives signals from the controller. Should never interact
    with the view directly.

    Attributes:
        model_auth_signal (pyqtSignal): sent to controller
    """

    model_auth_signal = pyqtSignal(bool)  # sent to controller

    def __init__(self):
        """Initialize Flow model."""
        super().__init__()

        self._engine = create_engine(
            "postgresql://flow_db_master:1pdSftvvtiP0GVQ4eytmMWQL4d0JpFHU@dpg-ci1gki67avjfjanekg50-a.frankfurt-postgres.render.com/flow_test_db_jz1j", echo=True)
        self._user_email = None
        self._is_authenticated = False

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
        return self._user_email

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
                self._user_email = login_request_details[0]
                self._is_authenticated = True
                self.model_auth_signal.emit(True)
            else:
                # authentication failed
                self._user_email = None
                self._is_authenticated = False
                self.model_auth_signal.emit(False)
        except IndexError:
            # query returned no results i.e. user not found
            self._user_email = None
            self._is_authenticated = False
            self.model_auth_signal.emit(False)
