"""Data model for Lab 2 - Percentage Formatting
"""


class Lab2PercentageModel:
    """Model for formatting percentage
    """

    def __init__(self, numerator: float, denominator: float, decimals: int) -> None:
        self.numerator: float = numerator
        self.denominator: float = denominator
        self.fraction: str = f'{numerator} / {denominator}'
        self.decimals: int = decimals
        self.result = self.format()

    def format(self) -> float | str:
        """Format the percentage based on contrsuctor data

        Returns:
            float: formatted percentage
        """
        result: float | str = 0
        if self.denominator != 0:
            result = self.numerator / self.denominator
        else:
            return "Cannot Divide By 0"
        return round(result, self.decimals)
