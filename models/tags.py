from abc import ABC, abstractmethod
from enum import Enum


class Tags(ABC):
    """An abstract class to represent tags."""

    @abstractmethod
    def add_tag(self, tag):
        pass

    @abstractmethod
    def remove_tag(self, tag):
        pass

    @abstractmethod
    def get_default_tags(self):
        pass

    @abstractmethod
    def get_user_tags(self):
        pass

    @abstractmethod
    def get_all_tags(self):
        pass

    @abstractmethod
    def get_single_tag(self, tag):
        pass

    @abstractmethod
    def load_tags_from_txt(self, tagstxt):
        pass


class DefaultIncomeTags(Enum):
    """Represents the default set of income tags. Tag values are always lowercase."""
    SALARY = 'salary'
    GIFT = 'gift'
    REFUND = 'refund'
    TRANSFER = 'transfer'
    OTHER = 'other'


class IncomeTags(Tags):
    """A class to represent income tags.

    Implements the Tags abstract class.

    Attributes:
        default_tags (set): The default set of tags.
        user_tags (set): The user's set of tags.

    Methods:
        add_tag(tag): Add a tag to the user's set of tags.
        remove_tag(tag): Remove a tag from the user's set of tags.
        get_default_tags(): Get the default set of tags.
        get_user_tags(): Get the user's set of tags.
        get_all_tags(): Get all tags (default and user).
        get_single_tag(tag): Get a tag.
        load_tags_from_txt(tagstxt): Populate the user's set of tags from the user_tags.txt file.
    """

    def __init__(self):
        """
        Initialize the Tags class.
        """
        self.default_tags = {tag.value for tag in DefaultIncomeTags}
        self.user_tags = set()

        self.load_tags_from_txt('resources/settings/user_income_tags.txt')

    def add_tag(self, tag):
        """
        Add a tag to the user's set of tags.

        Args:
            tag (str): The tag to add.
        """
        self.user_tags.add(tag.lower())

    def remove_tag(self, tag):
        """
        Remove a tag from the user's set of tags.

        Args:
            tag (str): The tag to remove.
        """
        self.user_tags.remove(tag.lower())

    def get_default_tags(self):
        """
        Get the default set of tags.

        Returns:
            set: The default set of tags.
        """
        return self.default_tags

    def get_user_tags(self):
        """
        Get the user's set of tags.

        Returns:
            set: The user's set of tags.
        """
        return self.user_tags

    def get_all_tags(self):
        """
        Get all tags (default and user).

        Returns:
            set: All tags.
        """
        return self.default_tags.union(self.user_tags)

    def get_single_tag(self, tag):
        """
        Get a tag.

        Args:
            tag (str): The tag to get.

        Returns:
            str: The tag.
        """
        if tag in self.default_tags:
            return tag
        elif tag in self.user_tags:
            return tag
        else:
            return None

    def load_tags_from_txt(self, tagstxt):
        """
        Populate the user's set of tags from the user_tags.txt file.

        Args:
            tagstxt (str): The path to the user_tags.txt file.
        """
        with open(tagstxt, 'r') as f:
            for line in f:
                self.user_tags.add(line.strip())


class DefaultExpenseTags(Enum):
    """Represents the default set of expense tags. Tag values are always lowercase."""
    GROCERIES = 'groceries'
    DINING = 'dining'
    ENTERTAINMENT = 'entertainment'
    TRAVEL = 'travel'
    UTILITIES = 'utilities'
    RENT = 'rent'
    MORTGAGE = 'mortgage'
    INSURANCE = 'insurance'
    HEALTH = 'health'
    EDUCATION = 'education'
    CLOTHING = 'clothing'
    PERSONAL = 'personal'
    PET = 'pet'
    SAVINGS = 'savings'
    HOLIDAY = 'holiday'


class ExpenseTags(Tags):
    """A class to represent expense tags.

    Implements the Tags abstract class.

    Attributes:
        default_tags (set): The default set of tags.
        user_tags (set): The user's set of tags.

    Methods:
        add_tag(tag): Add a tag to the user's set of tags.
        remove_tag(tag): Remove a tag from the user's set of tags.
        get_default_tags(): Get the default set of tags.
        get_user_tags(): Get the user's set of tags.
        get_all_tags(): Get all tags (default and user).
        get_single_tag(tag): Get a tag.
        load_tags_from_txt(tagstxt): Populate the user's set of tags from the user_tags.txt file.
    """

    def __init__(self):
        """
        Initialize the Tags class.
        """
        self.default_tags = {tag.value for tag in DefaultExpenseTags}
        self.user_tags = set()

        self.load_tags_from_txt('resources/settings/user_expense_tags.txt')

    def add_tag(self, tag):
        """
        Add a tag to the user's set of tags.

        Args:
            tag (str): The tag to add.
        """
        self.user_tags.add(tag.lower())

    def remove_tag(self, tag):
        """
        Remove a tag from the user's set of tags.

        Args:
            tag (str): The tag to remove.
        """
        self.user_tags.remove(tag.lower())

    def get_default_tags(self):
        """
        Get the default set of tags.

        Returns:
            set: The default set of tags.
        """
        return self.default_tags

    def get_user_tags(self):
        """
        Get the user's set of tags.

        Returns:
            set: The user's set of tags.
        """
        return self.user_tags

    def get_all_tags(self):
        """
        Get all tags (default and user).

        Returns:
            set: All tags.
        """
        return self.default_tags.union(self.user_tags)

    def get_single_tag(self, tag):
        """
        Get a tag.

        Args:
            tag (str): The tag to get.

        Returns:
            str: The tag.
        """
        if tag in self.default_tags:
            return tag
        elif tag in self.user_tags:
            return tag
        else:
            return None

    def load_tags_from_txt(self, tagstxt):
        """
        Populate the user's set of tags from the user_tags.txt file.

        Args:
            tagstxt (str): The path to the user_tags.txt file.
        """
        with open(tagstxt, 'r') as f:
            for line in f:
                self.user_tags.add(line.strip())
