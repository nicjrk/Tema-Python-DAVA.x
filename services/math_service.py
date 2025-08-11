import asyncio


async def power(base: float, exponent: float) -> float:
    await asyncio.sleep(0.1)  # simulam calcul asincron
    return base ** exponent


async def fibonacci(n: int) -> int:
    await asyncio.sleep(0.1)
    if n <= 0:
        raise ValueError("n trebuie sa fie > 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


async def factorial(n: int) -> int:
    await asyncio.sleep(0.1)
    if n < 0:
        raise ValueError("n trebuie sa fie >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
