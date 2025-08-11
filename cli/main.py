import sys
import os
import asyncio
import click
from models.request_models import PowRequest, FibonacciRequest, FactorialRequest
from storage.db import init_db, log_request



sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)



# Initializam baza de date
init_db()


@click.group()
def cli():
    """CLI pentru operatii matematice"""
    pass


@cli.command()
@click.option('--base', required=True, type=float, help='Baza numarului')
@click.option('--exp', required=True, type=float, help='Exponentul')
def pow(base, exp):
    """Calculeaza puterea unui numar (async)"""
    from services.math_service import power
    req = PowRequest(base=base, exponent=exp)

    async def run():
        result = await power(req.base, req.exponent)
        click.echo(f"{req.base} ^ {req.exponent} = {result}")
        log_request("pow", f"base={base}, exp={exp}", str(result))

    asyncio.run(run())


@cli.command()
@click.option('--n', required=True, type=int, help='Termenul n din Fibonacci')
def fib(n):
    """Calculeaza al n-lea termen din sirul Fibonacci (async)"""
    from services.math_service import fibonacci
    req = FibonacciRequest(n=n)

    async def run():
        result = await fibonacci(req.n)
        click.echo(f"Fibonacci({req.n}) = {result}")
        log_request("fibonacci", f"n={n}", str(result))

    asyncio.run(run())


@cli.command()
@click.option('--n', required=True, type=int, help='Numar pentru factorial')
def fact(n):
    """Calculeaza factorialul unui numar (async)"""
    from services.math_service import factorial
    req = FactorialRequest(n=n)

    async def run():
        result = await factorial(req.n)
        click.echo(f"{req.n}! = {result}")
        log_request("factorial", f"n={n}", str(result))

    asyncio.run(run())


@cli.command()
def view():
    """Afiseaza toate operatiile efectuate"""
    from storage.view import show_all
    show_all()


if __name__ == '__main__':
    cli()
