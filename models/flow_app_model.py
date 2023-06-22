from PyQt6.QtCore import QObject, pyqtSignal


class FlowModel(QObject):
    """Flow model."""

    def __init__(self):
        super().__init__()

        self._user_email = None
        self._authenticated = False

    @property
    def user_email(self):
        """Get user.

        No associated setter because the user's email address should not be
        changed after login nor should it be changed by the user.

        Returns:
            str: The user's email address.

        """
        return self._user_email

    @property
    def authenticated(self):
        """Get authenticated.

        No associated setter because the user's authentication status should
        not be changed after login nor should it be changed by the user.

        Returns:
            bool: True if the user is authenticated, False otherwise.

        """
        return self._authenticated
