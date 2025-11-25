import json
import sys
import click
import os
import time
from pyfiglet import figlet_format
from rich.console import Console

def print_banner():
    console = Console()
    console.print()
    banner = figlet_format("TIME PHOTO STUDIO", font='slant')
    banner_ribbon = "无论过去不问将来无论过去不问将来无论过去不问将来无论过去不问将来"
    console.print(banner_ribbon, style="yellow on black")
    console.print(banner, style="bold cyan")
    console.print(banner_ribbon, style="yellow on black")

def delay_print(message, speed):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def preview():
    delay_print("\nPast or future, let it be.\n", 0.07)
    delay_print("\nCheng Xiaoshi, remember the rules as you take on new clients.\n\n", 0.05)
    print("Choose one from these options:\n1. Dive\n2. Add New Client\n3. Add New Task\n")

@click.command()
@click.option('--choice', prompt='Your choice', help='the option to choose.')
def options(choice):

    if (choice == "1"):
        print("How long would you like to dive: ")
        dive_options()

    elif (choice == "2"):
        print("Enter the name of your new client: ")
    
    elif (choice == "3"):
        print("Enter the name of your task: ")

@click.command()
@click.option('--divechoice', help='the option to choose.')
def dive_options(divechoice):
    print("blah")

def run():
    print_banner()
    preview()
    options()
    

if __name__ == '__main__':
    run()