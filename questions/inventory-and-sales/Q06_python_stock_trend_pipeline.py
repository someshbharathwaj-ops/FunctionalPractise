"""
QUESTION:
Clean a noisy list of stock prices, compute a rolling average of size `k`, and classify each price
movement relative to the previous valid price as bullish, bearish, or stable.

CONCEPT:
Filtering, zipping, moving-window analytics, functional pipelines.

DIFFICULTY:
Intermediate

APPROACH:
Invalid prices are removed first. A rolling average is built with `map` over index positions, and
trend labels are derived by zipping each price with its predecessor.

EXAMPLE RUN:
Valid prices: [120, 125, 130, 9000, 135, 140, 9500, 145, 200, 110]
Rolling average (k=3): [125.0, 3085.0, 3088.333, 3091.667, 3258.333, 3261.667, 3281.667, 151.667]
Price trends: [('START', 120), ('bullish', 125), ('bullish', 130), ('bullish', 9000), ('bearish', 135), ('bullish', 140), ('bullish', 9500), ('bearish', 145), ('bullish', 200), ('bearish', 110)]

NOTES:
The original code contained broken zipping and trend-classification logic. The refactor keeps the
same analytical intent and turns it into a complete pipeline.
"""

stock_prices = [120, -1, 20000, 125, 130, 9000, 135, 140, 9500, 145, 200, 110]


def filter_prices(prices: list[int]) -> list[int]:
    return list(filter(lambda price: 0 < price < 10000, prices))


def rolling_average(prices: list[int], window_size: int) -> list[float]:
    if window_size <= 0 or window_size > len(prices):
        return []

    return list(
        map(
            lambda index: round(
                sum(prices[index : index + window_size]) / window_size,
                3,
            ),
            range(len(prices) - window_size + 1),
        )
    )


def classify_trends(prices: list[int]) -> list[tuple[str, int]]:
    if not prices:
        return []

    changes = list(
        map(
            lambda pair: (
                "bullish"
                if pair[1] > pair[0]
                else "bearish"
                if pair[1] < pair[0]
                else "stable",
                pair[1],
            ),
            zip(prices, prices[1:]),
        )
    )
    return [("START", prices[0])] + changes


if __name__ == "__main__":
    valid_prices = filter_prices(stock_prices)
    print("Valid prices:", valid_prices)
    print("Rolling average (k=3):", rolling_average(valid_prices, 3))
    print("Price trends:", classify_trends(valid_prices))
