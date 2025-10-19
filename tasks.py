from invoke import task

@task
def test(ctx):
    """Run unit testing"""
    ctx.run("pytest src/tests/unit_test.py --maxfail=1 --disable-warnings -q", pty=True)

@task
def coverage(ctx):
    """Run unit testing with coverage report"""
    ctx.run("pytest src/tests/unit_test.py --cov=src --cov-report=term-missing", pty=True)

@task
def E2E(ctx):
    """Run a game with two AI playing each other win a semi-random time limit"""
    ctx.run("pytest src/tests/test_E2E.py -v --disable-warnings", pty=True)
