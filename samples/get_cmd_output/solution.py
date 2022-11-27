@task
def test(ctx):
    res = ctx.run("whoami")
    print(res.stdout)
