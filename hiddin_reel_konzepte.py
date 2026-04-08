# ============================================
# HIDDIN — 90 REEL KONZEPTE FÜR KLING
# Image-to-Video | Optimierte Prompts
# ============================================
#
# REGELN (aus Recherche):
# - Nur Bewegung beschreiben, NIE das Bild
# - 1 Kamera + max 2 Bewegungen
# - 20-40 Wörter
# - Immer Negative Prompt
# - Immer Endpunkt ("settles", "holds")
# - Style-Bibel am Ende jedes Prompts

NEGATIVE_PROMPT = "shaky camera, distortion, morphing screen, blurry text, flickering, extra objects, floating elements, low quality, cartoonish, 3D render"

STYLE_BIBLE = "cinematic lighting, shallow depth of field, warm gold color grade, high production value, 9:16 vertical format"

# 90 individuelle Kling Image-to-Video Prompts
# Jeder Prompt ist auf das jeweilige Thema und den Screenshot abgestimmt

REEL_KONZEPTE = {

    # PHASE 1 — PRE-LAUNCH (Tag 1-30)
    # Fokus: Geheimnisvoll, Teaser, Neugier wecken

    1: {
        "konzept": "Handy auf Restauranttisch, Bokeh-Lichter",
        "kamera": "Slow dolly-in auf den Phone-Screen",
        "bewegung": "Bokeh-Lichter im Hintergrund pulsieren sanft",
        "stimmung": "Geheimnisvoll, Premium",
        "prompt": "Camera slowly dollies in toward the phone screen. Background restaurant bokeh lights pulse gently and settle. Warm gold light intensifies on the screen surface.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    2: {
        "konzept": "Restaurant-Atmosphäre, leere Tische, Kamera fährt durch",
        "kamera": "Langsamer Tracking-Shot von links nach rechts",
        "bewegung": "Tischkerzen flackern, Licht ändert sich von leer zu einladend",
        "stimmung": "Problem zeigen → Lösung andeuten",
        "prompt": "Camera tracks slowly left to right. Candle flames flicker gently on tables. Warm amber light gradually intensifies. Camera settles on phone showing the app.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    3: {
        "konzept": "Smartphone schwebt leicht, dreht sich minimal",
        "kamera": "Static shot, Phone bewegt sich",
        "bewegung": "Phone dreht sich minimal (5 Grad) hin und her, schwebt",
        "stimmung": "Elegant, Premium Produkt",
        "prompt": "Phone gently rotates 5 degrees left then right and settles. Subtle floating motion, barely perceptible. Screen glow intensifies softly. Camera stays static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    4: {
        "konzept": "Teaser — nur das Auge-Logo sichtbar, dann Aufdeckung",
        "kamera": "Langsamer Tilt von unten nach oben",
        "bewegung": "Kamera fährt langsam nach oben, Logo taucht auf",
        "stimmung": "Mysteriös, Reveal-Moment",
        "prompt": "Camera slowly tilts upward revealing the screen. Gold light sweeps across the phone surface from bottom to top and holds. Dramatic and slow.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    5: {
        "konzept": "Hand greift nach Phone, Screen leuchtet auf",
        "kamera": "Close-up Static, Hand-Bewegung",
        "bewegung": "Finger tippt auf Screen, Screen-Glow verstärkt sich",
        "stimmung": "Aktiv, Call-to-Action",
        "prompt": "A hand reaches toward the phone, fingertip approaches screen. Screen glow brightens at touch point and slowly fades back. Camera holds static close-up.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    6: {
        "konzept": "Leerer Restauranttisch → Phone mit App erscheint",
        "kamera": "Slow dolly-back (Kamera fährt weg)",
        "bewegung": "Bokeh-Lichter werden schärfer, Phone bleibt fokussiert",
        "stimmung": "Transformation, Problemlösung",
        "prompt": "Camera slowly pulls back. Bokeh lights in background sharpen gradually. Phone remains in sharp focus. Depth of field shifts dramatically and settles.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    7: {
        "konzept": "Wochenrückblick — Phone dreht sich zur Kamera",
        "kamera": "Orbit um Phone (langsam von der Seite zur Front)",
        "bewegung": "Phone dreht sich zur Kamera, Screen wird sichtbar",
        "stimmung": "Enthüllung, Conclusion",
        "prompt": "Camera slowly orbits from side view to front view around the phone. Screen gradually becomes visible during rotation. Settles facing the viewer directly.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    8: {
        "konzept": "App-Erklärung — Screen-Content im Fokus",
        "kamera": "Extreme close-up, langsamer Zoom-out",
        "bewegung": "Kamera zoomt von Screen-Detail auf ganzes Phone",
        "stimmung": "Erklärend, Klar",
        "prompt": "Camera starts in extreme close-up on screen details, slowly zooms out to reveal full phone in hand. Smooth and steady movement, settles on full phone view.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    9: {
        "konzept": "Secret Experience — Geheimnis-Atmosphäre",
        "kamera": "Slow pan von links, goldenes Licht",
        "bewegung": "Goldener Lichtstrahl wandert über den Screen",
        "stimmung": "Exklusiv, Geheimnisvoll",
        "prompt": "Camera pans slowly from left to center. A warm golden light ray sweeps across the phone screen from left to right and fades. Atmospheric and cinematic.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    10: {
        "konzept": "Schritt-für-Schritt — Finger scrollt durch App",
        "kamera": "Static over-the-shoulder shot",
        "bewegung": "Daumen bewegt sich sanft auf Screen (scroll gesture)",
        "stimmung": "Tutorial, Einfach",
        "prompt": "A thumb gently swipes upward on the screen in a natural scrolling motion, twice, then rests. Camera stays static over-the-shoulder. Realistic hand physics.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    11: {
        "konzept": "Leere Tische Problem — Kamera fährt durch leeres Restaurant",
        "kamera": "FPV Tracking durch Restaurant",
        "bewegung": "Kamera bewegt sich langsam zwischen leeren Tischen durch",
        "stimmung": "Problem, Leer, Traurig",
        "prompt": "Camera drifts slowly forward between empty restaurant tables. Warm but dim lighting. Chairs slightly move as camera passes. Settles looking toward the entrance.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    12: {
        "konzept": "Score-Anzeige — Nummer zählt hoch",
        "kamera": "Static, Screen im Fokus",
        "bewegung": "Score-Zahl auf dem Screen zählt visuell hoch (0→80)",
        "stimmung": "Erfolg, Wachstum",
        "prompt": "Score numbers on the phone screen count upward rapidly. Gold light pulses with each number change. Camera holds perfectly static. Screen glow intensifies at peak.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    13: {
        "konzept": "QR-Code erscheint auf Screen",
        "kamera": "Macro close-up auf QR-Code",
        "bewegung": "QR-Code erscheint, leuchtet kurz auf",
        "stimmung": "Tech, Modern, Präzise",
        "prompt": "Camera holds close-up on QR code on screen. Gold scanning line sweeps across QR code once slowly and fades. Subtle screen glow. Camera perfectly static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    14: {
        "konzept": "Community-Frage — Phone liegt auf Tisch, Hand tippt",
        "kamera": "Overhead (von oben) Static Shot",
        "bewegung": "Hand legt Phone auf Tisch, Screen leuchtet auf",
        "stimmung": "Einladend, Menschlich",
        "prompt": "A hand places the phone face-up on a restaurant table from above. Screen lights up gently. Steam from nearby coffee cup drifts past. Camera holds overhead static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    15: {
        "konzept": "Marketing Tipp — Text auf Screen, Licht dramatisch",
        "kamera": "Slow dolly-in, dramatisch",
        "bewegung": "Licht wird dramatischer, Schatten wachsen",
        "stimmung": "Gewichtig, Wichtige Information",
        "prompt": "Camera slowly dollies in toward the phone. Dramatic lighting shifts from soft to high-contrast. Shadows deepen around the phone edges. Settles in close-up.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    16: {
        "konzept": "Lokaler Influencer — Phone zeigt Influencer-Liste",
        "kamera": "Tilt von oben nach unten",
        "bewegung": "Kamera fährt von oben herunter auf Phone-Screen",
        "stimmung": "Discovery, Entdecken",
        "prompt": "Camera slowly tilts down from above restaurant scene toward phone screen below. Settles in medium shot showing phone clearly. Smooth and intentional movement.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    17: {
        "konzept": "E-Mail sammeln — Notification poppt auf",
        "kamera": "Static, Screen-Notification im Fokus",
        "bewegung": "Notification erscheint auf Screen, vibriert leicht",
        "stimmung": "Erfolg, Neuer Lead",
        "prompt": "A notification appears on the phone screen. Phone vibrates subtly once. Screen brightens briefly then settles to normal. Satisfying micro-interaction feel.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    18: {
        "konzept": "DOI-Erklärung — Häkchen erscheint auf Screen",
        "kamera": "Close-up Static",
        "bewegung": "Grüner Haken erscheint auf Screen, kurze Gold-Explosion",
        "stimmung": "Bestätigung, Sicherheit, DSGVO",
        "prompt": "A checkmark animation appears on phone screen. Brief gold light pulse emanates from screen center and dissipates. Camera holds static close-up. Clean and satisfying.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    19: {
        "konzept": "Auszahlung — Münzen oder Euro-Symbol animiert",
        "kamera": "Static, Phone leicht schräg",
        "bewegung": "Screen zeigt Auszahlungs-Animation, subtil",
        "stimmung": "Verdienst, Fair, Transparent",
        "prompt": "Phone screen shows payment confirmation. Subtle shimmer effect on screen. Gold light sweeps once across phone body diagonally and fades. Camera stays static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    20: {
        "konzept": "Bewertungsmanager — Stern-Animation",
        "kamera": "Slow zoom-in auf Screen-Detail",
        "bewegung": "Kamera zoomt auf einen Stern auf dem Screen",
        "stimmung": "Power, Kontrolle, Sicherheit",
        "prompt": "Camera slowly zooms into star rating on phone screen. As camera approaches, a red star subtly dims to gray. Camera settles in extreme close-up on the stars.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    21: {
        "konzept": "Community-Post — Phone auf Tisch, Café-Atmosphäre",
        "kamera": "Gentle pan von Kaffee zu Phone",
        "bewegung": "Dampf von Kaffee zieht am Phone vorbei",
        "stimmung": "Entspannt, Einladend, Menschlich",
        "prompt": "Camera gently pans from steaming coffee cup to phone beside it. Coffee steam drifts across frame naturally. Settles with phone in focus, coffee softly blurred.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    22: {
        "konzept": "Early Access — Countdown-Uhr auf Screen",
        "kamera": "Static, leichte Handheld-Vibration",
        "bewegung": "Countdown-Timer auf Screen tickt runter",
        "stimmung": "Dringlichkeit, Exklusivität",
        "prompt": "Timer on phone screen counts down. Subtle pulse effect with each second. Camera holds with very slight natural handheld breathing. Tension builds in stillness.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    23: {
        "konzept": "Marketing Tipp QR — QR-Code wird gescannt",
        "kamera": "Over-the-shoulder, Kamera leicht bewegt",
        "bewegung": "Zweites Phone scannt QR-Code, Scan-Linie sichtbar",
        "stimmung": "Praktisch, How-To, Real",
        "prompt": "A second phone enters frame from above scanning the QR code. Scanning beam visible briefly. First phone screen confirms scan with subtle glow. Natural hand movement.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    24: {
        "konzept": "Kostenvergleich — Zahlen auf Screen",
        "kamera": "Static close-up auf Screen",
        "bewegung": "Zahlen auf Screen ändern sich (alt → neu, teuer → günstig)",
        "stimmung": "Überzeugend, Logisch",
        "prompt": "Numbers on phone screen transition from large to small in smooth animation. Screen flashes briefly gold at the final lower number. Camera perfectly static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    25: {
        "konzept": "Super Influencer — Netzwerk-Visualisierung",
        "kamera": "Slow zoom-out von Screen",
        "bewegung": "Screen zeigt wachsendes Netzwerk, Kamera fährt zurück",
        "stimmung": "Wachstum, Netzwerk, Power",
        "prompt": "Camera slowly pulls back from phone screen as network animation appears to expand beyond screen edges. Gold connecting lines pulse outward. Camera settles far back.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    26: {
        "konzept": "Mitbewerber hat Newsletter — zwei Phones",
        "kamera": "Slow pan zwischen zwei Phones",
        "bewegung": "Kamera wandert von dunklem Phone zu leuchtendem Hiddin-Phone",
        "stimmung": "Kontrast, Vergleich, Klar",
        "prompt": "Camera slowly pans from dark inactive phone on left to bright Hiddin phone on right. Warm light shifts to follow the camera movement. Settles on bright phone.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    27: {
        "konzept": "Keine Mindest-Follower — Verschiedene Phones",
        "kamera": "Overhead Pan über mehrere Phones",
        "bewegung": "Kamera fährt über eine Reihe von Phones verschiedener Größe",
        "stimmung": "Inklusiv, Für Alle",
        "prompt": "Camera pans overhead slowly across a row of different phones all showing the Hiddin app. Each screen glows identically. Smooth continuous movement, then holds.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    28: {
        "konzept": "Emotionaler Brand-Post — Restaurantbesitzer schaut auf Phone",
        "kamera": "Über-die-Schulter, Bokeh Restaurant",
        "bewegung": "Person dreht Phone leicht, Screen-Licht beleuchtet Gesicht",
        "stimmung": "Emotional, Menschlich, Hoffnung",
        "prompt": "Person's hands hold phone, screen light illuminates from below. Hands rotate phone slightly revealing screen glow. Background restaurant lights softly pulse. Intimate moment.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    29: {
        "konzept": "Letzte Chance — Timer läuft, Dringlichkeit",
        "kamera": "Rapid dolly-in, dann abrupt stopp",
        "bewegung": "Kamera fährt schnell auf Phone zu, stoppt knapp davor",
        "stimmung": "Dringlichkeit, Jetzt oder Nie",
        "prompt": "Camera quickly dollies toward phone and stops sharply just before reaching screen. Brief camera shake settles instantly. Screen pulses twice with urgency then holds.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    30: {
        "konzept": "30 Tage Milestone — Gold-Konfetti-Effekt",
        "kamera": "Static, Gold-Partikel fallen",
        "bewegung": "Goldene Licht-Partikel fallen langsam vor dem Phone",
        "stimmung": "Feier, Meilenstein, Dankbarkeit",
        "prompt": "Golden light particles drift slowly downward in front of phone. Particles catch light naturally as they fall and dissipate. Screen glows warmly throughout. Celebratory.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    # PHASE 2 — LAUNCH (Tag 31-60)
    # Fokus: App ist live, Features zeigen, Energie

    31: {
        "konzept": "Launch — Phone explodiert in Gold-Licht",
        "kamera": "Static, Gold-Licht-Burst",
        "bewegung": "Gold-Licht bricht aus Phone-Screen aus, weitet sich aus",
        "stimmung": "Launch, Energie, Es geht los",
        "prompt": "Bright gold light bursts from phone screen outward, illuminating surroundings, then gently fades back to normal screen glow. One powerful pulse. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    32: {
        "konzept": "Setup-Anleitung — Finger tippt Schritt für Schritt",
        "kamera": "Overhead Static",
        "bewegung": "Finger tippt nacheinander auf 5 Punkte auf dem Screen",
        "stimmung": "Einfach, Step-by-Step, Vertrauen",
        "prompt": "Finger taps five different points on phone screen sequentially. Brief glow at each tap point. Methodical and clear rhythm. Camera holds overhead static. Confident touches.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    33: {
        "konzept": "Erster Lead — Notification mit 1€",
        "kamera": "Close-up Tilt-down auf Screen",
        "bewegung": "Kamera fährt von oben auf Screen, Notification erscheint",
        "stimmung": "Erster Erfolg, Aufregung",
        "prompt": "Camera tilts down slowly toward phone screen. As it arrives, a notification appears with celebratory animation. Brief gold shimmer on screen. Settles in close-up.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    34: {
        "konzept": "Email Builder KI — Text erscheint auf Screen wie getippt",
        "kamera": "Static close-up",
        "bewegung": "Text erscheint auf Screen als würde er gerade geschrieben",
        "stimmung": "KI, Automatisch, Magie",
        "prompt": "Text appears on phone screen as if being typed by invisible hands. Cursor blinks. Text fills the screen naturally. Gold glow pulses softly. Camera perfectly static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    35: {
        "konzept": "Kein Marketing nötig — Vorher/Nachher Split",
        "kamera": "Static, Screen-Animation",
        "bewegung": "Screen zeigt Transition von leer zu voll (Leads-Counter)",
        "stimmung": "Transformation, Einfach starten",
        "prompt": "Phone screen transitions from empty state to filled with content in smooth animation. Numbers count up. Screen brightens. Camera holds static, witnessing the change.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    36: {
        "konzept": "Meta Ads — Zielkreis erscheint auf Karte",
        "kamera": "Zoom-in auf Screen mit Karten-Ansicht",
        "bewegung": "Kreis auf Karte pulsiert, zeigt Reichweite",
        "stimmung": "Präzise, Lokal, Targeted",
        "prompt": "Camera zooms slowly into map on phone screen. A circle on the map pulses outward twice showing reach area. Settles with map in focus. Geographic and precise feel.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    37: {
        "konzept": "1 Woche Live — Zahlen laufen hoch",
        "kamera": "Static mit Zahlen-Animation",
        "bewegung": "Mehrere Zahlen auf Screen laufen gleichzeitig hoch",
        "stimmung": "Wachstum, Erfolg, Zahlen",
        "prompt": "Multiple numbers on phone screen count upward simultaneously in different positions. Each reaches its target and pulses gold briefly. Energetic but controlled. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    38: {
        "konzept": "Bewertungsmanager — Roter Stern verschwindet",
        "kamera": "Close-up Static, dramatisch",
        "bewegung": "1-Stern Bewertung auf Screen wird durchgestrichen, verschwindet",
        "stimmung": "Kontrolle, Power, Sicherheit",
        "prompt": "A one-star rating on phone screen gets crossed out with a smooth animation and fades away. Brief red-to-green color shift. Screen normalizes. Satisfying and decisive.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    39: {
        "konzept": "Score Verbesserung — Kurve steigt",
        "kamera": "Slow zoom auf Kurven-Chart auf Screen",
        "bewegung": "Kamera zoomt auf aufsteigende Kurve",
        "stimmung": "Progress, Wachstum, Motivation",
        "prompt": "Camera slowly zooms into rising chart line on phone screen. Gold light traces along the rising line. Line reaches peak and holds. Camera settles on peak point.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    40: {
        "konzept": "3 Minuten Newsletter — Uhr dreht sich",
        "kamera": "Static, Zeit-Animation",
        "bewegung": "Uhr auf Screen dreht sich 3 Minuten schnell durch",
        "stimmung": "Schnell, Einfach, Zeitsparend",
        "prompt": "Clock on phone screen spins rapidly three times then stops. Timer reaches zero with brief celebration animation. Screen glows. Fast but controlled spin motion. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    41: {
        "konzept": "Auszahlung kommt — Geld-Transfer Animation",
        "kamera": "Static close-up Screen",
        "bewegung": "Transfer-Animation läuft auf Screen durch",
        "stimmung": "Belohnung, Fair, Transparent",
        "prompt": "Payment transfer animation flows across phone screen. Progress bar fills completely gold. Success indicator appears with subtle pulse. Clean financial transaction feel. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    42: {
        "konzept": "Statistiken — Drei Kreise drehen sich",
        "kamera": "Static, Screen-Animation",
        "bewegung": "Drei Donut-Charts auf Screen füllen sich gleichzeitig",
        "stimmung": "Data, Präzise, Professionell",
        "prompt": "Three circular progress charts on screen fill simultaneously to different percentages. Each completes with a subtle gold pulse. Screen glows with data energy. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    43: {
        "konzept": "Super Influencer Rechner — Zahlen explodieren",
        "kamera": "Static, dramatische Zahlen",
        "bewegung": "Zahlen auf Screen multiplizieren sich sichtbar",
        "stimmung": "Passives Einkommen, Wachstum, Reichtum",
        "prompt": "Numbers on phone screen multiply in visible calculation animation. Final sum appears large and bold with gold highlight. Brief shimmer effect. Impressive and clear. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    44: {
        "konzept": "Mundpropaganda vs Digital — Network-Visualization",
        "kamera": "Zoom-out von einem Punkt auf viele",
        "bewegung": "Netzwerk expandiert von einem Punkt auf viele",
        "stimmung": "Skalierbarkeit, Digital, Modern",
        "prompt": "Network of dots on phone screen expands outward from single central point. Connecting lines appear. Camera slowly pulls back as network grows. Settles with full network visible.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    45: {
        "konzept": "Goldene Posting-Stunde — Sonne geht auf",
        "kamera": "Static, Licht-Veränderung",
        "bewegung": "Licht wird wärmer und heller von links nach rechts",
        "stimmung": "Timing, Strategie, Optimal",
        "prompt": "Warm golden light sweeps slowly from left to right across phone and background. Settles in peak warm glow. Time-of-day feeling. Cinematic light transition. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    46: {
        "konzept": "Erster Feedback — Zitat erscheint auf Screen",
        "kamera": "Slow dolly-in auf Screen",
        "bewegung": "Kamera fährt langsam auf Zitat-Text zu",
        "stimmung": "Vertrauen, Authentisch, Social Proof",
        "prompt": "Camera slowly dollies toward phone screen where testimonial text appears word by word. Warm light on text. Camera settles in close-up on the final quote. Intimate feel.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    47: {
        "konzept": "3 Gründe — Drei Punkte erscheinen nacheinander",
        "kamera": "Static",
        "bewegung": "3 Checkmarks erscheinen nacheinander auf Screen",
        "stimmung": "Klar, Logisch, Überzeugend",
        "prompt": "Three checkmarks appear on phone screen one by one with brief gold pulse each. Third checkmark appears larger with stronger glow. Clean sequential reveal. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    48: {
        "konzept": "FAQ — Frage erscheint, dann Antwort",
        "kamera": "Static close-up Screen",
        "bewegung": "Frage erscheint, kurze Pause, Antwort erscheint darunter",
        "stimmung": "Klar, Hilfreich, Informativ",
        "prompt": "Question text appears on phone screen, pauses briefly, then answer text reveals below with smooth slide-down animation. Screen settles with both visible. Clean and clear.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    49: {
        "konzept": "Content-Ideen — Wörter fliegen auf Screen",
        "kamera": "Static, energetische Screen-Animation",
        "bewegung": "Content-Ideen-Wörter erscheinen nacheinander schnell",
        "stimmung": "Kreativ, Energie, Viele Ideen",
        "prompt": "Words appear rapidly on phone screen in different positions, overlapping slightly, then settle into organized layout. Energetic typing feel. Gold accents flash. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    50: {
        "konzept": "Nischen — Icons erscheinen auf Screen",
        "kamera": "Slow pan von links nach rechts über Screen",
        "bewegung": "Nischen-Icons erscheinen nacheinander von links",
        "stimmung": "Vielfalt, Für Alle, Inklusiv",
        "prompt": "Category icons appear on phone screen from left to right in smooth sequence. Each icon glows briefly as it appears. Final view shows full grid. Camera pans with reveal.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    51: {
        "konzept": "Community-Post — Kommentare erscheinen",
        "kamera": "Static, Screen-Animation",
        "bewegung": "Kommentar-Blasen erscheinen animiert",
        "stimmung": "Community, Dialog, Einladend",
        "prompt": "Comment bubbles appear on phone screen one by one floating upward naturally. Each bubble slightly different size. Organic social media feel. Screen glows warmly. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    52: {
        "konzept": "Flyer vs Hiddin — Papier verbrennt animiert",
        "kamera": "Static dramatic",
        "bewegung": "Linke Screen-Seite (Flyer) verbrennt, rechte (Hiddin) leuchtet",
        "stimmung": "Alt vs Neu, Dramatisch",
        "prompt": "Phone screen shows split: left side dims and fades away, right side brightens dramatically with gold light. Sharp contrast between dying and thriving. Camera holds static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    53: {
        "konzept": "Meta Ads vs Hiddin — CPL Vergleich",
        "kamera": "Static, Zahlen-Vergleich",
        "bewegung": "Zwei Zahlen nebeneinander, eine sinkt dramatisch",
        "stimmung": "Überzeugend, Klar, Günstig",
        "prompt": "Two numbers on phone screen side by side. Left number stays high, right number drops dramatically lower with speed lines. Right number glows gold when settled. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    54: {
        "konzept": "Kein Zeit für Marketing — Uhr läuft schnell",
        "kamera": "Static, Zeit-Stress",
        "bewegung": "Uhr auf Screen läuft sehr schnell, dann stoppt bei Hiddin",
        "stimmung": "Stress → Relief, Lösung",
        "prompt": "Clock on phone screen spins frantically fast then suddenly stops. Screen flashes briefly then settles into calm Hiddin app view. Relief contrast is clear. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    55: {
        "konzept": "Stammgast-Community — Personen-Icons sammeln sich",
        "kamera": "Slow zoom-out während Icons erscheinen",
        "bewegung": "Personen-Icons sammeln sich auf Screen, Kamera fährt zurück",
        "stimmung": "Community, Wachstum, Zusammen",
        "prompt": "Person icons accumulate on phone screen filling from center outward. Camera slowly pulls back as icons multiply. Final view shows full community. Warm gold glow throughout.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    56: {
        "konzept": "FOMO Secret Experience — Tür öffnet sich animiert",
        "kamera": "Static dramatic reveal",
        "bewegung": "Türen-Animation auf Screen öffnet sich, Gold-Licht strömt raus",
        "stimmung": "FOMO, Exklusiv, Begehrenswert",
        "prompt": "Door animation on phone screen slowly opens. Golden light streams through the opening gap. Full open reveals bright interior glow. Dramatic reveal moment. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    57: {
        "konzept": "100 neue Leads — Zähler läuft",
        "kamera": "Static, energetisch",
        "bewegung": "Lead-Counter läuft von 0 auf 100 schnell hoch",
        "stimmung": "Erfolg, Wachstum, Beeindruckend",
        "prompt": "Lead counter on phone screen rapidly counts from zero to 100. Each ten marks a brief gold pulse. Reaches 100 with strong gold flash and holds. Energetic and satisfying.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    58: {
        "konzept": "DSGVO-konform — Häkchen mit Schild",
        "kamera": "Static, vertrauensvoll",
        "bewegung": "Schild-Icon und Häkchen erscheinen, grüne Bestätigung",
        "stimmung": "Sicherheit, Vertrauen, Legal",
        "prompt": "Shield icon appears on phone screen with checkmark inside. Green glow emanates from icon and fades. Stable and trustworthy animation. Clean professional feel. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    59: {
        "konzept": "Food-Influencer werden — Kamera-Bewegung aufwärts",
        "kamera": "Slow tilt up (Kamera fährt aufwärts)",
        "bewegung": "Kamera fährt von unten auf Phone hoch, wie Aufstieg",
        "stimmung": "Aspiration, Aufstieg, Möglich",
        "prompt": "Camera slowly tilts upward from below phone level to eye level with screen. Movement feels like rising. Warm light intensifies as camera reaches screen height. Hopeful motion.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    60: {
        "konzept": "2 Monate Danke — Gold-Regen",
        "kamera": "Static, Gold-Partikel",
        "bewegung": "Goldene Partikel fallen von oben, dichte Gold-Regen",
        "stimmung": "Dankbarkeit, Feier, Milestone",
        "prompt": "Dense golden particles rain down from above in front of phone. Particles cascade naturally and accumulate. Phone screen shines through particle shower. Celebratory and warm.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    # PHASE 3 — WACHSTUM (Tag 61-90)
    # Fokus: Erfolge zeigen, Expertise, Zukunft

    61: {
        "konzept": "150 Leads Case Study — Kurve explodiert",
        "kamera": "Zoom-in auf explodierende Kurve",
        "bewegung": "Kurve auf Screen schießt steil nach oben",
        "stimmung": "Erfolg, Dramatisch, Beweisend",
        "prompt": "Growth chart on phone screen shoots upward dramatically. Line accelerates and flies off chart top. Gold trail follows the line. Camera zooms in as chart peaks. Explosive growth.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    62: {
        "konzept": "Marketing Tipp Reichweite vs Wirkung — Kontrast",
        "kamera": "Static, Screen-Vergleich",
        "bewegung": "Großer leerer Kreis vs kleiner voller Kreis auf Screen",
        "stimmung": "Einsicht, Kontrast, Klar",
        "prompt": "Two circles on phone screen: large empty one shrinks, small full glowing one expands. Final state shows small bright circle dominant. Insight animation. Camera perfectly static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    63: {
        "konzept": "Noch nie Influencer — Handshake Animation",
        "kamera": "Static warm",
        "bewegung": "Zwei Hände-Icons verbinden sich auf Screen",
        "stimmung": "Einfach, Verbindung, Beruhigend",
        "prompt": "Two hand icons approach each other on phone screen and connect in handshake. Brief warm gold glow at connection point. Friendly and reassuring animation. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    64: {
        "konzept": "Passives Einkommen — Geld kommt automatisch",
        "kamera": "Static, Flow-Animation",
        "bewegung": "Kontinuierlicher Strom von kleinen Münz-Icons fließt auf Screen",
        "stimmung": "Passiv, Automatisch, Kontinuierlich",
        "prompt": "Continuous stream of coin icons flows across phone screen from right to left in steady stream. Never stops. Endless passive flow feel. Gold colored. Camera holds static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    65: {
        "konzept": "Saisonaler Marketing-Plan — Kalender dreht sich",
        "kamera": "Static, Kalender-Animation",
        "bewegung": "Kalender-Seiten drehen sich schnell (12 Monate)",
        "stimmung": "Planung, Langfristig, Strategie",
        "prompt": "Calendar pages flip rapidly through all twelve months on phone screen, each with different color accent. Slows and settles on current month. Planning and strategy feel. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    66: {
        "konzept": "Mehr Einladungen — Einladungs-Icons regnen herunter",
        "kamera": "Static, Regen-Animation",
        "bewegung": "Einladungs-Umschlag-Icons fallen von oben auf Screen",
        "stimmung": "Fülle, Viele Möglichkeiten, Aufregend",
        "prompt": "Envelope icons rain down on phone screen from top. Multiple sizes, all gold tinted. They accumulate briefly then screen refreshes. Abundance feeling. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    67: {
        "konzept": "Restaurant verdient mehr — Kurve mit Restaurant-Foto",
        "kamera": "Slow dolly-in dramatisch",
        "bewegung": "Kamera fährt langsam auf Restaurant-Foto auf Screen zu",
        "stimmung": "Aspiration, Verdienst, Potential",
        "prompt": "Camera slowly dollies toward restaurant image on phone screen. Image brightens and fills more of frame as camera approaches. Warm inviting glow intensifies. Settles close.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    68: {
        "konzept": "3 Kanäle — Drei Icons leuchten auf",
        "kamera": "Static, sequenziell",
        "bewegung": "Email, Influencer, Google Icons leuchten nacheinander auf",
        "stimmung": "Komplett, Alle Kanäle, Vollständig",
        "prompt": "Three channel icons light up sequentially on phone screen: email, person, map pin. Each glows gold when activated. Final state all three glowing together. Complete system feel.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    69: {
        "konzept": "QR Code mehr Wert — QR wächst und leuchtet",
        "kamera": "Macro zoom-in auf QR",
        "bewegung": "QR-Code pulsiert und wächst leicht auf Screen",
        "stimmung": "Wert, Potential, Unterschätzt",
        "prompt": "QR code on phone screen slowly pulses and grows slightly larger. Gold scan line sweeps across twice. Code settles at slightly larger size. Value revelation feel. Camera zooms in.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    70: {
        "konzept": "Negative Bewertung richtig handhaben — Transformation",
        "kamera": "Static dramatic",
        "bewegung": "Rote Bewertung transformiert zu grüner Antwort auf Screen",
        "stimmung": "Kontrolle, Professionell, Lösung",
        "prompt": "Red review on phone screen transforms to green professional response below it. Color shift from red to green is smooth and deliberate. Authority and control feel. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    71: {
        "konzept": "Kein Marketing = Bankrott — Dunkelheit, dann Licht",
        "kamera": "Static, dramatischer Kontrast",
        "bewegung": "Screen wird dunkel, dann explodiert Hiddin-App in Licht",
        "stimmung": "Dramatisch, Wake-Up-Call, Kontrast",
        "prompt": "Phone screen slowly dims to nearly black, pauses briefly, then suddenly brightens with Hiddin app in full glow. Sharp contrast. Wake-up feel. Gold burst at brightness peak.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    72: {
        "konzept": "FOMO Psychologie — Tür schliesst sich vor Kamera",
        "kamera": "Dolly-in, Tür schliesst sich",
        "bewegung": "Kamera fährt auf Tür zu, Tür schliesst sich im letzten Moment",
        "stimmung": "FOMO, Exklusivität, Verpasst",
        "prompt": "Camera slowly approaches door animation on phone screen. Door begins closing as camera gets close. Closes completely with brief gold flash through crack. FOMO feeling.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    73: {
        "konzept": "Storytelling — Buch öffnet sich auf Screen",
        "kamera": "Static, Buch-Animation",
        "bewegung": "Buch-Icon öffnet sich, Seiten blättern sanft",
        "stimmung": "Geschichte, Authentisch, Emotional",
        "prompt": "Book icon on phone screen opens slowly, pages flutter naturally in gentle breeze. Warm light emanates from open pages. Storytelling atmosphere. Camera holds static close-up.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    74: {
        "konzept": "Engagement verbessern — Herz-Icons steigen auf",
        "kamera": "Static, aufsteigende Icons",
        "bewegung": "Herz-Icons steigen langsam auf Screen auf",
        "stimmung": "Engagement, Organisch, Wachstum",
        "prompt": "Heart icons rise slowly upward on phone screen like floating bubbles. Different sizes, organic movement. Screen glows with activity energy. Endless stream upward. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    75: {
        "konzept": "Frag Hiddin — Fragezeichen erscheinen",
        "kamera": "Static, spielerisch",
        "bewegung": "Fragezeichen erscheinen und verschwinden spielerisch auf Screen",
        "stimmung": "Einladend, Spielerisch, Community",
        "prompt": "Question marks appear and disappear playfully across phone screen in different positions. Some large, some small. Curious and inviting energy. Screen stays active. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    76: {
        "konzept": "Behind the Scenes — Vorhang hebt sich",
        "kamera": "Static, dramatisches Reveal",
        "bewegung": "Vorhang-Animation auf Screen hebt sich, zeigt App",
        "stimmung": "Behind the Scenes, Enthüllung, Authentisch",
        "prompt": "Curtain animation rises on phone screen from bottom revealing app content beneath. Smooth theatrical reveal. Gold light streams from under curtain as it lifts. Dramatic.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    77: {
        "konzept": "Guter Influencer — Magnet zieht Herzen an",
        "kamera": "Static magnetic",
        "bewegung": "Magnet-Icon zieht Herz-Icons von außen Screen-Mitte",
        "stimmung": "Anziehung, Qualität, Magnetisch",
        "prompt": "Magnet icon on phone screen pulls heart icons from screen edges toward center. Hearts accelerate toward magnet. Clean magnetic pull animation. Quality over quantity feel.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    78: {
        "konzept": "Marketing Budget — Kuchendiagramm dreht sich",
        "kamera": "Static, Kuchendiagramm",
        "bewegung": "Kuchendiagramm dreht sich und zeigt Hiddin-Anteil",
        "stimmung": "Planung, Strategie, Smart",
        "prompt": "Pie chart rotates on phone screen. One gold slice expands to show optimal allocation. Chart settles with gold portion dominant. Financial planning energy. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    79: {
        "konzept": "75 Tage Zahlen — Dashboard füllt sich",
        "kamera": "Static, Dashboard füllt sich",
        "bewegung": "Alle Dashboard-Werte füllen sich gleichzeitig auf",
        "stimmung": "Milestone, Wachstum, Daten",
        "prompt": "All dashboard metrics on phone screen fill simultaneously: bars grow, numbers rise, circles complete. Everything reaches peak together with unified gold glow. Milestone celebration.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    80: {
        "konzept": "5 günstigste Maßnahmen — Checkliste",
        "kamera": "Static, Checkliste",
        "bewegung": "5 Häkchen erscheinen nacheinander auf Checkliste",
        "stimmung": "Praktisch, Umsetzbar, Günstig",
        "prompt": "Five checkboxes on phone screen check off one by one in steady rhythm. Each check accompanied by subtle green glow. Final all-checked state glows uniformly. Satisfying sequence.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    81: {
        "konzept": "Community Danke — Herz-Explosion",
        "kamera": "Static, Herz-Feuerwerk",
        "bewegung": "Herz-Icons explodieren aus Screen-Mitte nach außen",
        "stimmung": "Dankbarkeit, Gemeinschaft, Emotion",
        "prompt": "Hearts burst outward from center of phone screen in all directions. Multiple sizes and gold tones. Explosion settles as hearts float gently upward and fade. Warm gratitude.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    82: {
        "konzept": "Herbst kommt — Jahreszeiten-Übergang",
        "kamera": "Static, Farbübergang",
        "bewegung": "Screen-Farbe wechselt von Sommer-Grün zu Herbst-Gold",
        "stimmung": "Saison, Vorbereitung, Wandel",
        "prompt": "Phone screen color temperature shifts gradually from cool green tones to warm amber autumn tones. Leaf shadows pass briefly across screen. Seasonal transition feel. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    83: {
        "konzept": "Profil optimieren — Checkliste wird grün",
        "kamera": "Slow zoom-in auf Profil-Screen",
        "bewegung": "Kamera fährt auf vollständiges Profil zu, alles wird grün",
        "stimmung": "Vollständig, Optimal, Bereit",
        "prompt": "Camera slowly zooms toward profile screen as items turn green one by one. Fully complete profile glows uniformly green. Camera settles on completed optimized profile. Ready feel.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    84: {
        "konzept": "ROI-Rechner — Zahlen multiplizieren",
        "kamera": "Static, Multiplikation dramatisch",
        "bewegung": "Kleine Zahl multipliziert sich dramatisch auf Screen",
        "stimmung": "ROI, Beeindruckend, Überzeugend",
        "prompt": "Small input number on phone screen multiplies dramatically. Multiplication animation shows exponential growth. Final large result highlighted in gold. Impressive ROI reveal. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    85: {
        "konzept": "Expansion — Karte expandiert auf Screen",
        "kamera": "Zoom-out von Deutschland auf Europa",
        "bewegung": "Karte auf Screen zoomt aus, zeigt mehr Länder",
        "stimmung": "Wachstum, International, Zukunft",
        "prompt": "Map on phone screen slowly zooms out from single city to show multiple countries. Location pins appear across new territories. Expansion animation. Camera pulls back with map.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    86: {
        "konzept": "10 Fehler — Rote X erscheinen dann verschwinden",
        "kamera": "Static, schnelle Sequenz",
        "bewegung": "10 rote X erscheinen schnell auf Screen, dann werden alle grün",
        "stimmung": "Problem → Lösung, Dramatisch",
        "prompt": "Ten red X marks appear rapidly on phone screen filling it. Brief pause. Then all flip to green checkmarks simultaneously with gold flash. Before and after in one shot. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    87: {
        "konzept": "Food-Influencer Community — Personen erscheinen",
        "kamera": "Static expanding",
        "bewegung": "Influencer-Avatare erscheinen und füllen Screen",
        "stimmung": "Community, Viele, Gemeinschaft",
        "prompt": "Avatar circles appear on phone screen multiplying and arranging themselves. Screen fills with diverse creator icons. Community grid forms. Warm gold glow unifies them. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    88: {
        "konzept": "Marketing messen — Messbalken füllen sich",
        "kamera": "Static, Balken wachsen",
        "bewegung": "Mehrere KPI-Balken wachsen auf ihre Zielwerte",
        "stimmung": "Messbarkeit, Kontrolle, Daten",
        "prompt": "Multiple KPI bars grow simultaneously to different target heights on phone screen. Each bar turns gold when reaching target. Dashboard comes alive with metrics. Camera static.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    89: {
        "konzept": "Jetzt anfangen — Start-Button leuchtet auf",
        "kamera": "Close-up dolly-in auf Button",
        "bewegung": "Kamera fährt auf Start-Button zu, Button leuchtet, pulsiert",
        "stimmung": "Call-to-Action, Jetzt, Entscheidungsmoment",
        "prompt": "Camera slowly approaches start button on phone screen. Button begins glowing and pulsing with invitation. Finger reaches toward screen from below frame. Decisive moment. Settles.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    },

    90: {
        "konzept": "90 Tage Finale — Gold-Feuerwerk",
        "kamera": "Static, großes Finale",
        "bewegung": "Gold-Feuerwerk aus Screen, maximale Intensität, dann sanft",
        "stimmung": "Finale, Feier, Achievement",
        "prompt": "Gold firework burst explodes outward from phone screen center at maximum intensity. Light fills frame completely then gently dims to warm glow. Phone screen shines as grand finale.",
        "negative": NEGATIVE_PROMPT,
        "style": STYLE_BIBLE
    }
}

def get_kling_prompt(tag_nr):
    konzept = REEL_KONZEPTE.get(tag_nr, REEL_KONZEPTE[1])
    full_prompt = konzept["prompt"] + " " + konzept["style"]
    return {
        "prompt": full_prompt,
        "negative_prompt": konzept["negative"],
        "konzept": konzept["konzept"],
        "kamera": konzept["kamera"],
        "stimmung": konzept["stimmung"]
    }

if __name__ == "__main__":
    # Test: Zeige Konzept für heute
    from datetime import date
    START_DATE = date(2026, 4, 9)
    today = date.today()
    delta = (today - START_DATE).days + 1
    if delta < 1: delta = 1
    if delta > 90: delta = ((delta - 1) % 90) + 1
    
    k = get_kling_prompt(delta)
    print(f"Tag {delta}")
    print(f"Konzept: {k['konzept']}")
    print(f"Kamera: {k['kamera']}")
    print(f"Stimmung: {k['stimmung']}")
    print(f"Prompt: {k['prompt']}")
    print(f"Negative: {k['negative_prompt']}")
