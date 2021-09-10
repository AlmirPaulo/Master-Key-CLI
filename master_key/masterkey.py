from pass_gen import generate_password
from models import Master_Password, Passwords, Base
from database import SessionLocal, engine
import typer, os


cli = typer.Typer()


@cli.command()
def create_mp(master_password: str, hint: str):
    # validations
    abc = "qwertyuiopasdfghjklzxcvbnm"
    db_check = Master_Password.query.filter_by(id=1).first()
    if db_check:
        typer.echo(f"You already have a Master Password.")

    elif any(i in master_password for i in "0123456789") == False:
        typer.echo("Your Master Password must to be alpanumeric.")

    elif any(i in master_password for i in abc) == False:
        typer.echo("Your Master Password must to be alpanumeric.")

    elif any(i in master_password for i in abc.upper()) == False:
        typer.echo("Your Master Password must to have uppercase and lowercase letters.")

    elif len(master_password) < 8:
        typer.echo("Your Master Password must to be at least 8 characters longer.")

    else:
        # insert data in db
        # print some output like "Done!"
        pass


@cli.command()
def get_hint():
    # get data from db
    # print it
    pass


@cli.command()
def create_passwd():
    # insert service in db
    # generate_password()
    # print the passwd
    pass


@cli.command()
def update_passwd():
    # update database
    # print the passwd
    pass


@cli.command()
def delete_passwd():
    # get data from user
    # update database
    # print some output like "Done!"
    pass


@cli.command()
def get_passwd():
    # get data from database
    # print it
    pass


if __name__ == "__main__":
    cli()
