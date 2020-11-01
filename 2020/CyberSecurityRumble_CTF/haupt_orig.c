#include <stdio.h>
#include <stdlib.h>
#include "fahne.h"

#define Hauptroutine main
#define nichts void
#define Ganzzahl int
#define schleife(n) for (Ganzzahl i = n; i--;)
#define bitrverschieb(n, m) (n) >> (m)
#define diskreteAddition(n, m) (n) ^ (m)
#define wenn if
#define ansonsten else
#define Zeichen char
#define Zeiger *
#define Referenz &
#define Ausgabe(s) puts(s)
#define FormatAusgabe printf
#define FormatEingabe scanf
#define Zufall rand()
#define istgleich =
#define gleichbedeutend ==

nichts Hauptroutine(nichts) {
    Ganzzahl i istgleich Zufall;
    Ganzzahl k istgleich 13;
    Ganzzahl e;
    Ganzzahl Zeiger p istgleich Referenz i;

    FormatAusgabe("%d\n", i);
    fflush(stdout);
    FormatEingabe("%d %d", Referenz k, Referenz e);

    schleife(7)
        k istgleich bitrverschieb(Zeiger p, k % 3);

    k istgleich diskreteAddition(k, e);

    wenn(k gleichbedeutend 53225)
        Ausgabe(Fahne);
    ansonsten
        Ausgabe("War wohl nichts!");
}
