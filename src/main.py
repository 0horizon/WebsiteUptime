# TotalHorizons / 0horizon
# 2/13/2024

# Imports
import requests
import time
import datetime
from rich.console import Console # Styling
from rich import print as rprint # Styling 

console = Console()
Websites = ["https://google.com"]

class UptimeChecker:
    def sendRequest(self, destination):
        dt = datetime.datetime.now()
        try:
            status = requests.get(destination)
            if status.status_code != 200:
                console.print(f"[red][bold][{dt}] {destination}[/bold] is down!")
            else:
                 console.print(f"[green][bold][{dt}] {destination}[/bold] is up and running.")
        except Exception as e:
                console.print(f"[yellow][bold][{dt}][/bold] We're unable to reach [bold]{destination}[/bold], status is unknown!\n[yellow]{e}")

    def checkWebsites(self):
        while True:
            for i in Websites:
                self.sendRequest(i)
                time.sleep(240)

UptimeClass = UptimeChecker()
UptimeClass.checkWebsites()
