# Interpol Notices API

Die API erlaubt den Zugriff auf Interpols Red Notices, Yellow Notices sowie United Nations Security Council Special Notices (UN Notices).

Interpol zufolge ist eine Red Notice eine Aufforderung an die Strafverfolgungsbehörden weltweit, eine Person bis zu Auslieferung, Übergabe oder ähnlichen rechtlichen Schritten ausfindig zu machen und vorläufig festzunehmen (cf. https://www.interpol.int/How-we-work/Notices/Red-Notices). 
Eine Red Notice enthält zwei Haupttypen von Informationen: 
* Informationen zur Identifizierung der gesuchten Person, wie Name, Geburtsdatum, Nationalität, Haar- und Augenfarbe, Fotos und Fingerabdrücke, sofern verfügbar; 
* Informationen im Zusammenhang mit dem Verbrechen, für das sie gesucht werden, was typischerweise Mord, Vergewaltigung, Kindesmissbrauch oder bewaffneter Raub sein kann. 

Eine Yellow Notice ist demgegenüber ein globaler Hinweis auf eine vermisste Person. Es wird für Opfer von elterlichen Entführungen, kriminellen Entführungen (Kidnappings) oder ungeklärtem Verschwinden ausgestellt (cf. https://www.interpol.int/en/How-we-work/Notices/Yellow-Notices).

Eine UN Notice warnt die Polizei weltweit vor Einzelpersonen und Organisationen, die Sanktionen des Sicherheitsrats der Vereinten Nationen unterliegen (cf. https://www.interpol.int/How-we-work/Notices/INTERPOL-United-Nations-Security-Council-Special-Notices).


## Red Notices


***URL:*** https://ws-public.interpol.int/notices/v1/red


Die API ermöglicht, verfügbare Red Notices über folgende Parameter eines GET-requests zu filtern:


**Parameter:** *forename*  (Optional)

Vorname (z.B. MAX).


**Parameter:** *name*  (Optional)

Nachname (z.B. Mustermann).


**Parameter:** *nationality*  (Optional)

Nationalität (z.B. DE).


**Parameter:** *ageMax*  (Optional)

Maximalalter (z.B. 120).


**Parameter:** *ageMin*  (Optional)

Minimalalter (z.B. 18).


**Parameter:** *freeText*  (Optional)

Freitextanfrage.


**Parameter:** *sexId*  (Optional)

Geschlechterkürzel (z.B. "F","M","U","").


**Parameter:** *arrestWarrantCountryId*  (Optional)

Land des Haftbefehlursprungs (z.B. DE).


**Parameter:** *page*  (Optional)

Seite (z.B. 1).


**Parameter:** *resultPerPage*  (Optional)

Ergebnisse pro Seite (z.B. 200)


## Red Notice Details

***URL:*** https://ws-public.interpol.int/notices/v1/red/{noticeID}


Die API ermöglicht, Details zu einzelnen Red Notices über den Pfad-Parameter *noticeID* (z.B. 1993-27493) eines GET-requests anzufragen.


## Red Notice Images

***URL:*** https://ws-public.interpol.int/notices/v1/red/{noticeID}/images


Die API ermöglicht, Images zu einzelnen Red Notices über den Pfad-Parameter *noticeID* (z.B. 1993-27493) eines GET-requests anzufragen.


## Yellow Notices


***URL:*** https://ws-public.interpol.int/notices/v1/yellow

Die API ermöglicht, verfügbare Yellow Notices über folgende Parameter eines GET-requests zu filtern:


**Parameter:** *forename*  (Optional)

Vorname (z.B. MAX).


**Parameter:** *name*  (Optional)

Nachname (z.B. Mustermann).


**Parameter:** *nationality*  (Optional)

Nationalität (z.B. DE).


**Parameter:** *ageMax*  (Optional)

Maximalalter (z.B. 120).


**Parameter:** *ageMin*  (Optional)

Minimalalter (z.B. 18).


**Parameter:** *freeText*  (Optional)

Freitextanfrage.


**Parameter:** *sexId*  (Optional)

Geschlechterkürzel (z.B. "F","M","U","").


**Parameter:** *page*  (Optional)

Seite (z.B. 1).


**Parameter:** *resultPerPage*  (Optional)

Ergebnisse pro Seite (z.B. 200)


## Yellow Notice Details

***URL:*** https://ws-public.interpol.int/notices/v1/yellow/{noticeID}


Die API ermöglicht, Details zu einzelnen Yellow Notices über den Pfad-Parameter *noticeID* (z.B. 2014-5590) eines GET-requests anzufragen.


## Yellow Notice Images

***URL:*** https://ws-public.interpol.int/notices/v1/yellow/{noticeID}/images


Die API ermöglicht, Images zu einzelnen Yellow Notices über den Pfad-Parameter *noticeID* (z.B. 2014-5590) eines GET-requests anzufragen.



## UN Notices


***URL:*** https://ws-public.interpol.int/notices/v1/un

Die API ermöglicht, verfügbare UN Notices über folgende Parameter eines GET-requests zu filtern:


**Parameter:** *name*  (Optional)

Nachname (z.B. Mustermann).


**Parameter:** *unReference*  (Optional)

UN-Referenz (Freitext).


**Parameter:** *unResolution*  (Optional)

UN-Resolution (z.B. 1267).


**Parameter:** *page*  (Optional)

Seite (z.B. 1).


**Parameter:** *resultPerPage*  (Optional)

Ergebnisse pro Seite (z.B. 200)


## UN Notice Details

***URL:*** https://ws-public.interpol.int/notices/v1/un/{noticeType}/{noticeID}


Die API ermöglicht, Details zu einzelnen UN Notices über die Pfad-Parameter *noticeType* (entweder "persons" oder "entities") und *noticeID* (z.B. 2021-84506) eines GET-requests anzufragen.


## UN Notice Images

***URL:*** https://ws-public.interpol.int/notices/v1/un/{noticeType}/{noticeID}/images


Die API ermöglicht, Images zu einzelnen UN Notices über die Pfad-Parameter *noticeType* (entweder "persons" oder "entities") und *noticeID* (z.B. 2021-84506) eines GET-requests anzufragen.


## Beispiel

```bash
redNotices=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/red?nationality=DE')
redNoticeDetails=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/red/1993-27493')
redNoticeImages=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/red/1993-27493/images')
yellowNotices=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/yellow?nationality=DE')
yellowNoticeDetails=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/yellow/2014-5590')
yellowNoticeImages=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/yellow/2014-5590/images')
UNNotices=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/yellow?nationality=DE')
UNNoticeDetails=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/un/persons/2021-84506')
UNNoticeImages=$(curl -m 60 'https://ws-public.interpol.int/notices/v1/un/persons/2021-84506/images')
```
