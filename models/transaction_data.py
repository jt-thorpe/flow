from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex


class TransactionData(QAbstractTableModel):
    def __init__(self, data=None, is_income=None):
        super().__init__()
        self._data = data or []
        self._filter_is_income = is_income

    def rowCount(self, parent):
        """Return the number of rows in the model.

        Is an override of the QAbstractTableModel.rowCount() method.

        Args:
            parent (QModelIndex): the parent model index

        Returns:
            int: the number of rows in the model
        """
        if self._filter_is_income is None:
            return len(self._data)
        return sum(1 for transaction in self._data if transaction["is_income"] == self._filter_is_income)

    def columnCount(self, parent):
        """Return the number of columns in the model.

        Is an override of the QAbstractTableModel.columnCount() method.

        Args:
            parent (QModelIndex): the parent model index

        Returns:
            int: the number of columns in the model
        """
        return 6

    def data(self, index, role):
        """Return the data stored under the given role for the item referred to by the index.

        Is an override of the QAbstractTableModel.data() method.

        Args:
            index (QModelIndex): the index of the item
            role (Qt.ItemDataRole): the role of the item    

        Returns:
            object: the data stored under the given role for the item referred to by the index
        """
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        filtered_data = [
            transaction for transaction in self._data if transaction["is_income"] == self._filter_is_income]
        row = index.row()
        if row < len(filtered_data):
            transaction = filtered_data[row]
            col = index.column()
            if col == 0:
                return transaction["id"]
            elif col == 1:
                return transaction["user_id"]
            elif col == 2:
                return transaction["amount"]
            elif col == 3:
                return transaction["date"]
            elif col == 4:
                return transaction["description"]
            elif col == 5:
                return transaction["is_income"]
        return None

    def headerData(self, section, orientation, role):
        """Return the data for the given role and section in the header with the specified orientation.

        Is an override of the QAbstractTableModel.headerData() method.

        Args:
            section (int): the section in the header
            orientation (Qt.Orientation): the orientation of the header
            role (Qt.ItemDataRole): the role of the header

        Returns:
            object: the data for the given role and section in the header with the specified orientation
        """
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            if section == 2:
                return "amount"
            elif section == 3:
                return "date"
            elif section == 4:
                return "description"
        return super().headerData(section, orientation, role)

    def add_transaction(self, transaction):
        if self._filter_is_income is None or transaction["is_income"] == self._filter_is_income:
            self.beginInsertRows(QModelIndex(), len(
                self._data), len(self._data))
            self._data.append(transaction)
            self.endInsertRows()
