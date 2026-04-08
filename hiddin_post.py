import requests
import random
from PIL import Image
from io import BytesIO
import tempfile
import os
import base64
import time
import jwt
from datetime import date

# ============================================
# HIDDIN MARKETING PIPELINE v11
# Kling Video Reels | 3 neue Content-Kategorien
# ============================================

ANTHROPIC_KEY   = os.environ["ANTHROPIC_KEY"]
OPENAI_KEY      = os.environ["OPENAI_KEY"]
POSTSYNCER_KEY  = os.environ["POSTSYNCER_KEY"]
KLING_ACCESS    = os.environ["KLING_ACCESS"]
KLING_SECRET    = os.environ["KLING_SECRET"]
WORKSPACE_ID    = int(os.environ.get("WORKSPACE_ID", "70483"))

# Screenshots & Logo kommen von GitHub (kein lokales Dateisystem nötig)
SCREENSHOT_BASE_URL = "https://raw.githubusercontent.com/fullhousegastro/hiddin-marketing-assets/main/screenshots/"
LOGO_URL            = "https://raw.githubusercontent.com/fullhousegastro/hiddin-marketing-assets/main/assets/logo-icon.png"

START_DATE = date(2026, 4, 9)

ACCOUNTS_SQUARE = [
    {"id": 6225, "settings": {"post_type": "POST"}},
    {"id": 6226, "settings": {"post_type": "POST"}},
]
ACCOUNTS_REELS = [
    {"id": 6225, "settings": {"post_type": "REELS"}},
    {"id": 6224, "settings": {"post_mode": "DIRECT_POST"}}
]

HASHTAGS = {
    "restaurant":      "#hiddin #restaurantmarketing #influencermarketing #gastro #leadgenerierung",
    "influencer":      "#hiddin #influencer #foodinfluencer #gastro #contentcreator",
    "superinfluencer": "#hiddin #influencer #passiveseinkommen #foodinfluencer #gastro",
    "brand":           "#hiddin #secretexperience #restaurantmarketing #influencer #gastro",
    "keinmarketing":   "#hiddin #restaurantmarketing #gastro #digitalisierung #neukundengewinnung",
    "marketingtipp":   "#hiddin #marketingtipp #restaurantmarketing #gastro #gastronomietipps",
}

# ============================================
# 90-TAGE CONTENT PLAN
# ============================================
CONTENT_PLAN = {
    # PHASE 1 — PRE-LAUNCH (Tag 1-30)
    1:  {"type": "restaurant",    "thema": "Du zahlst fuer 6 Tools. Brauchst aber nur 1.", "kontext": "Mailchimp. QR-Generator. Meta Ads. Bewertungsmanager. Influencer-Tool. Newsletter. 6 Tabs. 6 Rechnungen. Bis zu 350 Euro im Monat fuer Tools die nicht miteinander reden. Hiddin ersetzt sie alle in einer App."},
    2:  {"type": "keinmarketing", "thema": "Dein Restaurant hat kein Marketing. Das kostet dich mehr als du denkst.", "kontext": "Kein Newsletter. Keine Influencer. Keine Leads. Kein System. Die meisten Restaurants verlassen sich auf Mundpropaganda allein. Das war 2010 OK. 2025 ist es existenzgefaehrdend. Hiddin ist der einfachste Einstieg ins digitale Marketing."},
    3:  {"type": "marketingtipp", "thema": "Marketing Tipp: Warum deine Stammgaeste deine beste Werbung sind.", "kontext": "Stammgaeste empfehlen weiter. Aber nur wenn du sie aktiv einbindest. Newsletter mit persoenlicher Ansprache. Exklusive Angebote nur fuer Abonnenten. QR-Code am Tisch der direkt zur Anmeldung fuehrt. So baust du eine echte Fan-Community auf."},
    4:  {"type": "brand",         "thema": "Etwas kommt. Und es veraendert wie Restaurants Gaeste gewinnen.", "kontext": "Hiddin verbindet Restaurants mit lokalen Influencern ueber exklusive Secret Experiences. Kein Lead kein Cent. Bald live. Jetzt auf die Warteliste unter hiddin.app"},
    5:  {"type": "influencer",    "thema": "1 Euro pro Lead. Ohne Reichweiten-Druck.", "kontext": "Kein Tausend-Follower-Minimum. Nur lokale Relevanz zaehlt. Teile einen QR-Code mit deinen Followern. Jeder der sich anmeldet bringt dir 1 Euro direkt auf dein Konto."},
    6:  {"type": "keinmarketing", "thema": "Restaurants die keine E-Mails sammeln verlieren Gaeste fuer immer.", "kontext": "Ein Gast kommt. Isst gut. Geht. Du hast seinen Kontakt nicht. Er kommt vielleicht wieder. Vielleicht nicht. Mit einem Newsletter-System behaeltst du den Kontakt. Mit Hiddin sammelst du automatisch E-Mails ueber Influencer-Kampagnen."},
    7:  {"type": "marketingtipp", "thema": "Marketing Tipp: Die 3-2-1 Regel fuer Restaurant-Newsletter.", "kontext": "3 Inhalte pro Newsletter: 1 Story hinter den Kulissen, 1 aktuelles Angebot, 1 persoenliche Empfehlung. 2 mal pro Monat versenden. 1 klarer Call-to-Action. Klingt einfach. Funktioniert. Hiddin's KI-Newsletter-Builder setzt das automatisch um."},
    8:  {"type": "brand",         "thema": "Was ist Hiddin? Erklaert in 30 Sekunden.", "kontext": "Restaurant erstellt Secret Experience. Influencer bekommt QR-Code. Influencer teilt ihn. Follower meldet sich an (DOI). Restaurant bekommt Lead. Zahlt 3 Credits. Influencer bekommt 1 Euro. Kein Lead kein Cent."},
    9:  {"type": "restaurant",    "thema": "Secret Experience — Was bedeutet das?", "kontext": "Ein exklusives Erlebnis nur fuer Influencer-Gaeste. Ein spezielles Menue. Ein Behind-the-Scenes Abend. Die Influencer teilen es. Ihre Follower wollen es auch. So entstehen echte Leads."},
    10: {"type": "influencer",    "thema": "So funktioniert Hiddin fuer Influencer — Schritt fuer Schritt.", "kontext": "1. Kostenlos registrieren. 2. Restaurant laedt ein. 3. QR-Code in Stories teilen. 4. Follower meldet sich an. 5. 1 Euro auf dein Konto. PayPal oder IBAN."},
    11: {"type": "keinmarketing", "thema": "Dein Restaurant ist voll am Wochenende. Dienstags leer. Warum?", "kontext": "Weil du keine aktive Marketingstrategie hast die Gaeste auch unter der Woche bringt. Mit gezielten Influencer-Kampagnen und Newsletter-Aktionen kannst du schwache Tage systematisch fuellen. Hiddin macht genau das moeglich."},
    12: {"type": "marketingtipp", "thema": "Marketing Tipp: So schreibst du eine Betreffzeile die geoeffnet wird.", "kontext": "Die Betreffzeile entscheidet in 2 Sekunden. 5 Formeln die funktionieren: Zahl plus Versprechen (3 neue Gerichte diese Woche). Frage stellen (Kennst du unser Geheimrezept?). Dringlichkeit (Nur bis Freitag). Neugier (Das haben wir noch nie gemacht). Persoenlich (Hey [Name] wir haben etwas fuer dich)."},
    13: {"type": "restaurant",    "thema": "QR-Code → Lead. So einfach ist das.", "kontext": "Hiddin generiert automatisch einen QR-Code pro Kampagne. Influencer teilt ihn. Follower scannt. Meldet sich an. Du bekommst den Kontakt. UTM-Tracking inklusive."},
    14: {"type": "brand",         "thema": "1 Woche Hiddin erklaert. Hast du Fragen?", "kontext": "Secret Experiences. Credits. Influencer-Scores. QR-Codes. Was interessiert dich am meisten? Schreib es in die Kommentare."},
    15: {"type": "marketingtipp", "thema": "Marketing Tipp: Warum Google Bewertungen ueber deinen Umsatz entscheiden.", "kontext": "92% der Gaeste lesen Bewertungen bevor sie ein Restaurant waehlen. 1 negativer Stern kann 30% Umsatz kosten. Aktiv auf Bewertungen antworten. Positive aktiv einfordern. Negative rechtlich pruefen lassen. Hiddin's Bewertungsmanager hilft bei allen drei Punkten."},
    16: {"type": "influencer",    "thema": "Warum lokale Influencer maechtiger sind als nationale.", "kontext": "5.000 lokale Follower in Muenchen sind mehr wert als 500.000 bundesweit fuer ein Restaurant in Muenchen. Hiddin setzt auf lokale Relevanz. Nicht Mega-Reichweite."},
    17: {"type": "keinmarketing", "thema": "Du hast 500 zufriedene Gaeste. Aber keine einzige E-Mail-Adresse.", "kontext": "Das ist das groesste verpasste Marketing-Potenzial in der Gastronomie. Jeder zufriedene Gast koennte ein Stammgast sein. Mit dem richtigen System. Mit Hiddin sammelst du automatisch bestaetigte E-Mail-Kontakte ueber Influencer-Kampagnen."},
    18: {"type": "brand",         "thema": "DOI — Was bedeutet das und warum ist es wichtig?", "kontext": "Double Opt-In bedeutet bestaedigter Kontakt. Der Follower bestaetigt seine Anmeldung per E-Mail. Erst dann wird abgerechnet. DSGVO-konform. Echter Lead. Kein Spam."},
    19: {"type": "marketingtipp", "thema": "Marketing Tipp: Der perfekte Instagram-Post fuer Restaurants.", "kontext": "Hook in Zeile 1 stopp-scrolling. Emotion in Zeile 2-3 erzeugen. Mehrwert oder Geschichte in Zeile 4-6. Klarer Call-to-Action am Ende. Weniger als 5 Hashtags. Echte Fotos schlagen Stock-Bilder immer. Poste zu Peak-Zeiten: 11-13 Uhr und 19-21 Uhr."},
    20: {"type": "restaurant",    "thema": "Google-Bewertungen: 1 Stern kann dich 30% Umsatz kosten.", "kontext": "Hiddin's Bewertungsmanager verbindet dein Google Business Profil. Automatischer Waechter. Negative 1-3 Sterne Bewertungen koennen rechtlich entfernt werden. 49 Credits nur bei Erfolg."},
    21: {"type": "keinmarketing", "thema": "Kein Budget fuer Marketing? Dann ist Hiddin genau richtig.", "kontext": "Hiddin kostet nur wenn ein Lead bestaetigt wird. 3 Euro pro echtem Kontakt. Kein Abo. Kein Monatsbudget. Kein Risiko. Der guenstigste Einstieg ins digitale Marketing fuer Restaurants."},
    22: {"type": "restaurant",    "thema": "Restaurants die frueh dabei sind bekommen Vorteile. Fuer immer.", "kontext": "Early Access bedeutet guenstigere Konditionen. Fuer immer gesperrt auf diesem Preis. Die Warteliste fuellt sich. Jetzt eintragen unter hiddin.app"},
    23: {"type": "marketingtipp", "thema": "Marketing Tipp: Wie du mit QR-Codes am Tisch Leads sammelst.", "kontext": "QR-Code am Tisch ist kein Ersatz fuer die Speisekarte. Er ist die Tuer zu einer direkten Kundenbeziehung. Fuehre zu einer Landing Page mit echtem Mehrwert: Rezept herunterladen. Stammgast-Vorteile sichern. Newsletter abonnieren. Mit Hiddin ist das komplett automatisiert."},
    24: {"type": "influencer",    "thema": "Was kostet dich ein Lead heute? Was kostet er mit Hiddin?", "kontext": "Meta Ads CPL oft 10-30 Euro pro Lead. Hiddin CPL 3 Euro. Nur bei bestaedigtem DOI-Lead. Kein Abo. Kein Risiko. Rechne selbst."},
    25: {"type": "superinfluencer","thema": "Super Influencer — Eine Rolle. Passives Einkommen. Invite-only.", "kontext": "Super Influencer rekrutiert andere Influencer. Pro deren Lead plus 0,50 Euro Provision. 10 Influencer mal 50 Leads mal 0,50 Euro gleich 250 Euro passiv pro Monat. Plus Bewertungsmanager-Provision."},
    26: {"type": "keinmarketing", "thema": "Dein Mitbewerber hat einen Newsletter. Du nicht. Was passiert jetzt?", "kontext": "Er schreibt seinen Gaesten regelmaessig. Erinnert sie an sich. Bietet exklusive Angebote. Sie kommen oefter. Du verlierst Marktanteile ohne es zu merken. Mit Hiddin startest du in 10 Minuten deinen ersten Newsletter."},
    27: {"type": "marketingtipp", "thema": "Marketing Tipp: Saisonales Marketing richtig planen.", "kontext": "Restaurants die saisonal planen haben 40% mehr Stammgaeste. Jede Saison eine neue Kampagne. Neue Gerichte. Neues Erlebnis. Neuer Anlass zum Kommen. Mit Hiddin planst du Secret Experiences Monate im Voraus und fuellst schwache Monate gezielt auf."},
    28: {"type": "brand",         "thema": "Wo Geheimnisse zu Gaesten werden. Bald ist es soweit.", "kontext": "Hiddin verbindet Restaurants mit lokalen Influencern. Authentisch. Messbar. Ohne Risiko. Eine App fuer alles."},
    29: {"type": "keinmarketing", "thema": "Letzte Chance: Sicher dir deinen Platz bevor die App live geht.", "kontext": "Wer jetzt auf die Warteliste kommt startet mit Vorteil. Guenstigere Credits. Prioritaet bei Influencer-Matching. Persoenlicher Onboarding-Support. Jetzt eintragen unter hiddin.app"},
    30: {"type": "brand",         "thema": "30 Tage. 30 Posts. Danke fuer eure Neugier. Es geht los.", "kontext": "30 Tage haben wir erklaert warum Restaurants Hiddin brauchen. Jetzt wird es ernst. Der Launch steht bevor. Seid dabei unter hiddin.app"},
    # PHASE 2 — LAUNCH (Tag 31-60)
    31: {"type": "brand",         "thema": "Hiddin ist live.", "kontext": "Ab heute koennen sich Restaurants und Influencer registrieren. Secret Experiences erstellen. Leads generieren. Fair verdienen. hiddin.app"},
    32: {"type": "restaurant",    "thema": "So richtest du deine erste Secret Experience ein.", "kontext": "Name eingeben oder KI vorschlagen lassen. Beschreibung. Zeitraum. Max Teilnehmer. QR-Code generieren. Influencer einladen. 5 Minuten Setup."},
    33: {"type": "influencer",    "thema": "Dein erster Lead mit Hiddin.", "kontext": "Einladung annehmen. QR-Code in Stories teilen. Follower scannt und meldet sich an. DOI bestaetigt. 1 Euro gutgeschrieben."},
    34: {"type": "marketingtipp", "thema": "Marketing Tipp: Email-Marketing hat 4200% ROI. So nutzt du es richtig.", "kontext": "Fuer jeden investierten Euro kommen im Schnitt 42 Euro zurueck. Das ist der hoechste ROI aller Marketing-Kanaele. Voraussetzung: Gute Liste. Relevante Inhalte. Regelmaessig versenden. Hiddin hilft dir beim Aufbau der Liste und beim Versand."},
    35: {"type": "keinmarketing", "thema": "Du glaubst Marketing ist zu kompliziert fuer dein Restaurant? Lies das.", "kontext": "Marketing muss nicht kompliziert sein. 1 Newsletter pro Monat. 1 Influencer-Kooperation pro Quartal. 1 aktive Google-Business-Seite. Das reicht fuer den Anfang. Hiddin baut alles in eine App. Setup in 10 Minuten."},
    36: {"type": "restaurant",    "thema": "Meta Ads direkt aus Hiddin.", "kontext": "Meta verbinden. Region 10-15km. Budget festlegen. KI generiert Anzeige. Veroeffentlichen. Custom Audience mit Leads synchronisiert. 99 Euro einmalig."},
    37: {"type": "brand",         "thema": "1 Woche live. Erste Restaurants. Erste Influencer. Erste Leads.", "kontext": "Hiddin waechst. Restaurants entdecken Secret Experiences. Influencer verdienen erste Euros. Leads werden generiert. Danke an alle Early Adopter."},
    38: {"type": "marketingtipp", "thema": "Marketing Tipp: Warum Influencer-Marketing fuer kleine Restaurants funktioniert.", "kontext": "Kleine Budgets. Grosse Wirkung. Lokale Influencer sprechen genau die richtige Zielgruppe an. Organisch wirkend. Hohe Glaubwuerdigkeit. CPL 3 Euro statt 20 Euro bei Meta Ads. Mit Hiddin komplett automatisiert und messbar."},
    39: {"type": "influencer",    "thema": "Hiddin Score verbessern — 5 konkrete Tipps.", "kontext": "1. Mehr Kooperationen abschliessen. 2. Hoehere DOI-Rate erzielen. 3. Profil vollstaendig ausfuellen. 4. Kanal verifizieren. 5. Aktiv auf Einladungen reagieren. Score steigt automatisch."},
    40: {"type": "keinmarketing", "thema": "Gastronom seit 10 Jahren. Noch nie einen Newsletter verschickt. Was tun?", "kontext": "Einfach anfangen. Keine Angst vor Perfektion. Der erste Newsletter muss nicht perfekt sein. Er muss nur gesendet werden. Mit Hiddin's KI-Newsletter-Builder ist er in 3 Minuten fertig. 3 Fragen beantworten. KI schreibt alles."},
    41: {"type": "influencer",    "thema": "Auszahlung: Wie und wann kommt dein Geld.", "kontext": "PayPal oder IBAN via Wise. Monatlich oder woechentlich. Mindestbetrag selbst festlegen. Gutschrift automatisch generiert. Transparent und puenktlich."},
    42: {"type": "marketingtipp", "thema": "Marketing Tipp: So optimierst du dein Google Business Profil.", "kontext": "Vollstaendige Infos. Aktuelle Oeffnungszeiten. Mindestens 20 hochwertige Fotos. Regelmaessige Posts. Auf alle Bewertungen antworten. Sonderzeiten eintragen (Feiertage). Produkte und Angebote hinzufuegen. Google bewertet Vollstaendigkeit. Mehr Vollstaendigkeit gleich mehr Sichtbarkeit."},
    43: {"type": "superinfluencer","thema": "Super Influencer Rechner: Wie viel kannst du verdienen?", "kontext": "10 Influencer mal 50 Leads mal 0,50 Euro gleich 250 Euro passiv. 20 Influencer gleich 500 Euro. 50 Influencer gleich 1.250 Euro monatlich. Dazu Bewertungsmanager-Provision. Invite-only."},
    44: {"type": "keinmarketing", "thema": "Warum Mundpropaganda allein nicht mehr reicht.", "kontext": "Mundpropaganda ist wertvoll. Aber nicht skalierbar. Nicht messbar. Nicht steuerbar. Digitales Marketing ist der verlaengerte Arm der Mundpropaganda. Mit Hiddin machst du aus jedem zufriedenen Gast einen digitalen Botschafter."},
    45: {"type": "marketingtipp", "thema": "Marketing Tipp: Die goldene Stunde fuer Restaurant-Posts.", "kontext": "Instagram: 11-13 Uhr und 19-21 Uhr haben hoechste Reichweite. TikTok: 18-22 Uhr. Facebook: 13-16 Uhr. Stories taeglich posten. Feed-Posts 4-5 mal pro Woche. Konsistenz schlaegt Qualitaet. Lieber regelmaessig als perfekt."},
    46: {"type": "restaurant",    "thema": "Erste Restaurant-Erfahrungen mit Hiddin.", "kontext": "Erste Restaurants berichten. Secret Experiences. Lead-Qualitaet. Newsletter-Ergebnisse. Authentische Stimmen aus der Community."},
    47: {"type": "keinmarketing", "thema": "3 Gruende warum Restaurants ohne digitales Marketing scheitern.", "kontext": "1. Keine Neukundenstrategie ausser Empfehlungen. 2. Kein Kontakt zu Bestandsgaesten ausser wenn sie kommen. 3. Keine Messbarkeit was Marketing-Ausgaben bringen. Hiddin loest alle drei Probleme in einer App."},
    48: {"type": "brand",         "thema": "FAQ: Die 10 haeufigsten Fragen zu Hiddin.", "kontext": "Was kostet ein Lead? Wie funktioniert DOI? Wann bekomme ich mein Geld? Wie verbessere ich meinen Score? Was ist eine Secret Experience? Alle Antworten auf hiddin.app"},
    49: {"type": "marketingtipp", "thema": "Marketing Tipp: Content-Ideen fuer Restaurants die nie ausgehen.", "kontext": "Kuechen-Behind-the-Scenes. Zulieferer vorstellen. Saisonales Gericht erklaeren. Stammgast des Monats. Rezept-Tipp. Team vorstellen. Bewertung hervorheben. Angebot der Woche. Event ankuendigen. Geschichte des Restaurants. 10 Ideen fuer 10 Posts. Wiederhole den Zyklus."},
    50: {"type": "influencer",    "thema": "Welche Nischen funktionieren bei Hiddin am besten?", "kontext": "Food und Gastro natuerlich. Aber auch Lifestyle, Familie, Kultur, lokales Reisen. Wer eine engagierte lokale Community hat profitiert. Nicht die Nische sondern die lokale Verbindung zaehlt."},
    51: {"type": "keinmarketing", "thema": "Dein Restaurant verdient mehr als leere Tische an schwachen Tagen.", "kontext": "Schwache Wochentage sind kein Schicksal. Sie sind ein Marketing-Problem. Mit gezielten Influencer-Kampagnen und Newsletter-Aktionen kannst du auch Montag und Dienstag fuellen. Hiddin gibt dir die Werkzeuge dafuer."},
    52: {"type": "marketingtipp", "thema": "Marketing Tipp: Warum Video-Content fuer Restaurants unverzichtbar ist.", "kontext": "Videos bekommen 3x mehr Engagement als Bilder. Reels und TikToks erreichen neue Zielgruppen organisch. Zeige Gerichte beim Anrichten. Atmosphaere am Abend. Koch beim Arbeiten. Authentisch schlaegt Perfekt. Smartphone reicht voellig."},
    53: {"type": "restaurant",    "thema": "Hiddin vs. Flyer — Warum Papier 2025 tot ist.", "kontext": "Flyer teuer, nicht messbar, landet im Muell. Hiddin 3 Euro pro Lead, vollstaendig messbar, DSGVO-konform, direkter Kontakt."},
    54: {"type": "keinmarketing", "thema": "Du hast kein Marketing weil du keine Zeit hast. Wir kennen das.", "kontext": "Gastronomie ist stressig. Marketing bleibt liegen. Aber genau deswegen braucht es ein System das automatisch laeuft. Hiddin laeuft im Hintergrund. Influencer generieren Leads. KI schreibt Newsletter. Du kochst."},
    55: {"type": "marketingtipp", "thema": "Marketing Tipp: So baust du eine treue Stammgast-Community auf.", "kontext": "Erkenne Stammgaeste persoenlich. Biete exklusive Vorteile. Sende regelmaessig Newsletter. Lade zu besonderen Events ein. Frage nach Feedback. Danke oeffentlich. Menschen bleiben dort treu wo sie sich gesehen fuehlen. Das ist guenstigeres Marketing als Neukunden-Akquise."},
    56: {"type": "brand",         "thema": "Das Geheimnis hinter Secret Experiences.", "kontext": "Menschen wollen Teil von etwas Exklusivem sein. FOMO ist real. Ein Secret das man teilen kann ist wertvoller als normale Werbung. Deshalb funktionieren Secret Experiences."},
    57: {"type": "keinmarketing", "thema": "Was wuerde passieren wenn 100 neue Menschen dein Restaurant entdecken?", "kontext": "Mit Hiddin ist das keine Fantasie. Eine Secret Experience. Ein Influencer mit 10.000 lokalen Followern. QR-Code geteilt. 100 neue Leads in 2 Wochen. 100 neue potenzielle Stammgaeste. Fuer 300 Euro."},
    58: {"type": "marketingtipp", "thema": "Marketing Tipp: DSGVO fuer Restaurants einfach erklaert.", "kontext": "Du darfst keine E-Mails ohne Einwilligung senden. Deswegen ist DOI so wichtig. Double Opt-In bestaetigt die Einwilligung. Alle Hiddin-Leads sind DOI-bestaetigt und damit DSGVO-konform. Kein Anwalts-Stress."},
    59: {"type": "influencer",    "thema": "Lokaler Food-Influencer werden — So startest du.", "kontext": "Authentisch ueber lokale Restaurants berichten. Echte Erlebnisse teilen. Community aufbauen. Mit Hiddin sofort Geld verdienen ohne Mindest-Followerzahl."},
    60: {"type": "brand",         "thema": "2 Monate Hiddin. Danke an alle die dabei sind.", "kontext": "Restaurants und Influencer vernetzen sich. Leads werden generiert. Fair bezahlt. Das ist erst der Anfang."},
    # PHASE 3 — WACHSTUM (Tag 61-90)
    61: {"type": "restaurant",    "thema": "So hat ein Restaurant in 30 Tagen 150 neue Leads generiert.", "kontext": "Secret Experience erstellt. Influencer eingeladen. QR-Code geteilt. Newsletter versendet. 150 bestaedigte Leads. 150 neue Kontakte."},
    62: {"type": "marketingtipp", "thema": "Marketing Tipp: Der Unterschied zwischen Reichweite und Wirkung.", "kontext": "1 Million Impressionen bei fremden Menschen bringen weniger als 1.000 Kontakte mit echtem Interesse. Zielgruppen-Praezision schlaegt Masse. Lokale Influencer haben praezise Zielgruppen. Hiddin's DOI-System filtert nur echte Interessenten."},
    63: {"type": "keinmarketing", "thema": "Du hast noch nie mit einem Influencer zusammengearbeitet. Kein Problem.", "kontext": "Hiddin uebernimmt das Matching. Du schreibst die Secret Experience. Hiddin zeigt dir passende lokale Influencer. Du laedt ein. Der Rest laeuft automatisch. Kein Agenturen-Stress. Kein unklares Briefing."},
    64: {"type": "superinfluencer","thema": "Super Influencer: Passives Einkommen aufbauen.", "kontext": "Recruiting-Link teilen. Influencer registrieren sich. Sie generieren Leads. Du verdienst 0,50 Euro pro Lead mit. Je mehr aktive Influencer desto mehr passives Einkommen."},
    65: {"type": "marketingtipp", "thema": "Marketing Tipp: Saisonales Marketing — Der Jahresplan fuer Restaurants.", "kontext": "Januar: Neujahrsvorsaetze-Kampagne. Februar: Valentinstag-Special. Maerz: Fruehlings-Erwaachen. April: Oster-Menue. Mai: Muttertag. Juni: Sommer-Start. Juli-August: Terrassen-Season. September: Herbst-Menue. Oktober: Oktoberfest-Stil. November: Pre-Christmas. Dezember: Weihnachts-Atmosphaere. Jeder Monat ein Anlass."},
    66: {"type": "influencer",    "thema": "Wie du mehr Restaurant-Einladungen bekommst.", "kontext": "Hiddin Score erhoehen. Profil vollstaendig. Kanal verifizieren. Regelmaessig aktiv. Erste Kooperationen gut abschliessen. Restaurants sehen Score und laden bevorzugt ein."},
    67: {"type": "keinmarketing", "thema": "Dein Restaurant ist besser als sein Marketing. Aendere das.", "kontext": "Viele grossartige Restaurants scheitern weil niemand von ihnen weiss. Nicht weil das Essen schlecht ist. Hiddin gibt deinem Restaurant die Sichtbarkeit die es verdient. Durch echte lokale Empfehlungen."},
    68: {"type": "marketingtipp", "thema": "Marketing Tipp: Kundenbindung 2025 — Die 3 wichtigsten Kanaele.", "kontext": "1. E-Mail-Newsletter direkter Kontakt ohne Algorithmus. 2. Influencer-Marketing organische Reichweite. 3. Google Business lokale Sichtbarkeit. Hiddin verbindet alle drei Kanaele in einer App."},
    69: {"type": "restaurant",    "thema": "Warum dein QR-Code mehr wert ist als du denkst.", "kontext": "Ein QR-Code ist die Tuer zu einer direkten Kundenbeziehung. Jeder Scan ist ein potenzieller Lead. Mit Hiddin ist jeder Lead messbar und DSGVO-konform."},
    70: {"type": "marketingtipp", "thema": "Marketing Tipp: Wie du negative Bewertungen richtig handhabst.", "kontext": "Sofort antworten. Ruhig bleiben. Entschuldigen ohne Schuld einzugestehen. Loesung anbieten. Offline weiterfuehren. Niemals streiten. Eine professionelle Antwort auf eine negative Bewertung ist oeffentlich sichtbar und zeigt anderen Gaesten deinen Umgang. Hiddin's Bewertungsmanager unterstuetzt dich dabei."},
    71: {"type": "keinmarketing", "thema": "Das guenstigste Marketing ist das das du nicht machst. Und dann bankrott gehst.", "kontext": "Kein Marketing zu betreiben ist nicht kostenguenstig. Es kostet dich Gaeste die du nie kennenlernst. Umsatz der nie entsteht. Stammgaeste die du nie aufbaust. Hiddin ist der guenstigste Einstieg: 3 Euro pro Lead. Kein Lead kein Cent."},
    72: {"type": "brand",         "thema": "Die Psychologie hinter Secret Experiences.", "kontext": "FOMO Fear of Missing Out ist der staerkste Marketing-Trigger. Ein Erlebnis das man nicht kaufen sondern nur durch den richtigen Kontakt bekommen kann ist unbezahlbar wertvoll. Das ist Hiddin."},
    73: {"type": "marketingtipp", "thema": "Marketing Tipp: Storytelling fuer Restaurants — So erzaehlst du deine Geschichte.", "kontext": "Warum hast du dieses Restaurant eroeffnet? Was ist deine Leidenschaft? Welche Geschichte steckt hinter deinem Lieblsgericht? Menschen kaufen keine Gerichte. Sie kaufen Geschichten. Teile deine. Authentisch. Unregelmaessig. Ohne Filter."},
    74: {"type": "influencer",    "thema": "Engagement-Rate verbessern: Was wirklich funktioniert.", "kontext": "Echte Fragen stellen. Auf Kommentare antworten. Lokale Themen ansprechen. Hinter-den-Kulissen zeigen. Weniger Werbung mehr Inhalt. Hiddin Score steigt automatisch."},
    75: {"type": "keinmarketing", "thema": "Frag dich: Wie viele neue Gaeste hast du diesen Monat gewonnen?", "kontext": "Wenn du die Antwort nicht weisst hast du kein Mess-System. Wenn du die Antwort weisst aber unzufrieden bist hast du kein Marketing-System. Hiddin gibt dir beides. Leads zaehlen. Kontakte sammeln. Ergebnisse messen."},
    76: {"type": "marketingtipp", "thema": "Marketing Tipp: So nutzt du User Generated Content fuer dein Restaurant.", "kontext": "Gaeste die Fotos machen und posten sind deine beste Werbung. Ermutige sie aktiv. QR-Code am Tisch mit Bitte um Tag. Hashtag erstellen und bewerben. Beste Posts reposten und danken. Wettbewerb ausschreiben. UGC ist kostenlos und glaubwuerdig."},
    77: {"type": "influencer",    "thema": "Was macht einen guten lokalen Food-Influencer aus?", "kontext": "Authentizitaet. Lokale Verbundenheit. Echtes Interesse an Gastronomie. Regelmaessige Aktivitaet. Engagement mit der Community. Nicht Follower-Anzahl sondern Verbindungsqualitaet."},
    78: {"type": "keinmarketing", "thema": "Marketing-Budget fuer Restaurants: So viel musst du ausgeben.", "kontext": "Empfehlung: 3-5% des Umsatzes. Bei 50.000 Euro Monatsumsatz sind das 1.500-2.500 Euro. Mit Hiddin kannst du dieses Budget optimal einsetzen: Jeder Euro messbar. Nur bei Erfolg bezahlen. Kein Streuverlust."},
    79: {"type": "brand",         "thema": "Hiddin in Zahlen: 75 Tage Wachstum.", "kontext": "Restaurants auf der Plattform. Influencer registriert. Leads generiert. Newsletter versendet. Hiddin waechst. Jeden Tag."},
    80: {"type": "marketingtipp", "thema": "Marketing Tipp: Die 5 guenstigsten Marketing-Massnahmen fuer Restaurants.", "kontext": "1. Google Business vollstaendig ausfuellen (kostenlos). 2. Instagram regelmaessig bespielen (kostenlos). 3. Stammgaeste um Bewertungen bitten (kostenlos). 4. QR-Code am Tisch fuer Newsletter-Anmeldung (guenstig). 5. Lokalen Influencer einladen (mit Hiddin ab 3 Euro pro Lead)."},
    81: {"type": "brand",         "thema": "Danke-Post: Community Shoutout.", "kontext": "Danke an alle Restaurants. Danke an alle Influencer. Danke an alle Super Influencer. Ihr seid Hiddin."},
    82: {"type": "keinmarketing", "thema": "Herbst kommt. Hast du einen Plan fuer die naechsten 3 Monate?", "kontext": "Die starke Gastro-Saison beginnt im Herbst. Wer jetzt Influencer einlaedt und Newsletter-Listen aufbaut ist vorbereitet. Wer wartet verliert Buchungen an Restaurants die bereits aktiv sind. Hiddin hilft dir jetzt zu starten."},
    83: {"type": "marketingtipp", "thema": "Marketing Tipp: Email-Automation fuer Restaurants einfach erklaert.", "kontext": "Willkommens-Mail sofort nach Anmeldung. Geburtstags-Mail mit Spezialangebot. Inaktivitaets-Mail nach 60 Tagen. Veranstaltungs-Einladung 2 Wochen vorher. Bewertungs-Anfrage 3 Tage nach Besuch. Diese 5 automatischen E-Mails laufen einmal eingerichtet fuer immer. Hiddin unterstuetzt Automation."},
    84: {"type": "restaurant",    "thema": "ROI-Rechner: Was bringt Hiddin wirklich?", "kontext": "100 Leads mal 3 Euro gleich 300 Euro Kosten. 100 neue E-Mail-Kontakte. Durchschnittlicher Gastro-Gaestewert 200 Euro pro Jahr. 100 Gaeste gleich 20.000 Euro Jahresumsatz. ROI 6.567%."},
    85: {"type": "keinmarketing", "thema": "Du brauchst kein Marketing-Studium um dein Restaurant zu vermarkten.", "kontext": "Du brauchst ein System. Hiddin ist so einfach gebaut dass jeder Gastronom es sofort versteht. KI schreibt Newsletter. Influencer generieren Leads. Statistiken zeigen Ergebnisse. Du konzentrierst dich aufs Wesentliche: dein Restaurant."},
    86: {"type": "marketingtipp", "thema": "Marketing Tipp: Die 10 haeufigsten Marketing-Fehler von Restaurants.", "kontext": "Kein Newsletter. Keine Influencer. Keine Messbarkeit. Kein Google Business. Keine Reaktion auf Bewertungen. Kein Budget-Plan. Kein CRM. Kein Stammgaeste-System. Kein Content-Plan. Kein Strategie-Dokument. Hiddin loest 8 von 10 direkt."},
    87: {"type": "influencer",    "thema": "Food-Influencer in Deutschland: Wie gross ist die Community?", "kontext": "Tausende lokale Food-Creator in Deutschland. Die meisten unterbezahlt oder ohne klares Einkommensmodell. Hiddin gibt ihnen eine Plattform. Fair. Messbar. Regelmaessig."},
    88: {"type": "marketingtipp", "thema": "Marketing Tipp: So misst du den Erfolg deines Restaurant-Marketings.", "kontext": "Newsletter Oeffnungsrate (Ziel 25%+). Klickrate (Ziel 3%+). Lead-Kosten (Ziel unter 5 Euro). Neue Gaeste pro Monat. Stammgaeste-Anteil. Bewertungs-Durchschnitt. Ohne Messung keine Optimierung. Hiddin zeigt dir alle Zahlen in Echtzeit."},
    89: {"type": "keinmarketing", "thema": "Es ist nie zu spaet anzufangen. Aber jetzt ist der beste Moment.", "kontext": "Jeder Tag ohne Marketing-System ist ein verpasster Tag. Leads die du nicht sammelst existieren nicht. Kontakte die du nicht pflegst gehen verloren. Fang heute an. Mit Hiddin. In 10 Minuten bist du dabei."},
    90: {"type": "brand",         "thema": "90 Tage. 90 Posts. 1 Mission: Wo Geheimnisse zu Gaesten werden.", "kontext": "90 Tage Hiddin. Restaurants und Influencer vernetzt. Leads generiert. Fair bezahlt. Marketing-Tipps geteilt. Das war erst der Anfang. Hiddin waechst weiter."},
}

def get_todays_post():
    today = date.today()
    delta = (today - START_DATE).days + 1
    if delta < 1: delta = 1
    if delta > 90: delta = ((delta - 1) % 90) + 1
    return delta, CONTENT_PLAN.get(delta, CONTENT_PLAN[1])

# Screenshot-Zuordnung pro Content-Typ
SCREENSHOT_MAP = {
    "restaurant":      ["restaurant-dashboard.jpg", "secret-experience.jpg", "finanzen.jpg", "statistiken.jpg"],
    "influencer":      ["influencer-dashboard.jpg", "KI-funktionen.jpg", "statistiken.jpg"],
    "superinfluencer": ["influencer-dashboard.jpg", "finanzen.jpg"],
    "brand":           ["welcome.jpg", "restaurant-dashboard.jpg", "KI-funktionen.jpg"],
    "keinmarketing":   ["welcome.jpg", "restaurant-dashboard.jpg", "marketing-tipps.jpg"],
    "marketingtipp":   ["marketing-tipps.jpg", "email-builder.jpg", "statistiken.jpg", "bewertungen.jpg"],
}

THEMA_SCREENSHOT_MAP = {
    "Email Builder":        ["email-builder.jpg", "email-builder-editor.jpg", "email-builder-inhalte.jpg", "email-builder-sektionen.jpg", "email-builder-vorschau.jpg"],
    "Newsletter":           ["email-builder.jpg", "email-builder-vorschau.jpg"],
    "Bewertung":            ["bewertungen.jpg"],
    "Google":               ["bewertungen.jpg"],
    "Meta Ads":             ["meta-ads.jpg"],
    "Secret Experience":    ["secret-experience.jpg"],
    "QR":                   ["secret-experience.jpg", "restaurant-dashboard.jpg"],
    "Credits":              ["finanzen.jpg"],
    "Depot":                ["finanzen.jpg"],
    "Statistik":            ["statistiken.jpg"],
    "ROI":                  ["statistiken.jpg", "finanzen.jpg"],
    "Auszahlung":           ["finanzen.jpg"],
    "Support":              ["support.jpg"],
    "KI":                   ["KI-funktionen.jpg", "email-builder.jpg"],
    "Score":                ["influencer-dashboard.jpg"],
    "Influencer":           ["influencer-dashboard.jpg"],
    "Super Influencer":     ["influencer-dashboard.jpg", "finanzen.jpg"],
    "Passiv":               ["influencer-dashboard.jpg"],
    "Marketing Tipp":       ["marketing-tipps.jpg"],
}

# All available screenshots (for fallback)
ALL_SCREENSHOTS = [
    "KI-funktionen.jpg", "bewertungen.jpg", "email-builder-editor.jpg",
    "email-builder-inhalte.jpg", "email-builder-sektionen.jpg", "email-builder-vorschau.jpg",
    "email-builder.jpg", "finanzen.jpg", "influencer-dashboard.jpg", "marketing-tipps.jpg",
    "meta-ads.jpg", "restaurant-dashboard.jpg", "secret-experience.jpg",
    "statistiken.jpg", "support.jpg", "welcome.jpg"
]

def download_screenshot(filename):
    """Screenshot von GitHub Raw URL herunterladen"""
    url = SCREENSHOT_BASE_URL + filename
    r = requests.get(url, timeout=15)
    if r.status_code == 200:
        return r.content
    return None

def get_screenshot_for_post(post):
    """Gibt Dateiname des passenden Screenshots zurück"""
    thema = post.get("thema", "")
    for keyword, screens in THEMA_SCREENSHOT_MAP.items():
        if keyword.lower() in thema.lower():
            for screen in screens:
                if screen in ALL_SCREENSHOTS:
                    return screen
    typ = post.get("type", "brand")
    screens = list(SCREENSHOT_MAP.get(typ, ["restaurant-dashboard.jpg"]))
    random.shuffle(screens)
    for screen in screens:
        if screen in ALL_SCREENSHOTS:
            return screen
    return random.choice(ALL_SCREENSHOTS)

def screenshot_to_base64(filename):
    content = download_screenshot(filename)
    if not content:
        raise Exception("Screenshot nicht gefunden: " + filename)
    return base64.b64encode(content).decode("utf-8")

def get_kling_token():
    now = int(time.time())
    payload = {"iss": KLING_ACCESS, "exp": now + 1800, "nbf": now - 5}
    return jwt.encode(payload, KLING_SECRET, algorithm="HS256")

def generate_mockup_image(screenshot_filename, size="1024x1024"):
    """GPT-4o erstellt Handy-Mockup Bild"""
    screenshot_bytes = download_screenshot(screenshot_filename)
    if not screenshot_bytes:
        raise Exception("Screenshot nicht gefunden: " + screenshot_filename)
    r = requests.post(
        "https://api.openai.com/v1/images/edits",
        headers={"Authorization": "Bearer " + OPENAI_KEY},
        files={"image": ("screenshot.jpg", screenshot_bytes, "image/jpeg")},
        data={
            "model": "gpt-image-1",
            "prompt": "Create a professional smartphone mockup showing this exact app screen. Place the screen into a realistic black iPhone at a slight 3/4 angle. Background: dark atmospheric upscale restaurant with warm gold bokeh lighting. Cinematic professional photography. No extra text or watermarks.",
            "size": size,
            "quality": "high",
            "n": "1"
        }
    )
    data = r.json()
    if "error" in data:
        raise Exception("GPT-Image Fehler: " + data["error"]["message"])
    return base64.b64decode(data["data"][0]["b64_json"])

def generate_video_reel(image_bytes, tag_nr=1):
    """Kling Image-to-Video: Individuelles Konzept pro Tag"""
    from hiddin_reel_konzepte import get_kling_prompt
    konzept = get_kling_prompt(tag_nr)
    img_b64 = base64.b64encode(image_bytes).decode("utf-8")
    token = get_kling_token()
    print("   Konzept: " + konzept["konzept"])
    print("   Stimmung: " + konzept["stimmung"])
    r = requests.post(
        "https://api.klingai.com/v1/videos/image2video",
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"},
        json={
            "model_name": "kling-v1-6",
            "image": img_b64,
            "prompt": konzept["prompt"],
            "negative_prompt": konzept["negative_prompt"],
            "cfg_scale": 0.5,
            "mode": "pro",
            "duration": "5",
            "aspect_ratio": "9:16"
        }
    )
    data = r.json()
    if data.get("code") != 0:
        raise Exception("Kling Fehler: " + str(data.get("message", data)))
    task_id = data["data"]["task_id"]
    print("Kling Task ID: " + task_id + " — warte auf Video...")
    for i in range(36):
        time.sleep(5)
        status_r = requests.get(
            "https://api.klingai.com/v1/videos/image2video/" + task_id,
            headers={"Authorization": "Bearer " + token}
        )
        status = status_r.json()
        task_status = status["data"]["task_status"]
        print("Status: " + task_status + " (" + str((i+1)*5) + "s)")
        if task_status == "succeed":
            video_url = status["data"]["task_result"]["videos"][0]["url"]
            video_r = requests.get(video_url)
            return video_r.content
        elif task_status == "failed":
            raise Exception("Kling Video fehlgeschlagen")
    raise Exception("Kling Timeout nach 3 Minuten")

def generate_caption(screenshot_filename, post):
    screenshot_b64 = screenshot_to_base64(screenshot_filename)
    zielgruppe = {
        "restaurant": "Restaurantbesitzer",
        "influencer": "Lokale Food-Influencer",
        "superinfluencer": "Influencer mit grossem Netzwerk",
        "brand": "Restaurants und Influencer",
        "keinmarketing": "Restaurantbesitzer die noch kein digitales Marketing machen",
        "marketingtipp": "Restaurantbesitzer und Gastronomen"
    }.get(post["type"], "Alle")
    prompt = (
        "Du bist Social Media Manager fuer Hiddin — B2B SaaS App die Restaurants mit lokalen Influencern ueber Secret Experiences verbindet.\n\n"
        "BRAND VOICE: selbstbewusst, direkt, geheimnisvoll, premium. Kurze kraftvolle Saetze.\n"
        "SLOGAN: Wo Geheimnisse zu Gaesten werden\n\n"
        "HEUTIGES THEMA: " + post["thema"] + "\n"
        "KONTEXT: " + post["kontext"] + "\n"
        "ZIELGRUPPE: " + zielgruppe + "\n\n"
        "Schau dir den App-Screenshot an und baue ihn natuerlich ein.\n\n"
        "STRUKTUR:\n"
        "1. Hook — 1 starke Zeile\n\n"
        "2. Problem oder Fakt mit Zahlen — 2-3 Zeilen\n\n"
        "3. Loesung oder Tipp — konkret — 2-3 Zeilen\n\n"
        "4. CTA — hiddin.app\n\n"
        "3-5 Emojis. Nur Caption, keine Hashtags."
    )
    r = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": 600,
            "messages": [{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": screenshot_b64}},
                {"type": "text", "text": prompt}
            ]}]
        }
    )
    return r.json()["content"][0]["text"].strip() + "\n\n" + HASHTAGS[post["type"]]

def generate_comment(post):
    prompt = (
        "Schreibe einen ersten Kommentar unter einen Hiddin Post zum Thema: " + post["thema"] + "\n"
        "Stelle eine direkte Frage an die Community die zum Antworten einlaedt.\n"
        "Authentisch, nicht wie Marketing. 2-3 Zeilen, 1-2 Emojis. Nur den Text."
    )
    r = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
        json={"model": "claude-sonnet-4-6", "max_tokens": 150, "messages": [{"role": "user", "content": prompt}]}
    )
    return r.json()["content"][0]["text"].strip()

def add_logo_overlay(image_bytes):
    try:
        img = Image.open(BytesIO(image_bytes)).convert("RGBA")
        w, h = img.size
        logo_r = requests.get(LOGO_URL, timeout=10)
        if logo_r.status_code != 200:
            raise Exception("Logo nicht geladen: " + str(logo_r.status_code))
        logo = Image.open(BytesIO(logo_r.content)).convert("RGBA")
        logo_w = int(w * 0.12)
        logo_h = int(logo.height * (logo_w / logo.width))
        logo_resized = logo.resize((logo_w, logo_h), Image.LANCZOS)
        pad = int(w * 0.04)
        img.paste(logo_resized, (pad, pad), logo_resized)
        final = img.convert("RGB")
        buf = BytesIO()
        final.save(buf, format="JPEG", quality=95)
        buf.seek(0)
        return buf
    except Exception as e:
        print("Logo-Fehler: " + str(e))
        return BytesIO(image_bytes)

def upload_image(image_bytes):
    img_with_logo = add_logo_overlay(image_bytes)
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp.write(img_with_logo.read())
        tmp_path = tmp.name
    with open(tmp_path, "rb") as f:
        r = requests.post(
            "https://postsyncer.com/api/v1/media/upload/file",
            headers={"Authorization": "Bearer " + POSTSYNCER_KEY},
            files={"file": ("hiddin_post.jpg", f, "image/jpeg")},
            data={"workspace_id": str(WORKSPACE_ID)}
        )
    os.unlink(tmp_path)
    return r.json()["media"]["id"]

def upload_video(video_bytes):
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp:
        tmp.write(video_bytes)
        tmp_path = tmp.name
    with open(tmp_path, "rb") as f:
        r = requests.post(
            "https://postsyncer.com/api/v1/media/upload/file",
            headers={"Authorization": "Bearer " + POSTSYNCER_KEY},
            files={"file": ("hiddin_reel.mp4", f, "video/mp4")},
            data={"workspace_id": str(WORKSPACE_ID)}
        )
    os.unlink(tmp_path)
    return r.json()["media"]["id"]

def create_draft(caption, media_id, accounts):
    r = requests.post(
        "https://postsyncer.com/api/v1/posts",
        headers={"Authorization": "Bearer " + POSTSYNCER_KEY, "Content-Type": "application/json"},
        json={
            "workspace_id": WORKSPACE_ID,
            "content": [{"text": caption, "media": [media_id]}],
            "schedule_type": "draft",
            "accounts": accounts
        }
    )
    return r.json()

# ============================================
# RUN
# ============================================
print("=" * 55)
print("HIDDIN MARKETING PIPELINE v11")
print("Kling Reels | 90-Tage Plan | 3 Kategorien")
print("=" * 55)

import sys
if len(sys.argv) > 1:
    override_tag = int(sys.argv[1])
    post_data = CONTENT_PLAN.get(override_tag, CONTENT_PLAN[1])
    tag_nr, post = override_tag, post_data
else:
    tag_nr, post = get_todays_post()
print("\nTag " + str(tag_nr) + " von 90")
print("Typ: " + post["type"].upper())
print("Thema: " + post["thema"])

screenshot_filename = get_screenshot_for_post(post)
print("Screenshot: " + screenshot_filename)

print("\nSchritt 1: Caption generieren...")
caption = generate_caption(screenshot_filename, post)
print("Caption fertig")

print("\nSchritt 2: Engagement-Kommentar generieren...")
comment = generate_comment(post)
print("Kommentar fertig")

ist_reel_tag = (tag_nr % 2 == 0)

if ist_reel_tag:
    print("\nREEL TAG (gerade) — Instagram Reels + TikTok (gleiches Video)")

    print("\nSchritt 3: 9:16 Mockup generieren...")
    image_vertical = generate_mockup_image(screenshot_filename, "1024x1536")
    print("9:16 Bild fertig")

    print("\nSchritt 4: Kling generiert Video-Reel...")
    try:
        video_bytes = generate_video_reel(image_vertical, tag_nr)
        print("Video fertig (" + str(len(video_bytes)//1024) + " KB)")
        use_video = True
    except Exception as e:
        print("Kling Fehler: " + str(e) + " — nutze 9:16 Bild als Fallback")
        use_video = False

    print("\nSchritt 5: Video hochladen...")
    if use_video:
        media_id_reel = upload_video(video_bytes)
    else:
        media_id_reel = upload_image(image_vertical)
    print("Hochgeladen ID: " + str(media_id_reel))

    print("\nSchritt 6: 1 Draft fuer Instagram Reels + TikTok...")
    post1 = create_draft(caption, media_id_reel, ACCOUNTS_REELS)
    print("Draft Reels/TikTok: " + str(post1.get("id")))

    print("\n" + "=" * 55)
    print("FERTIG! Tag " + str(tag_nr) + " — REEL TAG")
    print("1 Video → Instagram Reels + TikTok")
    print("=" * 55)

else:
    print("\nBILD TAG (ungerade) — Instagram Feed + Facebook")

    print("\nSchritt 3: 1:1 Mockup generieren...")
    image_square = generate_mockup_image(screenshot_filename, "1024x1024")
    print("1:1 Bild fertig")

    print("\nSchritt 4: Bild hochladen + Logo...")
    media_id_square = upload_image(image_square)
    print("Hochgeladen ID: " + str(media_id_square))

    print("\nSchritt 5: 1 Draft fuer Instagram Feed + Facebook...")
    post1 = create_draft(caption, media_id_square, ACCOUNTS_SQUARE)
    print("Draft Feed/Facebook: " + str(post1.get("id")))

    print("\n" + "=" * 55)
    print("FERTIG! Tag " + str(tag_nr) + " — BILD TAG")
    print("1 Bild → Instagram Feed + Facebook")
    print("=" * 55)
