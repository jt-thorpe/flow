"""A module that contains the PyQtTransactionTableModel class.

This module contains the PyQtTransactionTableModel class, which is a model to hold
transaction data, which can be displayed in a QTableView. Follows PyQt's Model/View
design pattern.

Classes:
    PyQtTransactionTableModel: A class to represent a PyQt transaction table model.
"""

from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex, QVariant


class PyQtTransactionTableModel(QAbstractTableModel):
    """A class to represent a PyQt transaction table model.

    Inherits from QAbstractTableModel.

    Attributes:
        transactions (list): a list of transactions
        total_amount (float): the total amount of all transactions in the model

    Methods:
        rowCount: Return the number of rows under the given parent.
        columnCount: Return the number of columns for the children of the given parent.
        data: Return the data stored under the given role for the item referred to by the index.
        headerData: Return the data for the given role and section in the header with the specified orientation.
        get_total_amount: Return the total amount of all transactions in the model.
        add_transaction: Add a transaction to the model.
        remove_transaction: Remove a transaction from the model.
    """

    def __init__(self, transactions=None, parent=None):
        super().__init__(parent)
        self.transactions = transactions or []
        self.total_amount = 0.00

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows under the given parent.

        Is an override of the QAbstractTableModel.rowCount() method.

        Args:
            parent (QModelIndex): the parent index

        Returns:
            int: the number of rows under the given parent
        """
        return len(self.transactions)

    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns for the children of the given parent.

        Is an override of the QAbstractTableModel.columnCount() method. Always returns 3 as
        only displays Amount, Date, and Description.

        Args:
            parent (QModelIndex): the parent index

        Returns:
            int: the number of columns for the children of the given parent
        """
        return 3

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Return the data stored under the given role for the item referred to by the index.

        Is an override of the QAbstractTableModel.data() method. QVariant is an equivalent to
        a Python object.

        Args:
            index (QModelIndex): the index of the item
            role (Qt.ItemDataRole): the role of the item

        Returns:
            QVarient: the data stored under the given role for the item referred to by the index
        """
        if not index.isValid() or not (0 <= index.row() < len(self.transactions)):
            return QVariant()

        transaction = self.transactions[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            column = index.column()
            if column == 0:
                return QVariant(str(transaction.get_amount()))
            elif column == 1:
                return QVariant(str(transaction.get_date()))
            elif column == 2:
                return QVariant(transaction.get_description())
        elif role == Qt.ItemDataRole.UserRole + 1:  # Displaying ID
            return QVariant(str(transaction.get_id()))
        elif role == Qt.ItemDataRole.UserRole + 2:  # Displaying User ID
            return QVariant(str(transaction.get_user_id()))

        return QVariant()

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """Return the data for the given role and section in the header with the specified orientation.

        Is an override of the QAbstractTableModel.headerData() method. QVariant is an equivalent to
        a Python object.

        Args:
            section (int): the section of the header
            orientation (Qt.Orientation): the orientation of the header
            role (Qt.ItemDataRole): the role of the item

        Returns:
            QVarient: the data for the given role and section in the header with the specified orientation
        """
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            headers = ['Amount', 'Date', 'Description']
            return QVariant(headers[section])
        return QVariant()

    # Optional: Implement setData to allow editing if necessary
    # def setData(self, index, value, role=Qt.EditRole):
    #     if index.isValid() and 0 <= index.row() < len(self.transactions):
    #         # Implement editing logic here
    #         return True
    #     return False

    def get_total_amount(self):
        """Return the total amount of all transactions in the model.

        Returns:
            float: the total amount of all transactions in the model
        """
        return float(self.total_amount)

    def add_transaction(self, transaction):
        """Add a transaction to the model.

        Args:
            transaction (Transaction): the transaction to add

        Returns:
            None
        """
        self.beginInsertRows(QModelIndex(), len(
            self.transactions), len(self.transactions))
        self.transactions.append(transaction)
        self.endInsertRows()

        self.total_amount += float(transaction.get_amount())

    def remove_transaction(self, row):
        """Remove a transaction from the model.

        Args:
            row (int): the row of the transaction to remove

        Returns:
            float: the amount of the transaction removed or None if the row is invalid
        """
        # BORKED
        if 0 <= row < len(self.transactions):
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.transactions[row]
            self.endRemoveRows()

            removed_amount = self.transactions[row].get_amount()
            self.total_amount -= removed_amount
            return removed_amount
