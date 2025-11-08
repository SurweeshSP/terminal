import os
import subprocess
import webbrowser
import datetime
import pyttsx3
from rich.console import Console
from rich.prompt import Prompt

console = Console()
engine = pyttsx3.init()
LOG_FILE = os.path.expanduser("~/assistant_log.txt")

def speak(text):
    console.print(f"[green][Voice][/green] {text}")
    engine.say(text)
    engine.runAndWait()

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")



def open_app(app_name):
    apps = {
        "vscode": "code",
        "chrome": "chrome.exe",
        "notepad": "notepad.exe",
        "spotify": "spotify.exe",
        "explorer": "explorer.exe",
        "terminal": "wt.exe"
    }

    console.print(f"[bold cyan]Opening {app_name}...[/bold cyan]")
    if app_name in apps:
        try:
            subprocess.Popen(apps[app_name], shell=True)
            log_event(f"Opened app: {app_name}")
            speak(f"{app_name} opened successfully.")
        except Exception as e:
            log_event(f"Error opening {app_name}: {e}")
            console.print(f"[red]Failed to open {app_name}[/red]")
            speak("Failed to open the app.")
    else:
        webbrowser.open(f"https://www.google.com/search?q={app_name}")
        speak(f"Searching online for {app_name}")
        log_event(f"Searched online for {app_name}")

def search_web(query):
    console.print(f"[yellow]Searching for:[/yellow] {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")
    log_event(f"Searched web for: {query}")
    speak(f"Search complete for {query}")

def run_command(cmd):
    console.print(f"[bold magenta]Running command:[/bold magenta] {cmd}")
    log_event(f"Executing command: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            console.print(f"[green]{result.stdout}[/green]")
        if result.stderr:
            console.print(f"[red]{result.stderr}[/red]")
        log_event(f"Command completed: {cmd}")
        speak("Done.")
    except Exception as e:
        log_event(f"Command failed: {e}")
        console.print(f"[red]Error running command: {e}[/red]")
        speak("Command failed.")

def spotify_mode():
    """Enter Spotify mode: interpret commands with 'spotify>' prompt"""
    console.print("[bold cyan]Entered Spotify Mode. Type 'exit spotify' to return.[/bold cyan]")
    speak("Spotify mode activated.")
    log_event("Entered Spotify mode")

    while True:
        cmd = Prompt.ask("[bold green]spotify>[/bold green]").strip().lower()

        if cmd in ["exit", "exit spotify", "quit"]:
            console.print("[cyan]Leaving Spotify mode...[/cyan]")
            speak("Exiting Spotify mode.")
            log_event("Exited Spotify mode")
            break

        elif cmd.startswith("play "):
            song = cmd.replace("play ", "").strip()
            console.print(f"Playing: {song}")
            log_event(f"Spotify play: {song}")
            speak(f"Playing {song} on Spotify.")
            webbrowser.open(f"https://open.spotify.com/search/{song.replace(' ', '%20')}")

        elif cmd == "pause":
            console.print("Paused playback (simulated).")
            log_event("Spotify pause")
            speak("Paused Spotify playback.")

        elif cmd == "next":
            console.print("Skipped to next song (simulated).")
            log_event("Spotify next")
            speak("Next song.")

        elif cmd.startswith("search "):
            query = cmd.replace("search ", "").strip()
            console.print(f"Searching for {query} in Spotify...")
            log_event(f"Spotify search: {query}")
            webbrowser.open(f"https://open.spotify.com/search/{query.replace(' ', '%20')}")
            speak(f"Searching for {query} on Spotify.")

        else:
            console.print("[red]Unknown Spotify command.[/red]")
            speak("Unknown command.")


def main():
    console.print("\n[bold cyan]WSL AI Terminal Assistant[/bold cyan]")
    console.print("[dim]Type 'exit' to quit.[/dim]")
    console.print("[dim]Examples: open vscode | search neuralink | run ls -l | open spotify:[/dim]\n")

    while True:
        cmd = Prompt.ask("[bold white]>[/bold white]").strip().lower()

        if not cmd:
            continue

        if cmd == "exit":
            speak("Goodbye!")
            log_event("Exited terminal assistant.")
            break
        elif cmd.startswith("open spotify:"):
            open_app("spotify")
            spotify_mode()
        elif cmd.startswith("open "):
            app = cmd.replace("open ", "").strip()
            open_app(app)
        elif cmd.startswith("search "):
            query = cmd.replace("search ", "").strip()
            search_web(query)
        elif cmd.startswith("run "):
            command = cmd.replace("run ", "").strip()
            run_command(command)
        else:
            run_command(cmd)

if __name__ == "__main__":
    main()
