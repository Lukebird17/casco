# Communications-Based Train Control (CBTC)

Komponenten, Funktionen und Betrieb

4. Auflage

FLASH-CARDS INSIDE

---

Communications-Based Train Control (CBTC)

---

# SPRINGER NATURE

[
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "GoA0",
    "Onsight train operation TOS": "GoA1",
    "Non-automated train operation NTO": "GoA2",
    "Semi-automated train operation STO": "GoA3",
    "Driverless train operation DTO": "GoA4"
  },
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "Sichern der Zugbewegung (Abschn. 5.1)",
    "Onsight train operation TOS": "Sichern des Fahrweges",
    "Non-automated train operation NTO": "Bediener",
    "Semi-automated train operation STO": "technisches System",
    "Driverless train operation DTO": "technisches System",
    "Unattended train operation UTO": "technisches System"
  },
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "Sichern der Zugbewegung (Abschn. 5.1)",
    "Onsight train operation TOS": "Sichern der Abstandshaltung",
    "Non-automated train operation NTO": "Bediener",
    "Semi-automated train operation STO": "technisches System",
    "Driverless train operation DTO": "technisches System",
    "Unattended train operation UTO": "technisches System"
  },
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "Sichern der Zugbewegung (Abschn. 5.1)",
    "Onsight train operation TOS": "Sichern der Geschwindigkeit",
    "Non-automated train operation NTO": "Bediener",
    "Semi-automated train operation STO": "Bediener (teilw. Überwachung durch technisches System)",
    "Driverless train operation DTO": "technisches System",
    "Unattended train operation UTO": "technisches System"
  },
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "Fahren des Fahrzeugs (Abschn. 5.2)",
    "Onsight train operation TOS": "Ermittlung des optimalen Fahrprofils",
    "Non-automated train operation NTO": "Bediener",
    "Semi-automated train operation STO": "technisches System",
    "Driverless train operation DTO": "technisches System",
    "Unattended train operation UTO": "technisches System"
  },
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "Fahren des Fahrzeugs (Abschn. 5.2)",
    "Onsight train operation TOS": "Regelung von Bremse und Traktion gemäß des optimalen Fahrprofils",
    "Non-automated train operation NTO": "Bediener",
    "Semi-automated train operation STO": "technisches System",
    "Driverless train operation DTO": "technisches System",
    "Unattended train operation UTO": "technisches System"
  },
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "Überwachen der Profilfreiheit (Abschn. 5.3)",
    "Onsight train operation TOS": "Verhinderung von Kollisionen mit Objekten",
    "Non-automated train operation NTO": "Bediener",
    "Semi-automated train operation STO": "Bediener",
    "Driverless train operation DTO": "Bediener",
    "Unattended train operation UTO": "technisches System"
  },
  {
    "Grundlegende Sicherungsfunktionen im Bahnbetrieb": "Überwachen der Profilfreiheit (Abschn. 5.3)",
    "Onsight train operation TOS": "Verhinderung von Kollisionen mit Personen",
    "Non-automated train operation NTO": "Bediener",
    "Semi-automated train operation STO": "Bediener",
    "Driverless train operation DTO": "Bediener",
    "Unattended train operation UTO": "technisches System"
  }
]

---

[
  {
    "Überwachen des Fahrgastwechsels (Abschn. 5.4)": "Sichern der Bahnsteigkante",
    "Steuern und Überwachen der Türfreigabe": "Bediener",
    "Bediener": "technisches System oder Bediener",
    "technisches System oder Bediener": "technisches System"
  },
  {
    "Überwachen des Fahrgastwechsels (Abschn. 5.4)": "Sicherstellung der Abfertigungsbedingungen",
    "Steuern und Überwachen der Türfreigabe": "Bediener",
    "Bediener": "technisches System oder Bediener",
    "technisches System oder Bediener": "technisches System"
  },
  {
    "Überwachen des Fahrgastwechsels (Abschn. 5.4)": "Automatischer Zugbetrieb (Abschn. 5.5)",
    "Steuern und Überwachen der Türfreigabe": "Ein- und Aussetzen von Fahrzeugen",
    "Bediener": "Bediener",
    "technisches System oder Bediener": "Bediener",
    "technisches System": "technisches System"
  },
  {
    "Überwachen des Fahrgastwechsels (Abschn. 5.4)": "Automatischer Zugbetrieb (Abschn. 5.5)",
    "Steuern und Überwachen der Türfreigabe": "Überwachung des Fahrzeugzustands",
    "Bediener": "Bediener",
    "technisches System oder Bediener": "Bediener",
    "technisches System": "technisches System"
  },
  {
    "Überwachen des Fahrgastwechsels (Abschn. 5.4)": "Störfallerkennung und Störfallmanagement (Abschn. 5.6)",
    "Steuern und Überwachen der Türfreigabe": "Fahrzeugdiagnose, Erkennung von Feuer und Rauch, Handlungen bei Störfällen",
    "Bediener": "Bediener",
    "technisches System oder Bediener": "Bediener",
    "technisches System": "technisches System und/ oder Bediener in Leitstelle"
  }
]

---

Automatisierungsgrad nehmen naturgemäß die Anforderungen an das Signalsystem und die eingesetzten Fahrzeuge zu. Die einzelnen Funktionen werden in Kap. 5 näher erläutert.

### 3.1 Grade of Automation 0: Zugbetrieb auf Sicht

Beim Zugbetrieb auf Sicht (Train Operations on Sight, TOS) ist der Fahrzeugführer in vollem Umfang für die sichere Durchführung der Fahrzeugbewegung (insbesondere den Folgefahrschutz) verantwortlich, da hier fahrzeugseitig keinerlei Überwachung der zulässigen Fahrweise realisiert ist (IEC 62290-1:2014). Die Fahrzeuge verkehren auf eingeschränkt gesicherten Fahrwegen. Einzelweichensteuerungen stellen und sichern Weichen in der Endlage und zeigen dies dem Fahrzeugführer an. Einfache Fahrsignalanlagen gewährleisten an eingleisigen Strecken den Gegenfahrschutz. Bahnübergänge vermeiden Unfälle zwischen Straßenverkehrsteilnehmern und Schienenfahrzeugen. In komplexeren Streckentopologien erfolgt eine Fahrwegsicherung über Fahrstraßen. Dieser Automatisierungsgrad kann in zwei Stufen unterschieden werden:

• Automatisierungsgrad 0a – nicht assistierter Zugbetrieb auf Sicht: Der Fahrer beobachtet stets den Verkehr in seinem Sichtfeld, den Fahrweg und die Höchstgeschwindigkeit. Er kontrolliert das Anfahren und das Bremsen, erkennt Gefahren-situationen und hält das Schienenfahrzeug bei Bedarf an. Die Fahrweise entspricht also dem Führen eines Personenkraftwagens (Pkw) im öffentlichen Straßenraum.

- Automatisierungsgrad 0b – assistierter Zugbetrieb auf Sicht: Der Fahrer wird durch ein Fahrerassistenzsystem in einzelnen Aspekten seiner Fahraufgabe unterstützt. Sensoren erfassen hierbei das Verkehrsumfeld und Algorithmen analysieren die Fahrsituation. Der Fahrer wird über einen Warnhinweis zum rechtzeitigen und richtigen Eingreifen aufgefordert (informierendes Assistenzsystem), beziehungsweise es erfolgt ein automatischer Eingriff in die Fahrdynamik des Schienenfahrzeugs (intervenierendes Assistenzsystem) und der Fahrer wird hierüber informiert (Jung et al. 2018).

### 3.2 Grade of Automation 1: Nicht automatisiierter Zugbetrieb

Beim nicht automatisierten Zugbetrieb (Non-automated Train Operations, NTO) wird das Fahrzeug auf technisch gesicherten Fahrwegen vom Fahrer geführt (IEC 62290-1:2014). Technische Einrichtungen signalisieren dem Fahrer, dass der Fahrweg technisch gesichert ist. Dies bedeutet, dass die Fahrzeugbewegung technisch vor Gegenfahrten, Flankenfahrten, Folgefahrten und Unfällen mit systemfremden Verkehrsteilnehmern (Kraftfahrzeugen und Fußgängern) geschützt ist. Der Fahrzeugführer führt das Fahrzeug gemäß der betrieblichen Vorgaben. Die Einhaltung der zulässigen Fahrweise wird auf dem Fahrzeug überwacht. Je nach konkreter Ausprägung der Überwachung kann dieser Automatisierungsgrad in zwei Stufen unterschieden werden:

---

• Automatisierungsgrad 1a – nicht automatisiierter Zugbetrieb mit punktförmiger Übertragung und Überwachung der zulässigen Fahrweise des Fahrzeugs: Hierbei erhält das Fahrzeug an einem diskreten Punkt entlang der Strecke eine Information über den Zustand des Signals. Das Fahrzeuggerät leitet im Bedarfsfall eine sicherheitsgerichtete Reaktion ein. Diese Systeme dienen der Vermeidung der Überfahrt Halt zeigender Signale (Fahrsperre).

- Automatisierungsgrad 1b – nicht automatisierter Zugbetrieb mit kontinuierlicher Übertragung und Überwachung der zulässigen Fahrweise des Fahrzeugs: Hierbei erhält das Fahrzeug von der Streckeneinrichtung Führungsgrößen, mit denen die Fahrzeugbewegung kontinuierlich überwacht werden kann. Diese Systeme überwachen die Einhaltung der zulässigen Fahrweise des Zuges kontinuierlich und gehen damit über den zuvor beschriebenen Funktionsumfang (Fahrsperre) hinaus. Die Datenübertragung von der Strecke zum Fahrzeug kann entweder an diskreten Punkten oder kontinuierlich erfolgen.

### 3.3 Grade of Automation 2: Halbautomatischer Zugbetrieb

Beim halbautomatischen Zugbetrieb (Semi-automatic Train Operation, STO) die Steuerung der Traktionsleistung und der Bremsen wird von einem technischen System übernommen (IEC 62290-1:2014). Der Fahrer bleibt in diesem Automatisierungsgrad nach wie vor auf dem Führerstand. Er erteilt den Befehl für die Türöffnung, überwacht den Fahrgastwechsel und fertigt den Zug in der Station ab. Liegen alle Abfertigungsbedingungen vor, erteilt er den Abfahraufrag für eine sichere Abfahrt des Zuges aus der Haltestelle. Der Fahrer überwacht die Fahrt zur nächsten Station und kann in Gefahrensituationen sofort eingreifen (Rumsey 2010). Das Fahrzeug bremst selbsttätig mit einer hohen Genauigkeit auf die Zielposition in der nächsten Station. Auf diese Weise kann eine von der Leitebene vorgegebene optimale Fahrstrategie vom Fahrzeug selbsttätig umgesetzt werden.

### 3.4 Grade of Automation 3: Begleiteter fahrerloser Zugbetrieb

Beim begleiteten fahrerlosen Zugbetrieb (Driverless Train Operation, DTO) kann sich der Fahrer vom Führerstand des Zuges entfernen. Der Fahrer bleibt aber weiterhin an Bord des Zuges, um seine betrieblichen Aufgaben zu erfüllen und um im Falle des Funktionsausfalls der Automatisierungssysteme die Verantwortung für das Führen des Zuges über den hierfür vorgesehenen Notführerstand auf dem Fahrzeug unverzüglich wieder zu übernehmen. Da der Fahrer nach wie vor auf dem Fahrzeug ist, resultieren hieraus für die Entstörung und Wiederherstellung des Regelbetriebs Zeitgewinne im Vergleich zum im nächsten Abschnitt dargestellten unbegleiteten fahrerlosen Zugbetrieb, bei dem das Betriebspersonal das Fahrzeug erst fußläufig durch den Tunnel erreichen muss. Da der Fahrer in diesem Automatisierungsgrad die Fahrt des Zuges nicht mehr überwacht und die vor dem Zug liegende Strecke nicht mehr im Voraus einsehen kann, stellt dieser Automatisierungssysteme ein.

---

grad höhere Anforderungen an Gewährleistung der Profilfreiheit für die Zugfahrten (beispielsweise durch fahrzeugseitige Hinderniserkennungssysteme). Im Automatisierungsgrad DTO können die Türen und die Abfahrt des Zuges vom Bahnsteig entweder automatisch oder manuell von einem beliebigen Ort im Zugverband (und damit nicht zwingend vom Führerstand des Zuges) gesteuert werden. Dies wirkt sich insbesondere an Endhaltestellen positiv auf den Durchsatz aus, da die Zeit gespart werden kann, die bei geringeren Automatisierungsgraden für den Wechsel des Führerstandes erforderlich ist. Der Fahrzeugführer muss nun nicht mehr den ganzen Zugverband entlang von einem Führerstand zum anderen gehen (Rumsey 2010).

### 3.5 Grade of Automation 4: Unbegleiteter fahrerloser Zugbetrieb

Der unbegleitete fahrerlose Zugbetrieb (Unmanned Train Operation, UTO) kann Zugbewegungen ohne Fahrgäste (zum Beispiel für Fahrten in ein Abstellgleis oder in einem automatisiert betriebenen Depot) oder den Betrieb von Zügen im Fahrgastbetrieb ohne Begleitpersonen an Bord umfassen. Letzteres setzt voraus, dass der Zug bei Ausfällen von Steuerungssystemen ferngesteuert werden kann oder zumindest von entlang der Strecke verfügbarem Personal in möglichst kurzer Zeit erreicht werden kann. Gegebenenfalls ist es auch möglich, das Fahrzeug über die Darstellung der Führerstandsanzeige und Echtzeitkamerabildern aus der Leitstelle in der Rückfallebene situativ fernzusteuern. Im (Brandenburger et al. 2017) Störungsfall müssen die Fahrgäste an Bord aus der Leitstelle heraus beruhigt werden. Daher sind gute Kommunikationsverbindungen zwischen dem Fahrzeug und den Mitarbeitern des Verkehrsunternehmens unerlässlich. Eine Automatisierung der Türsteuerung ist für diesen Automatisierungsgrad zwingend erforderlich und muss entsprechend sicher gestaltet sein. Dies bedeutet, dass eingeklemmte Kleidungsstücken oder Personen sicher erkannt werden müssen und in diesem Fall unmittelbar eine sicherheitsgerichtete Reaktion eingeleitet wird. Ein erhöhter Schutz der Strecke vor dem Eindringen unberechtigter Personen sowie technische Systeme zur Hinderniserkennung sind ebenfalls erforderlich.

## Literatur

Brandenburger N, Naumann A, Grippenkoven J, Jipp M (2017) Der Train Operator – Situative Fernsteuerung von automatisierten Zügen. EI – Eisenbahningenieur 09/2017, S 13–15

IEC 62290-1:2014 Railway applications – urban guided transport management and command/control systems – part 1: system principles and fundamental concepts

Jung HS, Rüffer M, Schindler C (2018) Fahrerassistenzsysteme für die Straßenbahn. Nahverkehr 36(7+8):26–35

Rumsey A (2010) Semi-automatic, driverless and unattended operation of trains. Signal + Draht 102(3):43–46

---

# Betriebsarten und Betriebsartenübergänge im automatisierten Betrieb

## SN Flashcards

Als Käufer*in dieses Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards“ mit Fragen zur Wissensüberprüfung und zum Lernen von Buchinhalten nutzen.

1. Gehen Sie bitte auf https://flashcards.springernature.com/login und



2. erstellen Sie ein Benutzerkonto, indem Sie Ihre Mailadresse angeben und ein Passwort vergeben.

3. Verwenden Sie den folgenden Link, um Zugang zu Ihrem SN Flashcards Set zu erhalten: ▶ https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht funktionieren, senden Sie uns bitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Die Zugbeeinflussungssysteme dienen einer optimalen Abwicklung des Betriebs. Hierfür stehen – in Abhängigkeit vom Ausstattungsgrad von Fahrzeug und Infrastruktur – unterschiedliche Betriebsarten zur Verfügung. Jede Betriebsart umfasst eine Teilmenge an Sicherungsfunktionen. Die verschiedenen Betriebsarten werden in Abschn. 4.1 dargestellt. Zwischen den Betriebsarten sind diverse Übergänge möglich. Diese sind an eindeutige Kriterien geknüpft und werden technisch überwacht. In Abschn. 4.2 werden die zwischen den Betriebsarten bestehenden Übergänge anhand ausgewählter Beispiele in halbauto- matisch betriebenen Systemen erläutert. In Abschn. 4.3 werden exemplarische Betriebsarten übergänge in unbegleitet fahrerlosen Systemen näher ausgeführt.

---

### 4.1 Betriebsarten im Überblick

Automatische Zugbeeinflussungssysteme werden in verschiedenen betrieblichen Situationen in verschiedenen Betriebsarten betrieben. Die Betriebsarten sind gekennzeichnet durch einen unterschiedlichen Umfang vom Zugbeeinflussungssystem zur Verfügung stehenden Überwachungsfunktionen. Die Betriebsarten und Betriebsartenübergänge stellen einen (endlichen) Zustandsautomaten dar. Hierbei gibt es eine endliche Anzahl von Zuständen und definierte Übergangsbedingungen. Abb. 4.1 stellt einen Zustandsautomaten mit den üblichen Betriebsarten und Betriebsartenübergängen (Transitionen) dar. Diese Betriebsarten können unterschieden werden in Betriebsarten für den Regelbetrieb (vgl. Abschn. 4.1.1), Betriebsarten für Gefahren- und Störzustände (vgl. Abschn. 4.1.2), Betriebsarten für Ausschaltzustände (vgl. Abschn. 4.1.3) sowie Betriebsarten für nicht mit CBTC ausgerüstete Bestandsstrecken (vgl. Abschn. 4.1.4). Zusätzlich zu den in Abb. 4.1 dargestellten Betriebsarten können von den Betreibern im Einzelfall weitere Betriebsarten gewünscht werden. Beispiele hierfür sind ein ferngesteuerter Betrieb, bei dem die Leitstelle die Rolle des Fahrpersonals übernimmt oder die Umschaltung zwischen ver-

[
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Aus der Zuglenkung heraus wird für den in die Station eingefahrenen Zug die Sicherung des Fahrwegs aus der Station in die Kehranlage angestoßen.",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Aus der Zuglenkung heraus wird für den in die Station eingefahrenen Zug die Sicherung des Fahrwegs aus der Station in die Kehranlage angestoßen."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Nach erfolgreicher Sicherung des Fahrweges erhält der Fahrer auf der Führerstandsanzeige eine Anforderung zum Start der fahrerlosen Kehrfahrt.",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Nach erfolgreicher Sicherung des Fahrweges erhält der Fahrer auf der Führerstandsanzeige eine Anforderung zum Start der fahrerlosen Kehrfahrt."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Der Fahrer verläßt das Fahrzeug und geht zu einem Schlüsselschalter am Ende des Bahnsteigs.",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Der Fahrer verbleibt auf dem Fahrzeug."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Der Fahrer führt vom Bahnsteigende aus eine Sichtprüfung durch und prüft, ob der Gleisbereich zwischen Bahnsteigende und Kehranlage frei von Hindernissen ist. Er bestätigt dies bestätigt durch Betätigen des Schlüsselschalters am Bahnsteigende. Er erteilt damit einen Abfahraufrag für den Zug zur Einfahrt in die Kehranlage (vgl. Ziffer 1 in Abb. 4.2).",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Der Fahrer erteilt einen Abfahraufrag für den Zug zur Einfahrt in die Kehranlage durch Betätigung einer Quittungstaste am aktiven (vorderen) Führerstand (Ziffer 1). Durch den baulichen Abschluss mit Bahnsteigtüren muss nicht mit Hindernissen in der Kehranlage gerechnet werden. Der Fahrer kann nun durch den Führerstand am anderen Ende des Zuges gehen."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Das Fahrzeug fährt selbsttätig in die Kehranlage ein und kommt dort im gewünschten Gleis vor dem Prellbock zum Stillstand.",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Das Fahrzeug fährt selbsttätig in die Kehranlage ein und kommt dort im gewünschten Gleis vor dem Prellbock zum Stillstand."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Der Zug rüstet automatisch den führenden Führerstand ab, wechselt den Führerstand und rüstet den Führerstand auf der anderen Fahrzeugseite für die Fahrt aus der Kehranlage auf (Ziffer 2).",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Der Zug rüstet automatisch den führenden Führerstand ab, wechselt den Führerstand und rüstet den Führerstand auf der anderen Fahrzeugseite für die Fahrt aus der Kehranlage auf (Ziffer 2)."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Aus der Zuglenkung heraus wird der Fahrweg für die Ausfahrt des Fahrzeugs aus der Kehranlage und die Einfahrt des Zuges in die Station eingestellt und technisch gesichert.",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Aus der Zuglenkung heraus wird der Fahrweg für die Ausfahrt des Fahrzeugs aus der Kehranlage und die Einfahrt des Zuges in die Station eingestellt und technisch gesichert."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Der Fahrer wechselt auf den gegenüberliegenden Bahnsteig und geht zum Schlüsselschalter am Bahnsteiganfang. Der Fahrer führt vom Bahnsteiganfang aus eine Sichtprüfung durch und prüft, ob der Gleisbereich zwischen Bahnsteiganfang und Kehranlage frei von Hindernissen ist (Ziffer 3). Er bekommt dazu angezeigt, dass der Fahrweg technisch gesichert ist.",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Die Streckeneinrichtung erteilt nach erfolgreicher Fahrwegsicherung einen Abfahraufrag für den Zug zur Ausfahrt aus der Kehranlage in das Stationsgleis (Ziffer 3). Das Fahrzeug verläßt die Kehranlage selbsttätig (Ziffer 4) und fährt selbsttätig bis zum Haltepunkt am Bahnsteigende des Stationsgleises (Ziffer 5). Durch den baulichen Abschluss mit Bahnsteigtüren muss nicht mit Hindernissen in der Kehranlage und im Stationsgleis gerechnet werden."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Das Fahrzeug fährt selbsttätig bis zu einer Übergabestelle am Bahnsteiganfang. Der Fahrer führt hierbei eine kontinuierliche Überwachung der Zugbewegung durch. In Notfällen kann der Zug jederzeit vom Fahrer durch Rückstellen des Schlüsselschalters zwangsgebremst werden. Das Fahrzeug kommt an der Übergabestelle am Bahnsteiganfang zum Stillstand (Ziffer 4).",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Die Streckeneinrichtung erteilt nach erfolgreicher Fahrwegsicherung einen Abfahraufrag für den Zug zur Ausfahrt aus der Kehranlage in das Stationsgleis (Ziffer 3). Das Fahrzeug verläßt die Kehranlage selbsttätig (Ziffer 4) und fährt selbsttätig bis zum Haltepunkt am Bahnsteigende des Stationsgleises (Ziffer 5). Durch den baulichen Abschluss mit Bahnsteigtüren muss nicht mit Hindernissen in der Kehranlage und im Stationsgleis gerechnet werden."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Der Fahrer steigt an der Übergabestelle in das Fahrzeug ein und besetzt den Führerstand. Der Fahrer setzt die Fahrt bis zum Haltepunkt im Ausfahrgleis der Station fort und überwacht den vor ihm liegenden Gleisbereich im Stationsbereich auf Freisein von Hindernissen. Der Fahrer bringt den Zug am Haltepunkt zum Stillstand (Ziffer 5).",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Die Streckeneinrichtung erteilt nach erfolgreicher Fahrwegsicherung einen Abfahraufrag für den Zug zur Ausfahrt aus der Kehranlage in das Stationsgleis (Ziffer 3). Das Fahrzeug verläßt die Kehranlage selbsttätig (Ziffer 4) und fährt selbsttätig bis zum Haltepunkt am Bahnsteigende des Stationsgleises (Ziffer 5). Durch den baulichen Abschluss mit Bahnsteigtüren muss nicht mit Hindernissen in der Kehranlage und im Stationsgleis gerechnet werden."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Der Fahrer erteilt eine Türfreigabe und überwacht den Fahrgastwechsel. Anschließend beginnt er die Zugfahrt zur nächsten Station.",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Der Fahrer erteilt eine Türfreigabe und überwacht den Fahrgastwechsel. Anschließend beginnt er die Zugfahrt zur nächsten Station."
  },
  {
    "Kehrfahrt bei Betrieb ohne Bahnsteigtüren": "Vetrauensintervall mit Synchronisation",
    "Kehrfahrt bei Betrieb mit Bahnsteigtüren": "Größen"
  }
]

[
  {
    "Feature": "Barnstoke",
    "Value": "1.0 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0.5 m"
  },
  {
    "Feature": "Barnstoke",
    "Value": "0.5 m"
  },
  {
    "Feature": "Cruising",
    "Value": "0."
  },
  {
    "Feature": "Energy Level",
    "Value": "State"
  },
  {
    "Feature": "1",
    "Value": "Basis State"
  },
  {
    "Feature": "2",
    "Value": "Basis State"
  },
  {
    "Feature": "3",
    "Value": "Basis State"
  },
  {
    "Feature": "4",
    "Value": "Basis State"
  },
  {
    "Feature": "5",
    "Value": "Basis State"
  },
  {
    "Feature": "6",
    "Value": "Basis State"
  },
  {
    "Feature": "7",
    "Value": "Basis State"
  },
  {
    "Feature": "8",
    "Value": "Basis State"
  },
  {
    "Feature": "9",
    "Value": "Basis State"
  },
  {
    "Feature": "10",
    "Value": "Basis State"
  },
  {
    "Feature": "11",
    "Value": "Basis State"
  },
  {
    "Feature": "12",
    "Value": "Basis State"
  },
  {
    "Feature": "13",
    "Value": "Basis State"
  },
  {
    "Feature": "14",
    "Value": "Basis State"
  },
  {
    "Feature": "15",
    "Value": "Basis State"
  },
  {
    "Feature": "16",
    "Value": "Basis State"
  },
  {
    "Feature": "17",
    "Value": "Basis State"
  },
  {
    "Feature": "18",
    "Value": "Basis State"
  },
  {
    "Feature": "19",
    "Value": "Basis State"
  },
  {
    "Feature": "20",
    "Value": "Basis State"
  },
  {
    "Feature": "21",
    "Value": "Basis State"
  },
  {
    "Feature": "22",
    "Value": "Basis State"
  },
  {
    "Feature": "23",
    "Value": "Basis State"
  },
  {
    "Feature": "24",
    "Value": "Basis State"
  },
  {
    "Feature": "25",
    "Value": "Basis State"
  },
  {
    "Feature": "26",
    "Value": "Basis State"
  },
  {
    "Feature": "27",
    "Value": "Basis State"
  },
  {
    "Feature": "28",
    "Value": "Basis State"
  },
  {
    "Feature": "29",
    "Value": "Basis State"
  },
  {
    "Feature": "30",
    "Value": "Basis State"
  },
  {
    "Feature": "31",
    "Value": "Basis State"
  },
  {
    "Feature": "32",
    "Value": "Basis State"
  },
  {
    "Feature": "33",
    "Value": "Basis State"
  },
  {
    "Feature": "34",
    "Value": "Basis State"
  },
  {
    "Feature": "35",
    "Value": "Basis State"
  },
  {
    "Feature": "36",
    "Value": "Basis State"
  },
  {
    "Feature": "37",
    "Value": "Basis State"
  },
  {
    "Feature": "38",
    "Value": "Basis State"
  },
  {
    "Feature": "39",
    "Value": "Basis State"
  },
  {
    "Feature": "40",
    "Value": "Basis State"
  },
  {
    "Feature": "41",
    "Value": "Basis State"
  },
  {
    "Feature": "42",
    "Value": "Basis State"
  },
  {
    "Feature": "43",
    "Value": "Basis State"
  },
  {
    "Feature": "44",
    "Value": "Basis State"
  },
  {
    "Feature": "45",
    "Value": "Basis State"
  },
  {
    "Feature": "46",
    "Value": "Basis State"
  },
  {
    "Feature": "47",
    "Value": "Basis State"
  },
  {
    "Feature": "48",
    "Value": "Basis State"
  },
  {
    "Feature": "49",
    "Value": "Basis State"
  },
  {
    "Feature": "50",
    "Value": "Basis State"
  },
  {
    "Feature": "51",
    "Value": "Basis State"
  },
  {
    "Feature": "52",
    "Value": "Basis State"
  },
  {
    "Feature": "53",
    "Value": "Basis State"
  },
  {
    "Feature": "54",
    "Value": "Basis State"
  },
  {
    "Feature": "55",
    "Value": "Basis State"
  },
  {
    "Feature": "56",
    "Value": "Basis State"
  },
  {
    "Feature": "57",
    "Value": "Basis State"
  },
  {
    "Feature": "58",
    "Value": "Basis State"
  },
  {
    "Feature": "59",
    "Value": "Basis State"
  },
  {
    "Feature": "60",
    "Value": "Basis State"
  },
  {
    "Feature": "61",
    "Value": "Basis State"
  },
  {
    "Feature": "62",
    "Value": "Basis State"
  },
  {
    "Feature": "63",
    "Value": "Basis State"
  },
  {
    "Feature": "64",
    "Value": "Basis State"
  },
  {
    "Feature": "65",
    "Value": "Basis State"
  },
  {
    "Feature": "66",
    "Value": "Basis State"
  },
  {
    "Feature": "67",
    "Value": "Basis State"
  },
  {
    "Feature": "68",
    "Value": "Basis State"
  },
  {
    "Feature": "69",
    "Value": "Basis State"
  },
  {
    "Feature": "70",
    "Value": "Basis State"
  },
  {
    "Feature": "71",
    "Value": "Basis State"
  },
  {
    "Feature": "72",
    "Value": "Basis State"
  },
  {
    "Feature": "73",
    "Value": "Basis State"
  },
  {
    "Feature": "74",
    "Value": "Basis State"
  },
  {
    "Feature": "75",
    "Value": "Basis State"
  },
  {
    "Feature": "76",
    "Value": "Basis State"
  },
  {
    "Feature": "77",
    "Value": "Basis State"
  },
  {
    "Feature": "78",
    "Value": "Basis State"
  },
  {
    "Feature": "79",
    "Value": "Basis State"
  },
  {
    "Feature": "80",
    "Value": "Basis State"
  },
  {
    "Feature": "81",
    "Value": "Basis State"
  },
  {
    "Feature": "82",
    "Value": "Basis State"
  },
  {
    "Feature": "83",
    "Value": "Basis State"
  },
  {
    "Feature": "84",
    "Value": "Basis State"
  },
  {
    "Feature": "85",
    "Value": "Basis State"
  },
  {
    "Feature": "86",
    "Value": "Basis State"
  },
  {
    "Feature": "87",
    "Value": "Basis State"
  },
  {
    "Feature": "88",
    "Value": "Basis State"
  },
  {
    "Feature": "89",
    "Value": "Basis State"
  },
  {
    "Feature": "90",
    "Value": "Basis State"
  },
  {
    "Feature": "91",
    "Value": "Basis State"
  },
  {
    "Feature": "92",
    "Value": "Basis State"
  },
  {
    "Feature": "93",
    "Value": "Basis State"
  },
  {
    "Feature": "94",
    "Value": "Basis State"
  },
  {
    "Feature": "95",
    "Value": "Basis State"
  },
  {
    "Feature": "96",
    "Value": "Basis State"
  },
  {
    "Feature": "97",
    "Value": "Basis State"
  },
  {
    "Feature": "98",
    "Value": "Basis State"
  },
  {
    "Feature": "99",
    "Value": "Basis State"
  },
  {
    "Feature": "100",
    "Value": "Basis State"
  },
  {
    "Feature": "101",
    "Value": "Basis State"
  },
  {
    "Feature": "102",
    "Value": "Basis State"
  },
  {
    "Feature": "103",
    "Value": "Basis State"
  },
  {
    "Feature": "104",
    "Value": "Basis State"
  },
  {
    "Feature": "105",
    "Value": "Basis State"
  },
  {
    "Feature": "106",
    "Value": "Basis State"
  },
  {
    "Feature": "107",
    "Value": "Basis State"
  },
  {
    "Feature": "108",
    "Value": "Basis State"
  },
  {
    "Feature": "109",
    "Value": "Basis State"
  },
  {
    "Feature": "110",
    "Value": "Basis State"
  },
  {
    "Feature": "111",
    "Value": "Basis State"
  },
  {
    "Feature": "112",
    "Value": "Basis State"
  },
  {
    "Feature": "113",
    "Value": "Basis State"
  },
  {
    "Feature": "114",
    "Value": "Basis State"
  },
  {
    "Feature": "115",
    "Value": "Basis State"
  },
  {
    "Feature": "116",
    "Value": "Basis State"
  },
  {
    "Feature": "117",
    "Value": "Basis State"
  },
  {
    "Feature": "118",
    "Value": "Basis State"
  },
  {
    "Feature": "119",
    "Value": "Basis State"
  },
  {
    "Feature": "120",
    "Value": "Basis State"
  },
  {
    "Feature": "121",
    "Value": "Basis State"
  },
  {
    "Feature": "122",
    "Value": "Basis State"
  },
  {
    "Feature": "123",
    "Value": "Basis State"
  },
  {
    "Feature": "124",
    "Value": "Basis State"
  },
  {
    "Feature": "125",
    "Value": "Basis State"
  },
  {
    "Feature": "126",
    "Value": "Basis State"
  },
  {
    "Feature": "127",
    "Value": "Basis State"
  },
  {
    "Feature": "128",
    "Value": "Basis State"
  },
  {
    "Feature": "129",
    "Value": "Basis State"
  },
  {
    "Feature": "130",
    "Value": "Basis State"
  },
  {
    "Feature": "131",
    "Value": "Basis State"
  },
  {
    "Feature": "132",
    "Value": "Basis State"
  },
  {
    "Feature": "133",
    "Value": "Basis State"
  },
  {
    "Feature": "134",
    "Value": "Basis State"
  },
  {
    "Feature": "135",
    "Value": "Basis State"
  },
  {
    "Feature": "136",
    "Value": "Basis State"
  },
  {
    "Feature": "137",
    "Value": "Basis State"
  },
  {
    "Feature": "138",
    "Value": "Basis State"
  },
  {
    "Feature": "139",
    "Value": "Basis State"
  },
  {
    "Feature": "140",
    "Value": "Basis State"
  },
  {
    "Feature": "141",
    "Value": "Basis State"
  },
  {
    "Feature": "142",
    "Value": "Basis State"
  },
  {
    "Feature": "143",
    "Value": "Basis State"
  },
  {
    "Feature": "144",
    "Value": "Basis State"
  },
  {
    "Feature": "145",
    "Value": "Basis State"
  },
  {
    "Feature": "146",
    "Value": "Basis State"
  },
  {
    "Feature": "147",
    "Value": "Basis State"
  },
  {
    "Feature": "148",
    "Value": "Basis State"
  },
  {
    "Feature": "149",
    "Value": "Basis State"
  },
  {
    "Feature": "150",
    "Value": "Basis State"
  },
  {
    "Feature": "151",
    "Value": "Basis State"
  },
  {
    "Feature": "152",
    "Value": "Basis State"
  },
  {
    "Feature": "153",
    "Value": "Basis State"
  },
  {
    "Feature": "154",
    "Value": "Basis State"
  },
  {
    "Feature": "155",
    "Value": "Basis State"
  },
  {
    "Feature": "156",
    "Value": "Basis State"
  },
  {
    "Feature": "157",
    "Value": "Basis State"
  },
  {
    "Feature": "158",
    "Value": "Basis State"
  },
  {
    "Feature": "159",
    "Value": "Basis State"
  },
  {
    "Feature": "160",
    "Value": "Basis State"
  },
  {
    "Feature": "161",
    "Value": "Basis State"
  },
  {
    "Feature": "162",
    "Value": "Basis State"
  },
  {
    "Feature": "163",
    "Value": "Basis State"
  },
  {
    "Feature": "164",
    "Value": "Basis State"
  },
  {
    "Feature": "165",
    "Value": "Basis State"
  },
  {
    "Feature": "166",
    "Value": "Basis State"
  },
  {
    "Feature": "167",
    "Value": "Basis State"
  },
  {
    "Feature": "168",
    "Value": "Basis State"
  },
  {
    "Feature": "169",
    "Value": "Basis State"
  },
  {
    "Feature": "170",
    "Value": "Basis State"
  },
  {
    "Feature": "171",
    "Value": "Basis State"
  },
  {
    "Feature": "172",
    "Value": "Basis State"
  },
  {
    "Feature": "173",
    "Value": "Basis State"
  },
  {
    "Feature": "174",
    "Value": "Basis State"
  },
  {
    "Feature": "175",
    "Value": "Basis State"
  },
  {
    "Feature": "176",
    "Value": "Basis State"
  },
  {
    "Feature": "177",
    "Value": "Basis State"
  },
  {
    "Feature": "178",
    "Value": "Basis State"
  },
  {
    "Feature": "179",
    "Value": "Basis State"
  },
  {
    "Feature": "180",
    "Value": "Basis State"
  },
  {
    "Feature": "181",
    "Value": "Basis State"
  },
  {
    "Feature": "182",
    "Value": "Basis State"
  },
  {
    "Feature": "183",
    "Value": "Basis State"
  },
  {
    "Feature": "184",
    "Value": "Basis State"
  },
  {
    "Feature": "185",
    "Value": "Basis State"
  },
  {
    "Feature": "186",
    "Value": "Basis State"
  },
  {
    "Feature": "187",
    "Value": "Basis State"
  },
  {
    "Feature": "188",
    "Value": "Basis State"
  },
  {
    "Feature": "189",
    "Value": "Basis State"
  },
  {
    "Feature": "190",
    "Value": "Basis State"
  },
  {
    "Feature": "191",
    "Value": "Basis State"
  },
  {
    "Feature": "192",
    "Value": "Basis State"
  },
  {
    "Feature": "193",
    "Value": "Basis State"
  },
  {
    "Feature": "194",
    "Value": "Basis State"
  },
  {
    "Feature": "195",
    "Value": "Basis State"
  },
  {
    "Feature": "196",
    "Value": "Basis State"
  },
  {
    "Feature": "197",
    "Value": "Basis State"
  },
  {
    "Feature": "198",
    "Value": "Basis State"
  },
  {
    "Feature": "199",
    "Value": "Basis State"
  },
  {
    "Feature": "200",
    "Value": "Basis State"
  },
  {
    "Feature": "201",
    "Value": "Basis State"
  },
  {
    "Feature": "202",
    "Value": "Basis State"
  },
  {
    "Feature": "203",
    "Value": "Basis State"
  },
  {
    "Feature": "204",
    "Value": "Basis State"
  },
  {
    "Feature": "205",
    "Value": "Basis State"
  },
  {
    "Feature": "206",
    "Value": "Basis State"
  },
  {
    "Feature": "207",
    "Value": "Basis State"
  },
  {
    "Feature": "208",
    "Value": "Basis State"
  },
  {
    "Feature": "209",
    "Value": "Basis State"
  },
  {
    "Feature": "210",
    "Value": "Basis State"
  },
  {
    "Feature": "211",
    "Value": "Basis State"
  },
  {
    "Feature": "212",
    "Value": "Basis State"
  },
  {
    "Feature": "213",
    "Value": "Basis State"
  },
  {
    "Feature": "214",
    "Value": "Basis State"
  },
  {
    "Feature": "215",
    "Value": "Basis State"
  },
  {
    "Feature": "216",
    "Value": "Basis State"
  },
  {
    "Feature": "217",
    "Value": "Basis State"
  },
  {
    "Feature": "218",
    "Value": "Basis State"
  },
  {
    "Feature": "219",
    "Value": "Basis State"
  },
  {
    "Feature": "220",
    "Value": "Basis State"
  },
  {
    "Feature": "221"
  }
]

---

### 5.2 Hauptfunktion Fahren des Fahrzeugs

[
  {
    "Störungs-kategorie": "Kategorie A",
    "Aussetzen des Zuges": "Zug liegengeblieben/stillgesetzt auf freier Strecke",
    "Einsatz mobilen Betriebspersonals": "Entsendung auf freie Strecke",
    "Auswirkungen auf die Fahrgäste": "gegebenenfalls Evakuierung von freier Strecke einleiten",
    "Werkstattzuführung": "kurzfristiges Bergen des Zuges von freier Strecke"
  },
  {
    "Störungs-kategorie": "Kategorie B",
    "Aussetzen des Zuges": "sofort an geeignetem Ort",
    "Einsatz mobilen Betriebspersonals": "Entsendung zum Aussetzort",
    "Auswirkungen auf die Fahrgäste": "Information über vorzeitigen Ausstieg am Aussetzort",
    "Werkstattzuführung": "Überführung bei nächster Gelegenheit (spätestens am Ende des Betriebstages)"
  },
  {
    "Störungs-kategorie": "Kategorie C",
    "Aussetzen des Zuges": "Aussetzen am geplanten Zielort",
    "Einsatz mobilen Betriebspersonals": "Entsendung zum Aussetzort",
    "Auswirkungen auf die Fahrgäste": "Keine Auswirkungen",
    "Werkstattzuführung": "Überführung bei nächster Gelegenheit (spätestens am Ende des Betriebstages)"
  },
  {
    "Störungs-kategorie": "Kategorie D",
    "Aussetzen des Zuges": "nicht erforderlich",
    "Einsatz mobilen Betriebspersonals": "nicht erforderlich",
    "Auswirkungen auf die Fahrgäste": "Keine Auswirkungen",
    "Werkstattzuführung": "Überführung bei ohneh in anstehender Wartung"
  }
]

---

### 5.6 Hauptfunktion Störfallerkennung und Störfallmanagement

Insbesondere, wenn sich für den Betrieb kein Fahrzeugführer mehr an Bord der Fahrzeuge befindet, müssen Störfälle automatisch erkannt werden. Hierbei gibt Störfälle, die durch fahrzeugseitige oder infrastrukturseitige technische Systeme automatisch erkannt werden. Es erfolgt in diesem Fall eine unverzügliche automatische Meldung des Störfalls an die Leitstelle und die Umsetzung einer sicherheitsgerichteten Reaktion des Automatisierungssystems im Betrieb. Beispiele hierfür sind die Aktivierung infrastruktur- oder fahrzeugseitiger fahrgastbezogener Sicherheitssysteme (Abschn. 5.6.1), das Auslösen infrastruktur- oder fahrzeugseitiger Brandmeldesysteme (Abschn. 5.6.2), die Evakuierung von Fahrgästen (Abschn. 5.6.3), das Auslösen der fahrzeugseitigen Hinderniserkennung (Abschn. 5.6.4) oder das Auslösen einer fahrzeugseitigen Entgleisungserkennung (Abschn. 5.6.5). Jeder Störfall erfordert ein manuelles Eingreifen des Betriebspersonals zur Entstörung.

#### 5.6.1 Oberfunktion Fahrgastalarmmeldungen

Störfälle können durch Fahrgäste in den Fahrzeugen oder in Haltestellen erkannt werden. Die Fahrgäste melden die Störfälle durch geeignete technische Einrichtungen wie beispielsweise Einrichtungen für Sprechverbindungen zwischen Fahrgästen in den Haltestellen und der Leitstelle.

## Auswertung fahrzeugseitiger Fahrgastalarmmeldungen

Ein Beispiel hierfür ist die Meldung eines Vorfalls auf einem Fahrzeug über eine Schnittstelle für den Fahrgastalarm. Die Schnittstelle für den Fahrgastalarm unterstützt verschiedene Funktionen (DIN EN 16334-2:2020).

• Möglichkeit der Alarmierung der Betriebsleitstelle für die Fahrgäste im Notfall: Das Fahrgastalarmsystem befindet sich im Fahrgastbereich. Wird ein Fahrgastalarmgriff betätigt, muss er in der aktivierten Position einlasten und sich deutlich sichtbar von der unbetätigten Normalstellung unterscheiden. Zusätzlich sollte der Fahrgast eine Rückmeldung über die Betätigung mittels eines optischen oder akustischen Signals erhalten. Das Betätigen eines Fahrgastalarmgriffs wird dem Betriebspersonal in der Leitstelle angezeigt und von diesem quittiert. Die Leitstelle baut dann eine Sprechverbindung zum Fahrgast auf. An der Schnittstelle für den Fahrgastalarm wird dem Fahrgast eine Rückmeldung angezeigt, wenn die Sprechverbindung in die Leitstelle zustande gekommen ist. Sollte eine Funktionsstörung des Fahrgastalarmsystems erkannt werden, wird dies ebenfalls auf der Leitstelle angezeigt, damit entsprechende Maßnahmen eingeleitet werden können (DIN EN 16334-2).

• Anhalten des Zuges in Übereinstimmung mit den Betriebsvorschriften: Unter bestimmten Betriebsbedingungen (z. B. im Tunnel) kann eine Bremsüberbrückung gefordert sein. Hierbei darf beim Fahren zwischen Bahnhöfen oder an Orten, an denen

---

eine Passagierevakuiierung schwierig ist (Tunnel) das Fahrgastalarmsystem nicht unmittelbar eine Bremsung anfordern. Dies erfordert eine Erkennung des Bahnsteigbereichsendes. Der Bereich des unmittelbaren Bremsens am Bahnsteig liegt zwischen dem Abfahrtsort des Zuges und dem Zugschluss des Zuges, der den Bahnsteig verlässst. Dies kann entweder durch Einbindung in ein Signalsystem erkannt werden (physische Erkennung) oder durch Auswertung der Deaktivierung der Türfreigabe und einer vom Fahrzeug zurückgelegten Distanz erfolgen (nicht-physische Erkennung).

- Erteilen einer Erlaubnis an den Zug je nach Bedingung weiterzufahren und an einem sicheren Ort zu halten: Das Fahrgastalarmsystem darf nur durch autorisiertes Personal in der Leitstelle zurückgesetzt werden. Dies darf nur dann aus der Leitstelle heraus passieren, wenn ein CCTV (Closed Circuit Television) auf den Fahrzeugen eingesetzt wird. Da Fahrzeuge mehrere Fahrgastalarmgriffe haben, werden über die Fahrzeugsteuerung Informationen zur Lokalisierung des betätigten Fahrgastalarmgriffs im Zugverband bereitgestellt. Wenn ein CCTV verfügbar ist, darf das Fahrgastalarmsystem Informationen an das CCTV geben, um aufzuzeigen, an welchem Ort ein Fahrgastalarmgriff betätigt wurde, um die vorrangige Überwachung des betreffenden Bereiches zu ermöglichen. Nachdem das Fahrgastalarmsystem zurückgesetzt wurde, kann der Zug seine Fahrt bis zu einem sicheren Ort fortsetzen.

Über verschiedene Wege eingehende Störfallmeldungen werden auf einer Leitstelle angezeigt. Das Leitstellenpersonal kann von dort die angemessene sicherheitsgerichtete Reaktion anstoßen und eine geordnete Rückkehr in den Regelbetrieb koordinieren (beispielsweise die Evakuierung von Fahrgästen, vgl. Abschn. 5.6.2). Abb. 5.20 zeigt ein Beispiel der Bedienung und Anzeige für fahrzeugseitige Einrichtungen auf der Leitstelle eines unbegleiteten fahrerlosen Systems.

## Auswertung infrastrukturseitiger Fahrgastalarmmeldungen

Auch infrastrukturseitige Alarme werden ausgewertet, dem Bediener auf dem Bedienplatz angezeigt (vgl. Abb. 5.21) und führen zu Systemreaktionen des Automatisierungssystems zur sicheren Seite. Diese Systemreaktionen erfordern ebenfalls die Mitwirkung von Betriebs- personal zur Behebung der Störung. Dies gilt für exemplarisch für die folgenden Beispiele:

- Auslösen der Bahnsteiggleisüberwachung: Das Eindringen von Personen in den vom Bahnsteig aus erreichbaren Gleisbereich muss technisch erkannt werden. Dies führt zu einer sicherheitsgerichteten Reaktion des Automatisierungssystems. Dieser Sachverhalt ist in Abb. 5.21 exemplarisch dargestellt. Über zähl- und protokollpflichte Bedienhandlung werden. Zur Steigerung der Verfügbarkeit bei Störungen kann ebenfalls über eine zähl- und protokollpflichtige Bedienhandlung der Leitstelle die Bahnsteiggleisüberwachung zurückgesetzt werden. Voraussetzung hierfür ist, dass ein wirksamer Gefährdungsausschluss durch eine ständige Fernbeobachtung des betreffenden Gleisbereichs aus der Leitstelle gegeben ist oder durch Betriebspersonal vor Ort gegeben ist und das Betriebspersonal den Fahrbetrieb im Bedarfsfall stillsetzen kann (VDV 2000).

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6951e45b-82ed-4352-ab89-a31ba79e08b1/markdown_0/imgs/img_in_image_box_91_90_888_721.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A31%3A49Z%2F-1%2F%2Fb5e0da3f2ce59a2fd95eb9a5c3e750133ab5be71558f3919f9bd2bbe97b6d5c2" alt="Image" width="83%" /></div>


<div style="text-align: center;">Abb. 5.20 Fahrzeuglupe zur Anzeige von Systemzuständen der Fahrzeuge und zur Störfall- behandlung. (Quelle: VAG Nürnberg; Siemens Mobility GmbH)</div>


- Auslösen des Nothaltschalters in der Station: Der Nothaltschalter ist Teil des fahrgastbezogenen Sicherheitssystems in Haltestellen zum Stillsetzen des Fahrgastbetriebs im Notfall. Die konkrete Reaktion des Automatisierungssystems umfasst neben einer Auslösung einer Notbremsung des in die Station einfahrenden Fahrzeugs auch die Abschaltung des Traktionsstroms im Ereignisfall. Für die Umsetzung der Schutzmaßnahmen ist im jeweiligen Einzelfall die konkrete Stationstopologie zu berücksichtigen. Weist die Station einen mittig liegenden Bahnsteig mit zwei außen liegenden Stationsleisen auf, kann die automatische Zwangsreaktion für jedes Stationsgleis einzeln erfolgen. Weist die Station jedoch außen liegende Bahnsteige mit zwei innen liegenden Stationsgleisen auf, muss die automatische Zwangsreaktion (Abschaltung des Traktionsstroms) für beide Stationsgleise erfolgen, da ein Übertreten von einem auf das andere Richtungsgleis möglich ist. Die Umsetzung der konkreten Projektierung ist also abhängig von der jeweiligen Stationstopologie. Der Nothaltschalter dient vornehmlich zum Abdecken von Gefahrenmomenten aus dem Fahrgastbetrieb im Bereich der Bahnsteigkante. Auch hier kann über eine zähl- und protokollpflichte Bedienhandlung die Meldung Nothalt zurückgesetzt werden. Ebenso kann über eine zähl- und proto-

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//46a3acca-66c5-42fd-bebd-fbfbe1318428/markdown_0/imgs/img_in_image_box_78_64_872_602.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A31%3A52Z%2F-1%2F%2Fe0d8e0afe558a1bc60fefb7c03980518f88698f1fe16d4f7d94701d7d07ecd23" alt="Image" width="83%" /></div>


<div style="text-align: center;">Abb. 5.21 Ausschnitt des Bedien- und Anzeigesystems der fahrerlosen U-Bahn in Nürnberg zur Darstellung der Elementzustände des Bahnsteigsicherungssystems. (Quelle: VAG Nürnberg; Siemens Mobility GmbH)</div>


kollpflichte Bedienhandlung der Nothalt zurückgesetzt werden. Es gelten die gleichen Voraussetzungen wie bei der zuvor dargestellten Deaktivierung der der Bahnsteiggleisüberwachung (VDV 2000).

• Auslösen der Eindringüberwachung: Das Eindringen von Personen in den benachbarten Gleisbereich von Stationen muss technisch erkannt werden. Dies ist in Abb. 5.21 exemplarisch dargestellt. Über eine zähl- und protokollpflichte Bedienhandlung kann die Meldung der Eindringüberwachung zurückgesetzt und ebenso deaktiviert werden. Eine Fortführung des Betriebs bei deaktivierter Eindringüberwachung ist nur dann möglich, wenn eine Fernbeobachtung des Eindringortes durch einen Betriebsbediensteten möglich ist und dieser den Fahrgastbetrieb im angrenzenden Streckenbereich stillsetzen kann. Alternativ kann der Fahrerstand mit einem Betriebsbediensteten zum Zwecke der Streckenbeobachtung besetzt werden (VDV 2000).

#### 5.6.2 Oberfunktion Brandmeldung

Brände können durch Überhitzung und Kurzschlüsse in technischen Bereichen sowie durch Vandalismus oder Verstöße gegen Rauchverbote entstehen. Um frühzeitig eine durch Brand bzw. Rauch ausgehende Gefährdung der Fahrgäste zu verhindern, werden

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7a1f0e7c-cc1f-41b2-8e59-a9058b036e5b/markdown_0/imgs/img_in_image_box_82_93_874_329.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A31%3A56Z%2F-1%2F%2Ff5c40ecaabcdb078e599850eda942bce65751ccbc0707320008b8e877ae5ab24" alt="Image" width="83%" /></div>


<div style="text-align: center;">Abb. 5.22 Installation von Wassernebellöschanlagen auf Schienenfahrzeugen</div>


daher sowohl Infrastruktur als auch Fahrzeuge mit einer Brandmeldeanlage ausgestattet (vgl. Abb. 5.22 links für einen Sensor im Fahrzeuginnern). Hierbei kommen Sensoren mit verschiedenen Detektionsverfahren zum Einsatz, die auch miteinander kombiniert werden können:

- Fotoelektrisches Detektionsverfahren: Dieses Detektionsverfahren ist geeignet, eine Rauchentwicklung zu erkennen. Zentrales Element dieses Detektionsverfahrens ist eine Lichtquelle (Infrarot- oder Laserstrahl) und eine Fotolinse als Sensor. Solange kein Rauch in die Kammer des Rauchmelders eindringt, wird der Lichtstrahl nicht gestört bzw. unterbrochen und trifft auf die Fotolinse. Dringen jedoch Rauchpartikel in die Rauchkammer des Melders ein, wird der Lichtstrahl durch die Rauchpartikel unterbrochen. Daraufhin bricht die Verbindung zum Fotosensor ab und der Alarm wird aktiviert.

• Thermisches Detektionsverfahren: Dieses Detektionsverfahren ist geeignet, von einer Temperaturentwicklung auf ein Brandereignis zu schließen. Nach diesem Detektionsverfahren arbeitende Sensoren erfassen die Umgebungstemperatur via Heißleiter. Heißleiter bestehen aus elektrisch leitendem Material, das bei hohen Temperaturen besser Strom leitet als bei niedrigen. Steigt also die Umgebungstemperatur schnell genug an, erwärmt sich auch der Heißleiter und es kommt zu Veränderungen in seiner Stromleitungsfähigkeit. Wird bei einer solchen Messung eine schnell ansteigende Temperatur festgestellt, löst ein Wärmemelder Alarm aus. Ebenso wird Alarm ausgelöst, sobald eine vorher konfigurierte Umgebungstemperatur überschritten wird.

Bei unterirdischen Verkehrsanlagen besteht die Gefahr einer extrem schnellen Brandausbreitung. Daher kommen auf den Schienenfahrzeugen zusätzlich zu den Sensoren auch Löschsysteme zum Einsatz. So kommt im Fahrgastraum von Zügen beispielsweise eine Wassernebellöschtechnik zum Einsatz (vgl. Abb. 5.22 in der Mitte). Diese Brandbekämpfungs-anlagen verwenden Wasser als Löschmittel, das aus Düsen in feinsten Tropfen versprüht wird. Die Verwendung von Wassernebellöschanlagen bietet die folgenden Vorteile:

• Stickeffekt: Der Wassernebel verdrängt beim Auftreffen auf die Flammen und durch die aus der unmittelbare Verdampfung resultierende Volumenvergrößerung des Wassernebels die Luft und damit den 21%igen Sauerstoffanteil vom Brandherd.

---

• Wärmebindung: Der Wassernebel erzeugt eine maximale Wärmebindung durch die sehr große Tröpfchenoberfläche. Dies führt beispielsweise zu einer Absenkung der Umgebungstemperatur von 1000 unter 40 °C.

• effektive Rauchpartikelbindung: Als zusätzlicher Nebeneffekt werden durch die Feinstropfen die entstehenden Rauchgase gebunden. Hierdurch wird die Sichtweite in den angrenzenden Bereichen stark erhöht und möglicherweise ein Fluchtweg sicher geschützt.

• geringerer Wasserverbrauch: Wasserbellöschanlagen benötigen im Vergleich zu konventionellen Sprinkleranlagen eine deutlich kleinere Wassermenge (20 % der Wassermenge eines konventionellen Sprinklers). Diese geringeren Wassermengen erzeugen deutlich geringere Wasserschäden.

Die Installation der Tanks für die Wasserversorgung erfolgt platzsparend in existierenden Leerräumen (bspw. unter Sitzen, vgl. Abb. 5.22 auf der rechten Seite). Die Auslösung des Löschsystems kann über eine Kommunikationsleitung erfolgen (bspw. Train Control and Monitoring System, TCMS) erfolgen oder alternativ bei einer definierten Temperatur automatisch auslösen. Der Einbau der Tanks für die Wasserversorgung erfolgt in vorhandenen Leerräumen in der Fahrzeugkonstruktion (beispielsweise unter Sitzen).

## Systemreaktion bei Ansprechen fahrzeugseitiger Brandmeldeanlagen

Brandmeldeanlagen sind in verschiedenen Komponenten des Fahrzeugs sowie im Fahrgastraum vorgesehen und direkt mit der Fahrzeugsteuerung verbunden. Bei Ansprechen des fahrzeugseitigen Brandmeldesystems erfolgt eine ortsselektive Meldung an die Leitstelle und wird in der Fahrzeuglupe (Abb. 5.20) angezeigt. Durch den Einsatz spezieller funktionserhaltender Kabel im Fahrzeug wird erreicht, dass im Falle eines sich entwickelnden Brandes die Mindestfunktionen des Fahrzeugs aufrecht erhalten bleiben. Das Fahrzeug kann auf diese Weise sicher die nächste Haltestelle erreichen, sodass dort eine Evakuierung erfolgen kann (Müller und Schmidt 2003). Die Fahrgastraumtüren werden auf der vorgegebenen Seite durch eine Bedienhandlung auf der Fahrzeuglupe (Abb. 5.20) freigegeben. Die Türen können dann von den Fahrgästen geöffnet werden.

## Systemreaktion bei Ansprechen infrastrukturseitiger Brandmeldeanlagen

Neben der Auswertung fahrzeugseitiger Brandmeldungen müssen auch Brandmeldungen infrastrukturseitiger Einrichtungen ausgewertet werden. Darüber hinaus werden sicherheitsgerichtete Reaktionen angestoßen:

• Bei erkanntem Rauch in einer Haltstelle werden Züge, die sich in Annäherung befinden, die Haltestelle ohne Halt durchfahren. Züge, die sich in der vorhergehenden Haltestelle befinden, werden durch Unterbindung der Abfertigung von der Annäherung auf die Haltestelle zurückgehalten. Züge, die in Annäherung auf die vorhergehende Haltestelle sind, werden angehalten.

---

• Bei erkanntem Rauch zwischen zwei Haltestellen werden Züge, die sich im betreffenden Streckenbereich befinden, weiterfahren, sofern keine Fahrtrestriktionen bestehen. Auch hier werden Züge in der vorhergehenden Haltestelle an der Ausfahrt gehindert, bzw. in Anfahrt auf die vorhergehende Haltestelle befindliche Züge angehalten.

#### 5.6.3 Oberfunktion Evakuierung

Liegt eine kritische Betriebssituation vor, ist die Idealvorstellung das gezielte Stillsetzen des Fahrbetriebs. Ist dies nicht möglich, sind die Fahrgäste aus den Tunnelbereichen zu evakuieren, wobei zwischen Selbstrettung und Fremdrettung unterscheiden wird. Eine Evakuierung kann auch als Kombination aus Selbst- und Fremdrettung umgesetzt werden. Eine große Rolle spielt in allen drei Fällen die situationsangemessene Information der Fahrgäste. Hierfür muss es möglich sein, die Fahrgäste über die eingetretene Störung zu informieren und sie über die erforderlichen Maßnahmen (gezieltes Stillsetzen des Fahrbetriebs, Selbst- und Fremdrettung) zu informieren.

## Gezieltes Stillsetzen des Fahrbetriebs

Bei einem gezielten Stillsetzen des Fahrbetriebs fahren die Züge nach Eintritt des kritischen Ereignisses noch bis zur nächsten Haltestelle, um die Fahrgäste aus dem Fahrzeug zu entlassen. Es soll nach Möglichkeit verhindert werden, dass Fahrzeuge im Tunnel zum Stillstand kommen. So wird verhindert, dass die Fahrgäste nicht beunruhigt sind, eine Notfalltüröffnung anfordern und auf diese Weise die betrieblichen Herausforderungen in dieser Störungssituation noch weiter verschlimmern. Möglicherweise erfordert die Umsetzung dieser Strategie weitere Einrichtungen auf dem Fahrzeug. Ein Beispiel für die zur Umsetzung eines Havariekonzepts zusätzliche Einrichtungen auf dem Fahrzeug sind Batterien zur Speicherung von Traktionsenergie. Hierdurch kann im Falle von Ausfällen der Traktionsstromversorgung das Fahrzeug noch bis zur nächsten Haltestelle fahren, mindestens jedoch zum nächsten Notausgang zur Vereinfachung der Selbstrettung (siehe nächster Abschnitt).

## Unterstützung der Selbstrettung von Fahrgästen

Selbstrettung ist die Fähigkeit zum richtigen Umgang mit Situationen, die das eigene Leben bedrohen. Der Betroffene ist zur Abwendung der Lebensbedrohung für sich selbst in der Lage, eine solche Situation zu erkennen und angemessen darauf zu reagieren. Bei der Selbstrettung ist zu berücksichtigen, dass aufgrund des eingetretenen Notfalls nicht bis zur Fremdrettung gewartet werden kann. Es muss daher auch eine Türnotöffnung aus dem Innern des Fahrzeugs auch bei Ausfall der Stromversorgung der Türsteuerung möglich sein. Allerdings gelten für die Notöffnung einer Tür besondere Sicherheitsanforderungen:

• Vermeidung versehentlicher und missbräuchlicher Türöffnungen: Um Unfälle beim versehentlichen oder missbräuchlichen Notöffnen von Türen zu verhindern, dürfen die

---

Fahrzeugtüren nicht selbsttätig öffnen. Es sollte daher bei der Gestaltung der Fahrzeugtüren das Prinzip der zwei Handlungen angewendet werden. Dies ist zum Beispiel dann der Fall, wenn mit der ersten Handlung die Türnotöffnung von den Fahrgästen im Fahrzeug betätigt wird. Mit der zweiten Handlung kann dann die Tür von den Fahrgästen von Hand aufgeschoben werden (VDV 2017).

• Automatische Aktivierung von Schutzmaßnahmen: Eine automatische Einrichtung einer Befahrbarkeitssperre für in der Gegenrichtung verkehrende oder folgende Züge kann erforderlich werden, um zu verhindern, dass vor einem Notfall flüchtende Fahrgäste mit anderen Zügen kollidieren. Diese Befahrbarkeitssperre kann beispielsweise automatisch gesetzt werden, wenn bei einem Zug eine unerwartete Türöffnung außerhalb einer Station erkannt wird. Gleiches gilt für die Fahrspannungsabschaltung (VDV 2000).

- Eine Freigabe der Tür-Notentriegelung ist beispielsweise für die Evakuierung relevant. Sobald sich der Zug in Bewegung setzt, wird die Tür-Notentriegelung gesperrt, da in diesem Fall bei Öffnung der Tür die Sicherheit der Fahrgäste nicht ausreichend sichergestellt ist (VDV 2017). Bleibt der Zug im Tunnel störungsbedingt stehen, so bleibt die Tür-Notentriegelung so lange gesperrt, bis entsprechende Sicherheitsmaßnahmen wie Anhalten des Gegenverkehrs, Stromschiene spannungslos schalten und Einschalten der Tunnelbeleuchtung eingeleitet werden konnten. Erst dann wird die Türnotentriegelung mit einer Bedienung auf der Fahrzeuglupe freigegeben (Abb. 5.19) und den Fahrgästen ein gefahrloses Verlassen des Zuges ermöglicht (Müller und Schmidt 2003).

## Unterstützung der Fremdrettung von Fahrgästen

Als Fremdrettung wird die Befähigung zum richtigen Umgang mit lebensbedrohenden Situationen anderer bezeichnet. Hierbei werden die Rettenden befähigt, solche Situationen zu erkennen, zu beurteilen und situationsbezogen zu reagieren. Die Rettenden sind in der Lage, ohne Eigengefährdung anderen Personen Hilfe zu leisten. Das Ziel der Fremdrettung besteht darin, den Betroffenen aus der lebensbedrohenden Situation herauszuhelfen. Bei Verkehrsbetreibern sind an der Fremdrettung nicht nur unterschiedliche Stellen im Unternehmen zu beteiligen, sondern auch Abstimmungen mit Behörden und Organisationen mit Sicherheitsaufgaben (BOS) zu treffen. Grundsätzlich können verschiedene Ansätze der Fremdrettung unterschieden werden, die durch eine entsprechende Gestaltung technischer und organisatorischer Maßnahmen unterstützt werden müssen:

• Notfalltüröffnung der Fahrzeugtür von außen: Fahrzeugseitig ist sicherzustellen, dass es den Betriebsbediensteten, bzw. dem Rettungsdienst möglich ist, das Fahrzeug von außen ohne den Einsatz spezieller Werkzeuge zu betreten. Eine Notfalltüröffnung von außen muss also möglich sein. Die Zugsicherungsanlage ist hierbei nicht beteiligt.

• Ferngesteuerter Betrieb des Fahrzeugs aus der Leitstelle: Um ein besetztes Fahrzeug im Falle einer Störung aus dem Tunnel zu fahren, kann von den Betreibern auch ein ferngesteuerter Betrieb vorgesehen werden. Hierbei fährt Leitstellenpersonal das Fahrzeug fernbedient aus der Leitstelle aus dem Gefahrenbereich. Hierzu können fahrzeug

---

Abb. 5.23 Kamera am Fahrzeug zur Fernsteuerung aus der Leitstelle (Beispiel: Fahrzeug vom Typ X für die fahrerlose Linie U5 der Wiener Linien)

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//fce09749-da1b-441b-aa2d-b13f5ba11166/markdown_0/imgs/img_in_image_box_444_80_936_675.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A32%3A11Z%2F-1%2F%2F50a3ce6c499c5dbc55d7eb9d1c4809070b3e1628919ab9d2e452b11a1d57314e" alt="Image" width="51%" /></div>


seitig Kameras vorgesehen werden, über welche der vor dem Fahrzeug liegende Streckenbereich von der Leitstelle aus eingesehen werden kann (vgl. Abb. 5.23).

Einsatz eines Rettungszuges: Für den Fall eines betriebsverhindernden Ausfalls eines fahrerlosen Zuges können Rettungszüge zur Bergung des havarierten Zuges zum Einsatz kommen. Der Bediener der Leitstelle kommuniziert über eine Sprechverbindung mit den Fahrgästen im Fahrzeug und analysiert den Status des havarierten Zuges aus der Ferne. Abhängig von der konkreten Situation bzw. der betrieblichen Gepflogenheiten des Betreibers können verschiedene Strategien zum Bergen der Fahrgäste zum Einsatz kommen. Die erste Möglichkeit ist, dass der Rettungszug von hinten möglichst dicht an den liegengebliebenen Zug heranfährt und zum Stillstand kommt. Die Fahrgäste wechseln dann in das zweite Fahrzeug, welches die Fahrgäste in die nächstgelegene Station bringt. Die zweite Möglichkeit ist, dass der Rettungszug auf dem Gegengleis auf Höhe des liegengebliebenen Zuges zum Stillstand kommt. Beide Züge öffnen die Türen und es werden Rettungsstege zwischen den Zügen ausgelegt, über welche die Fahrgäste in den anderen Zug übersteigen können. Anschließend bringt der Rettungszug die Fahrgäste zur nächstgelegenen Station. Die dritte Möglichkeit ist, den liegengebliebenen Zug wegzuschieben. Dies ist ggf. aber nicht mit besetzten Fahrzeugen zulässig. In diesem Fall lässt der Bediener der Leitstelle alle Fahrgäste des (dem vorausfahrenden liegengebliebenen Fahrzeug folgenden) Rettungszuges an einer Station aussteigen. Er erteilt dem Rettungszug ein Kommando, sich dem havarierten Zug

---

zu nähern. Anschließend wird eine automatische fahrerlose Kupplung des Rettungszuges mit dem havarierten Zug durchgeführt. Hierfür erhält der Rettungszug eine Erlaubnis zur Annäherung an den havarierten Zug mit niedriger Geschwindigkeit. Der Rettungszug kuppelt mechanisch mit dem havarierten Zug und bildet mit diesem einen Zugverband. Anschließend erfolgt eine Neukonfiguration des gebildeten Zugverbandes (beispielsweise neue Zuglänge). Anschließend schiebt, bzw. zieht der Rettungszug den havarierten Zug. Der Zugverband kommt in der nächsten Station an einer Position zum Stillstand, die ein sicheres Aussteigen der Fahrgäste ermöglicht. Hierbei wird die Position etwaig vorhandener Bahnsteigtüren mit berücksichtigt.

#### 5.6.4 Oberfunktion Hinderniserkennung

Für den automatischen Betrieb kann jeweils am führenden Drehgestell ein aktiver Bahnräumer vorgesehen werden, der durch Hindernisse im Gleisbereich ausgelöst wird. Sollte ein Gegenstand auf diesen Bahnräumer treffen, erkennen Endlagenschalter den Druck auf den Bahnräumer und lösen eine nicht aufhebbare Bremsung bis zum Stillstand aus (May et al. 2012). Es wird in diesem Fall eine Meldung auf der Fahrzeuglupe (Abb. 5.20) in der besetzten Leitstelle angezeigt, sodass von dort weitere betriebliche Maßnahmen veranlasst werden können (VDV 1997). Mobiles Betriebspersonal stellt durch eine Sichtkontrolle sicher, dass die die Hinderniserkennung auslösende Bedingung nicht mehr vorliegt. In diesem Fall kann das Leitstellenpersonal über eine registrierpflichtige Bedienhandlung die ausgelöste Hinderniserkennung zurücksetzen. Anschließend kann das Fahrzeug die Fahrt fortsetzen. Ein Beispiel eines aktiven Bahnräumers ist in Abb. 5.24 dargestellt.

Abb. 5.24 Aktiver Bahnräumer zur Hinderniserkennung am führenden Drehgestell (Beispiel: Fahrzeug vom Typ X für die fahrerlose Linie U5 der Wiener Linien)

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//4d3a65b6-9fe0-465e-be9b-44f2dd7d6e4d/markdown_0/imgs/img_in_image_box_389_889_877_1256.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A32%3A15Z%2F-1%2F%2F33591af25d12f0d4e9c1589887c1233576b3794bee567738b394cb6b41a12a6c" alt="Image" width="51%" /></div>

---

<div style="text-align: center;">Abb. 5.25 Beschleunigungssensor am führenden Fahrwerk zur Entgleisungserkennung (Beispiel: Fahrzeug vom Typ X für die fahrerlose Linie U5 der Wiener Linien)</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5403775c-c208-4776-97e5-b080654d7ce6/markdown_0/imgs/img_in_image_box_380_81_873_456.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A32%3A19Z%2F-1%2F%2F411a4bcfff042c88c8d1b191251b3f6301e9785364898fa152cca6dce0730cb4" alt="Image" width="51%" /></div>


#### 5.6.5 Oberfunktion Entgleisungserkennung

Es müssen auf dem Fahrzeug Einrichtungen vorhanden sein, die mindestens das führende Fahrwerk auf Entgleisung überwachen können (Müller und Schmidt 2003). Technisch kann dies beispielsweise über Beschleunigungssensoren an den Achsen erkannt werden. Die Beschleunigungssensoren erkennen, wenn ein Räderpaar nicht mehr auf der Schiene aufsitzt. Wird eine Entgleisung erkannt, muss eine Bremsung des Fahrzeugs bis zum Stillstand erfolgen. Darüber hinaus muss die Entgleisung der besetzten Betriebsstelle gemeldet und auf der Fahrzeuglupe (Abb. 5.19) als Notfallmeldung angezeigt werden (VDV 1997). Das Personal der Betriebsleitstelle ergreift dann erforderliche betriebliche Maßnahmen wie bspw. Anhalten des Gegenverkehrs (DIN EN 62267:2010). Mobiles Betriebspersonal führt eine Sichtkontrolle am Fahrzeug durch und entscheidet vor Ort über das weitere Vorgehen. Im Falle einer fehlerhaft ausgelösten Entgleisungsmeldung wird das Leitstellen- personal informiert, welches über eine registrierpflichtige Bedienhandlung auf der Fahrzeuglupe (Abb. 5.19) die ausgelöste Entgleisungserkennung zurücksetzt. Anschließend kann das Fahrzeug die Fahrt fortsetzen. Ein Beispiel eines am führenden Fahrwerk angebrachten Beschleunigungssensors zur Entgleisungserkennung ist in Abb. 5.25 dargestellt.

## Literatur

Brückner N, Isailovski A (2010) CrCo – Ein Algorithmus zum Einsparen von Fahrenergie. Signal + Draht 102:43–46

DIN EN 16334-2:2020 Bahnanwendungen – Fahrgastalarmsystem – Teil 2: Systemanforderungen für städtische Schienenbahnen. Deutsche Fassung EN 16334-2:2020

DIN EN 62267:2010 Bahnanwendungen – Automatischer städtischer schienengebundener Personennahverkehr (AUGT) – Sicherheitsanforderungen. Deutsche Fassung EN 62267:2009

---

Dombrowsky H, Müller R, May A, Seitzinger E (2008) Premiere für Deutschlands erste automatisierte U-Bahn. Nahnverkehr 26(5):8–16

Eichner D, Uhrig B (2021) Innovationen in CBTC-Anwendungen. Signal + Draht 113:34–44. EN17168:2021-09: Platform barrier systems

Haspel U, vom Hövel R (2001) Risikobeherrschung nach CENELEC bei der fahrerlosen Metro Kopenhagen. Eisenbahntechn Rundsch 50(7/8):418–426

IEEE 1474.1-2004 – IEEE standard for Communications-Based Train Control (CBTC) performance and functional requirements

Krins ST, Rudall Y, Ruiter T (2016) Ein autarkes System zur Steuerung von Bahnsteigtüren. Signal + Draht 108(11):16–21

Kuhlmeyer T (2020) Technische Abfertigungshilfen. Eisenbahningenieur 07/2020, S 46–50

Maschek U (2018) Sicherung des Schienenverkehrs – Grundlagen und Planung der Leit- und Sicherungstechnik. Springer Vieweg, Wiesbaden

May A, Luber T, Meier-Alt B (2012) Aktuelle Entwicklungen im Nürnberger U-Bahn-System. Eisenbahntechn Rundsch 61(1+2):40–4

Mühleck K-H, et al (2022) Betriebliche Aufgaben im Zugbegleitdienst: Fachwissen für Zugbegleiter und Kundenbetreuer – Teil 3. Deine Bahn 10/2022, S 28–35

Müller R, Schmidt K (2003) Eine automatische U-Bahn für Nürnberg – Technische Besonderheiten der AGT-Fahrzeuge für Nürnberg. Eisenbahntech Rundsch 52(11):679–685

Ortloff A, Aust F (2016) Controlguide OCS – Sicherung von Baustellen im Gleisbereich mit mobilen Geräten. Signal + Draht 108:39–49

Pachl J (2016) Systemtechnik des Schienenverkehrs – Bahnbetrieb planen, steuern und sichern. Springer Vieweg, Wiesbaden

Rahn K (2011) Green Mobility – Effiziente Zugbeeinflussung mit CBTC-Systemen. Signal + Draft 103(10):26–29

Ritter N (2014) Signal- und Zugsicherungsanlagen für Nahverkehrsbahnen. Signal + Draht 106(11):15–25

TR Bremse (2008) Technische Regeln für die Bemessung und Prüfung der Bremsen von Fahrzeugen nach der Verordnung über den Bau und Betrieb der Straßenbahnen. Ausgabe: Dezember 2008

Verband Deutscher Verkehrsunternehmen (1997) BOStrab-Richtlinien für den Fahrbetrieb ohne Fahrzeugführer (FoF), Entwurf, Januar 1997

Verband Deutscher Verkehrsunternehmen (2000) VDV-Schrift 399. Anforderungen an Einrichtungen zur Gewährleistung der Fahrgastsicherheit in Haltestellen bei Fahrbetrieb ohne Fahrzeugführer

Verband Deutscher Verkehrsunternehmen (2014) VDV-Schrift 336-2. Funktionale Anforderungen für Signal- und Zugsicherungsanlagen sowie Betriebsleitsysteme des städtischen schienengebundenen Personennahverkehrs. Teil 2. Zugsicherungsanlagen. VDV, Köln

Verband Deutscher Verkehrsunternehmen (2017) VDV-Schrift 157: Anforderungen an den Einklemm- und Verletzungsschutz sowie an Notöffnungseinrichtungen an Türen von Personenfahrzeugen nach BOStrab. VDV, Köln

---

# Verlässlichkeit automatischer Zugbeeinflussungssysteme

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//11392835-13ee-4a86-8c4b-427bb0dc0928/markdown_0/imgs/img_in_image_box_905_114_952_182.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A32%3A22Z%2F-1%2F%2Fd44f4c7373223381aad1649a01447c796d21a2f3cd66e984821020379eab3e9a" alt="Image" width="4%" /></div>


## SN Flashcards

Als Käufer*in dieses Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards“ mit Fragen zur Wissensüberprüfung und zum Lernen von Buchinhalten nutzen.

1. Gehen Sie bitte auf https://flashcards.springernature.com/login und

2. erstellen Sie ein Benutzerkonto, indem Sie Ihre Mailadresse angeben und ein Passwort vergeben.





3. Verwenden Sie den folgenden Link, um Zugang zu Ihrem SN Flashcards Set zu erhalten: ▶ https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht funktionieren, senden Sie uns bitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com



Ziel eines Bahnsystems ist die Bereitstellung einer bestimmten Stufe der Ausprägung des Schienenverkehrs, der fahrplangemäß und sicher ist. Neben den eigentlichen funktionalen Anforderungen müssen automatische Zugbeeinflussungssysteme auch nicht-funktionale Anforderungen erfüllen. Die Verlässlichkeit als Systemeigenschaft automatischer Zug- beeinflussungssysteme wird im englischen Sprachgebrauch auch mit der Abkürzung RAMSS bezeichnet. Hierbei stehen die einzelnen Buchstaben für spezifische Aspekte, die in der Systemgestaltung automatisierter Zugbeeinflussungssysteme mit berücksichtigt werden müssen.

---

• Reliability (Zuverlässigkeit),

• Availability (Verfügbarkeit),

• Maintainability (Instandhaltbarkeit),

• Safety (Sicherheit im Sinne eines Schutzes der Umwelt vor Systemversagen).

• Security (Angriffssicherheit, das heißt Sicherheit im Sinne eines Schutzes des Systems vor Störeinflüssen aus der externen Umwelt).

Diese einzelnen Aspekte werden in den folgenden Abschnitten näher beleuchtet.

### 6.1 Sicherheit

Die übergeordnete Zielstellung der Betreiber von Nahverkehrssystemen ist ein sicherer und ordnungsgemäßer Betrieb. Hierbei müssen zwei unterschiedliche Aspekte betrachtet werden. Zum einen geht es um den Schutz der Fahrgäste und der Umwelt vor Systemversagen. Dies ist Gegenstand der funktionalen Sicherheit (englisch: Safety) und wird in Abschn. 6.1.1 dargestellt. Zum anderen geht es aber auch um den Schutz des Systems vor unberechtigten Zugriff Dritter (englisch: Security). Dies ist ebenfalls Gegenstand einer zielgerichteten Systemgestaltung und wird daher in Abschn. 6.1.2 dargestellt. Getreu der Devise „what's not secure is not safe“ bestehen zwischen diesen beiden Sicherheitsaspekten Wechselwirkungen.

#### 6.1.1 Funktionale Sicherheit (Safety)

Sicherheit ist die „Freiheit von unvertretbaren Risiken“. Das Risiko ist hierbei die Kombination aus der Wahrscheinlichkeit, mit der ein Schaden auftritt und dem Ausmaß dieses Schadens. Hierfür hat sich in den hierfür relevanten Normen (DIN EN 50126-1:2018-10; DIN EN 50129:2019-06) ein Verfahren etabliert, welches im Entwicklungsprozess eine klar definierte Schnittstelle zwischen den Betriebsanforderungen des Betreibers einschließlich der Umgebung und dem Sicherungssystem als der technischen Lösung des Herstellers etabliert. Hinsichtlich der Sicherheit wird diese Schnittstelle durch eine Liste von Gefährdungen bestimmt, die zu einem Unfall führen können. Das Ergebnis der Risikoanalysen sind Gefährdungsraten, die mit dem Zugsicherungssystem verbunden sind. Wenn das mit dem Zugsicherungssystem verbundene Risiko geringer als ein vorgegebener Risikogrenzwert ist, dann werden diese Gefährdungsraten tolerierbare Gefährdungsraten (Tolerable Hazard Rate, THR) genannt.

In diesem Zusammenhang sind die Aufgaben des Betreibers die folgenden:

• Festlegung funktionaler Anforderungen für das betreffende System. Die Anforderungen sind zunächst unabhängig von dessen konkreter technischer Ausführung. Hierbei kann auf einschlägige Standards zurückgegriffen werden. So enthält beispielsweise DIN EN

---

62267 auf hoher Betrachtungsebene gehaltene Sicherheitsanforderungen. Diese sind anwendbar auf automatische städtische fahrer- oder begleiterlose Systeme, die auf einem (vom übrigen Verkehr) unabhängigen Bahnkörper verkehren (DIN EN 62267:2010).

• Identifikation systemrelevanter Gefährdungen: Die Gefährdungsidentifikation beinhaltet eine systematische Analyse eines Systems. Diese hat zum Ziel, Gefährdungen, die sich während des Lebenszyklusses eines Systems ergeben können, zu erkennen.

• Analyse der Folge von Gefährdungen: Die Folgenanalyse befasst sich mit der Quantifizierung wahrscheinlicher Konsequenzen, die sich aus einer identifizierten Gefährdung ergeben können.

- Um sicherzustellen, dass das gewählte Risiko tolerierbar ist, können verschiedene Risikoakzeptanzprinzipen zur Anwendung kommen (Anwendung von Regelwerken, Vergleich mit Referenzsystemen oder eine explizite Risikoabschätzung). Nach der Wahl und Anwendung des Risikoakzeptanzprinzips wird der Prozess mit der Risikobeurteilung und der Festlegung von Sicherheitsanforderungen fortgesetzt.

• Ableitung tolerierbarer Gefährdungsraten, beispielsweise mittels einer geeigneten Risikoanalysemethode (Braband 2005).

Der Hersteller ist verpflichtet, eine Gefährdungsbeherrschung zu argumentieren. Dies umfasst die folgenden Aspekte:

• Festlegung der konkreten Systemarchitektur unter Berücksichtigung der tolerierbaren Gefährdungsraten für jede Gefährdung.

• Analyse der Ursachen für jede Gefährdung.

• Verfeinerung der Sicherheitsanforderungen im Sinne einer Zuweisung der Gefährdungsraten und der korrespondierenden Sicherheitsintegritsanforderungen (Sicherheitsintegritätslevel, SIL) auf die betreffenden Teilsysteme.

- Dokumentation eines Sicherheitsnachweises (englisch: Safety Case). Der zentrale Bestandteil des Sicherheitsnachweises ist der Technische Sicherheitsbericht (englisch: Technical Safety Report). Gegenstand des Sicherheitsnachweises ist die Betrachtung des korrekten funktionalen Verhaltens des Systems. Dies bedeutet, dass alle in der Risikoanalyse identifizierten Gefährdungen durch Schutzfunktionen des Zugsicherungssystems auch tatsächlich erfüllt werden. Ebenfalls wird gezeigt, dass Ausfallauswirkungen (Einfach- und Mehrfachausfälle) beherrscht werden, sowie ein sicherer Betrieb bei wirkenden externen Umwelteinflüssen sichergestellt werden kann (vgl. DIN EN 50129:2019-06). In Bezug auf die Kommunikation zwischen Fahrzeug- und Streckeneinrichtungen müssen Gefährdungen durch Wiederholung, Auslassung, Einfügung, Verfälschung, Verzögerung und Manipulation übertragener Informationen beherrscht werden. Hierfür sind technische Maßnahmen zur Absicherung der Ende-zu-Ende-Verbindung in einschlägigen Standards für Bahnanwendungen (vgl. DIN EN 50159:2011-04) vorgegeben.

---

Wegen der großen Bedeutung der Risikoanalyse wird diese nachfolgend vertieft behandelt. Die DIN EN 50126 legt für die Durchführung der Risikoanalyse kein bestimmtes Verfahren fest. Zur Einstufung des Risikos schlägt sie qualitative Kategorien für die Häufigkeit und den Schweregrad vor. Die Risikobewertung muss durch Kombination der Häufigkeit des Eintritts eines Gefahrenfalls mit der Schwere der Konsequenzen erfolgen. Die Risikobewertung soll im Ergebnis eine qualitative Kategorie ermitteln, die der notwendigen Risikominderung entspricht. Aus der notwendigen Risikominderung können dann Sicherheitsintegritätsanforderungen (Sicherheitsintegritätslevel, SIL) abgeleitet werden.

Es besteht eine Vielzahl verschiedener methodischer Ansätze für die Durchführung von Risikoanalysen. Diese können in qualitative Ansätze (beispielsweise Expertenschätzungen), semi-quantitative Ansätze (beispielsweise Risikographen) oder quantitative Ansätze (beispielsweise simulationsbasierte Ansätze) unterschieden werden. Da eine gesamte Darstellung der Bandbreite verschiedener Risikoanalysemethoden den Rahmen dieses Buches sprengen würde, wird im Folgenden exemplarisch auf zwei ausgewählte semi-quantitative Risikoanalysemethode eingegangen. Für eine umfassende Darstellung wird auf weiterführende Fachliteratur verwiesen (Schnieder und Schnieder 2013).

## Ermittlung der Sicherheitsintegritätsanforderung mittels Risikograph

Der Verband Deutscher Verkehrsunternehmen hat in (VDV 2008) einen Vorschlag aus- gearbeitet, wie der Risikograph nach DIN EN 61508-5 für Zugsicherungsanlagen genutzt werden kann. Eine analoge Anwendung des Risikographen zur Ermittlung sicherheitstechnischer Anforderungen für die elektrische Ausrüstung von Schienenfahrzeugen erfolgt in (VDV 2005) und (VDV 2009). Für die Bestimmung der Risikominderung werden insgesamt vier verschiedene Risikoparameter verwendet. Die Auswahl der Risikoparameter sowie die darauf basierende Ableitung des Sicherheitsintegritätslevels (SIL) wird exemplarisch für die Funktion der Überwachung der vorgegebenen Grenzgeschwindigkeit (abhängig von der Streckentopografie, vorübergehenden Langsamfahrstellen, Nothalten oder Zielpunkten) dargestellt. Die Auswirkung beim Fehlerfall dieser Schutzfunktion ist, dass eine Überschreitung der vorgegebenen Grenzgeschwindigkeit nicht erkannt wird und daher keine Zwangsbremsung erfolgt. Dies kann letzten Endes zu einem Zusammenstoß mit anderen Fahrzeugen oder zu einer Entgleisung führen. Die Risikoparameter können für das gewählte Beispiel wie folgt gewählt werden:

• Bestimmung der Auswirkung des Vorfalls C (Consequence) mit den Merkmalsausprägungen von geringen Verletzungen (C1), schweren irreversiblen Verletzungen einer oder mehrerer Personen oder dem Tod einer Person (C2), dem Tod mehrerer Personen (C3) oder dem Tod sehr vieler Personen (C4). Im gewählten Beispiel muss bei einer Entgleisung oder einem Zusammenstoß von Zügen mit maximal mehreren Toten gerechnet werden. Deshalb wird für den Risikoparameter C für das gewählte Beispiel die Ausprägung C3 gewählt.

• Bestimmung der Häufigkeit und Zeit des Aufenthalts im Gefahrenbereich F (Frequency) mit den Merkmalsausprägungen eines seltenen bis öfteren Aufenthalt im gefährlichen

---

Bereich (F1), oder einem häufigen bis dauernden Aufenthalt im gefährlichen Bereich (F2). In dem gewählten Beispiel ist von einem dauerhaften Fahrgastaufenthalt in den Zügen auszugehen. Deshalb wird für den Risikoparameter F die Ausprägung F2 gewählt.

• Bestimmung der Möglichkeit, den gefährlichen Vorfall zu vermeiden P (Probability) mit den Ausprägungen der Möglichkeit unter bestimmten Bedingungen (P1) oder der Unmöglichkeit zur Vermeidung eines gefährlichen Vorfalls (P2). Im gewählten Beispiel besteht keine Möglichkeit zur Vermeidung eines gefährlichen Vorfalls. Deshalb wird für den Parameter P die Ausprägung P2 gewählt.

• Bestimmung der Wahrscheinlichkeit des unerwünschten Ereignisses W mit den Merkmalen einer sehr geringen Wahrscheinlichkeit unerwünschter Ereignisse und nur wenigen unerwünschten Ereignissen (W1), einer geringen Wahrscheinlichkeit unerwünschter Ereignisse und nur wenigen unerwünschten Ereignissen (W2) oder einer relativ hohen Wahrscheinlichkeit, dass unerwünschte Ereignisse auftreten und häufige unerwünschte Ereignisse sind wahrscheinlich (W3). Im gewählten Beispiel ist mit einem unmittelbaren Eintritt der Gefährdung bei einer Geschwindigkeitsüberschreitung des Fahrzeugs zu rechnen. Aus diesem Grund wird für den Risikoparameter W die Ausprägung W3 gewählt.

Abb. 6.1 zeigt, wie die Auswahl der einzelnen Risikoparameter im Risikograph zu einer nachvollziehbaren Ableitung eines Sicherheitsintegritätslevels für die betrachtete Funktion führt (VDV 2008). Demnach ist die betrachtete Funktion mit einem Sicherheitsintegritätslevel SIL 4 auszulegen.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ce957563-5f47-4ea6-bb5e-8f9f6c6576d4/markdown_0/imgs/img_in_image_box_217_785_749_1238.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A32%3A42Z%2F-1%2F%2Fff0a5918ec437391d20c9654a377619615459569cfdc2863b679960cdba4281d" alt="Image" width="55%" /></div>


<div style="text-align: center;">Abb. 6.1 Bestimmung des Sicherheitsintegritätslevels (SIL) nach VDV-Schrift 331</div>

---

## Ermittlung der Sicherheitsintegritätsanforderung mittels Risikomatrix

Ein weiterer semi-quantitativer Ansatz der Risikoanalyse ist die Risikomatrix nach DIN EN 50126-1. Hierfür müssen die beiden Risikokomponenten der Wahrscheinlichkeit oder der Häufigkeit des Auftretens von Ereignissen sowie des Schweregrads des etwaigen Schadens für mögliche betrieblicher Gefährdungen anhand qualitativer Kriterien ermittelt werden. In einem deutschen CBTC-Projekt wurden die qualitativen Kategorien für die Gefährdungsrate  $ \lambda $  (gefährliche Ereignisse pro Stunde) wie folgt definiert:

• häufig: Das Ereignis wird häufig stattfinden (tolerierbare funktionale Ausfallrate  $ \lambda  \lt  10^{-5}/h $ ; anzuwenden ist Sicherheitsintegritätslevel SIL 0)

• wahrscheinlich: Das Ereignis wird voraussichtlich oft auftreten (tolerierbare funktionale Ausfallrate  $ 10^{-6}/h  \lt  \lambda \leq 10^{-5}/h $ ; anzuwenden ist Sicherheitsintegritätslevel SIL 1)

gelegentlich: Das Ereignis wird voraussichtlich mehrere Male auftreten (tolerierbare funktionale Ausfallrate  $ 10^{-7}/h  \lt  \lambda \leq 10^{-6}/h $ ; anzuwenden ist Sicherheitsintegritätslevel SIL 2)

- selten: Es kann davon ausgegangen werden, dass das Ereignis auftreten wird (tolerierbare funktionale Ausfallrate  $ 10^{-8}/h  \lt  \lambda \leq 10^{-7}/h $ ; anzuwenden ist Sicherheitsintegritätslevel SIL 3)

• unwahrscheinlich: Es kann angenommen werden, dass das Ereignis ausnahmsweise auftreten kann (tolerierbare funktionale Ausfallrate  $ 10^{-9}/h  \lt  \lambda \leq 10^{-8}/h $ ; anzuwenden ist Sicherheitsintegritätslevel SIL 4)

sehr unwahrscheinlich: Es kann angenommen werden, dass das Ereignis nicht auftritt (tolerierbare funktionale Ausfallrate  $ \lambda \leq 10^{-9}/h $ ; anzuwenden ist Sicherheitsintegritäts-level SIL 4)

Im gleichen Projekt wurden – geringfügig von der DIN EN 50126-1 abweichend – die folgenden qualitativen Kategorien für das Schadensausmaß verwendet:

- catastrophal: Unfalltote und/oder zahlreiche Schwerverletzte (und/oder schwere Umweltschäden)

• kritisch: einzelner Unfalltoter und/oder Schwerverletzter (und/oder nennenswerte Unfallschäden)

• marginal: kleine Verletzung (und/oder nennenswerte Bedrohung der Umwelt)

• unbedeutend: mögliche geringfügige Verletzung

Die Kategorien des Schadensausmaßes und der Schadensschwere können in einer Matrix miteinander verschränkt werden. Die Kategorien für den Schweregrad sind hierbei in der horizontalen Achse dargestellt. Die Kategorien für die Häufigkeit einer Gefährdung sind in der vertikalen Achse dargestellt. Jedes der Felder der Matrix entspricht einem Risiko als Kombination von Häufigkeit und Schadensschwere. Jedem dieser Risiken kann nun eine Risikoakzeptanzkategorie zugeordnet werden. In dem zuvor geschilderten Projekt wurden nach DIN EN 50126-1 die Risikoakzeptanzkategorien wie folgt gewählt:

---

• untragbar: Das Risiko muss eliminiert werden (rote Farbcodierung in der Risikobewertungsmatrix).

• unerwünscht: Das Risiko darf nur akzeptiert werden, wenn eine Minderung nicht durchführbar ist und die Zustimmung des Betreibers oder der Technischen Aufsichtsbehörde vorliegt (orangefarbene Farbcodierung in der Risikobewertungsmatrix).

• tolerierbar: Das Risiko kann unter der Voraussetzung angemessener Maßnahmen (z. B. Instandhaltungsverfahren und -regeln und mit Zustimmung des Betreibers) toleriert und akzeptiert werden (gelbfarbene Farbcodierung in der Risikobewertungsmatrix).

• vernachlässigbar: Das Risiko ist ohne Zustimmung des Betreibers akzeptabel (grüne Farbcodierung in der Risikobewertungsmatrix).

Die Anwendung der Risikomatrix soll auch hier mit der Funktion der Überwachung der vorgegebenen Grenzgeschwindigkeit verdeutlicht werden. Im Fehlerfall dieser Schutzfunktion überschreitet der Zug die zulässige Geschwindigkeit und das Fahrzeuggerät gibt in diesem Fall fehlerhaft keinen Zwangsbremsbefehl aus. Die Anwendung der Risikomatrix soll die Frage beantworten, mit welcher Sicherheitsintegrität diese Funktion bereitgestellt werden muss.

Die Durchführung der Risikoanalyse beginnt mit einer Bewertung des initialen Risikos (vor risikoreduzierenden Maßnahmen). Hierbei wird die Häufigkeit des Überschreitens des Geschwindigkeitsgrenzwertes als „gelegentlich“ angenommen. Das Schadensausmaß wird hierbei jedoch als „katastrophal“ angenommen, weil mit tödlich verunglückten Fahrgästen gerechnet werden muss. Die Verknüpfung von Häufigkeit und Schadensschwere führt in der Risikobewertungsmatrix zu einem als „untragbar“ bewerteten Risiko. Das Ergebnis der initialen Risikobewertung ist in Abb. 6.2 als dunkelgrau hinterlegter Kreis vermerkt. Für dieses Risiko ist eine Reduktion zwingend erforderlich.

Das Risiko kann reduziert werden, wenn beispielsweise die Häufigkeit des gefährlichen Ereignisses reduziert wird. Dies gelingt beispielsweise, wenn die Funktion mit einer höheren Sicherheitsintegritätsstufe entwickelt wird. Die Annahme ist hierbei, dass bei einem höheren Sicherheitsintegritätslevel durch umfangreichere Maßnahmen im Entwurf und der Implementierung der Schutzfunktion zum einen zufällige Fehler im Betrieb


[
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "Gefahrenstufen"
  },
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "katastrophal"
  },
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "untragbar"
  },
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "untragbar"
  },
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "untragbar"
  },
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "unerwünscht"
  },
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "unerwünscht"
  },
  {
    "Risikobewertungsmatrix nach DIN EN 50126-1": "tolerabel"
  }
]

<div style="text-align: center;">Abb. 6.2 Bestimmung des erforderlichen Sicherheitsintegritätslevels (SIL) nach DIN EN 50126-1</div>

---

sicher beherrscht und zum anderen gefährliche Systemzustände durch mögliche systematische Fehler vermieden werden können. Es stellt sich also die Frage, wie weit die Häufigkeit reduziert werden muss, um das Restrisiko (englisch: residual risk) in den Bereich eines mindestens „tolerierbaren“ Risikos zu bringen. In diesem Fall wäre das Restrisiko mit Einschränkungen (bspw. Umsetzung angemessener Maßnahmen und Zustimmung des Betreibers, siehe oben) akzeptabel. Mit Blick auf die Risikobewertungsmatrix darf die Häufigkeit für ein tolerierbares Risiko bei gleichzeitig katastrophalem Schadensausmaß nur „sehr unwahrscheinlich“ sein. Die tolerierbare Gefährdungsrate in diesem Fall liegt gemäß Risikobewertungsmatrix bei  $ \lambda \leq 10^{-9}/h $ . Dies entspricht einer Sicherheitsintegritätsstufe SIL4. Das Ergebnis der Bewertung des Restrisikos ist in Abb. 6.2 als hellgrau hinterlegter Kreis dargestellt. Der Pfeil zwischen dem dunkelgrauen und dem hellgrauen Kreis symbolisiert die erreichte Risikoreduktion. Es sind also gemäß DIN EN 50129 umfangreiche Maßnahmen zur Vermeidung systematischer Fehler, bzw. zur sicheren Beherrschung zufälliger Fehler im Betrieb umzusetzen.

#### 6.1.2 Angriffssicherheit (Security)

Städtische Schienenverkehrssysteme sind kritische Verkehrsinfrastrukturen (vgl. BSI-KritisV 2016). Ihr Funktionieren ist für die Wirtschaft und unser gesellschaftliches Zusammenleben essenziell. Schutzziele bezeichnen hier den Zustand von Verkehrssystemen, der bei einem unberechtigten Zugriff Dritter erhalten bleiben soll. Insgesamt werden vier verschiedene Schutzziele unterschieden: die Verfügbarkeit, die Integrität, die Authentizität sowie die Vertraulichkeit. Die effektive Erreichung der zuvor genannten Schutzziele in kritischen Verkehrsinfrastrukturen erfordert das aufeinander abgestimmte Zusammenwirken von technischen, organisatorischen, und physischen Schutzmaßnahmen. Ein solch umfassendes Schutzkonzept wird auch als „tiefgestaffelte Verteidigung“ (englisch: Security in depth) bezeichnet (Schnieder 2020). Dieser Konzeption liegt die Vorstellung zu Grunde, dass eine einzelne Schutzmaßnahme allein keinen ausreichenden Schutz gegen unberechtigten Zugriff Dritter bietet. Die wirksame Anordnung mehrerer voneinander unabhängiger Barrieren vermag jedoch die Wahrscheinlichkeit eines erfolgreichen Zugriffs von außen deutlich zu reduzieren. Die verschiedenen Kategorien der Schutzmaßnahmen werden nachfolgend vorgestellt.

- Technische Schutzmaßnahmen: Eine zentrale Komponente von CBTC-Systemen ist das Datenübertragungssystem, welches eine sichere, zeitgerechte und zugriffsgeschützte Übertragung von Informationen zwischen Fahrzeug – und Streckeneinrichtungen ermöglichen muss. Hierbei ist vor allem auch ein unberechtigter Zugriff oder eine Manipulation der Daten zu verhindern. Daher werden CBTC-Systeme durch eine Security-Architektur gegen unberechtigte Zugriffe Dritter geschützt (zum Beispiel durch Firewalls). Die Auswahl technischer Schutzmaßnahmen gegen einen unberechtigten

---

Zugriff Dritter erfolgt auf der Grundlage internationaler Standards (vgl. DIN IEC 62443-3-3:2015-06). Beispiele von technischen Maßnahmen sind eine Verschlüsselung und Authentifizierung über Internet Protocol Security (IPsec) unter Verwendung von kryptografischen Hash-Funktionen (beispielsweise HMAC-SHA-256) sowie zusätzliche technische Maßnahmen wie ein zyklischer Schlüsselaustausch.

Organisatorische Schutzmaßnahmen: Für einen umfassenden Schutz der für die Verkehrssteuerung erforderlichen informationstechnischen Systeme ist die Einrichtung eines umfassenden Informationssicherheitsmanagementsystems (ISMS) durch das Verkehrsunternehmen ratsam (Schnieder und Magerkurth 2018a). Vorgaben an ein solches Managementsystem ergeben sich unter anderem aus dem internationalen Standard DIN EN ISO 27001. Hierbei werden, einem risikoorientierten Ansatz folgend, bestehende Angriffspunkte für unberechtigte Zugriffe von außen identifiziert und geschlossen. Darüber hinaus werden organisatorische Vorkehrungen getroffen im Sinne verbindlich definierter Prozesse, Rollen und Verantwortlichkeiten, um unberechtigte Zugriffe zu offenbaren und durch eine prompte Reaktion (Schnieder und Magerkurth 2018b) zügig zu schließen.

• Maßnahmen des physischen Zugriffsschutzes: Gewisse Bedrohungen setzen einen direkten (physischen) Zugriff auf die informationstechnischen Systeme des Betreibers voraus. Ein möglicher Angreifer muss für einen erfolgreichen Zugriff auf konkrete Assets in mehrere Schutzzonen eindringen. Durch die Anordnung von Alarmsystemen, Zutrittskontrollsystemen sowie der Auswahl von Schließsystemen wirksamer Widerstandsklassen wird ein unberechtigter Zugriff wesentlich erschwert.

### 6.2 Verfügbarkeit (Availability)

Die Verfügbarkeit automatisierter Zugbeeinflussungssysteme ist für ihren sicheren Betrieb essenziell. Verfügbarkeit bezeichnet „die Fähigkeit eines Produkts, in einem Zustand zu sein, in dem es unter vorgegebenen Bedingungen zu einem vorgegebenen Zeitpunkt oder während einer vorgegebenen Zeitspanne eine geforderte Funktion erfüllen kann unter der Voraussetzung, dass die geforderten äußeren Hilfsmittel bereitstehen.“ (DIN EN 50126-1:2018). Eine Maximierung der Verfügbarkeit lässt sich herunterbrechen auf mehrere Teilaspekte:

- Minimierung der mittleren Ausfallzeit: Dieses Ziel wird durch die Verbesserung der Instandhaltbarkeit (Maintainability) erreicht. Dies ist in Abschn. 6.2.1 beschrieben.

• Maximierung der mittleren Klarzeit: Dieses Ziel wird durch die Erhöhung der Zuverlässigkeit (Reliability) erreicht. Dies ist in Abschn. 6.2.2 beschrieben.

- Fehlertoleranz: Gestaltung der technischen Systeme, dass diese trotz Beeinträchtigung einzelner Komponenten ihre Funktion dennoch erfüllen. Dies ist in Abschn. 6.2.3 beschrieben.

---

#### 6.2.1 Optimierung der Instandhaltbarkeit (Maintainability) zur Steigerung der Verfügbarkeit

Die Minimierung der mittleren Ausfallzeit (englisch: mean down time, MDT) ist ein weiterer Ansatzpunkt zur Steigerung der Verfügbarkeit des städtischen Schienenverkehrs-systems (vgl. Abb. 6.3). Zu diesem Zweck werden die Zugsicherungsanlagen entsprechend instandhaltbar gestaltet. Hierbei bezeichnet Instandhaltbarkeit (Maintainability), die Wahrscheinlichkeit, dass für eine Komponente unter gegebenen Einsatzbedingungen eine bestimmte Instandhaltungsmaßnahme innerhalb einer festgelegten Zeitspanne ausgeführt werden kann. Hierbei wird zwischen einer präventiven und einer korrektiven Instandhaltung unterschieden. Präventive Instandhaltung bezeichnet hierbei die Instandhaltung in vorgegebenen Zeitabständen oder nach vorgegebenen Kriterien, die zur Verringerung der Ausfallwahrscheinlichkeit oder der Vermeidung der Verschlechterung der Funktion einer Einheit vorgesehen ist (DIN EN 50126-1:2018-10). Demgegenüber handelt sich bei der korrektiven Instandhaltung um die nach Erkennung des Fehlzustands durchgeführte Instandhaltung, die das Produkt wieder in einen Zustand versetzt, in dem es eine geforderte Funktion erfüllen kann (DIN EN 50126-1:2018-10). Bezüglich der korrektiven Instandhaltungsaktivitäten können verschiedene Ebenen unterschieden werden:

- Erste Instandhaltungsebene: Auf dieser Ebene erfolgt die Lokalisierung und der Austausch einer fehlerhaften kleinsten tauschbaren Einheit (line replaceable unit, LRU). Dies schließt Test- und Nachweisaktivitäten mit ein. Die defekte kleinste tauschbare Einheit wird der zweiten Instandhaltungsebene übergeben. Aktivitäten der ersten Instandhaltungsebene werden an der Strecke oder direkt auf dem Fahrzeug in der Werkstatt durchgeführt. Für diese Tätigkeiten werden Werkzeuge wie Messinstrumente und Laptops benötigt (Guizard 2006).

Zweite Instandhaltungsebene: Diese Instandhaltungsebene identifiziert den Fehler und ersetzt das fehlerhafte Bauteil in der kleinsten tauschbaren Einheit (beispielsweise eine fehlerhafte Baugruppe in einem Baugruppenträger). Es erfolgt ein abschließender Funktionstest. Die fehlerhafte Komponente wird der dritten Instandhaltungsebene übergeben, wohingegen die funktionsfähige kleinste tauschbare Einheit der ersten Instandhaltungsebene übergeben wird. Aktivitäten der zweiten Instandhaltungsebene erfolgen in der Werkstatt, da spezielle Werkzeuge für die Wiederherstellung der Funktionsfähigkeit erforderlich sind (Guizard 2006).

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//738d55a3-43f8-4409-8ea8-030e78c2aa5c/markdown_0/imgs/img_in_image_box_208_1097_725_1264.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A33%3A02Z%2F-1%2F%2F32c7bd9dc8ebbb653c73d51a989511363f021a5f7ab5825ff2efa02b82c3ad62" alt="Image" width="54%" /></div>


<div style="text-align: center;">Abb. 6.3 Zusammenhang der Kenngrößen der Verfügbarkeit</div>

---

• Dritte Instandhaltungsebene: Diese Instandhaltungsaktivitäten erfolgen beim Hersteller. Hier werden fehlerhafte Bauteile identifiziert und getauscht. Es erfolgt ein Funktionstest. Die reparierte Baugruppe wird der zweiten Instandhaltungsebene bereitgestellt. Diese Instandhaltungsebene erfordert spezielle Prüfadapter, die nur beim Hersteller zur Verfügung stehen (Guizard 2006).

Die Instandhaltbarkeit kann durch die folgenden Aspekte positiv beeinflusst werden, um in der Praxis möglichst kurze Zeiten zur Wiederherstellung der Betriebsfähigkeit des städtischen Schienenverkehrssystems nach Störungen zu erreichen:

- Diagnosesysteme: Jede technische Komponente sowohl der streckenseitigen als auch der fahrzeugseitigen Einrichtungen wird kontinuierlich auf ihre Funktionsfähigkeit überwacht. Da die Fahrzeuge durch den Streckenatlas und die fahrzeugautarke Ortung über weitreichende Informationen verfügen, können sie von ihnen erkannte Ausfälle oder Abweichungen in der Infrastruktur an die Leitstelle melden. Beispiele hierfür sind erkannte defekte Transponder entlang der Strecke oder erkannte zu geringe Feldstärken der streckenseitigen Access Points des Datenübertragungssystems. Ist eine Komponente ausgefallen, wird dies offenbart und eine Störmeldung in der Leitstelle angezeigt. Auf Basis der lokalisierten Fehler können voraussichtlich erforderliche Ersatzteile bestimmt werden und je nach Dringlichkeit der Fehlerbehebung Maßnahmen zur Entstörung (beispielsweise Abarbeitung von Wartungsaufträgen am Tag oder in der Nachtsperrpause) disponiert werden.

• Tauschkomponenten: Die Hersteller geben für jede eingesetzte Komponente eine Mean Time Between Failures (kurz MTBF) an. Dies ist die englische Bezeichnung für die mittlere Betriebsdauer zwischen Ausfällen für reparierbare Einheiten. Unter „Betriebsdauer“ versteht man die Betriebszeit zwischen zwei aufeinanderfolgenden Ausfällen einer instandsetzbaren Einheit. Zusammen mit dem Mengengerüst der gesamten Anlage und den logistischen Verzugsdauern (Lieferfristen der Hersteller) kann der erforderliche Ersatzteilbedarf abgeschätzt werden, sodass der Hersteller für einen ausreichenden Ersatzteilvorrat sorgen kann.

• Ausgebildetes Personal: Für die Instandhaltung ist qualifiziertes Personal erforderlich. Die Einführung hochautomatisierter Zugbeeinflussungssysteme erfordert für die Verkehrsunternehmen eine Anpassung ihrer Organisation. Dies liegt in zwei Effekten begründet. Zum einen verlagern sich die Instandhaltungsaktivitäten durch die deutlich reduzierten Außenanlagenkomponenten und die aufwändigere Instandhaltung der Fahrzeugeinrichtungen in den Betriebshof. Zum anderen verändern sich insbesondere für die Instandhaltung der Infrastruktur die durchzuführenden Instandhaltungsaktivitäten deutlich, da nun – in deutlichem Gegensatz zu traditionellen signaltechnischen Systemen – fast ausschließlich Netzwerkkomponenten instandzuhalten sind (Rüffer et al. 2019). Insbesondere bei fahrerlosem Betrieb ist für die Beurteilung von Zeiten zur Entstörung und zur Wiederherstellung des Regelbetriebs auch die Frage relevant, wo sich Betriebspersonal aufhält, welches auf die Fahrzeuge im Störungsfall bedienen kann.

---

Beim unbegleiteten fahrerlosen Betrieb (UTO) sind – sofern keine Möglichkeit zur situativen Fernsteuerung des Fahrzeugs aus der Leitstelle heraus gegeben ist – möglicherweise erhebliche Verzugszeiten durch erforderliche Fußwege des Betriebspersonals zum gestörten Fahrzeug zu berücksichtigen.

• Remote Software Update: Gerade bei einer großen Fahrzeugflotte stellen sich Softwareupdates als außerordentlich aufwändig heraus. Die Hersteller von CBTC-Systemen bieten daher Lösungen zum sicheren Fernladen von Fahrzeugeinrichtungen über drahtlose Kommunikationssysteme an. Dies spart Zeit und Ressourcen in der Instandhaltung.

#### 6.2.2 Erhöhung der Zuverlässigkeit (Reliability) zur Steigerung der Verfügbarkeit

Die Maximierung der mittleren Klarzeit (engl.: mean up time, MUT) ist ein Ansatzpunkt zur Steigerung der Verfügbarkeit des städtischen Schienenverkehrssystems (vgl. Abb. 6.2). Zu diesem Zweck werden die Fahrzeug- und Streckeneinrichtungen entsprechend zuverlässig gestaltet. Zuverlässigkeit bezeichnet hierbei die „Wahrscheinlichkeit dafür, dass eine Einheit ihre geforderte Funktion unter gegebenen Bedingungen für eine gegebene Zeitspanne [...] erfüllen kann“. Durch die folgenden Maßnahmen in der Gestaltung elektronischer Systeme kann auf die Zuverlässigkeit Einfluss genommen werden:

- Einsatz betriebsbewährter Komponenten: Eine Komponente gilt als betriebsbewährt, wenn eine entsprechend dokumentierte Untersuchung ergeben hat, dass Nachweise aus früheren Einsätzen belegen, dass die Komponente für den Einsatz in einem sicherheitstechnischen System geeignet ist. Hierbei werden hohe Anforderungen an die Dokumentation von Felderfahrungen gestellt. So muss beispielsweise die Spezifikation unverändert sein und es dürfen keine oder nur unbedeutende Fehler aufgetreten sein. Außerdem müssen die Beobachtungen auf einer ausreichenden Anzahl an Betriebsstunden beruhen.

- Einsatz qualifizierter Komponenten: dieser Ansatz ist insbesondere in der Automobilindustrie ausgeprägt. Die Qualifizierung elektronischer Komponenten kann Branchenstandards folgen. Um eine Qualifizierung gemäß dieser Standards zu erhalten, muss eine Komponente einen strengen Prozess mit unterschiedlichen Prüfungen bestehen (bspw. Klimatests).

Derating: Üblicherweise besteht eine Reserve zwischen den Konstruktionsgrenzen eines Bauteils und den im Betrieb auftretenden Belastungen. Somit ist ein Bauteil oder System, dass unterhalb seiner Auslegungsgrenze betrieben wird, zuverlässiger als ein Bauteil, das an oder oberhalb seiner Auslegungsgrenze betrieben wird. Durch Derating kann also die Zuverlässigkeit erhöht, bzw. die Lebensdauer einer Komponente gesteigert werden.

• Fehlererkennung und Fehlerkorrektur: Bei der Speicherung, Verarbeitung und Übertragung von Daten können Fehler auftreten. Fehler entstehen hierbei durch das Ändern, Löschen oder Hinzufügen von Bits. Beim Behandeln von Fehler gibt es zwei Möglichkeiten. Die Fehlererkennung zeigt an, dass ein Fehler aufgetreten ist. Bei der Fehlerkorrektur wird der Fehler nicht nur erkannt, sondern auch gleich behoben.

---

#### 6.2.3 Fehlertolerante Systeme zur Steigerung der Verfügbarkeit

Technische Systeme, die trotz Beeinträchtigung einzelner Komponenten ihre Funktion weiterhin erfüllen, werden als fehlertolerant bezeichnet. Redundanz bezeichnet hierbei das Vorhandensein von mehr als für die sichere Ausführung der vorgesehenen Aufgabe notwendigen Mittel. Die Anwendung von Redundanz führt dazu, dass eine Betrachtungs- einheit ihre vorgesehene Aufgabe auch ei einer begrenzten Anzahl von Ausfällen auch weiterhin ausführen kann. Betrachtungseinheiten, für die diese Eigenschaften zutreffen, heißen fehlertolerant. In Bezug auf die Umsetzung der Fehlertoleranz können unterschied- liche Redundanzkonzepte unterschieden werden:

- Funktionsbeteiligte Redundanz (heiße Redundanz, englisch: active redundancy): Während des fehlerfreien Betriebs sind alle mehrfach vorhandenen Systemkomponenten an der Funktionserfüllung beteiligt. Im Fehlerfall übernehmen die intakten Komponenten die Aufgabe der defekten Komponente unverzüglich.

• Nicht funktionsbeteiligte Redundanz (Standbyredundanz, englisch passive redundancy): Redundanz, bei der die zusätzlichen Mittel eingeschaltet sind, aber erst bei Störung oder Ausfall an der Ausführung der vorgesehenen Aufgabe beteiligt sind.

- Kalte Redundanz (englisch: cold redundancy): Redundanz, bei der die zusätzlichen Mittel zur Ausführung der vorgesehenen Aufgabe erst bei Störung oder Ausfall eingeschaltet werden.

Beispielhafte Ansätze der Gestaltung fehlertoleranter Systeme sind nachfolgend in Bezug auf die einzelnen Systemkomponenten von CBTC-Systemen aufgeführt:

- Die Fahrzeugeinrichtungen verfügen über eine so genannte „Head-Tail-Redundanz“. Das bedeutet, dass es in jedem Zug zwei sichere Rechner gibt (jeweils einen an jedem Ende des Zuges). Im Normalbetrieb ist eine Fahrzeugeinrichtung aktiv und die Fahrzeugeinrichtung am anderen Fahrzeugende ist passiv. Die passive Fahrzeugeinrichtung hat keine Kontrolle über den Zug, verfügt aber in seinen Streckenatlas über ein aktuelles Prozessabbild. Die aktive Fahrzeugeinrichtung ist nicht notwendigerweise diejenige am vorderen Ende des Zuges. Um die Ausfallsicherheit zu verbessern, ist das System mit einer automatischen, nahtlosen Umschaltung zwischen den beiden Fahrzeugeinrichtungen an Bord ausgestattet.

- Die zentralen Streckeneinrichtungen sind ebenfalls mehrkanalig ausgelegt. Hier kommen für die sicheren Rechner der CBTC-Streckenzentrale beispielsweise 2-von-3 Rechnersysteme zum Einsatz. Für den Fall, dass ein Rechnerkanal ausfällt, sind nach wie vor zwei Rechnerkanäle für die Bearbeitung der sicherheitstechnischen Funktionen im Betrieb. Bei CBTC-Systemen wirkt sich außerdem positiv aus, dass weniger technische Komponenten im Gleis verbaut sind, da weitestgehend – wenn nicht gar vollständig – auf eine sekundäre Gleisfreimeldung und ortsfeste Signale verzichtet werden kann.

• Auch beim Datenkommunikationssystem stellen verschiedene Arten von Redundanz sicher, dass ein Ausfall eines Geräts die Leistung des Betriebs nicht negativ beeignet.

---

trächtigt. So ist die redundante Hardware des Datenkommunikationssystems über zwei redundante Strom- und Glasfaserkabel mit möglichst abweichender Leitungsführung an die CBTC-Streckeneinrichtung angebunden. Für den Fall, dass ein Glasfaserkabel durchtrennt ist, ist noch eine zweite Datenverbindung vorhanden, so dass der Betrieb aufrechterhalten werden kann. Darüber hinaus verfügen die Access Points jeweils über mehrere Antennen und sind in ausreichend kurzen Abschnitten entlang der Strecke installiert, dass ein Zug zu jeder Zeit mehrere Access Points erreichen kann. Jede Nachricht des CBTC-Systems wird verdoppelt und über zwei Pfade versendet.

• Auch in der Betriebsleittechnik (Automatic Train Supervision, ATS) dient Redundanz der Steigerung der Verfügbarkeit des Systems. Bei der Redundanz wird zwischen „cold standby“ und „hot standby“ unterschieden. Die Arbeitsplatzrechner arbeiten im „cold standby“. Dafür gibt es in der Leitstelle mehr Arbeitsplatzrechner als Bediener. Wenn ein Arbeitsplatzrechner ausfällt, wechselt der Bediener den Arbeitsplatz und loggt sich dort wieder ein. Die Server hingegen arbeiten im „hot standby“. Dabei verarbeitet der passive Server alle ankommenden Daten von den Schnittstellen. Der passive Server unterscheidet sich dadurch vom aktiven, dass er keine Ausgaben durchführt. Der aktive und der passive Server überwachen sich gegenseitig. Es erfolgt eine automatische Übernahme der Funktion des aktiven Servers durch den passiven Server, nachdem der passive Server den Ausfall des aktiven Servers erkannt hat. Es erfolgt eine Aktualisierung des passiven Servers durch den aktiven nach Wiederanlaufen des passiven Servers. Fällt der passive Server aus, erfolgt eine Information an den Fahrdienstleiter oder den Wartungstechniker (Mücke 2005). Um auch gegen den Fall des kompletten Ausfalls der Leitstelle gewappnet zu sein können teilweise im Netz verteilte örtliche Bedienplätze vorgesehen werden oder aber eine vollständig ausgerüstete zweite Leitstelle an einem anderen Ort.

- Unterbrechungsfreie Stromversorgung (USV, bzw. englisch: Uninterruptible Power Supply, UPS): Diese Systeme dienen der Sicherstellung der Stromversorgung kritischer elektrischer Geräte bei Störungen im Stromnetz, wie beispielsweise kurzfristigen Stromausfällen und Stromschwankungen in Form von Über- oder Unterspannungen. Dies betrifft insbesondere die zentralen Streckeneinrichtungen sowie die Betriebsleittechnik.

## Literatur

Braband J (2005) Risikoanalysen in der Eisenbahn-Automatisierung. Eurailpress, Hamburg

DIN EN 50126-1:2018-10 Bahnanwendungen – Spezifikation und Nachweis von Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS) – Teil 1: Generischer RAMS-Prozess; Deutsche Fassung EN 50126-1:2017 (DIN EN 50126-1 2018)

DIN EN 50129:2019-06 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – Sicherheitsrelevante elektronische Systeme für Signaltechnik; Deutsche Fassung EN 50129:2018

DIN EN 50159:2011-04 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – Sicherheitsrelevante Kommunikation in Übertragungssystemen; Deutsche Fassung EN 50159:2010

---

DIN EN 62267:2010 DIN EN 62267:2020-07: Automatischer städtischer schienengebundener Personennahverkehr (AUGT) – Sicherheitsanforderungen. Deutsche Fassung EN 62267:2009

DIN IEC 62443-3-3:2015-06 Industrielle Kommunikationsnetze – IT-Sicherheit für Netze und Systeme – Teil 3-3: Systemanforderungen zur IT-Sicherheit und Security-Level (IEC 62443-3-3:2013 + Cor.:2014)

Guizard M (2006) Maintenance is a priority for communication based train control solutions. Signal + Draht 98(4):35–37

Mücke W (2005) Betriebsleittechnik im öffentlichen Verkehr. Eurailpress, Hamburg

Rüffer M, Schmidt C, Jung C, Schnieder L (2019) Innovation und Digitalisierung im Signal- und Zugsicherungsdienst. Nahverkehr 37(7+8):46–50

Schnieder L (2020) Security Engineering – Ein ganzheitlicher Ansatz zum Schutz Kritischer Infra- strukturen im Verkehr, 2. Aufl. Springer, Berlin

Schnieder L, Magerkurth G (2018a) Notfallmanagementpläne für Schienenverkehrssysteme als Bestandteil eines Informationssicherheitsmanagementsystems (ISMS). Eisenbahntech Rundsch 67(11):47–50

Schnieder L, Magerkurth G (2018b) Schutz kritischer Infrastrukturen im ÖPNV – Aufbau eines zertifizierungsfähigen Informationssicherheitsmanagementsystems (ISMS). Nahverkehr 36(11):39–43

Schnieder E, Schnieder L (2013) Verkehrssicherheit: Maße und Modelle, Methoden und Maßnahmen für den Straßen- und Schienenverkehr. Springer, Berlin

Verband Deutscher Verkehrsunternehmen (VDV) (2005) VDV-Schrift 161-1: Sicherheitstechnische Anforderungen an die elektrische Ausrüstung von Stadt- und U-Bahn-Fahrzeugen; Teil 1: Grundlagen. VDV, Köln

Verband Deutscher Verkehrsunternehmen (VDV) (2009) VDV-Schrift 161-2: Sicherheitstechnische Anforderungen an die elektrische Ausrüstung von Stadt- und U-Bahn-Fahrzeugen; Teil 2: Sicherheitsintegritätsanforderungen an fahrzeugbezogene elektrische/elektronische/programmierbare elektronische Schutzfunktionen (E/E/PE). VDV, Köln

Verband Deutscher Verkehrsunternehmen (2008) Sicherheitsintegritätsanforderungen für Signal- und Zugsicherungsanlagen gemäß BOStrab. VDV-Schrift 331

Verordnung zur Bestimmung Kritischer Infrastrukturen nach dem BSI-Gesetz (BSI-Kritisverordnung – BSI-KritisV) (22. April 2016) (BGBl. I S. 958). Zuletzt geändert durch Art. 1 V. v. 21.06.2017 (BGBl. I S. 1903)

---

# Abwägung von Kosten und Nutzen automatischer Zugbeeinflussungssysteme

## SN Flashcards

Als Käufer*in dieses Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards“ mit Fragen zur Wissensüberprüfung und zum Lernen von Buchinhalten nutzen.

1. Gehen Sie bitte auf https://flashcards.springernature.com/login und



2. erstellen Sie ein Benutzerkonto, indem Sie Ihre Mailadresse angeben und ein Passwort vergeben.

3. Verwenden Sie den folgenden Link, um Zugang zu Ihrem SN Flashcards Set zu erhalten: ▶ https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht funktionieren, senden Sie uns bitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Kosten-Nutzen-Analysen werden in zahlreichen Bereichen der öffentlichen Daseinsvorsorge zur Entscheidungsunterstützung eingesetzt. So verpflichtet in Deutschland etwa § 7 Bundeshaushaltsordnung die öffentlichen Körperschaften dazu, vor einer Ausgabe eine Wirtschaftlichkeitsuntersuchung durchzuführen (vgl. hierzu Arnold 2017; Kossak 2018). Kosten-Nutzen-Analysen sind eine solche Form der Wirtschaftlichkeitsuntersuchung. Dieser Abschnitt stellt dar, welche Betrachtungen bei der Einführung automatischer Zugbeeinflussungssysteme auf der Kostenseite durchgeführt werden (Abschn. 7.1). Des Weiteren stellt dieser Abschnitt

---

dar, wie der Nutzen von Verkehrsinfrastrukturprojekten ermittelt wird (Abschn. 7.2). Über- wiegt der Nutzen die Kosten, qualifiziert dies eine Infrastrukturmaßnahme für eine Förderung aus öffentlichen Haushaltsmitteln.

### 7.1 Ermittlung der Kostenkomponente mittels Lebenszykluskostenrechnung

Investitionen in die Automatisierung von Stadtschnellbahnsystemen sind in der Regel mit einem hohen Investitionsvolumen verbunden (Capital Expenditure, CAPEX). Gleichzeitig weisen diese Investitionsgüter eine sehr lange Lebensdauer auf. Falsche Entscheidungen zu Beginn des Lebenszyklus können daher nur schwer und wenn dann nur mit erheblichem Aufwand korrigiert werden. Aus diesem Grund hat sich in den letzten Jahrzehnten in der öffentlichen Beschaffung das Konzept der Lebenszykluskosten (life cycle costs, LCC) durchgesetzt (DIN IEC 60300-3-3:1999). Demnach wird die über einen langfristigen Investitionszeitraum (beispielsweise 25 Jahre) insgesamt wirtschaftlichste Investitionsalter-native beschafft. Hierbei können zum Beispiel geringere Instandhaltungsaufwände (Operational Expenditure, OPEX) in der Phase des Betriebs teilweise höhere initiale Beschaffungskosten kompensieren (Wolberg und Kiefer 2000).

#### 7.1.1 Elemente der Lebenszykluskosten

Die Gesamtheit aller Kosten wird im so genannten „Kostenwürfel“ (vgl. Abb. 7.1) dargestellt. Nachfolgend werden die drei Dimensionen des Kostenwürfels nach (DIN IEC 60300-3-3:1999) eingeführt. Die erste Seite des Würfels ist die technische Struktur des betrachteten Zugbeeinflussungssystems. Dies wird auch als Produktaubruchstruktur bezeichnet. Die zweite Seite des Würfels sind die in der Analyse betrachteten Lebenszyklus-phasen. Dies wird auch als Kostenaufbruchstruktur bezeichnet. Die dritte Seite des Würfels sind schließlich die in der Wirtschaftlichkeitsbetrachtung berücksichtigten Kostenarten.

Produktaubruchstruktur (vertikale Achse des Kostenwürfels): Die vertikale Achse des „Kostenwürfels“ (vgl. Abb. 7.1) ist die Produktaubruchstruktur (englisch: Product-/Work Breakdown Structure, kurz: PBS/WBS). Sie umfasst neben der technischen Struktur des betrachteten Systems auch unterstützende Dienstleistungen und Arbeitspakete. Hier wird der betrachtete Technikumfang aufgegliedert und definiert, was für Kosten anfallen. Die LCC-Analyse für die Leit- und Sicherungstechnik von Schienenverkehrsunternehmen kann sich hierbei an in der Literatur diskutierte Produktaubruchstrukturen (Gutsche 2010) orientieren. Die Produktaubruchstruktur besteht beim Fahren auf Zugsicherung aus den Elementen der Außenanlage (Gleisfreimeldeeinrichtungen wie Achszählsysteme oder Gleisstromkreise, bewegliche Fahrwegelemente wie Weichen und Gleissperren sowie ortsfeste Signale), der Innenanlage (je nach Art des Stellwerks Relaisgestelle oder Rechnerschränke mit den zugehörigen Kabelabschlussgestellen), der Leittechnik (Zuglenkrechner sowie Bedien- und Anzeigesysteme) und der Art der Zugbeeinflussung. Hierbei müssen für

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//93007511-6374-4ed9-a831-05e65655ba2f/markdown_0/imgs/img_in_image_box_115_130_1275_803.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A33%3A31Z%2F-1%2F%2F8cb194264225bfb1703a21251d41e322800f80a9b959b78d5a922feefe0924a6" alt="Image" width="85%" /></div>


<div style="text-align: center;">Abb. 7.1 Verschiedene Perspektiven auf die Lebenszykluskosten</div>

---

CBTC-Systeme auch die Komponenten des gewählten Datenkommunikationssystems mit betrachtet werden. Ist die Produktaufbruchstruktur modelliert, können für den zu betrachtenden Streckenabschnitt die konkreten Mengenwerte ergänzt werden, so dass sich hieraus eine Stückliste (englisch: bill of quantity, BoQ) ergibt. Für möglicherweise bestehende Mengenrisiken sollten hier bereits Vorkehrungen getroffen werden.

Kostenaufbruchstruktur, Lebenszyklusphasen (horizontale Achse des Kostenwürfels): Die horizontale Achse des „Kostenwürfels“ in Abb. 7.1 heißt Kostenaufbruchstruktur (englisch: Cost Breakdown Structure, kurz CBS). Sie zeigt, in welcher Phase des Lebenszyklus die jeweiligen Kosten anfallen. Beispielsweise sind dies die drei Hauptphasen: Beschaffung, Betrieb (Instandhaltung) und Entsorgung. Der grundsätzliche Aufbau einer Kostenaufbruchstruktur für Bahnanwendungen ist in der Regel vor allem geprägt durch die Investitionskosten, die Kosten für den Betrieb (Betriebspersonal, Energie sowie Kosten für System-Unverfügbarkeit im Sinne von Verspätungen) und die Kosten für die Instandhaltung. Hierbei müssen die einzelnen Instandhaltungsaktivitäten pro Komponente der Produktaufbruchstruktur betrachtet werden. Aus den Instandhaltungsanweisungen der Hersteller und/oder rechtlichen Vorgaben resultieren Aufwände für regelmäßig durchzuführende Sichtprüfungen (Inspektionen). Aus den Zuverlässigkeitskennwerten der einzelnen Komponenten können darüber hinaus Annahmen abgeleitet werden, wie häufig es zu einem Komponentenausfall kommen wird. Außerdem sind neben den Ersatzteilkosten auch Annahmen über die für eine Instandsetzung erforderlichen Zeiten (Mean Time to Repair, MTTR) bekannt, die hier ebenfalls zu berücksichtigen sind (Wolberg und Kiefer 2000).

Kostenarten: Die dritte Dimension, welche den Kostenwürfel entstehen lässt, stellen die Kostenarten (englisch: Cost Categories, kurz CC) dar. Die Kostenarten benennen die Bereiche, die Kosten verursachen und gliedern diese in kostenverursachende Elemente (englisch: Cost Elements, kurz CE) auf. Bei der Betrachtung eines kostenverursachenden Elements befindet man sich demzufolge auf der kleinsten Betrachtungsebene. Es können verschiedene Kostenarten unterschieden werden, wie beispielsweise Materialkosten, Personalkosten, Werkzeugkosten und Entsorgungskosten. Beispiele für Kostenelemente sind beispielsweise Kosten für Roh-, Hilfs- und Betriebsstoffe, Kosten für die Wartung eines Weichenantriebes oder die Entsorgung eines Relais. Die Angaben für die Kostenarten stammen idealerweise aus einem bei dem Betreiber eingesetzten Softwaresystem (Hannusch 2015). Auch bei der Abschätzung der einzelnen Kostenpositionen sollten Risiken, beispielsweise in Bezug auf zu erwartende zukünftige Preissteigerungen, mit berücksichtigt werden. Einen Ansatz, die zukünftige Kostenentwicklung in die Berechnung der Lebenszykluskosten mit einzubeziehen könnte die Extrapolation verschiedener für einzelne Kostenpositionen zutreffender Indizes (bspw. Arbeitskostenindex) darstellen.

#### 7.1.2 Berechnung der Lebenszykluskosten

Die Berechnung der Lebenszykluskosten erfolgt mittels so genannter dynamische Investitionsrechnungsverfahren. Hierbei werden die bei den langen Lebensdauern von Zug

---

sicherungsanlagen erheblichen Unterschiede im Anfallen von Zahlungen (Aufwendungen aber auch Erträge) einer Investition berücksichtigt. Die Idee ist hierbei, dass alle über den Lebenslauf einer geplanten Investition anfallenden vermögenswirksamen Zahlungen auf den Beginn einer Planung abgezinst werden (Huch et al. 1997). Dieser Kapitalwert ist das Entscheidungskriterium für den Vergleich unterschiedlicher Investitionsalternativen. Der Kapitalwert bildet sich als Differenz zwischen der Summe aller auf den Anfangszeitpunkt abgezinsten Einzahlungen und der Summe aller auf den Anfangszeitpunkt abgezinsten Auszahlungen, die mit dieser Investition zusammenhängen. Für die relative Vorteilhaftigkeit können die Investitionsalternativen entsprechend der Höhe des Kapitalwerts geordnet werden. Der Kapitalwert  $ C_{0} $  einer Investitionsalternative über einen Zeitraum t berechnet sich auf Basis periodenspezifischer Einzahlungen  $ E_{t} $  und Auszahlungen  $ A_{t} $  sowie des kalkulatorischen Zinssatzes i zu:

 $$ C_{0}=\sum_{t=1}^{n}\frac{\left(E_{t}-A_{t}\right)}{\left(1+i\right)^{t}} $$ 

#### 7.1.3 Ergebnisse der Analyse der Lebenszykluskosten

Über die lange Lebensdauer signaltechnischer Einrichtungen weisen automatische Zug- beeinflussungssysteme im Vergleich zu konventionellen Bahnsystemen hinsichtlich ihrer Lebenszykluskosten erhebliche Vorteile auf. Diese werden nachfolgend skizziert:

• Reduzierte Anzahl Außenanlagenelemente der Streckeneinrichtung: Durch die kontinuierliche Datenübertragung zwischen Fahrzeugen und Strecke kann auf einen Großteil der ortsfesten Sensorik zur Gleisfreimeldung verzichtet werden. Sofern nicht von der Zulassungsbehörde anders gefordert, können auch ortsfeste Signale vollständig entfallen, da nunmehr eine Führerstandssignalisierung mit einer entsprechend hohen Verfügbarkeit vorliegt. Die geringe Anzahl an Außenanlagenelementen resultiert neben geringen Anschaffungskosten auch in erheblichen Einsparungen für die Instandhaltung.

- Energieeinsparung: Die kontinuierliche Datenübertragung zwischen Fahrzeug- und Streckeneinrichtung legt die Grundlage für die automatische Fahr- und Bremssteuerung (Automatic Train Operation, ATO). Hierdurch gelingt – sofern die Betriebssituation es zulässt – die Umsetzung einer energiesparenden Fahrweise mit Einsparung entsprechender Kosten für die Traktionsenergie. Die energiesparende Fahrweise resultiert hierbei neben dem optimalen Ausfahren der eigenen Trajektorie auch aus vermiedenen Folgeverspätungen.

• Einsparung von Personalkosten: Im unbegleiteten fahrerlosen Betrieb verkehrende Bahnen benötigen für den betrieblichen Ablauf kein Personal. Je nach System kann die Bereitstellung und die Abstellung von Zügen sowie die Beförderung von Fahrgästen effizienter gestaltet werden. Darüber hinaus können mit unbegleitet fahrerlos ver-

---

kehrenden Bahnen weitere Verkehrsangebote entwickelt werden, die heute mit hohen Personalkosten (Nacht- oder Sonn- und Feiertagszuschläge) und Einschnitten im Privatleben des Betriebspersonals verbunden sind. Auf diese Weise wird durch die Automatisierung beispielsweise ein durchgängiger U-Bahnbetrieb auch während der Nacht oder ein uneingeschränkter Verkehr an Feiertagen möglich.

- Zusätzliche Fahrgeldeinnahmen: Die dichtere Zugfolge führt zu einer Steigerung der Attraktivität des öffentlichen Personennahverkehrs. Zusätzliche Fahrgäste bedeuten mehr Umsatz für die Verkehrsunternehmen.

### 7.2 Ermittlung der Nutzenkomponente mit Betriebssimulationen und Verkehrsmodellen

Für die Ermittlung des Nutzens einer signaltechnischen Erneuerung muss zunächst die Einfluss des CBTC-Systems auf die Leistungsfähigkeit der untersuchten Strecken betrachtet werden. Dies geschieht mittels betriebswissenschaftlicher Untersuchungen, was in Abschn. 7.2.1 näher ausgeführt wird. In der Regel wird durch CBTC-Systeme ein positiver Beitrag auf die Leistungsfähigkeit der betrachteten Strecke nachgewiesen. Dies eröffnet Freiheitsgrade hinsichtlich der Definition zusätzlicher Angebote des öffentlichen Personennahverkehrs (ÖPNV), was in Abschn. 7.2.2 beschrieben wird. Um einen gesellschaftlichen Nutzen aus den zusätzlichen Bedienungsangeboten (Fahrplanfahrten) zu ermitteln, müssen die gesamten verkehrlichen Effekte betrachtet werden. Hierzu kommen Verkehrsmodelle zum Einsatz. Dies wird in Abschn. 7.2.3 beschrieben. Der auf dieser Basis ermittelten Nutzenkomponente kann die zuvor dargestellten Kostenkomponente (Lebenszykluskostenrechnung) zur Ableitung eines Kosten-Nutzen-Faktors gegenübergestellt werden.

#### 7.2.1 Simulative Untersuchung der Leistungsfähigkeit signaltechnischer Ausrüstungsvarianten

Mit der Betriebssimulation lässt sich das Leistungsverhalten für verschiedene Infrastruktur- und Betriebsprogrammvarianten für einen gegebenen Untersuchungszeitraum grundsätzlich bewerten und vergleichen. Die Betriebssimulation kann Auskunft darüber geben, in welchem Auslastungsbereich sich der aktuelle oder ein geplanter Fahrplan bewegt und wie groß eventuell vorhandene Kapazitätsreserven (bezogen auf den betrachteten Netzausschnitt) sind. In CBTC-Projekten werden Betriebssimulationen mit Hilfe einer geeigneten Simulationssoft-ware durchgeführt. Die folgenden Abschnitte beschreiben die im Rahmen einer Betriebssimulation durchzuführenden aufeinander aufbauenden Schritte (Becker et al. 2019).

## V orbereitung des Simulationsmodells

Für den in der Simulation zu betrachtenden Streckenbereich müssen die für die Durchführung der verschiedenen Betrachtungen erforderlichen Grunddaten des Simulations

---

models erfasst werden. Grundlage einer Betriebssimulation sind im Wesentlichen die nachfolgend dargestellten drei Gruppen von Daten (Ostermann et al. 2005):

Infrastrukturdaten: Die Infrastruktur des zu simulierenden Netzes des Betreibers wird mittels eines Grafikeditors entworfen und verwaltet. Hierbei werden die wesentlichen Merkmale der Strecke als Knoten-Kanten-Modell abgebildet. Es handelt sich hierbei um kanten- oder knotenbewerte Grafen (Becker et al. 2019). An jeder Stelle, an der sich ein Attribut der Strecke ändert, wird im Modell ein Knoten gesetzt. Die Infrastruktur wird hierbei oftmals von Hand aufgenommen. Die benötigten Daten können wie folgt unterschieden werden:

• Daten zur Gleistopologie wie Weichen, Kreuzungen und Gleisenden.

- Daten zur Sicherungslogik wie Signale, Spezifika der eingesetzten Zugsicherungssysteme (Fahrstraßenlogik), Lage und Länge von Gleisfreimeldeabschnitten und technische Reaktionszeiten (Umlaufzeiten von Weichenantrieben, Fahrstraßenbildezeiten und weitere Details wie beispielsweise eine einzelementweise Auflösung von Fahrstraßen).

Vorgaben für die zulässige und mögliche Fahrweise der Fahrzeuge wie das Gradientenprofil (Neigungen und Gefälle) sowie zulässige Geschwindigkeiten beispielsweise bedingt durch Bogenradien (zum Beispiel in abzweigenden Weichensträngen).

• Betriebsbeeinflussende Daten wie Haltepositionen und Nutzlängen der Bahnsteige

• Referenz- und Messpunkte.

Fahrplan- und Betriebsdaten: Für eine realistische Abbildung des Betriebs werden Fahrpläne in das Simulationswerkzeug eingegeben. Hierbei werden verschiedene Aspekte differenziert:

• Modellierung des Soll-Fahrplans: Die im Simulationsmodell zu berücksichtigenden Daten umfassen die Grunddaten des Soll-Fahrplans von den Einbruchstellen des Zuges in den betrachteten Netzausschnitt. Konkrete Parameter umfassen hierbei:

– Modellierung der Haltezeiten. Hierbei werden Verkehrshaltezeiten, das heißt dem Fahrgastwechsel dienenden Haltestellenaufenthalte (minimale Haltezeiten und Sollhaltezeiten) abgebildet. Des Weiteren werden möglicherweise noch Haltezeit-reserven im Fahrplan berücksichtigt. Darüber hinaus werden auch Betriebshaltezeiten abgebildet. Betriebshaltezeiten dienen nicht unmittelbar dem Fahrgastwechsel. Ein Beispiel hierfür sind zusätzliche im Fahrplan zu berücksichtigende Zeitanteile für das Kehren von Fahrzeugen an den Endhaltestellen (Wendezüge), das Kuppeln und Trennen von Zügen (Flügelzugkonzepte) sowie gegebenenfalls die Abwicklung geplanter Rangierfahrten.

– Modellierung der Fahrzeiten mit Abfahrts- und Ankunftszeiten in den Stationen, Sollfahrzeiten und (Regel-)Zuschlägen auf die Fahrzeit zur Kompensation möglicher Störungen im Betriebsablauf.

---

- Modellierung weiterer Zeitanteile, welche durch die Umstiege von Fahrgästen erforderlich werden. Ein Beispiel hierfür ist die logische Verknüpfung zweier Zugfahrten durch die Berücksichtigung von Anschlussbeziehungen. Ist der zubringende Zug verspätet, wird bei einer Anschlussbindung die Verspätung auf den abbringenden den Zug übertragen.

- Daten des Ist-Betriebsgeschehens: Um das reale Betriebsgeschehen im betrachteten Netzausschnitt abzubilden, werden einbrechende Züge mit einer Verspätungsverteilung beaufschlagt. Diese wird repräsentiert durch eine Verspätungsfunktion und sollte einer möglichst realen Verspätungsverteilung an dieser Stelle entsprechen (beispielsweise aus Daten des Intermodal Transport Control Systems, ITCS). Über den Laufweg der Fahrzeuge können darüber hinaus Primärverspätungen (verlängerte technische Fahrzeit, Haltezeit) induziert werden, welche ebenfalls durch Verteilungsfunktionen beschrieben werden. Zusätzlich sollten auch für die Haltestellen im betrachteten Netzausschnitt Verspätungsverteilungen vorliegen, damit diese später mit den Simulationsergebnissen verglichen werden können (Büker et al. 2021).

Fahrzeugdaten pro Fahrzeugbaureihe: Für die Stadtbahnfahrzeuge werden die technischen Daten aller in der Simulation vorkommenden Fahrzeuge und Fahrzeugkombinationen verwaltet. Konkret betrifft dies von den Fahrzeugherstellern vorgegebene (und im CBTC-Fahrzeugrechner projektierte) garantierte Bremsverzögerungen sowie das üblicherweise im Betrieb realisierte Beschleunigungsverhalten der Fahrzeuge, Laufwiderstandsdaten, die Anzahl der Wagen pro Zug sowie die Zuglänge.



## V alidierung und Kalibrierung der Betriebssimulation

Um eine hohe Aussagekraft der Simulationsergebnisse zu erhalten, muss dieses valide sein. Daher wird man vor Beginn der Simulationsmodell auf den Prüfstand stellen (Becker et al. 2019). Dies geschieht in zweierlei Hinsicht:

- Frühzeitige Durchführung von Simulationen, um Lücken oder möglicherweise unzureichend modellierte Aspekte im Simulationsmodell zu offenbaren. Hierzu werden auf Grundlage des hinterlegten Fahrplans frühzeitig Simulationsläufe gestartet, um das Simulationsmodell bei Bedarf zu korrigieren.

In einem weiteren Schritt wird das Simulationsmodell kalibriert. Dies stellt sicher, dass das Simulationsmodell eine valide Abbildung der Wirklichkeit darstellt und zu den gleichen Ergebnissen führt, wie diese sich auch im realen Betrieb einstellen. Hierfür wird der Ist-Zustand der Betriebsabwicklung auf zu betrachtenden Strecke modeliert. Zur Bewertung der aktuellen Betriebsqualität werden die Verspätungen aus den Simulationsergebnissen bei der durchgeführten Betriebssimulation betrachtet (Cui und Martin 2014). Hierfür werden die Verspätungen an den relevanten Fahrzeitmesspunkten (den Stationen) gemessen und mit den vorliegenden Werten aus dem Intermodal Transport Control System (ITCS) des Betreibers verglichen.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b8d3ddab-9279-4159-bb4e-7c81b1821527/markdown_0/imgs/img_in_image_box_86_92_926_465.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A33%3A55Z%2F-1%2F%2Fa29e5b2e234b6ee47ea60bb010d9db45e370f2ea362c77e27e8092c6e645e30b" alt="Image" width="88%" /></div>


<div style="text-align: center;">Abb. 7.2 Beispielhafte Darstellung eines Simulationsmodells. (Quelle: VIA Consulting & Development GmbH)</div>


Abb. 7.2 zeigt das Zusammenwirken der verschiedenen Modellbestandteile in einem Simulationswerkzeug. In der oberen Bildhälfte ist die zulässige Fahrweise des Zuges in einem statischen Geschwindigkeitsprofil dargestellt. Unterhalb der zulässigen Geschwindigkeit ist die vom Zug tatsächlich realisierte Geschwindigkeit dargestellt. In der unteren Bildhälfte sind die Zeit-Weg-Linien (Sperrzeitenbänder) der Zugfahrten dargestellt. Die Zahlen in Abb. 7.2 markieren Charakteristika, wie sie sich in einem CBTC-System ergeben. In der Darstellung der vom Zug realisierten Fahrweise wird deutlich, dass die maximal zulässige Geschwindigkeit nicht erreicht wird, weil der Zug schon frühzeitig auf das Geschwindigkeitsziel bremst (Ziffer 1). Hinter dem Zielbahnsteig schließt sich ein Kehrgleis mit einer geringen zulässigen Geschwindigkeit von 25 km/h an (Ziffer 2). In der unteren Bildhälfte wird deutlich, dass die erreichbaren Zugfolgezeiten in städtischen Bahnsystemen wesentlich durch die Haltestellenaufenthaltszeiten bestimmt werden (Ziffer 3). Ebenfalls wird deutlich, dass die Sperrzeitenbilder von der Fahrzeuggeschwindigkeit abhängen. Die Nachbelegung (Teil des Sperrzeitenbandes unterhalb der Zeit-Weg-Linie eines Zuges) wächst mit fallender Geschwindigkeit (vgl. Ziffer 4). Die Vorbelegung (Teil des Sperrzeitenbandes oberhalb der Zeit-Weg-Linie eines Zuges) wächst überproportional zur Geschwindigkeit (vgl. Ziffer 5). Zuletzt wird auch deutlich, dass Weichenlagen ebenfalls einen Einfluss auf die Sperrzeitenbänder haben. Die Weiche ist ein zu sichernder (ortsfester) Gefahrenpunkt. Ihre korrekte Endlage muss vor Zulassen einer Zugfahrt vorhanden sein (Büker et al. 2019). Aus diesem Grund zeigt sich diese frühzeitige Beanspruchung der Weiche für die Zugfahrt in der Vorbelegung für die jeweilige Zugfahrt (vgl. Ziffer 6).

## Durchführung der Simulationsläufe

Um für das jeweilige Entscheidungsproblem zu validen Aussagen zu kommen, werden in der Regel mehrere Varianten des Simulationsmodells dem jeweiligen Nachweisziel fol-

---

gend modifiziert und durchlaufen (Becker et al. 2019). Im Sinne des Monte-Carlo-Verfahrens wird für jedes betrachtete Simulationszenario eine ausreichende Menge von Simulationsläufen durchgeführt, so dass hieraus statistisch belastbare Kennzahlen resultieren. Jeder Simulationslauf erhält als Input eine Liste zufällig generierter primärer Verspätungsdaten, welche zug- und betriebsstellenspezifisch sind (Büker et al. 2021). Die Erstellung der unterschiedlichen Simulationszenarien erfolgt nach dem in der Verkehrsplanung üblichen Mitfall-/Ohnefall-Prinzip.

• Ohne-Fall: Durchführung des aktuellen Fahrplanangebots mit aktueller Technik: Dieses stellt die Referenz für alle Änderungen im System dar. Um tragfähige Simulationsergebnisse zu erhalten, war dieses Simulationsmodell Gegenstand der zuvor dargestellten Validierung und Kalibrierung.

- Mit-Fall 1: Durchführung des aktuellen Fahrplanangebotes mit zukünftiger Technik: Durch den Übergang von einer konventionellen Zugsicherung mit Fahrsperre zu einem CBTC-System gelingt ein Übergang vom Fahren im festen Raumabstand zu einem Fahren im wandernden Raumabstand. Hierdurch beeinflussen sich die Züge nicht mehr gegenseitig und es kommt nicht mehr zu einer Verspätungsübertragung. Hierdurch entstehen Kapazitätsreserven.

• Mit-Fall 2: Hochskalieren des Fahrplanangebotes mit zukünftiger Technik: Die zukünftig gewünschten Fahrplantakte werden in der Betriebssimulation abgebildet. Hier-durch kann bewertet werden, inwieweit noch Kapazitätsreserven bestehen und in wel-chem Auslastungsbereich die Strecke betrieben wird.

Die Ergebnisse der einzelnen Simulationsläufe werden jeweils für sich ausgewertet. Die Ergebnisse der unterschiedlichen Simulationsläufe werden einander gegenübergestellt, um die relative Vorteilhaftigkeit der unterschiedlichen untersuchten Systemvarianten zu analysieren und für die nachgelagerten Entscheidungsprozesse (unter anderem zur Förderwürdigkeit des jeweiligen Projekts) transparent und nachvollziehbar zu dokumentieren.

#### 7.2.2 Nutzung der höheren Leistungsfähigkeit für Anpassungen im ÖPNV-Angebot

In städtischen Räumen ist das Bedienungsangebot spurgeführter Verkehrssysteme im wesentlichen bereits heute durch die Struktur der vorhandenen Verkehrsanlagen, bzw. die vorhandene Zugsicherung eingeschränkt. Da konventionelle Zugsicherungsanlagen lediglich das Fahren im festen Raumabstand unterstützen kann die Kapazität in bestehenden Netzen möglicherweise noch durch die Gefäßgrößen der Fahrzeuge (bspw. Betrieb mit längeren Fahrzeugen) erhöht werden. Auf Grund baulicher Restriktionen wie bspw. Bahnsteiglängen ist auch dies gegebenenfalls nicht möglich. Hier zeigt sich, dass die durch CBTC-Systeme mögliche Abkehr vom Fahren im festen Raumabstand, bzw. der damit verbundene Übergang zu einem Fahren im wandernden Raumabstand weitergehende

---

Potenziale zur Angebotsverbesserung im öffentlichen Personennahverkehr (ÖPNV) eröffnet. Diese Potenziale stellen sich wie folgt dar:

- Angebotsausweitungen: Durch die geringen Zugfolgezeiten können auf einer Linie mehr Fahrten pro Fahrtrichtung und Stunde abgewickelt werden. Dies erlaubt beispielsweise die Einführung neuer Linien. Aus Sicht des Fahrgastes wirken sich mögliche neue Direktlinien, bei denen auf bestimmten Verkehrsrelationen für die Fahrgaste die Notwendigkeit zu Umstiegen entfällt unmittelbar positiv auf die wahrgenommene Dienstleistungsqualität aus.

• Verbesserung der Betriebsqualität: Bei schienengebundenen Verkehrssystemen stellt die Leistungsfähigkeit die Anzahl an Zugfahrten dar, welche auf einer Schieneninfrastruktur unter Einhaltung einer zulässigen Betriebsqualität abgewickelt werden kann. Die Anzahl fahrbarer Zugfahrten wird maßgeblich durch den Ausbauzustand der zugrundeliegenden Infrastruktur beeinflusst. Hierfür ist insbesondere das verbaute Zugsicherungssystem maßgeblich. Wird nun die Leistungsfähigkeit erhöht, hat dies – sofern es nicht zu einer Angebotsausweitung kommt – zunächst positive Effekte auf die Betriebsqualität. Dies verbessert die von den Fahrgästen wahrgenommene Dienstleistungsqualität durch geringere Störungen im Betriebsablauf und hieraus resultierende Verspätungen.

• Reisezeitgewinne: Dies beschreibt Veränderungen der Reisezeit der Fahrgäste beim Mitfall gegenüber dem Ohnefall. Aus Sicht des Fahrgastes führen beispielsweise dichtere Fahrplantakte (resultierend aus Angebotsausweitungen, siehe oben) zu kürzeren Wartezeiten an den Stationen. Dies wirkt sich somit unmittelbar positiv auf die Reisezeit aus.

#### 7.2.3 Bewertung des verkehrlichen Nutzens von Anpassungen im ÖPNV-Angebot

Neben der Vermeidung von Verkehr trägt vor allem die Verkehrsverlagerung auf umweltschonendere Verkehrsträger dazu bei, die negativen Auswirkungen von Verkehr auf die Umwelt einzudämmen. Die von der Verkehrspolitik gesetzten Rahmenbedingungen spielen eine Schlüsselrolle bei der Ermöglichung von Verkehrsverlagerung. Im Personenverkehr kann die Verkehrsverlagerung vom motorisierten Individualverkehr auf den Öffentlichen Personenverkehr u. a. durch einen stärkeren Ausbau der öffentlichen Verkehrsangebote gefördert werden. Die signaltechnische Erneuerung von städtischen Schienenverkehrssystemen hoher Leistungsfähigkeit ermöglicht – wie bereits zuvor dargestellt – den Ausbau öffentlicher Verkehrsangebote.

Da die Investition in die signaltechnische Erneuerung erhebliche finanzielle Mittel bindet, ist hier der Nachweis der Sinnhaftigkeit dieser Maßnahmen im Zusammenhang des Gesamtverkehrsnetzes zu führen. Hierbei kommt es vor allem darauf an zu prognostizieren, welchen Einfluss die Verbesserungen des Angebots im öffentlichen Personennahver-

---

kehr auf die tatsächliche Verkehrsnachfrage in der betrachten Region haben werden. Um diese Frage nach den verkehrlichen Nutzenwirkungen qualifiziert beantworten zu können, kommen Verkehrsnachfragemodell zum Einsatz. Dafür wird das das Betrachtungsgebiet in gleichwertige Verkehrszellen eingeteilt. Die Größe, Homogenität und Verfügbarkeit soziodemographischer Daten beeinflusst die Genauigkeit der späteren Ergebnisse des Nachfragemodells. Untereinander sind die Verkehrszellen durch Verkehrslinien verbunden. Verkehrszellen und Verkehrslinien zusammen ergeben das Netzmodell. Auf Basis des Netzmodells kann nun in mehreren aufeinander aufbauenden Schritten die Verkehrsnachfrage ermittelt werden:

Verkehrserzeugung: Jede Verkehrszelle ist Quelle oder Senke von Verkehrsbeziehungen. Je nachdem, ob eine Zelle als Wohn- oder als Arbeitsstätte dient, werden zu unterschiedlichen Zeiten unterschiedliche Verkehrsmengen erzeugt. Diese Daten können aus der Statistik entnommen oder berechnet werden.

- Verkehrsverteilung: Durch die Berechnung der Verkehrserzeugung bleibt unklar, auf welche anderen Verkehrszellen sich der Verkehr verteilt. Es gibt unterschiedliche mathematisch formulierte Zielwahlmodelle. Als Ergebnis der Anwendung Zielwahlmodelle kann die verkehrliche Verflechtung der Verkehrszellen untereinander im betrachtenen Raum in Form einer Quelle-Ziel-Matrix dargestellt werden.

• Verkehrsaufteilung (Verkehrsmittelwahl): Bei der Verkehrsmittelwahl wird die Aufteilung des Verkehrs auf individuelle (MIV = motorisierter Individualverkehr, NIV = nicht-motorisierter Individualverkehr) und öffentliche Verkehrsmittel (ÖV) – der sogenannte Modal Split – ermittelt.

Verkehrsumlegung (Verkehrswegewahl): Bei der Verkehrsumlegung wird bestimmt, welche Route der Verkehr wählt, um von der Quelle zum Ziel zu gelangen.

Auch die Nachfragemodelle werden mittels Ohnefall-/Mitfallprinzip vergleichend betrachtet. Dadurch, dass die Einführung von CBTC-Systemen Angebotsverbesserungen der Nahverkehrsbetreiber ermöglicht, werden in diesen Modellen Nutzen der Reisenden in Form von Reisezeitgewinnen und auch hieraus resultierende Verkehrsverlagerungen zwischen den Verkehrsträgern bewertbar. Insbesondere der Verkehrsverlagerung auf umweltschonendere Verkehrsträger wird vor dem Hintergrund einer forcierten Umwelt- und Klimapolitik ein gesellschaftlicher Nutzen zugesprochen.

## Literatur

Arnold M (2017) Standardisierte Bewertung Version 2016 – Ergebnisse der Weiterentwicklung und Fortschreibung. Nahverkehr 35(9):42–46

Becker M, Büker T, Hennig E, Felix K (2019) Sound evaluation of simulation results. In: RailNorrköping 2019 – 8th International Conference on Railway Operations Modelling and Analysis (ICROMA), Norrköping, S 99–115

---

Büker T, Grafagnino T, Hennig E, Kuckelberg A (2019) Enhancement of blocking-time theory to represent future interlocking architectures. In: RailNorrköping 2019 – 8th International Conference on Railway Operations Modelling and Analysis (ICROMA), Norrköping, S 219–240

Büker T, Schnieder L, van Hovell M, Meurer D (2021) Eisenbahnbetriebswissenschaftliche Untersuchung von CBTC-Systemen. Signal + Draht 113(9):25–33

Cui Y, Martin U (2014) Algorithmus zur automatisierten Kalibrierung von Modellen bei der Betriebssimulation. Eisenbahntechn Rundsch 63(11):10–14

DIN IEC 60300-3-3:1999-03 Zuverlässigkeitsmanagement – Teil 3: Anwendungsleitfaden – Hauptabschn 3: Betrachtung der Lebenszykluskosten (IEC 60300-3-3:1996)

Gutsche K (2010) Integrierte Bewertung von Investitions- und Instandhaltungsstrategien für die Bahnsicherungstechnik, Bd 9. Berichte aus dem DLR-Institut für Verkehrssystemtechnik, Braunschweig

Hannusch G (2015) Anforderungen an IT-Systeme für das Asset Management im Bahnverkehr. Eisenbahningenieur 65(7):34–36

Huch B, Behme W, Ohlendorf T (1997) Rechnungswesenorientiertes Controlling – Ein Leitfaden für Studium und Praxis. Physica, Heidelberg

Kossak A (2018) Reaktivierung des allgemeinen Schienenpersonenverkehrs auf der Kandertalstrecke – Teil1. Eisenbahntechn Rundsch 67(6):22–25

Ostermann N, Schlögel A, Oster M, Messauer C (2005) Anwendungen der Betriebssimulation. Elektrotech Informationstech (e&i) 122(4):124–130

Wolberg J, Kiefer J (2000) Life Cycle Costs – Die Kosten von Betrieb, Wartung und Verfügbarkeit. Signal + Draht 92(6):19–22

---

# Umbau, Test und Inbetriebnahme automatischer Zugbeeinflussungssysteme

## SN Flashcards

Als Käufer*in dieses Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards“ mit Fragen zur Wissensüberprüfung und zum Lernen von Buchinhalten nutzen.

1. Gehen Sie bitte auf https://flashcards.springernature.com/login und



2. erstellen Sie ein Benutzerkonto, indem Sie Ihre Mailadresse angeben und ein Passwort vergeben.

3. Verwenden Sie den folgenden Link, um Zugang zu Ihrem SN Flashcards Set zu erhalten: ▶ https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht funktionieren, senden Sie uns bitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Die Erneuerung der Signaltechnik wird insbesondere in Europa in den nächsten Jahren immer bedeutender, da ein Großteil der bestehenden Infrastruktur der U-Bahnsysteme in den Großstädten mehr als 30 Jahre alt ist (de Silvestre 2005). Viele Betreiber stehen aus folgenden Gründen vor Ersatzinvestitionen:

Obsoleszenz: Ersatzteile für die bestehenden signaltechnischen Anlagen sind nicht mehr lieferbar (Laumen und Henning 2012). Dies stellt eine große Herausforderung für die Instandhaltung und die Aufrechterhaltung eines sicheren und ordnungsgemäßen Betriebs dar (McCullough 2008).

---

Kapazität: Mit den bestehenden signaltechnischen Systemen kann die zunehmende Verkehrsnachfrage zukünftig nicht mehr qualitätsgerecht bedient werden. Dichtere Zugfolgen sind mit den bestehenden signaltechnischen Anlagen nicht mehr realisierbar (McCullough 2008).

Damit in den Infrastrukturen der U-Bahn- und Stadtbahnbetreiber eine Umrüstung bestehender Signaltechnik auf die zukünftige CBTC-Systeme erfolgreich ist, sind sinnvolle Migrationsstrategien zu entwickeln. Dies wird in Abschn. 8.1 behandelt. Grundlage einer erfolgreichen Projektumsetzung ist die Projektierung von Streckeneinrichtungen und Fahrzeugeinrichtungen, was in den Abschn. 8.2 und 8.3 beschrieben wird. Den Nachweis über die korrekte Realisierung der automatisierungstechnischen Funktionen liefert ein efektives Testmanagement. Dies wird in Abschn. 8.4 behandelt. Vor Aufnahme des Betriebes muss das betriebliche Regelwerk erstellt werden, bzw. im Rahmen eines Er- neuerungsprojekts angepasst werden (Abschn. 8.5). Abschließend müssen – wie in Abschn. 8.6 dargestellt – verschiedene Zielgruppen des Betreibers zu den neuen Technologien geschult werden.

### 8.1 Definition der Migrationsstrategie

Die richtige Wahl der Erneuerungsstrategie ist einer der wichtigsten Erfolgsfaktoren. Dies gilt insbesondere für Projekte, die nicht „auf der grünen Wiese“ (englisch: green field projects) realisiert werden. Es gibt viele zu berücksichtigende Einflüsse und spezifische Einschränkungen, die bei der Definition der geeigneten Erneuerungsstrategie mit bedacht werden müssen. Die Entscheidung wird zusätzlich noch dadurch erschwert, dass die gewählte Erneuerungsstrategie einen enormen Kosteneffekt aufweist. Verschiedene Erneuerungsstrategien werden nachfolgend mit ihren bestehenden Einschränkungen, sowie den jeweiligen Vor- und Nachteilen beschrieben.

Die nachfolgenden Zielsetzungen gelten unabhängig von der gewählten Erneuerungsstrategie:

- Minimierung der Auswirkungen von Streckensperrungen auf den Fahrgastbetrieb: Ein möglichst ungehinderter Bauablauf erfordert während der Umsetzung der Erneuerungsstrategie Streckensperrungen. Hierbei müssen die Streckensperrungen selbst frühzeitig geplant werden. Hierbei gibt es zwei unterschiedliche Strategien:

– Ausschließliche Nutzung von Nachsperrpausen: Der erste Ansatz ist die ausschließliche Nutzung von Nachtsperrpausen (in der Regel 3 bis 4 Stunden in jeder Nacht) für die Installationsarbeiten. Diese Strategie hat den unbestreitbaren Vorteil, dass sie keine Auswirkungen für die Fahrgäste hat. Das Fahrplanangebot wird auch während der Bauphase ohne Einschränkungen aufrechterhalten und muss nicht durch kostenträchtige Schienenersatzverkehre kompensiert werden. Nachteil dieser Strategie ist, dass durch die für das tägliche Einrücken in den Baustellenbereich und die Räu-

---

mung der Baustelle erforderlichen Vor- und Nachlaufzeiten sowie die in der Regel kurze Zeit einer nächtlichen Sperrpause sehr wenig Zeit für die Durchführung der erforderlichen Bauarbeiten verbleibt. Der Baufortschritt vollzieht sich daher weniger zügig und die Bauzeit erstreckt sich hierdurch über einen längeren Zeitraum. Da über die eigentlichen Lohnkosten hinaus noch erhebliche Zuschläge für Nachtarbeit zu zahlen sind, bringt diese Strategie auch erhebliche Kosten mit sich.

– Vollsperrung der Strecke: Ein gegensätzlicher Ansatz ist die Vollsperrung der Strecke. Die komplette Sperrung ermöglicht einen optimalen Bauablauf, da Vor- und Nachlaufzeiten für die tägliche Einrichtung und Rücknahme von Baustellenbereichen entfallen. Da die Arbeiten in diesem Ansatz nicht zwingend nachts durchgeführt werden müssen, können bei diesem Ansatz die erheblichen Zusatz-kosten für Zuschläge für Nachtarbeit entfallen. Allerdings sind mit diesem Ansatz massive Auswirkungen für die Fahrgäste verbunden, da das Fahrtenangebot komplett entfällt und mit Schienenersatzverkehren aufgefangen werden muss. Aus diesem Grund werden Vollsperrungen in der Regel vorzugsweise in den Sommerferien durchgeführt, da hier durch die ohnehin geringere Verkehrsnachfrage weniger Fahrgäste von den Streckensperrungen betroffen sind. Außerdem müssen die eingesparten Kosten für Nachtzuschläge und Produktivitätsgewinne sorgfältig gegen die erheblichen Zusatzkosten für umfangreiche Produktivitätsgewinne sorgfältig gegen die erheblichen Zusatzkosten für umfangreiche Schienenersatzverkehre abgewogen werden.

Gewährleistung einer ausreichenden Fahrzeuganzahl für den Betrieb: Neben den zuvor beschriebenen Streckensperrungen muss auch die Ausrüstung der Fahrzeuge von Beginn an mit bedacht werden. Für die Ausrüstung der Fahrzeuge müssen diese für einen gewissen Zeitraum außer Betrieb genommen werden, um in der Werkstatt mit der neuen Fahrzeugausrüstung versehen zu werden. Hier- durch reduziert sich währen des Migrationszeitraums zumeist die Fahrzeug- reserve, wenn nicht gar die Anzahl der für den Betrieb zur Verfügung stehenden Fahrzeuge. Die Umbaustrategie muss daher frühzeitig mit dem für die Fahrzeuge verantwortlichen Unternehmensbereich abgestimmt werden. Außerdem müssen auch geeignete Werkstattkapazitäten (Gruben und Testgleise) für die Durchführung der Fahrzeugumrüstung zur Verfügung stehen.

- Minimierung der technischen und betrieblichen Risiken während der Migrationsphase: Hierbei sind unter anderen auch Rückwirkungen von Veränderungen im Gesamtsystem zu bewerten. So ist beispielsweise bei einer nachträglichen Ergänzung von Bahnsteigtüren zu prüfen, inwieweit Bahnsteigflächen für das Fahrgastaufkommen (Wartefläche) oder für die Entfluchtung im Falle eines Notfalls noch ausreichend sind. Außerdem führt das nachträgliche Einbringen von Bahnsteigtüren im Stationsbereich zu weiteren nachträglichen Änderungen beispielsweise hinsichtlich der Be- und Entlüftung.

- Minimierung der Kosten für die Migrationsphase: Hierbei sind auch die Investitions- und Betriebskosten etwaiger Doppelausrüstungen von Fahrzeugen und Infrastruktur zu bewerten. Jede zusätzlich vorgehaltene Einrichtung muss beispielsweise regelmäßig inspiziert und instandgehalten werden.

---

Um das Projektrisiko zu mindern, werden während der Bauphase streckenseitige Umschalteinrichtungen zwischen dem alten Zugsicherungssystem und dem neuen Zugsicherungssystem sowie mögliche Rückfallebenen zwischen dem neuen und dem bestehenden Zugsicherungssystem empfohlen. Die CBTC-Streckeneinrichtung (Streckenzentrale, Funksystem und Ortungsreferenzpunkte) kann beispielsweise als Overlay-System zu einem bestehenden Zugsicherungssystem installiert werden. Auf jeden Fall sind die projektspezifischen Besonderheiten bei der Auswahl der Erneuerungsstrategie zu berücksichtigen. Im Folgenden werden mit der Doppelausrüstung von Fahrzeugen und der Doppelausrüstung der Infrastruktur die beiden unterschiedlichen Strategieoptionen beschrieben und hinsichtlich ihrer Vor- und Nachteile bewertet.

#### 8.1.1 Doppelausrüstung der Fahrzeuge

Eine mögliche Strategie für die Erneuerung der Zugsicherung im Netz eines Betreibers ist die Doppelausrüstung von Fahrzeugen und der abschnittsweise Umbau des gesamten Netzes. Die Migration erfolgt hierbei wie folgt:

Alle Züge werden mit den neuen CBTC-Fahrzeuggeräten ausgerüstet. Darüber hinaus sind (zumindest im ersten Bauabschnitt) alle Streckeneinrichtungen bereits installiert worden. Eine neue Leitstelle wird – parallel zum Betrieb der bestehenden Leittechnik – eingerichtet. Auf dieser Grundlage können während der Tageszeiten ohne Betrieb (in der Regel nachts) zunächst statische Tests und im Anschluss dynamische Tests für das neue Zugbeeinflussungssystem durchgeführt werden. Für die Durchführung der Testaktivitäten werden die Weichen und andere notwendige Fahrwegelemente über eine Umschalteinrichtung mit dem neuen Zugsicherungssystem verbunden. Nach den nächtlichen Test-phasen wird die Kontrolle über die Weichen und die anderen Feldelemente über die Umschalteinrichtung wieder an das bestehende Zugsicherungssystem zurückgegeben. Sobald die dynamischen Tests vollständig durchgeführt worden sind, kann im ersten Abschnitt der Betrieb mit dem neuen Zugbeeinflussungssystem aufgenommen werden. Deshalb müssen bereits frühzeitig im Projekt alle Züge, die in diesen Streckenabschnitt einfahren, über die entsprechende CBTC-Fahrzeugeinrichtungen verfügen. Auf diese Weise werden Schritt für Schritt die nächsten Bauabschnitte entlang der Linie mit CBTC-Streckeneinrichtungen in Betrieb genommen, bis die komplette Linie umgerüstet ist. Ist der Probebetrieb mit dem neuen Zugbeeinflussungssystem erfolgreich verlaufen, können die Altsysteme zurückgebaut werden. Diese Erneuerungsstrategie erfordert in der Übergangsphase eine Systemumschaltung zwischen dem bestehenden Zugbeeinflussungssystem und dem neuen Zugbeeinflussungssystem an den Grenzen der jeweiligen Baustufen. An einer definierten Systemwechselstelle schaltet der Fahrer zwischen den Zugbeeinflussungssystemen um. Hierfür werden in der Regel Stationsaufenthalte genutzt, da der Zug hier hält. Die Grenze muss mit Sorgfalt ausgewählt werden. Die Stellwerksgrenzen des Altsystems müssen hierbei mit berücksichtigt werden. Eine Systemgrenze innerhalb eines Stellwerksbereichs des Altsystems erfordert umfassende Änderungen im

---

Bestandssystem, die möglichst vermieden werden sollten. Die Anzahl der Systemwechselstellen sollte so gering wie möglich sein, da jede Systemwechselstelle zwar nur vorübergehender Natur ist, jedoch eine umfassende Projektierung erfordert. Die Leitebene kann oft ohne aufwändige Datenschnittstellen realisiert werden (Arpaci und Schwarte 2013).

Diese Erneuerungsstrategie weist die folgenden Vor- und Nachteile auf:

• Die Vorteile dieser Erneuerungsstrategie sind wie folgt:

– Eine schrittweise Erneuerung der signaltechnischen Infrastruktur ist möglich.

Jede Bauphase verfügt im Abschnitt über ein einheitliches Betriebskonzept. Es gibt in einem Abschnitt keinen Mischbetrieb mit verschiedenen Zugbeeinflussungssystemen.

• Die Nachteile dieser Erneuerungsstrategie sind wie folgt:

– Zum Zeitpunkt der Umrüstung des ersten Streckenabschnitts müssen bereits alle in diesem Abschnitt verkehrenden Züge über eine CBTC-Fahrzeugeinrichtung verfügen.

– Es werden Systemwechselstellen benötigt, an denen die Umschaltung zwischen altem Zugbeeinflussungssystem und dem neuen Zugbeeinflussungssystem erfolgt.

- Möglicherweise stellt die Installation einer zweiten Fahrzeugeinrichtung technisch eine unlösbare Aufgabe dar, da auf den Fahrzeugen keine ausreichenden Einbauräume für eine vorübergehende zweite Fahrzeugeinrichtung vorhanden sind.

#### 8.1.2 Doppelausrüstung der Streckeneinrichtungen

Die zweite mögliche Erneuerungsstrategie ist die doppelte Ausrüstung der Streckenbereiche, sodass ein Mischbetrieb von Fahrzeugen mit konventionellem Zugbeeinflussungssystem und Fahrzeugen mit CBTC-Fahrzeuggeräten möglich wird. Hierbei werden in einer ersten Projektphase alle CBTC-Streckengeräte im gesamten Netz installiert. Hierbei erhält das neue Zugsicherungssystem die für die Steuerung und Überwachung der Komponenten des alten Zugsicherungssystems erforderlichen technischen Schnittstellen.

Erhalten beispielsweise in einem alten Zugbeeinflussungssystem die Fahrzeuge die Informationen über ihre zulässige Fahrweise über von Gleisstromkreisen übertragene Geschwindigkeitscodes, muss das neue Stellwerk ebenfalls über eine Schnittstelle zu diesen Gleisstromkreisen verfügen. Eine neue Leittechnik wird parallel zur bestehenden Leittechnik eingerichtet. Diese Erneuerungsstrategie erfordert im Gegensatz zu der im vorherigen Abschnitt dargestellten Doppelausrüstung von Fahrzeugen nicht, dass in der ersten Phase schon alle Züge mit der CBTC-Fahrzeugeinrichtung ausgestattet werden. Sobald alle Teilsysteme installiert worden sind und die statischen Tests abgeschlossen sind, können die dynamischen Tests beginnen. Dies erfolgt in der Regel außerhalb der regulären Betriebszeiten (das heißt in der Regel nachts). Die Steuerung und Überwachung der Weichenantriebe, Signale und Komponenten des bestehenden Zugsicherungssystems werden mittels Umschalteinrichtung auf das neue Zugsicherungssystem umgestellt. Nach

---

dem Test wird die Steuerung und Überwachung wieder an das Altsystem übergeben. Sobald die dynamischen Tests abgeschlossen sind, kann der Fahrgastbetrieb im Mischbetrieb aufgenommen werden (Arpaci und Schwarte 2013).

Das neue Zugbeeinflussungssystem erkennt automatisch mit CBTC ausgerüstete Fahrzeuge. Die CBTC-Fahrzeuge werden im Abstandshalteverfahren des Fahrens im wandern-den Raumabstand (mit absolutem Bremswegabstand) geführt. Die noch nicht mit CBTC ausgerüsteten Fahrzeuge werden wie bisher auch vom bestehenden Zugbeeinflussungssystem geführt. Hierbei können die Alttechniken unterschiedlich ausgeprägt sein wie beispielsweise ein punktförmiges Zugbeeinflussungssystem, welches lediglich das Überfahren eines Halt zeigenden Signals verhindert oder aber ein älteres kontinuierlich wirkendes Zugbeeinflussungssystem, welches Informationen über die zulässige Fahrweise über Geschwindigkeitscodes auf das Fahrzeug übermittelt. Das neue Zugbeeinflussungssystem stellt sicher, dass im Mischbetrieb zwischen Fahrzeugen mit CBTC und ohne CBTC ausreichende Abstände zwischen den Zugfahrten eingehalten werden.

Üblicherweise werden alle Teilsysteme ersetzt, wenn eine Linie wegen Obsoleszenz (das heißt Teilsysteme sind nicht mehr lieferbar) erneuert werden muss. Daher werden in diesem Beispiel alte Gleisfreimeldesysteme und Zugbeeinflussungseinrichtungen in einer zweiten Phase ersetzt. Eine neue Gleisfreimeldung mit Achszählsystemen kann mühelos parallel zu bestehenden Gleisfreimeldesystemen installiert werden. Während der Migrationsphase kommt bereits das neue Zugbeeinflussungssystem zum Einsatz. Nur die Software muss später für die Tests des letzten Abschnitts ohne das Altsystem getauscht werden. Dies erfolgt in der Betriebspause. Sobald die dynamischen Tests mit der finalen Systemkonfiguration abgeschlossen sind, kann das letzte Altsystem abgeschaltet werden. Bevor dies allerdings passieren kann, müssen alle Züge, welche auf der Linie verkehren, mit CBTC ausgerüstet sen. Züge mit dem Altsystem können nicht mehr auf der Linie verkehren.

Der letzte Schritt ist der Rückbau des Altsystems, sobald der Testbetrieb erfolgreich absolviert wurde. Dieser Ansatz der Migration hat die folgenden Vor- und Nachteile:

• Die Vorteile dieser Erneuerungsstrategie sind wie folgt:

– Nicht alle Fahrzeuge müssen zu einem frühen Zeitpunkt mit CBTC ausgerüstet sein.

– Es gibt keine Baustufenschnittstelle mit einem Systemwechsel.

• Die Nachteile dieser Erneuerungsstrategie sind wie folgt:

– Es müssen komplexe Simulationen durchgeführt und Schnittstellen zur bestehenden Signaltechnik implementiert werden.

– Es müssen zwei Testphasen mit unterschiedlichen Systemkonfigurationen durchgeführt werden.

– Es bestehen zu einem Zeitpunkt verschiedene Betriebskonzepte in einem Streckenabschnitt in Abhängigkeit des Ausrüstungszustands des jeweiligen Zugtyps.

Die Doppelausrüstung von Streckeneinrichtungen wird oftmals dann ausgewählt, wenn eine Fahrzeugflotte nicht rechtzeitig verfügbar ist oder wenn nur neue Fahrzeuge ausgerüstet werden sollen oder können.

---

### 8.2 Anwendungspezifische Konfiguration automatischer Zugbeeinflussungssysteme

Leit- und Sicherungssysteme im Eisenbahnverkehr müssen individuell an die strecken-, betriebs- und fahrzeugspezifischen Randbedingungen angepasst werden. Diese Anpassung oder Konfiguration des Systems wird auch als Projektierung bezeichnet. Für einen sicheren Betrieb muss sichergestellt werden, dass die Projektierungsdaten fehlerfrei sind. Eine fehlerhafte Projektierung (wie zum Beispiel eine fehlerhaft projektierte zulässige Geschwindigkeit) kann somit trotz der nachgewiesenen Fehlerfreiheit der anwendungsunabhängigen Software des CBTC-Systems zu einem Versagen einer sicherheitsrelevanten Funktion führen. In der Ausführungsphase erstellt der Systemhersteller alle herstellerspezifischen Ausführungsunterlagen für die Strecken- und Fahrzeugeinrichtungen, die auf den Eingangsdaten des Betreibers basieren. Der Arbeitsaufwand des Herstellers im Rahmen der Ausführungsphase sowie die Kosten der Projektierung sind sehr stark abhängig von der Qualität der Eingangsdaten des Betreibers. Nachfolgend werden Aspekte der Projektierung von Strecken- und Fahrzeugeinrichtungen automatischer Zugbeeinflussungssysteme dargestellt (Schroeder 2002).

#### 8.2.1 Kategorien streckenspezifischer Konfigurationsdaten

Das Datenmodell des Streckenatlasses muss ein umfassendes Bild über die Schieneninfrastruktur mit allen sicherheitsrelevanten Parametern enthalten. Konkret umfassen die streckenspezifischen Projektierungsdaten die folgenden Kategorien:

- Gleisgeometrie: Grundsätzlich wird zunächst die Geometrie der Gleise erfasst. Die Erfassung der Geometrie kann durch bereits digital vorliegende Daten, digitalisierte Planzeichnungen oder aus der geometrischen Vermessung stattfinden, wie es heute in der Praxis schon durchgeführt wird.

- Gleistopologie: Im nächsten Schritt wird die Topologie aus der Geometrie abgeleitet. Topologische Knotenpunkte sind Weichen oder Gleisenden; Kreuzungsweichen werden topologisch durch bis zu vier Weichen repräsentiert. Die topologischen Punkte werden aus der Geometrie berechnet und die dazwischenliegenden Streckenelemente als topologische Gleiskanten identifiziert. Ergebnis eine ist eine Topologie, bei der die geometrisch beschriebenen Streckeneigenschaften auf Kanten mit wahren Längen bezogen sind.

- Ergänzung weiterer streckenspezifischer Daten: Die Aufnahme der weiteren streckenspezifischen Daten kann parallel zur Aufnahme der Topologie erfolgen, indem auf dem Weg von einem Referenzpunkt zum nächsten neben den Daten zur Aufnahme der Topologie diese Daten mit entsprechender Genauigkeit aufgenommen werden. Beispiele sind Angaben zu Belastbarkeit des Oberbaus, Lichtraumprofil, Notbremsüberbrückung oder Traktionsstromversorgung.

---

#### 8.2.2 Kategorien fahrzeugspezifischer Konfigurationsdaten

CBTC-Systeme haben Bremsmodelle, die gemäß der für das jeweilige Fahrzeug charakteristischen Parameter in anwendungsspezifisch konfigurierbaren Systemen hinterlegt werden. Möglicherweise müssen diese Parameter durch praktische Erprobungen ermittelt werden. Zu bestimmen sind die folgenden Fahrzeugparameter:

Traktionsabschaltung: Zeit vom Einleiten einer Zwangsbremsung bis die Zugkraft abgebaut ist.

• Reaktionszeit: Zeit bis zur Übertragung des Bremssignals im Zugverband und die Aufbauzeit der Bremskraft in den Bremssystemen der einzelnen Wagen.

• Bremsverzögerung: Mittlere Verzögerung während der Abbremsung, gestaffelt nach verschiedenen Geschwindigkeitsbereichen.

Die Bremsmodelle werden in der Regel für jede Fahrzeugserie unterschiedlich parametrisiert. Die Parameter können für die Betriebsbremsung und für die Zwangsbremsung für jedes Bremsmodell unterschiedlich festgelegt werden. Sicherheitsrelevant ist nur die Zwangsbremsung.

#### 8.2.3 Qualitätsmerkmale von Konfigurationsdaten

Durch welche Eigenschaften der Eingangsdaten oder der Projektierungsdaten kann die geforderte Qualität von Projektierungsdaten beschrieben werden? Zur Beschreibung der Qualität von Eingangsdaten wurden in (Schroeder 2002) folgende wesentlichen Qualitätsmerkmale identifiziert:

- Strukturelle Konsistenz: Die strukturelle Konsistenz bezieht sich auf die Abbildung der real existierenden physikalischen Objekte (Gleis, Weiche, usw.) als Informationen innerhalb eines Datenmodells. So dürfen zwischen zwei benachbarten Gleisabschnitten keine Sprünge in ihrer Lage existieren. Zwei Datenquellen dürfen nicht einen eindeutigen Punkt in der Realwelt mit zwei nicht eindeutig ineinander überführbaren Koordinaten beschreiben (Schroeder 2002).

- Vollständigkeit: Der Wirkbereich einer Zugsicherungsanlage muss informationstechnisch vollständig über Projektierungsparameter beschrieben sein. Eine unvollständige Beschreibung des realen Streckenabbildes führt dazu, dass die Technik ihre Sicherungsfunktion nicht vollständig über den gesamten Wirkbereich wahrnehmen kann (Schroeder 2002).

• Aktualität: Projektierungsdaten können nach der Häufigkeit der Aktualisierung in statische und dynamische Daten unterschieden werden. Für Projektierungsdaten, die häufig geändert werden müssen oder nur über einen kurzen Zeitraum beschränkt gültig

---

sind (zum Beispiel temporäre Langsamfahrstellen), ist die Aktualität der Daten ein wesentliches Qualitätsmerkmal (Schroeder 2002).

Genauigkeit: CBTC fordert, im Gegensatz zu konventionellen Systemen, metergenaue Angaben zu Standorten von sämtlichen relevanten Streckenelementen wie Signalen (sofern vorhanden), Balisen oder Weichen. Daher sind auch geeignete Messmethoden zu definieren.

Korrektheit: Durch „Papierprozesse“ und fehlende Schnittstellen findet eine Übergabe der Daten zwischen Projektphasen häufig in nicht maschinell lesbaren Formaten statt. Der deshalb notwendige manuelle Datentransfer ist durch hohe Aufwände und Fehleranfälligkeit geprägt. Wünschenswert sind durchgängige digitale Prozesse ohne Medienbrüche.

#### 8.2.4 Qualitätssichernde Prozesse für Konfigurationsdaten

Für die Entwicklung und Einführung von Zugsicherungssystemen müssen in Europa harmonisierte Sicherheitsnormen berücksichtigt werden. Anforderungen, die die Projektierung eines technischen Systems betreffen, leiten sich der DIN EN 50128 ab. In diesem Kapitel wird unterschieden zwischen der generischen Software (in der Regel Programme), die eine Zulassung für einen bestimmten Typ einer Zugsicherungstechnik hat, und den Projektierungsdaten, die je nach dem Anwendungsfall entsprechend generiert und im Laufe des Systemlebenszyklus gepflegt werden müssen. Im Rahmen der Qualitäts- sicherung für die Projektierungsdaten müssen die folgenden Dokumente erstellt werden:

- Daten-Generierungsplan: In diesem Dokument wird der Prozess der Datengenerierung beschrieben. Insbesondere müssen die einzelnen Verfahren zur Daten-Generierung sowie die verwendeten Softwaretools dargestellt werden, die im Rahmen des Datengenerungsprozesses verwendet werden. Insofern ist es erforderlich, dass neben der Beschreibung der Datenerfassung auch alle qualitätssichernden Prozesse erläutert werden. Für manuelle Handlungen muss die Qualifikation des eingesetzten Personals festgelegt werden. Für die verwendeten Werkzeuge (Soft- und Hardware) muss dargestellt werden (Koch et al. 2014; Schütte et al. 2008), dass diese frei von systematischen oder zufälligen Fehlern arbeiten. Gegebenenfalls muss auch die Unabhängigkeit zwischen der eigentlichen Datengenerierung sowie der Verifikation und Validation der projektierten Daten nachgewiesen werden (DIN EN 50128:2012-03).

- Daten-Testplan: In einem Daten-Testplan werden alle anzuwendenden, qualitäts-sichernden Maßnahmen festgehalten, die im Rahmen des Daten-Generierungsplans spezifiziert worden sind. Beispiele hierfür sind Testberichte, sowie Berichte im Rahmen der Verifikation und Validation der Projektierungsdaten (DIN EN 50128:2012-03).

- Daten-Testbericht: Die Ergebnisse der im Testplan spezifizierten Tests werden in einem Testbericht dokumentiert (DIN EN 50128:2012-03).

---

#### 8.2.5 Erfassung streckenspezifischer Konfigurationsdaten

Ausgangspunkt für die Projektierung von Streckeneinrichtungen sind Bestandspläne. Bestandspläne (englisch: „as built documentation“ oder im weiteren Verlauf des Lebenszyklus auch „as maintained documentation“) stellen den gegenwärtigen Zustand der Bahnanlagen und deren näherer Umgebung dar. In der Regel umfassen die Angaben die Beschreibung sämtlicher Bahnanlagen, Kilometrierungen der Gleise, geodätische Lage und Höhenfestpunkte, Krümmungs- und Neigungsverhältnisse der Gleise, Bauarten der Weichen und Kreuzungen, Gleisabstände, Gleisnummern, Signal- und Fahrstraßenbezeichnungen sowie Weichengrenzzeichen. Diese Unterlagen unterliegen einer Fortführungspflicht und sollten nach Möglichkeit zu jederzeit korrekt und aktuell sein (Adler et al. 1981). Die Hersteller von CBTC-Systemen benötigen all diese Angaben, um auf dieser Grundlage die Umbaumaßnahmen zu planen sowie die anwendungsspezifische Konfiguration des CBTC-Systems zu erstellen. Dort wo Bestandspläne nicht in der geforderten Qualität vorliegen, müssen diese zu Beginn eines Projekts mit hohem Aufwand aktuell erstellt werden. Falsche oder ungenaue Daten wie beispielsweise Distanzen können im Prozess der Realisierung, der Abnahme und im Betrieb lange unentdeckt bleiben. Dies kann zu zeit- und kostenintensiver Fehlersuche, sporadischen Störungen im Betrieb, betrieblichen Einschränkungen oder Behinderungen und in Extremfällen zu potenziellen Gefährdungen führen (Schütte et al. 2008).

Ein Beispiel, Projektierungsdaten effizient zu erfassen ist der Einsatz von Gleisgeometriemessfahrzeugen zur präzisen Aufzeichnung der mit CBTC auszurüstenden Strecke. Die von den Fahrzeugen erfassten Daten fließen nach entsprechender Nachprozessierung in den Aufbau des Streckenatlasses ein, der in den CBTC-Systemen sowohl an Bord von Zügen als auch in den Streckeneinrichtungen als gemeinsames Koordinatensystem von Fahrzeugen und Strecken verwendet wird. Die Gleisgeometriemessfahrzeuge sind in der Lage, die Gleislage mit höchster Präzision zu erkennen sowie aufzuzeichnen. Sämtliche Messungen werden von elektromechanischen, inertialen oder Lasermesseinrichtungen und einem elektronischen Datenverarbeitungssystem kontinuierlich aufgezeichnet. Idealerweise befinden sich die messtechnischen Einrichtungen auf einem für das jeweilige Netz zugelassenen Messfahrzeug. Auf diese Weise wird eine Aufzeichnung und die Speicherung der gemessenen Daten sowie eine Echtzeitauswertung bei Messgeschwindigkeiten von bis zu 90 km/h möglich (Cabrera 2009).

### 8.3 Umrüstung der Fahrzeuge mit CBTC-Fahrzeugsausrüstung

Die Fahrzeuge des Betreibers müssen mit CBTC-Fahrzeuggeräten ausgestattet werden. Hierbei kann es sich um neue Fahrzeuge handeln. In Bestandsnetzen müssen auch vorhandene Fahrzeuge umgerüstet werden. Bei der Ausrüstung von Fahrzeugen müssen Aspekte der betrieblichen, mechanischen und elektrischen Integration zwischen Fahrzeug

---

bauer und CBTC-Hersteller betrachtet werden (Schnieder et al. 2021). Außerdem müssen auch die wesentlichen Fahrzeugparameter (bspw. garantierte Bremskurven) abgestimmt werden.

#### 8.3.1 Definition betrieblicher Anwendungsfälle

Ausgangspunkt der Projektierung der Fahrzeugeinrichtungen ist immer die Erstellung eines Betriebskonzepts. Hierbei muss – ausgehend von der betrachteten Automatisierungstufe – dezidiert betrachtet werden, wie der Baukasten eines CBTC-Systems in der Betriebsabwicklung konkret angewendet werden soll. Zu betrachtende Aspekte sind hierbei unter anderem die Aufnahme in und die Entlassung aus verschiedenen Automatisierungsgraden sowie die Führung des Fahrzeugs in verschiedenen Betriebsarten (mit korrespondierenden Überwachungsfunktionen). Wesentlich ist – gerade bei einem Betrieb in GoA4 – insbesondere der betriebliche Ablauf bei technischen Störungen sowie Notfall- und Rettungskonzepte. Die verschiedenen betrieblichen Anwendungsfälle müssen in den folgenden Integrationsschritten hinsichtlich ihrer Auswirkung auf die konkreten technischen Eigenschaften des CBTC-Systems betrachtet werden.

#### 8.3.2 Definition Mechanische Integration des CBTC-Fahrzeuggeräts

Gemeinsam mit dem Lieferanten des CBTC-Systems und der mit dem Fahrzeugumbau beauftragten Firma wird die Positionierung der erforderlichen CBTC-Komponenten an und in den Fahrzeugen festgelegt. Hierbei sind vor allem die folgenden Komponenten in das Fahrzeug zu integrieren:

- Gehäuse (Geräteschrank/Geräteschränke oder Unterflurcontainer) für die zentralen und im Zugverband redundanten Rechnereinheiten. Dies umfasst Baugruppenträger für die sicherheitsrelevanten Funktionen des Zugbeeinflussungssystems (Automatic Train Protection, ATP), für Funktionen der nicht sicheren Fahrzeugsteuerung einschließlich der automatisierten Fahr-/Bremssteuerung und der automatischen Türsteuerung (Automatic Train Operation, ATO) sowie Steckerfelder für die Übernahme und Übergabe weiterer Signale von und zur Fahrzeugsteuerung zur Übernahme weiterer Automatisierungsfunktionen für höhere Automatisierungsgrade (bspw. Auf- und Abrüsten des Fahrzeugs).

- Konventionelle Schaltungstechnik zur Anpassung der Einzelsignale zwischen Zugsicherungssystem und Fahrzeug. Fahrzeugsignale müssen aus Sicherheitsgründen oft für das Zugsicherungssystem aufgearbeitet werden (Bereitstellung 2-kanaliger Signale). Signale die vom Zugsicherungssystem ausgegeben werden, können oft die Fahrzeugkomponenten nicht direkt ansteuern.

---

• Komponenten für die Kommunikation mit der Streckenausrüstung. Hierbei müssen Fahrzeugantennen unter dem Fahrzeug für das Auslesen von Transpondern für die Synchronisation der Weg- und Geschwindigkeitsmessung positioniert werden. Dafür müssen produktspezifische physikalische Besonderheiten, wie ausreichende eisenfreie Bereiche um die Antenne berücksichtigt werden. Auch muss für diese zusätzlichen Anbauten unter dem Fahrzeug die Profilfreiheit nachgewiesen werden, das heißt sie dürfen nicht so weit in den Gleisbereich ragen, dass sie beispielsweise mit bereits vorhandenen streckenseitiger Antennen von Altsystemen in Kontakt kommen. Des Weiteren müssen Funkantennen für die kontinuierliche, bidirektionale Datenübertragung zwischen Fahrzeug und Strecke auf den Fahrzeugen vorgesehen werden. Ein wichtiges Kriterium für den Anschluss der Funkantennen sind die zulässigen maximalen Leitungslängen hin zu den entsprechenden Rechnerkomponenten sowie die Dämpfung durch Verbindungselemente. Die Funkantennen werden von den Betreibern bevorzugt hinter der Frontscheibe des Fahrzeugs installiert. Hierbei ist zu prüfen, ob es sich um mit Metall bedampfte Scheiben handelt, die unter anderem dafür sorgen, dass weniger Sonne in den Führerstand fällt. Leider dämpfen oder reflektieren solche metallbedampften Scheiben auch den Mobilfunkempfang erheblich, sodass andere Einbauorte für die Funkantennen auf dem Fahrzeug gefunden werden müssen.

- Komponenten zur direkten Weg- und Geschwindigkeitsmessung. Hierbei kann es sich je nach dem Odometriekonzept des jeweiligen Herstellers um verschiedene technische Komponenten handeln. Bei Wegimpulsgebern müssen freie Achslagerdeckel idealerweise nicht gebremster oder nicht angetriebener Achsen im Zugverband identifiziert werden. Auch die Verwendung eines gemeinsamen Polrads mit anderen Wegimpulsgebern der Fahrzeugsteuerung ist möglich. Die Radarsensoren sind so anzuordnen, dass die Radarkegel sich ungestört ausbreiten und Reflektion vom Untergrund ungestört empfangen werden können. Auch für möglicherweise eingesetzte Beschleunigungsgeber gibt es zu berücksichtigende Randbedingungen bei der Positionierung im Fahrzeug.

- Komponenten des Datenbusnetzwerks des Zugsicherungssystems. CBTC Systeme besitzen ein eigenes, von der Fahrzeugsteuerung unabhängiges Datenbusnetzwerk (meist Ethernet). Eine wichtige Komponente im Datenbusnetzwerk des CBTC Systems ist ein Modem für die Datenübertragung zwischen Fahrzeug und Strecke, welches wegen den zulässigen Leitungslängen zu den Antennen nicht im Bereich der zentralen Recheneinheit untergebracht werden kann. Hinzu kommen abhängig von der Fahrzeugkonfiguration diverse Switches beispielsweise zur Signalverstärkung.

Bedien- und Anzeigeelemente. Selbst Fahrzeuge, die hauptsächlich im begleiteten fahrerlosen oder unbegleiteten fahrerlosen Betrieb verkehren sollen, benötigen zusätzliche Bedien- und Anzeigeelemente für das Zugsicherungssystem. Beispiele hierfür sind die Displays, Taster und Störschalter. Diese sind gemäß den Vorgaben einschlägiger technischer Regelwerke auf dem Führerstand anzuordnen (vgl. UIC (2002) und DIN EN 16186-1:2019-04). Hierbei müssen neben der Einhaltung normativer Sichtfelder bei der Integration von Komponenten in den Führerstand auch Aspekte der Ergonomie mit Berücksichtigung finden.

---

Mechanische Integration bedeutet hierbei, entsprechend große Bauräume für die Komponenten im und am Fahrzeug zu identifizieren. Auch muss dafür Sorge getragen werden, dass die betreffenden Komponenten in einer Art und Weise befestigt werden müssen, dass diese dauerhaft den dynamischen Beanspruchungen des Bahnbetriebs standhalten. Außerdem dürfen durch die Befestigungen keine sicherheitsrelevanten Bauteile (z. B. Drehgestelle) in ihrer Substanz geschwächt werden. Bei Nachrüstungen ist auch das Gewicht des Fahrzeugs zu berücksichtigen. So darf durch die zusätzlichen Komponenten für ein Zugsicherungssystem die zulässige Achslast nicht überschritten werden.

#### 8.3.3 Elektrische Integration des CBTC-Fahrzeuggeräts

Allgemein ist das CBTC-System in die vorhandene Fahrzeugsteuerung zu integrieren. Hierbei muss bei Bestandsfahrzeugen die bestehende elektrische Ausrüstung des Fahrzeugs erfasst werden. Die fahrzeugseitigen Schnittstellen (Input/Output) sind neben funktionellen Stromlaufplänen zu beschreiben. Gerade bei Bestandsfahrzeugen ist zu prüfen, ob die Anforderungen an Sicherheitsfunktionen im Bereich der Fahrzeugsteuerung den aktuellen Sicherheitsanforderungen entsprechen (vgl. VDV (2009) und IEC 62267). Gegebenenfalls sind in Abstimmung mit der Zulassungsbehörde (z. B. Technische Aufsichtsbehörde, TAB) Modifikationen an der Fahrzeugsteuerung erforderlich. In der Regel kommt es hier zu einem größeren Abstimmungsbedarf zwischen dem Fahrzeughersteller und dem Lieferanten des CBTC-Systems. Die Signale zwischen Fahrzeugsteuerung und CBTC-System können in sichere und nicht-sichere Signale unterteilt werden.

- Sichere Signale/Funktionen: (SIL ≥ 1): Beispiele für sichere Eingangssignale von der Fahrzeugsteuerung an das CBTC-System sind Bestätigungstaster, Taster für den Start des halb automatischen Betriebs, Status der Sicherheitsbremse, Türstatus, Zugintegrität, Kuppelstatus. Beispiele für sichere Ausgangssignale des CBTC-Systems zur Fahrzeugsteuerung sind unter anderem die Ansteuerung der Sicherheitsbremse, die sichere Antriebssperre, bzw. Traktionsfreigabe (oft in Bestandsfahrzeugen fahrzeugseitig nicht vorhanden), die Türfreigabe und die Blockierung der Türen (Freigabe Türnotentriegelung).

- Nicht-sichere Signale/Funktionen (SIL < 1): Diese Signale sind zu definieren. Hier ist jeweils festzulegen, wie die Signale im Bereich der Fahrzeugsteuerung abgegriffen werden sollen, bzw. an diese übergeben werden sollen. Neben Hardwareänderungen am Fahrzeug sind ggf. auch Änderungen im Bereich der Software der Fahrzeugsteuerung erforderlich. Bevorzugt wird die Übertragung nicht sicherer Signale über den jeweiligen Fahrzeugbus (z. B. Multifunction Vehicle Bus, MVB oder Ethernet-Consist Network, ECN). Bei Bestandsfahrzeugen muss oft auf die Übertragung von Einzelsignalen zwischen Zugsicherungssystem und Fahrzeugsteuerung zurückgegriffen werden.

---

### 8.4 Umrüstung der Strecke mit CBTC-Streckenausrüstung

Die Umrüstung der Streckeneinrichtung auf das neue CBTC-System ist Gegenstand detaillierter Planungen. Es hat sich allgemein bewährt, die gesamte Baumaßnahme in einzelne Baustufen zu trennen. Hierbei müssen die Baustufenschnittstellen sowohl in technischer als auch in betrieblicher Hinsicht sauber geplant werden. In der Regel beginnen die Baumaßnahmen in einem schwach befahrenen Streckenabschnitt in der Peripherie, um die Auswirkungen auf den Betrieb möglichst gering zu halten. Sind die eingesetzte Technik und die Bauabläufe erprobt, folgen betrieblich höher belastete Streckenbereiche.

Der Umfang der Umrüstung bestimmt die konkrete Bauablaufplanung. Hierbei ist eine Betrachtung erforderlich, welche Komponenten ggf. wiederverwendet werden können oder ob Komponenten des neuen CBTC-Systems parallel zum Bestandssystem installiert werden können:

- Optionale Lichtsignale: Falls erforderlich können neue Lichtsignale parallel zu den bestehenden Lichtsignalen des Bestandssystems installiert werden. Die Signale unterstützen einen möglichen Mischbetrieb oder einen Betrieb auf der Rückfallebene in CBTC-Systemen.

- Komponenten der sekundären Gleisfreimeldung: Achszähler für die sekundäre Gleisfreimeldung können problemlos als Rückfallebene parallel zu herkömmlichen Gleisfreimeldesystemen installiert werden.

Kabelanlage: Die Installation der neuen CBTC-Streckenausrüstung erfordert nach wie vor die Verlegung mehrerer Kupfer- und Glasfaserkabel entlang der Strecke. Der Zustand der bestehenden Kabelträge muss untersucht werden. Manchmal sind neue Kabelträge Kabelkanäle unvermeidlich, da die alten Kabelträge nicht mehr verwendet werden können.

• Technikräume: Die Standorte und die Anzahl der vorhandenen technischen Gebäude ergeben sich zumeist aus der Architektur und Technologie des Altsystems. Für neue Systeme gelten andere Zwänge. Auch zwischen den Anbietern gibt es Unterschiede. Typischerweise haben neue Systeme einen eher zentralen Ansatz. Die Vor- und Nachteile der Beibehaltung bestehender Standorte oder der Auswahl neuer Standorte müssen gegeneinander abgewogen werden.

• Leitstelle: Die neue Betriebsleitstelle kann parallel zur alten Betriebsleitstelle eingerichtet werden. Hierbei wird wegen der technischen Komplexität meist auf technische Schnittstellen zwischen altem und neuem System verzichtet.

Zur Risikominderung und Minimierung der betrieblichen Auswirkungen während der Migration, werden streckenseitige Umschalteinrichungen zwischen der neuen Zugsicherungs- anlage und dem Bestandssystem empfohlen. Die neue Zugsicherungsanlage sollten über

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b0089b3a-d31e-4965-b85f-f3a49365db9d/markdown_0/imgs/img_in_image_box_134_65_793_882.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A35%3A06Z%2F-1%2F%2Fbd12d3dc480ac89339e473b0e90f3d499e390751c989a85eaef3914fcd672eea" alt="Image" width="69%" /></div>


<div style="text-align: center;">Abb. 8.1 Kennzeichnung ungültiger Signale nach erfolgter Umschaltung</div>


eine Umschalteinrichtung mit den Feldelementen (Weichenantriebe, Signale) verbunden sein. Die Umschalteinrichtung ermöglicht eine effiziente Prüfung und Inbetriebnahme während der betriebsfreien Zeit.

Ist die Umschaltung erfolgreich vorgenommen und das CBTC-System im Fahrgastbetrieb, müssen die Signale des Altsystems als ungültig gekennzeichnet werden (vgl. Abb. 8.1). Dies geschieht durch Abdecken oder eine besondere Kennzeichnung (bspw. ein weißes Kreuz mit schwarzem Rand). Ist über eine gewisse Zeitspanne der störungsfreie Fahrgastbetrieb erfolgreich nachgewiesen worden, kann zu guter letzt die Demontage der Komponenten des Altsystems erfolgen. Dies ist in der Regel nicht mehr zeitkritisch und kann über einen längeren Zeitraum innerhalb der verfügbaren nächtlichen Sperrpausen ohne negative Auswirkungen auf den Fahrgastbetrieb erfolgen.

---

### 8.5 Definition der Teststrategie und Testdurchführung

CBTC-Systeme sind komplex und weisen viele in Bezug auf das konkrete Kundenprojekt konfigurierbare Merkmale auf. Die Erfahrung der Hersteller mit der Inbetriebnahme von CBTC-Systemen und umfassende Testaktivitäten gewährleisten, dass ein sicherer Fahrgastbetrieb aufgenommen werden kann. Die von den Herstellern verfolgten Teststrategien zielen darauf ab, Testaktivitäten im Feld auf das absolut erforderliche Mindestmaß zu beschränken. Allerdings können Testaktivitäten im Feld aus folgenden Gründen nicht vollständig vermieden werden (Diemunsch 2016):

- Betreiberspezifische Anpassungen: Die Betreiber fordern eine betreiberspezifische Zugsicherungstechnik, welche sie auf ihre spezifischen Besonderheiten anpassen möchten. Dies ist beispielsweise dann der Fall, wenn die Betreiber zusätzlich Funktionen fordern, die nicht dem Standardfunktionsumfang der herstellerspezifischen Produkte entsprechen. Teilweise sind die Betreiber aber auch zu Anpassungen gezwungen. Dies ist beispielsweise dann der Fall, wenn Fahrzeugeinrichtungen in die vorhandene Fahrzeugflotte integriert werden müssen. Die Tests insbesondere der Integration der Fahrzeugeinrichtungen in die Fahrzeuge können nicht im Hause des Herstellers durchgeführt werden.

• Konkrete Gegebenheiten im Feld: Wesentliche Effekte zeigen sich erst bei einer praktischen Erprobung im Feld. So erfordern beispielsweise sowohl die Zugortung als auch die Datenübertragung über Funk besondere Tests. Bei funkbasierten Systemen ist im Feld eine ausreichende Ausleuchtung der Strecke durch ausreichend viele Testfahrten zu bestätigen.

Das Erfordernis, Testaktivitäten zu optimieren wird insbesondere dadurch verstärkt, dass es sich bei einer Vielzahl aktueller CBTC-Projekte um eine Modernisierung von Zugsicherungssystemen in bestehenden Anlagen handelt. Hier muss der Umbau der Zugsicherungsanlagen mit minimalen Auswirkungen auf den Fahrgastbetrieb erfolgen. Diese Randbedingung erhöht die Komplexität der Projekte durch den auf die (kurzen) nächtlichen Sperrpausen beschränkten Zugang zur Strecke für die Montage, Tests und In- betriebnahme. Aus diesem Grund müssen die Testaktivitäten optimiert werden, um einen Umbau während des laufenden Betriebs zu ermöglichen. Dies geschieht dadurch, dass möglichst viele Tests bereits in den Testlaboren der Hersteller oder auf dedizierten Testgleisen der Betreiber durchgeführt werden.

#### 8.5.1 Umwelttests

Bereits in der Entwicklung der generischen Anwendungen werden die entwickelten CBTC-Systeme gegen zu erwartende Umwelteinflüsse getestet. Diese Testergebnisse

---

werden für die spezifische Anwendung dahingehend überprüft, ob die in dem Test nachgewiesenen Umwelteigenschaften auch für das betreffende Projekt zutreffen. Weichen die tatsächlichen Umwelteigenschaften von den spezifizierten Umwelteigenschaften des Produkts ab, muss eine Änderungsauswirkungsanalyse durchgeführt werden. Der Nachweis der Umwelteigenschaften umfasst die folgenden Aspekte:

- Elektromagnetische Verträglichkeit (EMV): Hierbei wird einerseits bewertet, ob auf den Prüfling wirkende elektromagnetische Felder einen Einfluss auf diesen haben. Andererseits werden auch die vom Prüfling emittierten elektromagnetischen Felder bewertet. Grundlage der Prüfungen sind einschlägige harmonisierte Normen (DIN EN 50121-1:2017).

Klimatetests: Bei diesen Tests wird der Prüfling extremen Maximal- und Minimal-temperaturen ausgesetzt. Hierbei wird eine definierte Anzahl an Temperaturzyklen durchlaufen. Ebenso wird der Prüfling unterschiedlichen Luftfeuchtigkeiten ausgesetzt (DIN EN 50155:2018).

• Mechanische Tests: Das Betriebsmittel muss ohne Verschlechterung der Eigenschaften ohne Fehlfunktionen Schwing- und Schockeinwirkungen, wie sie im Betrieb auftreten können, standhalten. Bei den genommten Testzyklen wird der Prüfling einer hochfrequenten Schwingung ausgesetzt. Weitere Tests umfassen Schocktests, welche eine mechanische Belastung in Form eines Stoßes simulieren (DIN EN 61373:2011-04).

- Schutz elektrischer Betriebsmittel: Die Gehäuse elektrischer Betriebsmittel erfüllen verschiedene Schutzarten. Die Schutzarten zielen zum einen auf den Schutz von Personen gegen Berühren unter Spannung stehender Teile innerhalb der Gehäuse ab (Berührungsschutz). Darüber hinaus dienen die Gehäuse dem Schutz des Betriebsmittels gegen Eindringen von Fremdkörpern, einschließlich Staub (Fremdkörperschutz). Außerdem schützen die Gehäuse das Betriebsmittel gegen schädliche Einwirkungen durch das Eindringen von Wasser (Wasserschutz). Die Schutzart durch ein Gehäuse wird anhand genormter Prüfverfahren nachgewiesen. Zur Klassifizierung dieser Schutzart wird der so genannte IP-Code verwendet (DIN EN 60529:2014-09).

#### 8.5.2 Fabriktests

Um Testaktivitäten im Feld weitgehend zu minimieren werden umfassende Tests in den Testcentern der Hersteller durchgeführt (Wigger 2016). Hierbei wird das CBTC-System in Simulationsumgebungen eingebettet. Auf diese Weise wird das CBTC-System bevor die Software im Feld getestet wird unter kontrollierten Bedingungen „auf Herz und Nieren“ getestet. Hierdurch wird schon frühzeitig eine weit reichende Anforderungsermittlung nachgewiesen und mögliche Fehler in der Software erkannt. Oftmals nimmt auch der

---

Betreiber an den Testaktivitäten teil (Factory Acceptance Test, FAT). Die folgenden Teststellungen können in den Testcentern der Hersteller effektiv bearbeitet werden:

Tests interner Schnittstellen des CBTC-Systems: Alle Nachrichten zwischen Leittechnik und dem Fahrzeuggerät, der Leittechnik und dem Streckengerät sowie zwischen dem Strecken- und dem Fahrzeuggerät werden getestet. Hierbei können Tests entweder auf realer oder emulierter Hardware durchgeführt werden.

CBTC-Funktionstests: Abgeleitet von den funktionalen Anforderungen im Projekt werden alle Funktionen mindestens an einer Stelle im Netz exemplarisch getestet.

• Größtmögliche Testabdeckung externer Schnittstellen: Hier muss insbesondere die Schnittstelle zwischen dem Streckengerät und dem konventionellen Zugsicherungssystem (Stellwerke) vollständig getestet werden. Gleichfalls sind aufwändige Tests der Schnittstelle zur Leittechnik erforderlich. Hierfür müssen Schnittstellensimulationen von den Herstellern selbst aufgebaut werden oder von den Herstellern externer Umsysteme bereitgestellt werden.

• Fehlereinstreuungstests: Im Testcenter können Fehlereinstreuungstests durchgeführt werden, die im Feld so nicht getestet werden können. Ein Beispiel hierfür ist die Vertauschung oder Verfälschung von Botschaften auf dem Funkkanal zum Nachweis der Wirksamkeit der getroffenen Sicherheitsmechanismen des Kommunikationsprotokolls.

- Unterstützung von Feldtests durch Nachstellen von Fehlern: Das Ziel der Tester im Feld ist es, einen erfolgreichen Nachweis der korrekten Funktion zu führen und nicht, Fehler aufzuspüren. Sobald die Tester im Feld einen Fehler erkennen, wird er den Testern im Testcenter gemeldet. Im Testcenter wird der Fehler mit der Hilfe von Entwicklung und Projektierern nachgestellt und analysiert. Die gewonnenen Erkenntnisse fließen in einen Korrekturstand der Software zur Inbetriebnahme ein. Kann der Fehler bis zur Inbetriebnahme nicht behoben werden, kann das CBTC-System gegebenenfalls vorübergehend mit betrieblichen Einschränkungen in Betrieb genommen werden.

#### 8.5.3 Fahrzeugtests

Ein wesentlicher Anteil an Projektaktivitäten erfolgt im Zusammenhang mit der Integration der CBTC-Fahrzeugeinrichtungen in die Fahrzeuge des Betreibers. Hierbei werden im Verlaufe eines Projekts verschiedene Tests mit den Fahrzeugen durchgeführt. Dies erfordert in der Regel eine enge Abstimmung zwischen dem Hersteller der CBTC-Systeme und dem Fahrzeughersteller.

- Ermittlung der Fahrzeugeigenschaften: Diese Testaktivität dient nicht dem Nachweis. Es müssen im Projekt vielmehr frühzeitig die (fahrdynamischen) Eigenschaften der Fahrzeuge erfasst und mit dem Fahrzeughersteller und Betreiber abgestimmt werden. Eine wesentliche Information sind Aussagen über die garantierte Zwangsbremsverzögerung, aber wegen der ATO-Funktion (Automatic Train Operation) auch die mög

---

liche Beschleunigung der Züge auf ebener Strecke. Die Angaben fließen in die projekt- spezifische Konfiguration der Software der ATP- und ATO-Fahrzeuggeräte ein.

Mechanische und elektrische Tests: Die ersten beiden Fahrzeuge eines Typs werden in der Regel als Prototypen umgesetzt. Hierbei wird die mechanische Integration der eingebauten CBTC-Komponenten besonders beachtet und es werden letzte offene Punkte geklärt. Die elektrischen Verbindungen werden genauso getestet wie die Kommunikation mit anderen elektronischen Systemen an Bord des Fahrzeugs. Die Tests an den Prototypenfahrzeugen erstrecken sich in der Regel über mehrere Wochen.

Statische und dynamische Inbetriebnahmetests der Fahrzeugeinrichtung: Für jedes installierte Fahrzeug wird die korrekte Montage der Fahrzeugeinrichtung geprüft. Für den Nachweis der korrekten Funktion der Sensoren für die Weg- und Geschwindigkeitsmessung ist eine kurze Fahrzeugbewegung erforderlich. Für die ATO müssen auch die Fahrzeugeigenschaften (Fahrdynamik) noch einmal betrachtet werden. Da die Ermittlung der Fahrzeugeigenschaften nur an ausgewählten Fahrzeugen durchgeführt wurde, können die tatsächlichen Fahrzeugeigenschaften in der Flotte abweichen. In diesem Fall kann es erforderlich werden, dass die projektspezifische Konfiguration der Fahrzeugsoftware an die Erkenntnisse der Fahrzeugtests angepasst werden muss. Um den Nachweis der korrekten Funktion der CBTC-Schutzfunktion für jeden Fahrzeugtyp zu erbringen, muss die CBTC-Streckeneinrichtung (Streckengerät und Funkausleuchtung) für mindestens einen Streckenbereich (zum Beispiel ein Testgleis im Betriebshof des Betreibers) vorhanden sein.



#### 8.5.4 Testgleis im Betriebshof

In Projekten werden üblicherweise Testgleise mit CBTC-Streckeneinrichtungen ausgerüstet. Diese Testgleise befinden sich üblicherweise auf Betriebshöfen oder in ihrer unmittelbaren Nachbarschaft. Hierbei sollten nach Möglichkeit alle betrieblich relevanten Streckenkonfigurationen und Anlagenelemente (beispielsweise verwendete Signaltypen) vorgesehen werden. Die Topologie des Testgleises sollte so gewählt werden, dass eine Aufnahme und Entlassung in einen automatischen Betrieb sowie ein Halt an einer oder mehreren virtuellen Haltestellen abgebildet werden kann.

Die Einrichtung eines Testgleises ist aus mehrerlei Gründen sinnvoll:

• Test der Fahrzeugeinrichtung: Nachweis der korrekten Funktion der Schnittstellen zwischen Fahrzeugeinrichtung und Fahrzeugleittechnik für die ersten Prototypenfahrzeuge.

• Systemtests: Nachweis der betreiberspezifischen CBTC-Funktionen

Statische und dynamische Inbetriebnahmetests für Serienfahrzeuge: Für jedes installierte Fahrzeug werden nach erfolgter Installation ausgewählte Testfälle durchgeführt. Diese umfassen beispielsweise den Aufbau einer Funkverbindung, die Lokalisierung

---

nach Überfahrt einer Ortsbake, den Empfang eines Fahrbefehls, eine anschließende kurze Fahrt und einen Abbau der Funkverbindung.

- Schulung: Die Fahrzeugführer müssen frühzeitig in den Betrieb mit dem neuen Zugsicherungssystem eingewiesen werden. Zu diesem Zweck muss das Testgleis eine ausreichende Länge aufweisen.

• Regressiontests: In der Ausrüstungsphase entstehende Korrekturstände der Software werden vorab im Testgleis getestet. Dies gilt auch für Korrekturen und Änderungen nach Aufnahme des Fahrgastbetriebs.

#### 8.5.5 Inbetriebnahmetests der Streckeneinrichtung

Die Tests an der Streckeneinrichtung erfolgen in mehreren aufeinander aufbauenden Schritten:

## Übereinstimmungsprüfung

Bevor die Durchführung von funktionalen Testfällen beginnen kann, muss die korrekte Ausführung der Installation getestet werden. Hierbei wird neben der korrekten Ausführung der Kabelarbeiten und der Erdung insbesondere die korrekte Zuordnung der realen Außenanlagenelemente zu ihren logischen Entsprechungen in der Software der CBTC-Streckeneinrichtung und der Leittechnik geprüft. Der Abschluss dieser Teststufe markiert den Übergang von der Installationsphase in die Testphase.

## Tests des Datenkommunikationssystems (insbesondere Funk)

Neben anderen CBTC-Subsystemen ist das Datenkommunikationssystem das erste zu installierende und zu testende System. Es werden Glasfaserkabel zwischen den Technikräumen entlang der Strecke verlegt und getestet. Ebenso werden Netzwerk-Switche installiert und getestet. Ein Netzwerkmanagement-System zur Verwaltung des Netzwerks muss vor Testdurchführung vorhanden sein. Hierüber können Nachweise zu korrekten Konfigurationen der Netzwerkswitche, der Datentransferraten sowie Latenzzeiten im Netzwerk erfasst werden. Aufbauend auf dieser Betrachtung des Netzwerks entlang der Strecke kann die eine ausreichende Funkabdeckung entlang der Strecke nachgewiesen werden. Der Nachweis der Funkabdeckung erfordert mindestens ein mit spezieller Messausrüstung ausgerüstetes Fahrzeug. Alternativ kann auch eine Messeinrichtung auf Fahrzeugen installiert werden, die im regulären Fahrgastbetrieb „mitschwimmen“. Prüfwerkzeuge messen zum einen die Stärke des elektromagnetischen Feldes der Funkverbindung auf dem Fahrzeug. Gleichzeitig können auch kontinuierlich Datenpakete über den Funkkanal gesendet werden, um die Paketverlustrate zu überwachen. Sollte das Fahrzeug über zwei redundante Fahrzeuggeräte an jedem Zugende verfügen, werden diese Tests gleichzeitig für beide Fahrzeuggeräte durchgeführt. Die Züge fahren für die Durchführung der Funkabdeckungstests zunächst mit langsamer Geschwindigkeit. Hierbei kann auch gezeigt werden, dass das Hand-over der Funkverbindung zwischen benachbarten Access Points bruchlos funktioniert. Es ist ebenfalls sinnvoll, worst-case-Bedingungen zu testen. Dies ist beispielsweise dann der Fall, wenn Access Points weit voneinander entfernt sind oder die

---

Signalausbreitung zwischen Access Points und Fahrzeug durch ein oder zwei zwischenstehende Fahrzeuge abgeschattet ist. Anschließend erfolgen Tests mit maximal zulässiger Streckengeschwindigkeit in allen Streckenbereichen. Der Test der Funkstrecke ist essenziell für das Fortschreiten der Testaktivitäten. Bestehen Lücken in der Funkabdeckung, können die funktionalen Testfälle (beispielsweise zur Lokalisierung des Zuges) nicht durchgeführt werden.

## Nachweis der Ortungsfunktion

Diese Tests weisen nach, dass der Zug in der Lage ist, seine Position hinreichend genau zu bestimmen und seine aktuelle Position im Streckennetz auf dem Fahrzeug zur Verfügung zu haben. Die Tests zum Nachweis der Ortungsfunktion setzen voraus, dass die Information über die Weichenlagen in der CBTC-Streckeneinrichtung vorhanden sind und dass eine Funkverbindung zwischen der CBTC-Streckeneinrichtung und der CBTC-Fahrzeug-einrichtung besteht. Neben den Testaktivitäten zum Datenkommunikationssystem ist der Nachweis der Ortungsfunktion die zweite Testaktivität im Feld. Diese beiden Nachweise sind die Grundlage für einen CBTC-Betrieb. Obwohl diese elementaren Funktionen nur einen kleinen Teil des Funktionsumfangs der CBTC-Systeme ausmachen, sind für diese Nachweise viele Sperrpausen erforderlich, da diese Tests auf allen Gleisen in beiden Fahrtrichtungen durchgeführt werden müssen.

## I ntegrationtests

Die Integration umfasst sowohl das Zusammenwirken der einzelnen Teilsysteme der CBTC-Systemlösung eines Herstellers als auch das Zusammenwirken mit den externen Schnittstellen des CBTC-Systems in der Systemlandschaft des Betreibers. Als Beispiel sind hier Schnittstellen zur Fahrgastinformation, Gebäudeautomatisierung, Traktionsstromversorgung aber möglicherweise auch anderer signaltechnischer Systeme genannt (beispielsweise Stellwerke) für den Fall, dass die CBTC-Systemlösung als Overlay zu einer bestehenden Fahrwegsicherung eingesetzt werden soll (Brückner 2017).

## Funktionstests

Nachdem die Tests für das Datenkommunikationssystem, die Ortungsfunkion und die Systemintegration erfolgreich verlaufen sind, können funktionale Tests durchgeführt werden. In der Regel werden hierfür Testumfänge aus den Fabriktests wiederholt. Die Herausforderung im Testmanagement liegt hierbei darin, eine sinnvolle Auswahl der zu testenden Funktionen einerseits zu treffen und andererseits die erforderliche räumliche Testabdeckung zu definieren. Stehen zunächst die sicherheitsrelevanten Funktionen im Vordergrund, werden hierauf aufbauend die automatisierungstechnischen Anteile getestet:

- Funktionstest Automatic Train Protection: Hierzu werden Nachweise konkreter Schutzfunktionen wie die Verhinderung der Überfahrt eines Gefahrpunktes getestet. Ebenso kann das Setzen und das Rücknehmen einer vorübergehenden Langsamfahrstelle für jeden Stellbereich einer CBTC-Streckeneinrichtung exemplarisch getestet werden.

---

- Funktionstest Automatic Train Operation: Für den Nachweis einer korrekten automatischen Steuerung der Züge gemäß der gültigen Geschwindigkeitsvorgaben werden spezifische Tests durchgeführt. Hierbei werden verschiedene Fahrzeuggeschwindigkeiten und Geschwindigkeitswechsel im statischen Geschwindigkeitsprofil getestet, um zu zeigen, dass der Zug die gewünschten Geschwindigkeitsvorgaben effektiv umsetzt. Gleiches gilt für die Haltegenauigkeit im Stationsbereich. Diese Tests erfolgen für alle Gleise in beiden Fahrtrichtungen.

- Funktionstest Automatic Train Supervision: Auch wenn der Großteil leittechnischer Funktionen bereits im Testcenter der Hersteller getestet werden kann, werden einige komplexe leittechnische Funktionen erst wirksam im Feld getestet. Eine erste Funktion, die getestet werden kann ist die Zuglaufverfolgung. Hierauf aufbauend können die Wechselwirkungen zwischen der Zuglaufverfolgung und dem Fahrplanmanagementsystem (beispielsweise hinsichtlich der Zuordnung von Fahrplanfahrten zu Zügen) sowie Funktionen der Konflikterkennung und Konfliktlösung getestet werden.

## Site Acceptance Tests (SAT)

Der Betreiber kann es sich vorbehalten, alle Testaktivitäten im Projekt zu begleiten und die vorgelegten Testnachweise zu bestätigen (Wigger 2016). In der Regel werden für den SAT aus der Systemanforderungsspezifikation abgeleitete Testfälle durchgeführt. Um den Zieltermin für die Inbetriebnahme des CBTC-Systems sicherzustellen, kann die Betriebsaufnahme zunächst gegebenenfalls nur mit einem reduzierten Funktionsumfang erfolgen. Komplexere (leittechnische) Funktionen können dann in Abstimmung mit dem Betreiber zu einem späteren Zeitpunkt ergänzt werden.

## Betriebserprobung (Schattenbetrieb)

Der Schattenbetrieb ist ein Testkonzept für Erneuerungsprojekte. Hierbei liegt die Sicherheitsverantwortung im bestehenden Zugsicherungssystem. Das neue Zugsicherungssystem läuft parallel mit und empfängt alle relevanten Führungsgrößen, greift bei erkannten Abweichungen aber nicht aktiv in den Prozess ein. Diese Phase kann sich möglicherweise über mehrere Monate erstrecken. In einem nächsten Schritt können zwischen den regulären Zugfahrten einzelne Zugfahrten ohne Fahrgäste unter CBTC-Überwachung durchgeführt werden. Verlaufen auch diese erfolgreich, kann eine Freigabe für den Betrieb mit Fahrgästen erfolgen (Dombrowsky et al. 2008).

## Zuverlässigkeitserprobung

Diese Testaktivitäten haben zum Ziel, den Nachweis zu erbringen, dass das CBTC-System die vertraglich fixierten Performance-Kennwerte (RAMSS) erfüllt. Hierfür werden bereits zum Zeitpunkt der Vertragsunterzeichnung zwischen Hersteller und Betreiber die konkreten Modalitäten der Nachweisführung festgelegt. Die Festlegungen umfassen die relevanten Kenngrößen (zum Beispiel die Mean Time Between Failure, MTBF), die zu betrachtende Grundgesamtheit (beispielsweise eine Linie), den Zeitraum der Tests sowie statistische Randbedingungen des Nachweisverfahrens (beispielsweise Chi-Quadrat-Tests mit einem bestimmten Konfidenzintervall). Die Nichteinhaltung der Zuverlässigkeitskennwerte ist gegebenenfalls mit einer Vertragsstrafe belegt.

---

### 8.6 Anpassung betrieblicher Regelwerke für den automatisierten Betrieb

In den Verkehrsunternehmen legen Dienstanweisungen legen fest, wie die rechtlichen Vorgaben im jeweiligen Verkehrsunternehmen umzusetzen sind (Schröter 2008). Nachfolgend werden zunächst die grundlegenden Prinzipien beschrieben, die der Erstellung des betrieblichen Regelwerks für eine exemplarische fahrerlose Linie zu Grunde liegen (Abschn. 8.5.1). Es schließt sich eine Darstellung der gewählten Vorgehensweise mit den Meilensteinen und Aufgaben an, die sich in die Logik eines sicherungstechnischen Ausrüstungsprojekts einfügt (Abschn. 8.5.2). Abschließend erfolgt eine Darstellung der Rollen und Verantwortlichkeiten in Bezug auf die Erstellung der betrieblichen Regelungen (Abschn. 8.5.3).

#### 8.6.1 Prinzipien der Regelwerksanpassungen in Erneuerungsprojekten

Die Erstellung der betrieblichen Regelwerke für eine fahrerlose U-Bahn-Linie zum Beispiel orientiert sich an mehreren grundlegenden Prinzipien (Schnieder 2024).

## Prinzip 1: Frühzeitiger Beginn der projektbegleitenden Ausarbeitung des betrieblichen Regelwerks

Dieses Prinzip ist wichtig, da die systemtechnische Ausprägung einer fahrerlosen U-Bahn-Linie und die betrieblichen Regeln wechselseitig aufeinander bezogen sind. Die gegenseitigen Bezüge stellen sich wie folgt dar:

• Auswirkungen des (bestehenden) betrieblichen Regelwerks auf den (zu wählenden) technischen Entwurf: Die bestehenden oder gewünschten betrieblichen Regelungen sind Ausdruck der Anforderungen des jeweiligen Verkehrsunternehmens. Diese Anforderungen wirken sich auf Details der vom Hersteller gewählten technischen Lösung aus. Gerade in der Phase der Pflichtenhefterstellung ist es daher wesentlich, dass Hersteller und Betreiber hier eng und partnerschaftlich zusammenarbeiten (Abb. 8.2).

• Auswirkungen des (zu wähenden) technischen Entwurfs auf das (bestehende) betriebliche Regelwerk: Die vom Hersteller gewählten technischen Lösungen beeinflussen die betrieblichen Regelungen des Verkehrsunternehmens für die Betriebsabwicklung auf

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//05e2d09c-b9ca-4037-9c4f-ce47dc75746a/markdown_0/imgs/img_in_image_box_213_1087_728_1265.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A35%3A36Z%2F-1%2F%2F21a105cbe674275fa9207bfd8e2349416319e02ca093507c45f46f0f59440fb3" alt="Image" width="54%" /></div>


<div style="text-align: center;">Abb. 8.2 Wechselseitige Beziehung zwischen betrieblichem Regelwerk und Entwurfsentscheidungen</div>

---

der fahrerlosen Linie – insbesondere auch deshalb, weil die Durchführung eines unbegleiteten fahrerlosen Betriebs für den jeweiligen Betreiber oftmals neu ist. In der Phase der Pflichtenhefterstellung ist die Großarchitektur bereits zum Großteil festgelegt und gilt daher als Randbedingung für alle weiteren Entwurfsschritte im Projekt (Abb. 8.2). Im weiteren Verlauf des Projekts resultieren zu berücksichtigende Anwendungsbedingungen aus dem Validierungsbericht (DIN EN 50128:2012-03) sowie aus den im technischen Sicherheitsbericht des Sicherheitsnachweises definierten sicherheitsbezogenen Anwendungsbedingungen (DIN EN 50129:2019-06), die einer unabhängigen Sicherheitsbewertung (DIN EN 50126-1:2018-10) unterworfen werden.

## Prinzip 2: Einbindung aller beteiligten Interessengruppen in den Erstellungsprozess des betrieblichen Regelwerks

Hierbei werden die verschiedenen Interessengruppen frühzeitig identifiziert und ihre Rolle und Mitwirkung bei der Erstellung des betrieblichen Regelwerks festgelegt. Außerdem wird festgelegt, welche Zielgruppen im betrieblichen Regelwerk angesprochen werden müssen (z. B. Instandhaltungspersonal, Fahrdienstleiter und Fahrpersonal). Die Planung und der Betrieb einer fahrerlosen U-Bahn-Linie erfordern das reibungslose und aufeinander abgestimmte Zusammenwirken verschiedener interner Funktionen des Verkehrsunternehmens. Daher wird für die Erstellung des betrieblichen Regelwerks eine interne Arbeitsgruppe unter Leitung eines Koordinators des Verkehrsunternehmens einberufen, die sich unter anderem aus Fahrpersonal, Fahrdienstleiter sowie Instandhaltungspersonal für Fahrzeuge und Streckeneinrichtungen zusammensetzt. Diese interdisziplinäre Zusammenstellung der Arbeitsgruppe stellt sicher, dass das betriebliche Regelwerk im Konsens verschiedener Unternehmensbereiche erstellt wird und damit im Projektverlauf auf eine höhere Akzeptanz stößt. Planung und Vorbereitung des Betriebs einer fahrerlosen U-Bahn-Linie erfordern darüber hinaus das aufeinander abgestimmte Zusammenwirken verschiedener Funktionen des Herstellers der sicherungstechnischen Einrichtungen (z. B. Teilsystemverantwortliche) sowie des Fahrzeugherstellers. Zudem müssen externe Interessengruppen mit in den Prozess eingebunden werden. Dies ist beispielsweise die Technische Aufsichtsbehörde sowie Vertreter von Behörden und Organisationen mit Sicherheitsaufgaben (BOS) wie Polizei und Feuerwehr. Abb. 8.3 stellt den kollaborativen Ansatz der Ausarbeitung des betrieblichen Regelwerks dar (Schnieder 2024).

## Prinzip 3: Anlehnung an bewährte Regelungen (evolutionärer Ansatz)

Die Verkehrsunternehmen betreiben in der Regel seit mehreren Jahrzehnten umfassende Verkehrssysteme. Dadurch verfügen sie zumindest für den Automatisierungsgrad 1 (NTO, non-automated train operation) über ein umfassendes und in der Praxis bewährtes Regelwerk. Gegebenenfalls wird dieses Regelwerk um einen halb automatischen Betrieb im Automatisierungsgrad 2 (STO, semi-automated train operation) ergänzt und fortgeschrieben und muss letztlich auf den Automatisierungsgrad 4 (UTO, unattended train operation) angepasst werden (Abb. 8.3). Dieser evolutionäre Ansatz birgt zwei Vorteile:

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//35a204fa-f878-461f-8d17-83c1f355d698/markdown_0/imgs/img_in_image_box_210_81_735_374.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A35%3A44Z%2F-1%2F%2Fee9d46315d65395e57546355a2d555f06d35e1dac1db428fd1138813e83e67a6" alt="Image" width="55%" /></div>


<div style="text-align: center;">Abb. 8.3 Partnerschaftliche Zusammenarbeit verschiedener Beteiligter in der Fortentwicklung des bestehenden betrieblichen Regelwerks</div>


• Das Verkehrsunternehmen verfügt bereits über eine lange Erfahrung im Betrieb eines U-Bahn-Systems. Es ist daher davon auszugehen, dass hier alle Details des Regelbetriebs vollumfänglich beschrieben sind (Vollständigkeit des zu erstellenden Regelwerks). Gleiches gilt für eine angemessene Beschreibung des Betriebs auf der Rückfallebene nach relevanten Störfällen („so viel wie nötig, so wenig wie möglich“).

• Die Weiterentwicklung des Regelwerks stellt die Akzeptanz innerhalb des Verkehrsunternehmens sicher. Außerdem können sich im Rahmen der Schulung die Teilnehmer, die ggf. schon vorher in anderen Unternehmensbereichen des Verkehrsunternehmens aktiv waren, schneller mit den neuen/ergänzten/geänderten Regeln vertraut machen, da diese im Grundsatz bereits bekannten Regelungen nicht widersprechen.

#### 8.6.2 Ablauf der Regelwerkserstellung im Erneuerungsprojekt

Die Erstellung des betrieblichen Regelwerks für die fahrerlose U-Bahn-Linie erfolgt in mehreren aufeinander aufbauenden Phasen. Jede Phase schließt mit einem definierten Qualitätsprüfpunkt ab.

- Phase 1: Die Auswirkungen der neuen Systemanforderungen auf die bestehenden betrieblichen Regeln und Vorschriften werden bewertet. Das Ergebnis dieser Phase ist eine erste Version der neuen Betriebsvorschriften und -verfahren zusammen mit einer Liste offener Punkte, die von einer gemeinsamen Arbeitsgruppe des Betreibers und des Herstellers des Sicherungssystems behandelt werden müssen.

- Phase 2: In der zweiten Phase implementiert der Hersteller die neue Systemlösung und führt Testaktivitäten im Labor durch. In der Regel kommt der Kunde in die Räumlichkeiten des Herstellers, um sich ein Bild von den erzielten Fortschritten zu machen. Dies wird als Factory Acceptance Test (FAT) bezeichnet. Während des FAT läuft das System in einer simulierten Umgebung, in der eine erste Version der Betriebsleitstelle in Betrieb ist. Dieser Aufbau kann zur Validierung der ersten Version der Betriebsvorschriften und -verfahren verwendet werden. Das Ergebnis ist eine zweite Version der neuen Betriebsvorschriften und -verfahren zusammen mit einer aktualisierten Liste der offenen Punkte.

---

• Phase 3: Bei typischen sicherungstechnischen Projekten wird der Betreiber höchstwahrscheinlich Schulungseinrichtungen für das Personal der Betriebsleitzentrale (Schult et al. 2015) und für die Fahrer (Dydak 2019) bestellen. Beide Einrichtungen werden zu einem bestimmten Zeitpunkt betriebsbereit sein. Während der Schulungen werden die Fahrer und das Personal der Betriebsleitzentrale mit dem neuen System sowie mit den neuen Betriebsregeln und -verfahren vertraut gemacht. Dies ist eine gute Gelegenheit, die neuen Betriebsvorschriften weiter zu validieren. Das Ergebnis ist eine dritte Version der Betriebsvorschriften und -verfahren zusammen mit einer aktualisierten Liste der offenen Punkte.

- Phase 4: Für die Durchführung von Integrationstests wird eine Teststrecke eingerichtet. Das Personal des Betreibers wird auf der Teststrecke zum ersten Mal mit dem neuen Sicherungssystem interagieren. Dies ist der erste Schritt von einer simulierten Umgebung zu realen „physischen“ Anlagen. Dies ist besonders wichtig für Betriebsvorschriften und -verfahren zu Wartungsaspekten. Aus diesem Grund bieten die Tests auf der Teststrecke weitere Möglichkeiten für die Validierung des neuen Regelwerks. Ergebnisse sind eine vierte Version der Betriebsvorschriften und -verfahren sowie eine aktualisierte Liste der offenen Punkte.

- Phase 5: Das neue Signalsystem wird umfassenden Testaktivitäten in der realen Betriebsumgebung unterzogen. Das Personal des Betreibers, sowohl an Bord der Züge als auch in der Betriebsleitzentrale, wird diese Aktivitäten gemeinsam durchführen. Eventuell fehlende Regelungen, Fehler oder missverständliche Formulierungen können so erkannt und behoben werden. Dies ist die letzte Chance, das Regelwerk zu validieren, bevor das System in den Echtbetrieb geht. Das Ergebnis dieser Phase ist der fünfte (und letzte) Satz von Betriebsvorschriften und -verfahren. Offene Fragen werden an die Betriebsphase weitergeleitet und müssen im Rahmen der regelmäßigen Aktualisierung des Regelwerks durch den Betreiber behandelt werden.

Für die Arbeiten in jeder der oben genannten Phasen müssen die Aufgaben klar zugewiesen werden. Dies kann durch Matrizen erreicht werden, aus denen hervorgeht, wer verantwortlich ist, wer rechenschaftspflichtig ist, wer unterstützend tätig ist und wer informiert werden muss (RACI-Matrix). Wenn dies zu einem frühen Zeitpunkt in einem Projekt vereinbart wird, verläuft die Aktualisierung der Betriebsvorschriften und -verfahren reibungslos und der Erfolg des Projekts ist sichergestellt.

#### 8.6.3 Rollen und Verantwortlichkeiten der Regelwerkserstellung im Erneuerungsprojekt

An der Erstellung der betrieblichen Regeln im Projekt der Ertüchtigung einer Linie für den unbegleiteten fahrerlosen Betrieb wirken verschiedene Rollen mit. Die Mitwirkenden repräsentieren dabei jeweils die verschiedenen Interessengruppen:

---

An der Ausarbeitung des Regelwerks zu beteiligende interne Stakeholder des Verkehrsunternehmens und ihre Aufgaben:

Koordinator des Verkehrsunternehmens: Koordiniert die Betreiberaktivitäten in Bezug auf die Anpassung des betrieblichen Regelwerks, stimmt die Umsetzung der zu regelnden Sachverhalte mit den Fachbereichen des Betreibers ab, koordiniert die Freigabe des Regelwerks durch den Betriebsleiter des Verkehrsunternehmens, stimmt sich mit den verschiedenen internen Fachbereichen des Verkehrsunternehmens ab, kommuniziert die Abstimmungsergebnisse termingerecht an den Koordinator des Herstellers.

Fachbereiche des Verkehrsunternehmens: An der Einführung des fahrerlosen Betriebs sind viele unterschiedliche Funktionen im Unternehmen beteiligt (Sicherungstechnik, Fahrzeug, Betrieb, Infrastruktur, etc.). Die Bedürfnisse der Fachbereiche werden im Rahmen der Koordination aufgegriffen und fließen in die Weiterentwicklung des Regelwerks ein.

Betriebsleiter: Das Verkehrsunternehmen hat einen Betriebsleiter zu bestellen. Diese Person ist bei allen Entscheidungen, die die Betriebsführung beeinflussen, einzubeziehen; dies umfasst insbesondere das betriebliche Regelwerk. Außerdem gibt sie das betriebliche Regelwerk in letzter Instanz frei (Straßenbahn-Bau- und Betriebsordnung vom 11. Dezember 1987).

An der Ausarbeitung des Regelwerks zu beteiligende interne Stakeholder des Herstellers und ihre Aufgaben:

Koordinator des Herstellers: Koordiniert in dieser Rolle die Herstelleraktivitäten in Bezug auf die Anpassung des betrieblichen Regelwerks, formuliert die zu regelnden Sachverhalte und leitet diese zur Umsetzung im Regelwerk an den Koordinator des Verkehrsunternehmens weiter.

Fachbereiche der Hersteller: Überführen die Pflichtenheftanforderungen in ein Produktkonzept und weisen das korrekte funktionale Verhalten und das Verhalten des Systems im Fehlerfall nach. Hieraus resultieren sicherheitsbezogene Anwendungsregeln, die ggf. im betrieblichen Regelwerk berücksichtigt werden müssen.

An der Ausarbeitung des Regelwerks zu beteiligende Externe und ihre Aufgaben:

• Behörden und Organisationen mit Sicherheitsverantwortung (BOS): Die Organisationen nehmen öffentliche Aufgaben zur Gefahrenabwehr oder Schadensbekämpfung wahr. Hierbei handelt es sich beispielsweise um die Polizei und die Feuerwehr.



- Gutachter: Die Technische Aufsichtsbehörde kann sich in der Wahrnehmung ihrer Sicherheitsaufsicht unabhängiger Sachverständiger bedienen. Diese werden regelmäßig über den Fortschritt der Erarbeitung des betrieblichen Regelwerks informiert. Etwaige Auflagen aus den Gutachten fließen bei Bedarf in die Weiterentwicklung des betrieblichen Regelwerks ein.

---

• Technische Aufsichtsbehörde (TAB): Aufsichtsbehörde des betreffenden Bundeslandes, die den sicheren und ordnungsgemäßen Betrieb des Verkehrsunternehmens überwacht. Etwaige Anforderungen der TAB müssen im betrieblichen Regelwerk berücksichtigt werden.

Die Verantwortlichkeiten sind exemplarisch einer RACI-Matrix darstellbar. Hierfür stehen die einzelnen Buchstaben für den jeweiligen Grad der Einbindung der beteiligten Personen (R – Responsible; A – Accountable; C – Consulted; I – Informed).

### 8.7 Schulung des Betriebspersonals

Bereits frühzeitig vor Aufnahme des Fahrgastbetriebs mit der neuen Technologie müssen verschiedene Zielgruppen im Unternehmen im Umgang mit CBTC-Systemen geschult werden. In diesem Abschnitt werden die Qualifikationsbedarfe aus Sicht von vier verschiedenen Zielgruppen dargestellt. Im konkreten Ausrüstungsprojekt müssen die Betreiber frühzeitig dafür Sorge tragen, dass die Schulung vom strukturiert Hersteller in die Hände des Betreibers übergeben wird. Hierfür haben sich in internationalen Projekten Train-the-Trainer-Konzepte vielfach bewährt.

#### 8.7.1 Schulungen der Fahrer

Die Fahrer müssen das CBTC System umfassend kennenlernen. Sie müssen die verschiedenen Betriebsarten, die Anzeigen des Führerstandsdisplays sowie auf diesem dargestellte Alarme und Informationen verstehen, korrekt interpretieren und im Betrieb in geeignete Reaktionen umsetzen. Hierbei müssen in der Schulung die folgenden Inhalte abgedeckt werden:

• Einweisung in die Führerstandsanzeige mit ihren Anzeigen und Bedienelementen

• Darstellung der Komponenten der CBTC-Fahrzeugeinrichtung

- Darstellungen der Bedienhandlungen in den verschiedenen betrieblichen Situationen (Aufrüsten des Fahrzeugs, Durchführen einer Permissivfahrt, manuelle Steuerung des Zuges entlang eines kontinuierlichen Überwachungsprofils, Führen des Zuges im halb automatischen Betrieb, Durchführung einer Kehrfahrt, Bergung liegengebliebener Fahrzeuge)

- Üben des Fahrens unter Nutzung der gesamten Bandbreite der zulässigen Betriebsartenwechsel

Die Schulungen werden durch geeignete Schulungseinrichtungen unterstützt. Da zum Zeitpunkt der Schulungsdurchführung die Anlagen noch nicht in vollem Umfang in Be-

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//f658eeaf-17f8-4bb9-bd05-4e874d925401/markdown_0/imgs/img_in_image_box_91_77_906_618.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A35%3A58Z%2F-1%2F%2F2ab3dacd349aaf519cab9f04922f18797bdebfdb696c2e6d65450702232ac41a" alt="Image" width="85%" /></div>


<div style="text-align: center;">Abb. 8.4 Fahrsimulator für Fahrerschulungen. (Quelle: Stadtwerke Verkehrsgesellschaft Frankfurt am Main mbH, VGF)</div>


trieb sind, kommen hierfür in der Regel Simulatoren für die Fahrzeugeinrichtungen (Dydak 2019) zum Einsatz. Ein beispielhafter Fahrsimulator ist in Abb. 8.4 dargestellt.

#### 8.7.2 Schulungen der Fahrdienstleiter

Das Personal auf der Leitstelle muss über ein weit reichendes betriebliches Wissen über das CBTC-System verfügen. Dies umfasst zum einen Betriebsführung im Regelbetrieb als auch die Betriebsführung auf der Rückfallebene. Hierzu müssen die Fahrdienstleiter ein umfassendes Verständnis der verschiedenen Betriebsarten haben. Sie müssen alle Bedienhandlungen, sowie Alarme und Informationen der Leittechnik verstehen und diese in angemessene betriebliche Entscheidungen umsetzen. Hierbei müssen in der Schulung die folgenden Inhalte abgedeckt werden:

- Funktionen der Fahrwegsicherung (gegebenenfalls Stellwerksfunktionen) sowie sicherheitsrelevante Bedienhandlungen über die Leittechnik. Diese Inhalte werden durch gezielte praktische Übungen vertieft.

- Einführung in die Diagnose und Wartungseinrichtungen samt Interpretation anstehender Störmeldungen.

---

- Funktionen und Einrichtungen der automatischen Zugüberwachung (ATS). Insbesondere Einführungen in Funktionen und Bedienhandlungen für die Zuglaufverfolgung (Automatic Train Tracking, ATT) und Zuglenkung (Automatic Route Setting, ARS) sowie möglicherweise weiterer Dispositionsfunktionen.

• Vertiefung der Lerninhalte durch gezielte praktische Übungen.

Die Schulungen werden durch geeignete Schulungseinrichtungen unterstützt. Da zum Zeitpunkt der Schulungsdurchführung die Anlagen noch nicht in vollem Umfang in Betrieb sind, kommen hierfür in der Regel Simulatoren für die Leitstellenbedienung (Schult et al. 2015) zum Einsatz. Diese Simulatoren bilden alle relevanten Details der Originalsysteme nach, um Trainingsbedürfnisse zu erfüllen. Die Bedienoberflächen werden mit der gleichen Bedienoberfläche das Originalsystem nachgebildet. Gleiches gilt für das zugrunde liegende Verhalten der Sicherungssysteme. Es kann hier eine realistische Topografie oder eine virtuelle Strecke nachgebildet werden. Der Zugbetrieb erfolgt auf der Grundlage eines Fahrplans, die Züge verkehren mit einer realistischen Fahrdynamik auf Basis von Zugkräften der Triebfahrzeuge, Zugmassen und -längen sowie Strecken- und Fahrstraßengeschwindigkeiten. Ein Schulungssimulator besteht meist aus einem Lehrer-Arbeitsplatz und mehreren Schüler-Arbeitsplätzen. Dem Trainer steht eine große Auswahl von Fehlfunktionen und Störungen zur Verfügung. Dies können Elementstörungen (Weichen, Signale etc.), Systemstörungen (Störungen von Streckeneinrichtungen oder des Datenkommunikationssystems etc.) oder auch betriebliche Störungen (Zug fährt über einen Gefahrpunkt hinaus, reduzierte Geschwindigkeit etc.) sein. Alle Störungen können in Störungsszenarien für standardisierte Tests zusammengefasst werden. Zur Nachbereitung einer Ausbildungseinheit stehen Zustandsspeicherfunktionen und Auswertungen zu Betriebsführung (Verspätungssminuten) und Bedienung zur Verfügung (Demitz et al. 2016).

#### 8.7.3 Schulungen des Instandhaltungspersonals

Die Schulung des Instandhaltungspersonals kann in zwei unterschiedliche Zielgruppen differenziert werden:

- Schulungen für die Instandhaltung der Streckeneinrichtungen: Ziel dieser Schulung ist es, ein umfassendes Verständnis für die Instandhaltung der Streckenausrüstung und die Ausrüstung in der Leitstelle zu vermitteln. Hierbei werden die folgenden Komponenten abgedeckt:

– Instandhaltung von Komponenten der Fahrwegsicherung (möglicherweise auch Stellwerk, Weichenantriebe, sekundäre Gleisfreimeldung, falls vorgesehen auch ortsfeste Signale)

– Instandhaltung der CBTC Streckeneinrichtung (Transponder und CBTC-Streckengerät)

– Instandhaltung der Leitstellentechnik

– Instandhaltung des Datenkommunikationssystems inklusive der hierfür erforderlichen Netzwerkkomponenten

---

- Schulungen für die Instandhaltung der Fahrzeugeinrichtungen: Das Ziel dieser Schulung ist es, ein umfassendes Verständnis für die Wartung der Fahrzeugausrüstung zu vermitteln:

– Instandhaltung von Komponenten des Führerstands (Führerstandsdisplay und Taster)

– Instandhaltung des Fahrzeugrechners (ATP und ATO)

– Instandhaltung der fahrzeugseitigen Anteile des Datenkommunikationssystems

## Literatur

Adler G et al (Hrsg) (1981) Lexikon der Eisenbahn, 6. Aufl. VEB Verlag für Verkehrswesen, Berlin

Arpaci M, Schwarte A (2013) Refurbishment of metro and commuter railways with CBTC to realize driverless systems. Signal + Draht 105(7+8):42–47

Brückner D (2017) Lösungen für das automatisierte Fahren im Nahverkehr. Signal + Draht 109(6):6–11

Cabrera A (2009) Gleisgeometriemessung in New York City. Eisenbahntechn Rundsch 58(12):712–715

Demitz J, Steffen W, István H (2016) RBC-Bedienoberflächen im internationalen Vergleich. EI – Eisenbahningenieur 2016:38–41

Diemunsch K (2016) Testing communications-based train control. In: Richard Y (Hrsg) Advances in communications-based train control systems. CRC Press, Boca Raton, S 15–41

DIN EN 16186-1:2019-04 Bahnanwendungen- Führerraum – Teil 1: Anthropometrische Daten und Sichtbedingungen. Deutsche Fassung EN 16816-1:214+A1:2018

DIN EN 50126-1:2018-10 Bahnanwendungen – Spezifikation und Nachweis von Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS) – Teil 1: Generischer RAMS-Prozess; Deutsche Fassung EN 50126-1:2017

DIN EN 50128:2012-03 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – Software für Eisenbahnsteuerungs- und Überwachungssysteme; Deutsche Fassung EN 50128:2011

DIN EN 50129:2019-06 Bahnanwendungen – Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme – Sicherheitsbezogene elektronische Systeme für Signaltechnik; Deutsche Fassung EN 50129:2018 + AC:2019

DIN EN 60529:2014-09 Schutzarten durch Gehäuse (IP-Code)

DIN EN 61373:2011-04 Bahnanwendungen – Betriebsmittel von Schienenfahrzeugen – Prüfungen für Schwingen und Schocken

Dombrowsky H, Müller R, May A, Seitzinger E (2008) Premiere für Deutschlands erste automatisierte U-Bahn. Nahnverker 26(5):8–16

Dydak P (2019) Warum Fahrsimulatoren? Vorteile und Grenzen dieses technischen Hilfsmittels bei der Aus- und Weiterbildung. Nahverkehr 37(1+2):12–15

IEC 62267 (2009) Railway applications – Automated urban guided transport (AUGT) – Safety requirements, Edition 1.0, 2009-07

Koch G, Schütte J, Benedikt W (2014) SAT.valid: Tool-gestützte Prüfung und Validierung von ETCS-Streckenausrüstungen. Signal + Draht 106(3):18–22

Laumen H, Henning S (2012) Obsoleszenz im Bereich LST. Signal + Draht 104(4):6–12

McCullough I (2008) Trends in modern Mastransit train control. Signal + Draht 100(10):41–47

Schnieder L (2024) Entwicklung von Regelwerken für den automatisierten Betrieb. Beitrag an- genommen zur Veröffentlichung. Eisenbahningenieur 74(2024):1/2

---

Schnieder L, Rainer D, Harald F (2021) Integration von CBTC-Systemen in Schienenfahrzeuge. Eisenbahntech Rundschau 6:30–33

Schroeder M (2002) Qualitätsmanagement von Projektierungsdaten für Zugsicherungssysteme. Signal + Draht 94(1+2):14–18

Schröter R (2008) Dienstanweisungen nach BOStrab. Der Nahverkehr 7+8, 29–36

Schult J, Rege G, Carroué C (2015) Betriebs- und Stellwerkssimulation BEST bei der üstra Hannoversche Verkehrsbetriebe AG. Signal + Draht 107(4):18–21

Schütte J, Jurtz S, Manschewski H-W (2008) SAT.engine – eine innovative Plattform zur Unterstützung von ETCS-Projekten. Signal + Draht 100(3):17–22

de Silvestre E (2005) CBTC applied to re-signalling metro lines upgrades performance. Signal + Draht 97(5):39–41

Straßenbahn-Bau- und Betriebsordnung vom 11. Dezember 1987 (BGBl. I S. 2648), zuletzt geändert durch Artikel 1 der Verordnung vom 1. Oktober 2019 (BGBl. I S. 1410)

UIC 651:2002-07 Layout of driver's cabs in locomotives, railcars, multiple unit trains and driving trailer

VDV-Schrift 161-2 (2009) Sicherheitstechnische Anforderungen an die elektrische Ausrüstung (10/2009)

Wigger P (2016) Verantwortlichkeiten bei Neubau, Erweiterung oder Modernisierung eines Nah- verkehrssystems. Signal + Draht 108(3):49–61

---

# Perspektiven und zukünftige Herausforderungen

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//f6709972-219c-4c43-9a27-4621e33e8e95/markdown_0/imgs/img_in_image_box_905_107_952_173.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A36%3A14Z%2F-1%2F%2Fbc36ec46fb7ef3db4b20ccfe70720ba26e76a3ef61e526e8bb80ccc24de1c327" alt="Image" width="4%" /></div>


## SN Flashcards

Als Käufer*in dieses Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards“ mit Fragen zur Wissensüberprüfung und zum Lernen von Buchinhalten nutzen.

1. Gehen Sie bitte auf https://flashcards.springernature.com/login und

2. erstellen Sie ein Benutzerkonto, indem Sie Ihre Mailadresse angeben und ein Passwort vergeben.

3. Verwenden Sie den folgenden Link, um Zugang zu Ihrem SN Flashcards Set zu erhalten: ▶ https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht funktionieren, senden Sie uns bitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Communications-Based Train Control Systeme haben sich in den letzten Jahrzehnten weltweit de facto als Standard herausgebildet (UITP 2019). Alle Systemhäuser haben mittlerweile in vielen Projekten Erfahrungen in der praktischen Realisierung gesammelt. Dies betrifft sowohl Neubauprojekte als auch komplexe Umbauten der signaltechnischen Infrastruktur „unter rollendem Rad“. Die CBTC-Ausrüstung städtischer Bahnsysteme wird zukünftig weiter zunehmen (vgl. Abschn. 9.1). Allerdings sind zukünftig von den Be- treibern und den Systemherstellern weitere Herausforderungen zu lösen. Dies ist neben der aktuell fehlenden Standardisierung der herstellerspezifischen Systemlösungen (vgl. Abschn. 9.2) auch eine Integration von CBTC-Systemen in die Systemtechnik und Ver-

---

kehrsplanung des Straßenverkehrs dort, wo Stadtbahnsysteme die Verkehrsfläche mit anderen Verkehrsteilnehmern teilen (vgl. Abschn. 9.3). Hinsichtlich zukünftiger Entwicklungsperspektiven sind auch aktuelle Entwicklungen in der Systemarchitektur relevant. Diese Themen werden in Abschn. 9.4 hinsichtlich einer alternativen Funktionsaufteilung zwischen Fahrzeug- und Streckeneinrichtungen erörtert.

### 9.1 Entwicklung der installierten Basis

Viele Städte weltweit haben in den letzten Jahren bereits neue Systeme mit kommunikationsbasierten Zugsicherungssystemen in Betrieb genommen. Dieser Trend wird sich zukünftig fortsetzen. Im nächsten Jahrzehnt ist weltweit eine rapide Zunahme fahrerloser Systeme absehbar (UITP 2019). Prognosen auf Grundlage bereits bestätigter Projekte zeigen, dass sich die Streckenlänge fahrerloser Metrosysteme von insgesamt 1026 km im Jahre 2018 in den nächsten zehn Jahren auf mehr als 3800 km mehr als verdreifachen wird (vgl. Abb. 9.1). Der größte Anteil wird hierbei auf die erwarteten Eröffnungen neuer Linien entfallen. Der überwiegende Anteil hiervon allgemein in Asien, bzw. speziell in China (Schnieder 2019a). Ein geringerer Anteil (7 % der Streckenlänge) wird auf europäische Modernisierungsprojekte entfallen. Auch in Deutschland ist dieser Trend inzwischen angekommen. In Nürnberg blickt der Betreiber inzwischen fast zehn Jahre Betriebserfahrung mit einem fahrerlosen System zurück. In Wien haben die Arbeiten für die Einführung einer fahrerlosen U-Bahn Linie (U5) begonnen (Heinrich et al. 2019). In Hamburg wird der Neubau einer fahrerlosen Linie der U-Bahn erwogen und die bestehenden Linien U2 und U4 werden in den nächsten Jahren in den halbautomatischen Betrieb überführt. Im Stadtbahnsystem der Stadt Frankfurt am Main werden die innerständischen Tunnelstrecken in den nächsten Jahren mit einem CBTC-System für den halbautomatischen Betrieb ertüchtigt. Weitere Betreiber im deutschsprachigen Raum befassen sich konkret mit der Systemauswahl und bereiten Ersatzinvestitionen in ihren Netzen vor. CBTC-Systeme werden daher in absehbarer Zukunft in Deutschland zunehmend zum Einsatz kommen.

### 9.2 Standardisierung von Systemlösungen

Bislang sind die CBTC-Systemlösungen ausschließlich proprietär. Durch die große Heterogenität von Nahverkehrssystemen zeichnet sich – den Bemühungen einiger ausgewählter Betreiber großer U-Bahn- und Stadtbahnsysteme zum Trotz – nicht ab, dass sich an diesem Zustand in absehbarer Zukunft etwas ändern wird. Damit sind die Betreiber mit ihrer Investitionsentscheidung über den gesamten Lebenszyklus der Anlage an einen Hersteller gebunden. Ursächlich hierfür sind die fehlende Interoperabilität und Austauschbarkeit von Komponenten.

---

• Interoperabilität bezeichnet die Möglichkeit, dass im Netz eines Betreibers Fahrzeug mit CBTC-Fahrzeugeinrichtungen eines Herstellers mit den Streckeneinrichtungen anderer Herstellers wechselwirken können. Um eine solche Interoperabilität zu erreichen, müssten CBTC-Systeme am Luftspalt zwischen Fahrzeug und Strecke logisch und physikalisch standardisiert sein (McCullough 2008). Dies ist aktuell nicht der Fall.

• Austauschbarkeit bedeutet die Möglichkeit, Elemente des CBTC-Systems gegen Sub-systeme/Komponenten eines anderen Herstellers auszutauschen. Hierbei soll es möglich sein, einzelne Elemente des CBTC-Systems austauschen zu können, ohne das gesamte System ersetzen zu müssen. Die Austauschbarkeit braucht standardisierte CBTC-Systemarchitekturen mit wohldefinierten Schnittstellen. Dies setzt unter anderem eine einheitliche Zuordnung von Funktionen auf Systemkomponenten voraus (McCullough 2008). Zukünftig könnten Betreiber in ihren Ausschreibungen Anleihen an im Betrieb von Eisenbahnen etablierte standardisierte Schnittstellen zu Nachbarsystemen (Stellwerke, Leitstelle und Funkstreckenzentrale) sowie zu dezentralen Feldelementen (bspw. für Weichen und Gleisfreimeldung) nehmen (Elsweiler 2014). Durch die Eulynx-Initiative liegen hier in der Praxis bewährte standardisierte Schnittstellen vor, von denen auch Nahverkehrsbetreiber profitieren könnten (Müller 2021).

Das insbesondere für Vollbahnen europaweit und herstellerübergreifend einheitlich definierte European Train Control System (ETCS) ist ein expliziter Gegenentwurf zu den proprietären CBTC-Systemlösungen. ETCS Level 3 und CBTC-Systeme sind einander hinsichtlich ihrer potenziellen wirtschaftlichen Auswirkungen im Sinne reduzierter Lebenszykluskosten vergleichbar. Einen klaren Vorteil weist das ETCS hinsichtlich der Austauschbarkeit und Interoperabilität auf. Demgegenüber weist CBTC genau dann Vorteile auf, wenn hohe Zugdichten gefordert werden und eine hohe Automatisierung (Driverless Train Operation oder höher) angestrebt wird. Wenn eine ausreichende Kapazität auch ohne das Fahren im wandernden Raumabstand geschaffen werden kann, können die Vorteile des ETCS möglicherweise zukünftig auch für die Nahverkehrsunternehmen genutzt werden (Schnieder 2019b, 2020).

### 9.3 Integration der Straßenverkehrstechnik in Stadtbahnsystemen

Für Stadtbahnsysteme ist die Einbindung der Straßenverkehrstechnik essenziell. Die durch das Fahren im wandernden Raumabstand in den zentralen Tunnelabschnitten realisierbaren kürzeren Zugfolgezeiten mit den hieraus resultierenden Kapazitätsgewinnen (Anzahl Zugfahrten pro Fahrtrichtung und Stunde) sind nur dann zu realisieren, wenn der Zufluss in die, bzw. der Abfluss aus den in der Regel halb automatisch betriebenen Tunnelstrecken ebenfalls signifikant verbessert wird. Bislang treffen aus dem Oberflächenbereich

---

in die zentrale Tunnelstrecke einbrechende Fahrzeuge ungleich verteilt im Takt der Umlaufzeit der Lichtsignalanlagen (in der Regel 90 Sekunden) im Zulauf der Tunnelstrecken ein und verursachen dort Verspätungen im Betriebsablauf. Dadurch, dass das Bestandssysteme bereits an ihrer rechnerischen Kapazitätsgrenze betrieben werden und den gesamten Tag über dichte Fahrplantakte gefahren werden, kann diese Verspätung über den Betriebstag hinweg nicht wieder abgebaut werden. Parallel zur systemtechnischen Erneuerung der Tunnelstrecken ist daher auch eine Steigerung der Leistungsfähigkeit der zu- und abbringenden im Fahren auf Sicht betriebenen Außenäste von Stadtbahnsystemen zwingend geboten. Hierfür müssen in Abstimmung mit dem jeweiligen Straßenverkehrsamt der Kommune verschiedene Architekturvarianten der Anbindung an das CBTC-System gegeneinander abgewogen werden (Sandrock und Riegelhuth 2014):

• Dezentrale Kommunikation zwischen Stadtbahnfahrzeugen und Lichtsignalanlagen: Klassischerweise geschieht die Beeinflussung von Lichtsignalanlagen durch eine Interaktion zwischen dem Stadtbahnfahrzeug und dem Steuergerät der Lichtsignalanlage. Hierbei kommen bislang Bake-Funk-Systeme im Sinne einer dezentralen ÖPNV-Priorisierung zum Einsatz. Fährt ein Fahrzeug in den Erfassungsbereich einer ortsfesten Bake, sendet das Fahrzeug ein Funktelegramm an den Empfänger der in der Nähe befindlichen Lichtsignalanlage. Das Stadtbahnfahrzeug sendet eine Anmeldung an das Steuergerät. Um Reisezeiten zu reduzieren, werden Rotphasen der Lichtsignalanlage gekürzt und Grünphasen verlängert. Alternativ werden Phasen eingefügt, entfallen oder werden getauscht. Das Stadtbahnfahrzeug erhält grünes Licht noch bevor es die Haltelinie erreicht, so dass es nicht abbremsen muss. Nachdem das Stadtbahnfahrzeug die Kreuzung passiert hat, sendet es eine Abmeldenachricht an das Steuergerät (Rüffer et al. 2019).

- Zentralenbasierte Kopplung von Stadtbahnfahrzeugen und Lichtsignalanlagen. Die Kommunen betreiben in der Regel eine Verkehrsmanagementzentrale. Bereits seit längerer Zeit haben die Kommunen die strategische Weichenstellung für den Einsatz herstellerunabhängiger Schnittstellenstandards in der Straßenverkehrstechnik vorgenommen, was unter dem Stichwort Open Communication Interface for Road Traffic Control Systems (OCIT) subsummiert wird. Dies umfasst bislang im Wesentlichen die sogenannte OCIT-Outstations Schnittstelle (OCIT-O) zur Verbindung der Lichtsignalsteuergeräte mit dem zentralen Verkehrsrechner. Über den Aufbau einer so genannten OCIT-Schnittstelle „Center-to-Center“ (OCIT-C) wird es in dieser Architekturvariante zukünftig möglich, die Leitebene des CBTC-Systems mit dem Verkehrsrechner der Kommune zu verbinden. Von der Leitebene des CBTC-Systems übertragene Zustandsdaten führen zu einer gezielten Priorisierung von Stadtbahnfahrzeugen an lichtsignalgeregelten Knoten im Straßenverkehrsnetz (Rüffer et al. 2019).

---

Neben der zuvor dargestellten systemtechnischen Integration müssen ebenfalls verkehrsplanerische Aspekte mit betrachtet werden. Hier kann es sinnvoll sein, gezielt Parameter wie Umlaufzeiten zu variieren und an der Koordination mehrerer hintereinanderliegender Knoten zu arbeiten.

### 9.4 Alternative Funktionsaufteilung zwischen Fahrzeug und Strecke

In Abschn. 2.1 wurde eine exemplarische Systemarchitektur für CBTC-Systeme vorgestellt, wie sie bislang allgemein bei den verschiedenen Herstellern üblich war. Neue technologische Entwicklungen ermöglichen alternative Funktionsaufteilungen zwischen Fahrzeug und Strecke. Daher wird in Abschn. 9.4.1 eine Zentralisierung sicherheits-relevanter Anwendungen in Rechenzentren dargestellt. Abschn. 9.4.2 stellt eine fahrzeug-zentrierte Sicht vor, welche die zuvor streckenseitige Logik auf das Fahrzeug portiert. Beiden Ansätzen ist gemein, dass nur noch Steuerungen zum Stellen und Überwachen einzelner Fahrwegelemente direkt entlang der Strecke verbleiben.

#### 9.4.1 Zentralisierung sicherheitsrelevanter Anwendungen in Rechenzentren

Die grundlegende Idee dieses Ansatzes ist es, die Logik der Fahrwegsicherung und der streckenseitigen Komponenten der Zugbeeinflussung in einem Rechenzentrum zu betreiben. Die zentrale Logik des Rechenzentrums ist über ein IP-basiertes Netzwerk mit Steuerungseinrichtungen verbunden, welche nur die Stell- und Überwachungslogik für die einzelnen Fahrwegelemente enthalten (OC, object controller). Technisch ist das Rechenzentrum mit COTS-Komponenten ausgeführt. COTS steht hierbei für Commercial off-the-shelf, d. h. es handelt sich hier um Komponenten „von der Stange“. Dies umfasst sowohl Hardware- als auch Softwareprodukte, die baugleich und in großen Stückzahlen hergestellt und verkauft werden. Durch den sehr hohen Grad der Zentralisierung im Rechenzentrum entsteht der Bedarf nach erweiterten Verfügbarkeitsmechanismen, denn es muss nicht nur der Ausfall einer einzelnen COTS-Hardware, sondern auch der Totalausfall des Rechenzentrums (etwa infolge von Stromausfall, Überschwemmung, Feuer) beherrscht werden. Für höchste Verfügbarkeit ist es deshalb notwendig, dass ein Rechenzentrum als Ganzes redundant an verschiedenen Orten installiert und betrieben werden kann (Steffens und Hempel 2023). Vorteile dieses Konzepts ergeben sich hinsichtlich der Instandhaltungs- und Updatepolitik. So ist es oftmals nicht mehr notwendig zur Anlage zu

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//56bbc101-f080-45a7-adbe-4574ce29ce20/markdown_0/imgs/img_in_image_box_65_88_872_685.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A36%3A33Z%2F-1%2F%2F6c517d8c4dbc8c82c38848e8dd68ea0401e8e5f5dfe4b6b8db886c4edd0f6d73" alt="Image" width="84%" /></div>


<div style="text-align: center;">Abb. 9.1 COTS-Hardware basiertes Rechenzentrum mit geografischer Redundanz</div>


fahren, um diagnose- und teilweise auch Wartungsarbeiten durchzuführen. Durch den Betrieb wesentlicher Systembestandteile im Rechenzentrum ergeben sich darüber hinaus möglicherweise Synergieeffekte mit anderem IT-Wartungspersonal beispielsweise im Bereich der Kommunikationstechnik (Abb. 9.1).

#### 9.4.2 Fahrzeugzentrierte Funktionsallocation

Bei dieser Systemausrägung entfallen in konventionellen CBTC-Architekturen (vgl. Abschn. 2.1) zuvor zentral verortete Funktionsanteile in der Infrastruktur (Schnieder 2020). Dies kann sehr deutlich am Streckenatlas festgemacht werden, der in konventionellen CBTC-Architekturen sowohl auf dem Fahrzeug als auch in den Infrastruktur-komponenten, quasi als „gemeinsames Koordinatensystem“, vorgehalten wurde. Durch eine direkte Kommunikation der Fahrzeuge untereinander (Vehicle to Vehicle Communication, V2V) über das streckenseitige Datenkommunikationssystem teilen sich die Fahrzeuge relevante Gefahrpunkte wie das Heck des vorausfahrenden Zuges direkt mit. Hier- durch entfallen Reaktionszeiten zur Signalverarbeitung in zwischenliegenden streckenseitigen Sicherungssystemen. Ein weiterer Unterschied ist die ausschließlich direkte Steuerung beweglicher Fahrwegelemente und Beanspruchung von Gleisabschnitten durch

---

dass Fahrzeug selbst auf der Grundlage einer unmittelbaren Kommunikation des Fahrzeugs mit dem Feldelement-Controller (quasi Einzelweichensteuerungen). War für die zuvor dargestellte konventionelle Systemausprägung eine Zuglaufverfolgung (Automatic Train Tracking, ATT) und Zuglenkung (Automatic Route Setting, ARS) durch die Auswertung von der Streckenseite bereitgestellter Zustandsgrößen von der Leitstelle prägend (Mücke 2005), beruht die Fahrwegauswahl und die Anforderung der korrekten Endlage der einzelnen hierfür erforderlichen beweglichen Fahrwegelemente nun auf dem individuellen „Einsatzauftrag“ (Mission), der jedem Fahrzeug direkt aus der Leitstelle übermittelt wird. Dies bedeutet, dass die sicherungstechnische Bemessung (beispielsweise von Streckenlängen wie Durchrutschwegen, Blockabschnittsteilungen oder Zeitanteilen wie geschwindigkeitsabhängige Einschaltzeiten) sowie die Darstellung im Streckenatlas nicht mehr statisch anhand der Flotteneigenschaften (beispielsweise bei Einschaltzeiten als „Worst Case“ dem schnellsten Fahrzeug) erfolgt. Diese Strecken und Zeitanteile werden nur von jedem Fahrzeug anhand seiner eigenen fahrdynamischen Eigenschaften berechnet. Dies erhöht die Flexibilität der Nutzung der Infrastruktur und gestattet eine Optimierung der erreichbaren Zugfolgezeiten.

## Literatur

Elsweiler B (2014) Beyond ETCS – Interoperable interfaces and more. IRSE NEWS 198, S 2

Heinrich N, Stuchlik C, Schnieder L (2019) Automatisierung der Linie U5 in Wien. Eisenbahntechn Rundsch 68(6):24–27

International Association of Public Transport (UITP) (2019) World report on metro automation. Brüssel

McCullough I (2008) Trends in modern mass-transit train control. Signal + Draht 100(10):41–47

Mücke W (2005) Betriebsleittechnik im öffentlichen Verkehr, 2. Aufl. Eurailpress, Hamburg

Müller R (2021) Digitale Stellwerke tragen die Digitalisierung der Bahn. EIK – Eisenbahningenieurkompendium 2021. Eurailpress, Hamburg, S 180–201

Rüffer M, Schmidt C, Schnieder L (2019) Erneuerung der Zugsicherung als Chance für die Automatisierung von Stadtbahnsystemen. Eisenbahntechn Rundsch 68(9):19–23

Sandrock M, Riegelhuth G (2014) Verkehrsmanagementzentralen in Kommunen – Eine vergleichende Darstellung. Springer, Berlin

Schnieder L (2019a) Stand und Perspektive von Metrosystemen in China. Eisenbahntechn Rundsch 68(7+8):10–13

Schnieder L (2019b) Zugbeeinflussungssysteme für Stadtbahnen im Vergleich. EI – Eisenbahningenieur 69(11):31–34

Schnieder L (2020) Funktionsallocation in funkbasierten Zugbeeinflussungssystemen – ein Vergleich. ETR – Eisenbahntechnsiche Rundchau 70(11):16–19

Steffens S, Hempel T (2023) Vom Digitalen Stellwerk in die Cloud. Deine Bahn 8:22–27

---

Stichwortverzeichnis

## A

Abfertigung 18, 98, 110  

Abfertigungsbedingungen 98  

Abfertigungsverfahren 78  

„Access Point“ 127, 130, 166  

Access Points 19, 21, 23  

Ausfahrbeschränkung 98  

„Austauschbarkeit“ 180, 181  

„Automatic Route Setting“ (ARS) 25, 185  

siehe auch Zuglenkung 25, 185  

Automatic Train Control (ATC) 11, 13  

Automatic Train Operation (ATO) 13, 27  

Automatic Train Protection (ARP) 13  

Automatic Train Protection (ATP) 13  

Automatic Train Supervision (ATS) 13, 23  

Automatic Train Tracking (ATT) 25  

siehe auch Zuglaufverfolgung 25  

„Automatisierungsgrad  

GoA 3 – begleiteter fahrerloser Zugbetrieb“ 90  

Automatisierungsgrad 13, 14, 17, 18, 40, 85, 103  

GoA 0 – Zugbetrieb auf Sicht 40, 84  

GoA 1 – halbautomatischer Zugbetrieb 41  

GoA 1 – nicht automatisierter Zugbetrieb 40, 85  

GoA 3 – begleiteter fahrerloser Zugbetrieb 41  

GoA 3 – vollautomatischer fahrerloser Betrieb 55  

„Automatisierungsgrad“ 89  

„Availability“ 118, 125

## B

Bahnsteigtür 86, 90–93, 95, 97  

Bahnübergang 65  

„Bandbreite“ 120, 174  

Befahrbarkeitseinschränkung 85  

Befahrbarkeitssperre 88  

Beschaffungskosten 8  

„Betriebshof“ 49, 55, 85, 127, 165  

„Betriebskosten“ 9, 149  

„Betriebssimulation“ 138, 140, 142  

Bremskurve 68

## C

„Capital Expenditure“ (CAPEX) 9, 134  

siehe auch Beschaffungskosten 134  

„Categories“ 136  

siehe auch Kostenarten 136  

„Cost Breakdown Structure“ (CBS) 136  

siehe auch Kostenaufbruchstruktur 136

## D

„Datenkommunikationssystem“ 56, 76, 129, 166, 167, 176, 184

design headway 7

„Disposition“ 5, 13, 25, 26, 176

„Doppelausrüstung“

Fahrzeuge 149, 150

Strecke 151

---

## E

Einfahrbeschränkung 89

Einklemmerkennung 99, 100

Einklemmschutz 100

„Elektronischer Verträglichkeit“

(EMV) 163

Evakuierung 86, 95, 103, 105,

106, 110–112

## F

„Factory Acceptance Test“ (FAT) 164  

Fahrerlaubnis 45, 47, 58, 66–68, 98  

„Fahrgastinformation“ 3, 4, 167  

Fahrstraßenverschluss 62  

Fahrstrategie 17, 77, 79  

Fehlerkategorie 104  

Fixed Block 5, 66  

Fixed Blockstand  

siehe auch fester Raumabstand 66  

Flankenschutz 15, 62, 88  

„Führerstandsanzeige“ 82, 83, 85, 102, 174

## G

Gegenfahrschutz 66

Geschwindigkeitsprofil, statistisches 67, 68

„Gleisfreimeldung“ 129, 137, 152, 181

sekundäre 129, 160, 176

Gleisfreimeldung

primäre 14

sekundäre 14

Gleiten 71, 72, 74

Grade of Automation (GoA) 40–42

siehe auch Automatisierungsgrad 40

## H

Handover 19, 22

headway 7

Hinderniserkennung 59, 86, 105, 114

## I 

„Inbetriebnahme“ 161, 162, 164 „Inbetriebnahmetest“ 165, 166

„Informationssicherheitsmanagementsystem“ (ISMS) 125  

„Infrastruktur, kritische“ 124  

„Integrationstest“ 172  

„Interoperabilität“ 181, 182

## K

Kehrfahrt, fahrerlose 53

„Kostenart“ 134, 136

„Kostenaufbruchstruktur“ 134

## L

„Lebenszykluskosten“ 8, 134, 136, 137, 181  

Lichtraumprofil 65, 66, 85  

„Lichtsignalanlage“ (LSA) 65, 182  

„Life Cycle Costs“ (LCC) 8, 134

## M

„Maintainability“ 118, 126  

„Migrationsstrategie“ 148  

Moving Block 5, 65  

siehe auch Raumabstand, wandernder 65

## N

Nachpositionieren 92

„Non-automated Train Operations“ (NTO) 40

siehe auch Automatisierungsgrad 40

Notführerstand 18

## 0

„Operational Expenditure“ (OPEX) 9, 134  

operational headway 7  

„Ortsbake“ 74  

Radarsensor 71  

„Ortung“ 13, 48, 49, 66, 70, 71, 75  

Beschleunigungssensor 115  

„Ortungsgenaugkeit“ 74

## P

„Product Breakdown Structure“ 134  

siehe auch Produktaubruchstruktur 134  

„Produktaubruchstruktur“ 134

---

## R

„Raumabstand“

wandernder 45, 51, 181

Raumabstand

fester 5, 27

wandernder 6, 28

„Raumabstandwandernder“ 152

„Reliability“ 118, 125, 128

„Risikoanalyse“ 118–120, 122, 123

„Risikograf“ 120, 121

Roaming 21–23

„Rückrollüberwachung“ 48

## S

„Safety“ 118, 119  

„Schleichfahrt“ 92  

„Schleudern“ 71, 72, 74  

„Schlupf“ 71, 72, 74  

    Gleiten 72  

    Security“ 118, 124  

    siehe auch Verlässlichkeit 118  

„Semi-automated Train Operation“ (STO) 83  

    siehe auch Automatisierungsgrad 83  

„Sicherheit“ 90, 118–120, 122–124  

„Sicherheitsintegritätslevel“ (SIL) 119–121, 123  

„Sicherheitsnachweis“ 119  

„Sieving“ 51  

„Site Acceptance Test“ (SAT) 168  

Sperrzeit 6  

Sperrzeitentreppe 6  

„Stellwerk“ 13, 15, 27, 28, 134, 150, 164, 167, 176, 181  

„Störungsbetrieb“ 56  

„Straßenverkehrstechnik“ 181  

„Streckenatlas“ 16, 51, 67, 75, 77

## T

„Technischer Sicherheitsbericht“ 119  

„Test“ 152, 163, 165, 167, 171  

„Testcenter“ 163, 164, 168  

„Testgleis“ 149, 162, 165, 166  

„Testlabor“ 162  

„Train Operations on Sight“ (TOS) 40  

siehe auch Automatisierungsgrad 40  

„Training“ 176  

Fahrdienstleiter 175  

Fahrertraining 174  

Instandhaltertraining 176  

„Traktionsstromversorgung“ 66, 76, 111, 153, 167  

„Türfreigabe“ 84, 89, 90, 106



## U

„Übereinstimmungsprüfung“ 166  

„Umselttest“ 162  

„Umweltbedingung“  

Klima 2, 163  

Unmanned Train Operation (UTO) 8  

siehe auch Automatisierungsgrad 8

## V 

„Verfügbarkeit“ 106, 118, 124, 125, 128, 130, 137, 144

Ausfallzeit, mittlere 125

Klarzeit, mittlere 125

„Verlässlichkeit“ 117

Angriffssicherheit 118

Instandhaltbarkeit 125

Sicherheit 122

## W

„Weichenverschluss“ 62

Wireless Local Area Networks (WLAN) 21

## Z

„Zugfolgezeit“ 6, 7, 56, 181, 185  

siehe auch headway 185  

„Zuglaufverfolgung“ 25, 168, 176, 185  

„Zuglenkung“ 25, 26, 176, 185  

„Zurücksetzen“ 92  

„Zu verlässigkeit“ 97, 118