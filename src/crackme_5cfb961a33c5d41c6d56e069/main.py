import typer

app = typer.Typer()


@app.command()
def keygen() -> None:
    typer.echo("Implement your keygen for crackme_5cfb961a33c5d41c6d56e069 here.")


if __name__ == "__main__":
    app()
