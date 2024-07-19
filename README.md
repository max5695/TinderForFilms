# TinderForFilms

TinderForFilms ist eine Anwendung, die es Benutzern ermöglicht, Filme zu bewerten und basierend auf diesen Bewertungen Filmempfehlungen zu erhalten. Die Anwendung verwendet die OMDB API, um Filmdaten abzurufen, und das kostenlose GPT-2 Modell, um Empfehlungen zu generieren.

## Installation

1. Klone das Repository:
    ```bash
    git clone https://github.com/max5695/TinderForFilms.git
    ```
2. Wechsle in das Projektverzeichnis:
    ```bash
    cd TinderForFilms
    ```
3. Erstelle und aktiviere eine virtuelle Umgebung:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Auf Windows: venv\Scripts\activate
    ```
4. Installiere die Abhängigkeiten:
    ```bash
    pip install -r requirements.txt
    ```

## Konfiguration

1. Erstelle eine Datei namens `.env` im Hauptverzeichnis des Projekts und füge deinen OMDB API-Schlüssel hinzu:
    ```
    API_KEY=dein_omdb_api_schluessel
    ```

## Nutzung

1. Stelle sicher, dass du die Datei `5years.json` im Verzeichnis `TinderForFilms/MovieDB/` hast. Diese Datei sollte eine Sammlung von Filmen der letzten 5 Jahre enthalten.
2. Starte die Anwendung:
    ```bash
    python main.py
    ```
3. Folge den Anweisungen im Terminal, um Filme zu bewerten. Du kannst Filme mit 'Like', 'Dislike', 'Neutral' bewerten oder 'Done' eingeben, um die Bewertung zu beenden.
4. Deine Bewertungen werden in der Datei `user_ratings.json` gespeichert.
5. Nach dem Beenden der Bewertung erhältst du eine Filmempfehlung basierend auf deinen Bewertungen.

## Beispiel

```
bash
Title: Inception
Director: Christopher Nolan
Synopsis: A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.
Year: 2010
Bewerten Sie den Film mit 'Like', 'Dislike', 'Neutral' oder geben Sie 'Done' ein, um zu beenden: like
Title: The Matrix
Director: Lana Wachowski, Lilly Wachowski
Synopsis: A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.
Year: 1999
Bewerten Sie den Film mit 'Like', 'Dislike', 'Neutral' oder geben Sie 'Done' ein, um zu beenden: done
Ihre Bewertungen wurden gespeichert.
Empfohlener Film: Basierend auf Ihren Bewertungen empfehle ich Ihnen, "Interstellar" zu schauen, da er ähnliche Themen wie "Inception" behandelt und ebenfalls von Christopher Nolan inszeniert wurde.
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE) Datei für Details.


## Kontakt

Bei Fragen oder Anregungen, bitte ein Issue im GitHub-Repository erstellen.
