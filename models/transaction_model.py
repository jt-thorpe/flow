from abc import ABC, abstractmethod
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex, QVariant
from PyQt6.QtGui import QStandardItem


class Transaction(ABC):
    """An abstract class to represent a transaction.

    Attributes:
        _id (QStandardItem): the id of the transaction
        _user_id (QStandardItem): the id of the user who made the transaction
        _amount (QStandardItem): the amount of the transaction
        _date (QStandardItem): the date of the transaction
        _description (QStandardItem): the description of the transaction

    Methods:
        data: Return the data stored under the given role for the item referred to by the index.
        setData: Set data under the given role for the item referred to by the index.
        get_id: Return the id of the transaction.
        get_user_id: Return the id of the user who made the transaction.
        get_amount: Return the amount of the transaction.
        get_date: Return the date of the transaction.
        get_description: Return the description of the transaction.
    """
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_user_id(self):
        pass

    @abstractmethod
    def get_amount(self):
        pass

    @abstractmethod
    def get_date(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class Income(QStandardItem, Transaction):
    """A class to represent an income.

    Inherits from QStandardItem and Transaction.

    Attributes:
        _id (QStandardItem): the id of the income
        _user_id (QStandardItem): the id of the user who received the income
        _amount (QStandardItem): the amount of the income
        _date (QStandardItem): the date of the income
        _description (QStandardItem): the description of the income

    Methods:
        data: Return the data stored under the given role for the item referred to by the index.
        setData: Set data under the given role for the item referred to by the index.
        get_id: Return the id of the income.
        get_user_id: Return the id of the user who received the income.
        get_amount: Return the amount of the income.
        get_date: Return the date of the income.
        get_description: Return the description of the income.
    """

    def __init__(self, id, user_id, amount, date, description):
        """Construct a new Income object.

        Args:
            id (int): the id of the income
            user_id (int): the id of the user who received the income
            amount (float): the amount of the income
            date (datetime): the date of the income
            description (str): the description of the income

        Returns:
            Income: a new Income object
        """
        super().__init__()
        self._id = self.setData(id, Qt.ItemDataRole.UserRole)
        self._user_id = self.setData(user_id, Qt.ItemDataRole.UserRole)
        self._amount = self.setData(amount, Qt.ItemDataRole.UserRole)
        self._date = self.setData(date, Qt.ItemDataRole.UserRole)
        self._description = self.setData(description, Qt.ItemDataRole.UserRole)

    def data(self, role):
        """Return the data stored under the given role for the item referred to by the index.

        Is an override of the QStandardItem.data() method.

        Args:
            role (Qt.ItemDataRole): the role of the item

        Returns:
            object: the data stored under the given role for the item referred to by the index
        """
        role_mappings = {
            Qt.DisplayRole: (self._amount, self._date, self._description),
            Qt.UserRole + 1: self._id,
            Qt.UserRole + 2: self._user_id,
            Qt.UserRole + 3: self._amount,
            Qt.UserRole + 4: self._date,
            Qt.UserRole + 5: self._description
        }
        if role in role_mappings:
            return role_mappings[role]
        return super().data(role)  # defer to QStandardItem.data()

    def setData(self, value, role):
        """Set data under the given role for the item referred to by the index.

        Is an override of the QStandardItem.setData() method.

        Args:
            value (object): the data to set
            role (Qt.ItemDataRole): the role of the item

        Returns:
            bool: True if successful, False otherwise
        """
        if role == Qt.UserRole + 1:
            self._id = value
        elif role == Qt.UserRole + 2:
            self._user_id = value
        elif role == Qt.UserRole + 3:
            self._amount = value
        elif role == Qt.UserRole + 4:
            self._date = value
        elif role == Qt.UserRole + 5:
            self._description = value
        else:
            return super().setData(value, role)  # defers to QStandardItem.setData()

        return True

    def get_id(self):
        """Return the id of the income.

        Returns:
            uuid: the id of the income
        """
        return self._id

    def get_user_id(self):
        """Return the id of the user who received the income.

        Returns:
            uuid: the id of the user who received the income
        """
        return self._user_id

    def get_amount(self):
        """Return the amount of the income.

        Returns:
            float: the amount of the income
        """
        return self._amount

    def get_date(self):
        """Return the date of the income.

        Returns:
            datetime: the date of the income
        """
        return self._date

    def get_description(self):
        """Return the description of the income.

        Returns:
            str: the description of the income
        """
        return self._description


class Expense(QStandardItem, Transaction):
    """A class to represent an expense.

    Inherits from QStandardItem and Transaction.

    Attributes:
        _id (QStandardItem): the id of the expense
        _user_id (QStandardItem): the id of the user who made the expense
        _amount (QStandardItem): the amount of the expense
        _date (QStandardItem): the date of the expense
        _description (QStandardItem): the description of the expense

    Methods:
        data: Return the data stored under the given role for the item referred to by the index.
        setData: Set data under the given role for the item referred to by the index.
        get_id: Return the id of the expense.
        get_user_id: Return the id of the user who made the expense.
        get_amount: Return the amount of the expense.
        get_date: Return the date of the expense.
        get_description: Return the description of the expense.
    """

    def __init__(self, id, user_id, amount, date, description):
        """Construct a new Expense object.

        Args:
            id (int): the id of the expense
            user_id (int): the id of the user who made the expense
            amount (float): the amount of the expense
            date (datetime): the date of the expense
            description (str): the description of the expense

        Returns:
            Expense: a new Expense object
        """
        super().__init__()
        self._id = self.setData(id, Qt.ItemDataRole.UserRole)
        self._user_id = self.setData(user_id, Qt.ItemDataRole.UserRole)
        self._amount = self.setData(amount, Qt.ItemDataRole.UserRole)
        self._date = self.setData(date, Qt.ItemDataRole.UserRole)
        self._description = self.setData(description, Qt.ItemDataRole.UserRole)

    def data(self, role):
        """Return the data stored under the given role for the item referred to by the index.

        Is an override of the QStandardItem.data() method.

        Args:
            role (Qt.ItemDataRole): the role of the item

        Returns:
            object: the data stored under the given role for the item referred to by the index
        """
        role_mappings = {
            Qt.DisplayRole: (self._amount, self._date, self._description),
            Qt.UserRole + 1: self._id,
            Qt.UserRole + 2: self._user_id,
            Qt.UserRole + 3: self._amount,
            Qt.UserRole + 4: self._date,
            Qt.UserRole + 5: self._description
        }
        if role in role_mappings:
            return role_mappings[role]
        return super().data(role)

    def setData(self, value, role):
        """Set data under the given role for the item referred to by the index.

        Is an override of the QStandardItem.setData() method.

        Args:
            value (object): the data to set
            role (Qt.ItemDataRole): the role of the item

        Returns:
            bool: True if successful, False otherwise
        """
        if role == Qt.UserRole + 1:
            self._id = value
        elif role == Qt.UserRole + 2:
            self._user_id = value
        elif role == Qt.UserRole + 3:
            self._amount = value
        elif role == Qt.UserRole + 4:
            self._date = value
        elif role == Qt.UserRole + 5:
            self._description = value
        else:
            return super().setData(value, role)

        return True

    def get_id(self):
        """Return the id of the expense.

        Returns:
            uuid: the id of the expense
        """
        return self._id

    def get_user_id(self):
        """Return the id of the user who made the expense.

        Returns:
            uuid: the id of the user who made the expense
        """
        return self._user_id

    def get_amount(self):
        """Return the amount of the expense.

        Returns:
            float: the amount of the expense
        """
        return self._amount

    def get_date(self):
        """Return the date of the expense.

        Returns:
            datetime: the date of the expense
        """
        return self._date

    def get_description(self):
        """Return the description of the expense.

        Returns:
            str: the description of the expense
        """
        return self._description


class PyQtTransactionTableModel(QAbstractTableModel):
    def __init__(self, transactions=None, parent=None):
        super().__init__(parent)
        self.transactions = transactions or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.transactions)

    def columnCount(self, parent=QModelIndex()):
        return 3

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.transactions)):
            return QVariant()

        transaction = self.transactions[index.row()]

        if role == Qt.DisplayRole:
            column = index.column()
            if column == 0:
                return QVariant(str(transaction.get_amount()))
            elif column == 1:
                return QVariant(str(transaction.get_date()))
            elif column == 2:
                return QVariant(transaction.get_description())
        elif role == Qt.UserRole + 1:  # Displaying ID
            return QVariant(str(transaction.get_id()))
        elif role == Qt.UserRole + 2:  # Displaying User ID
            return QVariant(str(transaction.get_user_id()))

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            headers = ['Amount', 'Date', 'Description']
            return QVariant(headers[section])
        return QVariant()

    # Optional: Implement setData to allow editing if necessary
    # def setData(self, index, value, role=Qt.EditRole):
    #     if index.isValid() and 0 <= index.row() < len(self.transactions):
    #         # Implement editing logic here
    #         return True
    #     return False
