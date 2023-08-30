import unittest
from models.tags import IncomeTags, ExpenseTags
from models.transaction_model import Income as IncomeTransaction
from models.transaction_model import Expense as ExpenseTransaction
from PyQt6.QtCore import Qt
from models.flow_app_model import FlowModel
from uuid import UUID
from unittest.mock import MagicMock
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from testing.postgresql import Postgresql


class TestFlowAppModelNoDBInteractions(unittest.TestCase):
    def setUp(self):
        self.flow_app_model = FlowModel()

    def test_engine(self):
        self.assertEqual(self.flow_app_model.engine, self.flow_app_model._engine)

    def test_user_email_pre_login(self):
        self.assertEqual(self.flow_app_model.user_email_id, None)

    def test_is_authenticated_pre_login(self):
        self.assertEqual(self.flow_app_model.is_authenticated, False)


class TestFlowAppModelDBInteractions(unittest.TestCase):
    def setUp(self):
        # Create a temporary PostgreSQL database for testing
        self.postgresql = Postgresql()
        test_db_url = "postgresql://flow_db_master:1pdSftvvtiP0GVQ4eytmMWQL4d0JpFHU@dpg-ci1gki67avjfjanekg50-a.frankfurt-postgres.render.com/flow_test_db_jz1j"
        self.engine = create_engine(test_db_url)
        self.flow_app_model = FlowModel()
        self.flow_app_model._engine = self.engine

    def tearDown(self):
        # Clean up the temporary PostgreSQL database after testing
        self.postgresql.stop()

    def test_authenticate_user(self):
        # Mocking session and query results
        mock_session = MagicMock(spec=Session)
        mock_session.__enter__.return_value = mock_session
        mock_session.execute.return_value.all.return_value = [(1, 'hashed_email')]
        self.flow_app_model._engine = MagicMock()
        self.flow_app_model._engine.begin.return_value.__enter__.return_value = mock_session

        # Replace the hard-coded salt with a fixed value for testing
        self.flow_app_model.authenticate_user(('user@example.com', 'password'))

        # Assert that authentication was successful
        self.assertTrue(self.flow_app_model.is_authenticated)
        self.assertEqual(self.flow_app_model.user_email_id, 1)

    def test_get_income_from_db(self):
        # Create test data in the in-memory SQLite database
        with self.engine.connect() as connection:
            connection.execute("CREATE TABLE income_table (user_id INTEGER, amount FLOAT)")

            # Add test income data
            connection.execute("INSERT INTO income_table (user_id, amount) VALUES (1, 100.0)")

        # Set the authenticated user
        self.flow_app_model._is_authenticated = True
        self.flow_app_model._user_email_id = 1

        # Get income data using the method
        income_data = self.flow_app_model.get_income_from_db()

        # Assert that the income data matches the inserted data
        self.assertEqual(len(income_data), 1)
        self.assertEqual(income_data[0]['user_id'], 1)
        self.assertEqual(income_data[0]['amount'], 100.0)


class TestIncomeTransactionl(unittest.TestCase):
    def setUp(self):
        self.income_transaction = IncomeTransaction(
            '872aea66-f99d-4878-941b-d2b77d9bec96',
            '02bba9a6-ffa8-420f-be1f-e92f05261086',
            '1000',
            '2023-08-26',
            'Test income'
        )

    def test_data_display_role(self):
        self.assertEqual(self.income_transaction.data(Qt.ItemDataRole.DisplayRole),
                         ('1000', '2023-08-26', 'Test income'))

    def test_data_user_role_1(self):
        self.assertEqual(self.income_transaction.data(Qt.ItemDataRole.UserRole + 1),
                         '872aea66-f99d-4878-941b-d2b77d9bec96')

    def test_data_user_role_2(self):
        self.assertEqual(self.income_transaction.data(Qt.ItemDataRole.UserRole + 2),
                         '02bba9a6-ffa8-420f-be1f-e92f05261086')

    def test_data_user_role_3(self):
        self.assertEqual(self.income_transaction.data(Qt.ItemDataRole.UserRole + 3), '1000')

    def test_data_user_role_4(self):
        self.assertEqual(self.income_transaction.data(Qt.ItemDataRole.UserRole + 4), '2023-08-26')

    def test_data_user_role_5(self):
        self.assertEqual(self.income_transaction.data(Qt.ItemDataRole.UserRole + 5), 'Test income')

    def test_get_id(self):
        self.assertEqual(self.income_transaction.get_id(),
                         '872aea66-f99d-4878-941b-d2b77d9bec96')

    def test_get_user_id(self):
        self.assertEqual(self.income_transaction.get_user_id(),
                         '02bba9a6-ffa8-420f-be1f-e92f05261086')

    def test_get_amount(self):
        self.assertEqual(self.income_transaction.get_amount(), '1000')

    def test_get_date(self):
        self.assertEqual(self.income_transaction.get_date(), '2023-08-26')

    def test_get_description(self):
        self.assertEqual(self.income_transaction.get_description(), 'Test income')


class TestExpenseTransaction(unittest.TestCase):
    def setUp(self):
        self.expense_transaction = ExpenseTransaction(
            '1a8c3dba-eb2e-4f6c-b0f7-e9429ce3a030',
            '02bba9a6-ffa8-420f-be1f-e92f05261086',
            '500',
            '2023-08-26',
            'Test expense'
        )

    def test_data_display_role(self):
        self.assertEqual(self.expense_transaction.data(Qt.ItemDataRole.DisplayRole),
                         ('500', '2023-08-26', 'Test expense'))

    def test_data_user_role_1(self):
        self.assertEqual(self.expense_transaction.data(Qt.ItemDataRole.UserRole + 1),
                         '1a8c3dba-eb2e-4f6c-b0f7-e9429ce3a030')

    def test_data_user_role_2(self):
        self.assertEqual(self.expense_transaction.data(Qt.ItemDataRole.UserRole + 2),
                         '02bba9a6-ffa8-420f-be1f-e92f05261086')

    def test_data_user_role_3(self):
        self.assertEqual(self.expense_transaction.data(Qt.ItemDataRole.UserRole + 3), '500')

    def test_data_user_role_4(self):
        self.assertEqual(self.expense_transaction.data(Qt.ItemDataRole.UserRole + 4), '2023-08-26')

    def test_data_user_role_5(self):
        self.assertEqual(self.expense_transaction.data(Qt.ItemDataRole.UserRole + 5), 'Test expense')

    def test_get_id(self):
        self.assertEqual(self.expense_transaction.get_id(),
                         '1a8c3dba-eb2e-4f6c-b0f7-e9429ce3a030')

    def test_get_user_id(self):
        self.assertEqual(self.expense_transaction.get_user_id(),
                         '02bba9a6-ffa8-420f-be1f-e92f05261086')

    def test_get_amount(self):
        self.assertEqual(self.expense_transaction.get_amount(), '500')

    def test_get_date(self):
        self.assertEqual(self.expense_transaction.get_date(), '2023-08-26')

    def test_get_description(self):
        self.assertEqual(self.expense_transaction.get_description(), 'Test expense')


class TestIncomeTags(unittest.TestCase):
    def setUp(self):
        self.income_tags = IncomeTags()

    def test_add_tag(self):
        self.income_tags.add_tag('test')
        self.assertEqual(self.income_tags.user_tags, {'test'})

    def test_remove_tag(self):
        self.income_tags.add_tag('test')
        self.income_tags.remove_tag('test')
        self.assertEqual(self.income_tags.user_tags, set())

    def test_get_default_tags(self):
        self.assertEqual(self.income_tags.get_default_tags(),
                         {'salary', 'gift', 'refund', 'transfer', 'other'})

    def test_get_user_tags(self):
        self.income_tags.add_tag('test1')
        self.assertEqual(self.income_tags.get_user_tags(), {'test1'})

    def test_get_all_tags(self):
        self.income_tags.add_tag('test2')
        self.assertEqual(self.income_tags.get_all_tags(), {
                         'salary', 'gift', 'refund', 'transfer', 'other', 'test2'})

    def test_get_single_tag(self):
        self.income_tags.add_tag('test3')
        self.assertEqual(self.income_tags.get_single_tag('test3'), 'test3')

    def test_load_tags_from_txt(self):
        self.income_tags.add_tag('test')
        self.income_tags.load_tags_from_txt('test/resources/test_user_income_tags.txt')
        self.assertEqual(self.income_tags.user_tags, {'test'})


class TestExpenseTags(unittest.TestCase):
    def setUp(self):
        self.expense_tags = ExpenseTags()

    def test_add_tag(self):
        self.expense_tags.add_tag('test')
        self.assertEqual(self.expense_tags.user_tags, {'test'})

    def test_remove_tag(self):
        self.expense_tags.add_tag('test')
        self.expense_tags.remove_tag('test')
        self.assertEqual(self.expense_tags.user_tags, set())

    def test_get_default_tags(self):
        self.assertEqual(self.expense_tags.get_default_tags(), {
                         'groceries', 'dining', 'entertainment', 'travel', 'utilities',
                         'rent', 'mortgage', 'insurance', 'health', 'education',
                         'clothing', 'personal', 'pet', 'savings', 'holiday'})

    def test_get_user_tags(self):
        self.expense_tags.add_tag('test')
        self.assertEqual(self.expense_tags.get_user_tags(), {'test'})

    def test_get_all_tags(self):
        self.expense_tags.add_tag('test')
        self.assertEqual(self.expense_tags.get_all_tags(), {
                         'groceries', 'dining', 'entertainment', 'travel', 'utilities',
                         'rent', 'mortgage', 'insurance', 'health', 'education',
                         'clothing', 'personal', 'pet', 'savings', 'holiday', 'test'})

    def test_get_single_tag(self):
        self.expense_tags.add_tag('test')
        self.assertEqual(self.expense_tags.get_single_tag('test'), 'test')

    def test_load_tags_from_txt(self):
        self.expense_tags.add_tag('test')
        self.expense_tags.load_tags_from_txt(
            'test/resources/test_user_expense_tags.txt')
        self.assertEqual(self.expense_tags.user_tags, {'test'})


if __name__ == '__main__':
    unittest.main()
