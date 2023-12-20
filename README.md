# Selenium Webseiten-Automatisierung

Dieses Python-Skript verwendet Selenium, um automatisierte Interaktionen auf einer spezifischen Webseite durchzuführen. Es loggt sich in die Webseite ein, navigiert zu einer Unterseite, und führt Aktionen basierend auf Button-Werten durch.

## Funktionsweise

Das Skript folgt diesen Schritten:

1. **Initialisierung des Webdrivers**: Es wird ein WebDriver für Chrome initialisiert, der für die Interaktion mit dem Browser erforderlich ist.

2. **Seite Öffnen**: Das Skript öffnet die Login-Seite der Zielwebseite.

3. **Benutzeranmeldung**: Es füllt die Anmeldefelder für Benutzername und Passwort aus und klickt auf den Login-Button. Hierbei müssen die Platzhalter `XXXXXXXX` durch die tatsächlichen Anmeldedaten ersetzt werden.

4. **Navigation**: Nach dem Login navigiert das Skript zu einer spezifischen Unterseite.

5. **Interaktion mit dem Dialogfenster**: Das Skript versucht, einen Button zum Öffnen eines Dialogfensters zu klicken und wartet dann, bis dieses sichtbar wird.

6. **Button-Aktionen**: Es sucht nach Buttons mit spezifischen Werten ('Kommen' oder 'Gehen') und klickt auf den ersten gefundenen Button dieser Kriterien.

7. **Protokollierung**: Jede ausgeführte Aktion (Klicken eines Buttons) wird mit einem Zeitstempel in eine Log-Datei geschrieben.

8. **Fehlerbehandlung**: Bei Fehlern oder wenn kein passender Button gefunden wird, beendet das Skript seine Ausführung und gibt eine Fehlermeldung aus.

## Hinweis zur Anpassung

Es ist wichtig, die Platzhalter `XXXXXXXX` für Benutzername und Passwort im Skript durch tatsächliche Anmeldedaten zu ersetzen. Andernfalls kann sich das Skript nicht erfolgreich auf der Webseite anmelden.

## Lizenz

Dieses Projekt ist unter der MIT Lizenz lizenziert.
