"""
CMSC 14200, Winter 2025
Homework #1, Task #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

class Card:
    """
    A class for representing cards in the Compatibility card game.

    In this game, each card has a set of features, where both the
    feature's name and value are strings. For example,
    a card could have three features: color, shape, and number.
    The values for these features could be "red", "circle", and "3",
    respectively.
    """

    def __init__(self, features: dict[str,str]) -> None:
        """
        Constructor. Initializes the card with the provided features.

        Once the features for a card are set, the values of the features
        can be changed, but the features themselves cannot be changed

        In other words, if we initialize the "color" feature to "red", we can
        change its value to "blue" later on. However, we cannot rename the
        feature to "colour" or add new features.

        Args:
            features (dict of str to str): The features of the card,
              with their initial values. For example:
              {"color": "red", "shape": "circle", "number": "3"}
        """
        self.features = features.copy()

    def __str__(self) -> str:
        """
        Returns a string representation of the card.
        """
        s = ("["
             + ", ".join([f"{k}: {v}" for k, v in self.features.items()])
             + "]")

        return s

    def set_feature(self, feature: str, value: str) -> None:
        """
        Set the value of a feature on the card.

        Args:
            feature (str): The name of the feature to set.
            value (str): The value to set the feature to.

        Returns: Nothing
        """
        if feature not in self.features:
            raise ValueError(f"Feature '{feature}' not in card")

        self.features[feature] = value

    def get_feature(self, feature:str) -> str:
        """
        Get the value of a feature on the card.

        Args:
            feature (str): The name of the feature to get.

        Returns: The value of the feature.
        """
        if feature not in self.features:
            raise ValueError(f"Feature '{feature}' not in card")
        return self.features[feature]

    def common_features(self, other_features: dict[str,str]) -> dict[str,str]: 
        """
        Find the common features between this card and some given features.

        A "common feature" is one that has the same name and value in both
        the card and the given features.

        For example, suppose the card has features {"color": "red",
        "shape": "circle", "number": "3"}, and we are given the features
        {"color": "red", "shape": "square", "number": "3"}. The common
        features between the two are {"color": "red", "number": "3"}.

        Args:
            other_features (dict of str to str): A dictionary of features to
                compare against.

        Returns (dict of str to str): The common features between the card and
           the given features.
        """
        common = {}
        for feature in self.features:
            if self.features[feature] == other_features.get(feature):
                common[feature] = self.features[feature]
        return common

    def compatible(self, other: "Card") -> bool:
        """
        Determine if this card is compatible with another card.

        A card is compatible with another card if both cards have a single
        common feature

        Args:
            other (Card): Another card

        Returns: True if both cards are compatible, False otherwise
        """
        return len(self.common_features(other.features)) == 1
