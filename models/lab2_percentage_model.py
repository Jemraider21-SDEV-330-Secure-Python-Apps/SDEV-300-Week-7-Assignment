from dataclasses import dataclass


class Lab2PercentageModel:
    """Model for formatting percentage
    """

    def __init__(self, numerator: float, denominator: float, decimals: int) -> None:
        self.numerator: float = numerator
        self.denominator: float = denominator
        self.fraction: str = f'{numerator} / {denominator}'
        self.decimals: int = decimals
        self.result = self.format()

    def format(self) -> float:
        """Format the percentage based on contrsuctor data

        Returns:
            float: formatted percentage
        """
        result: float = self.numerator / self.denominator
        return round(result, self.decimals)
