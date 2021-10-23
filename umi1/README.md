# Cvičení 1

## Zadání

![](images/Assignment.png)

## Řešení

Algoritmus pro řešení tohoto problému spočívá v rekurzivním prohledávání stavového prostoru **hrubou silou**. V každém kroku stavby tratě jsou postupně vyzkoušeny všechny druhy kolejí, dokud není nalezeno řešení. Algoritmus dokáže najít **uzavřenou** trať bez **překrývání** kolejí. Poradí si i s **výhybkami**.

Při tvorbě řešení bylo uvažováno následující zjednodušení:

* k dispozici máme **ROVNÉ** (*straight*), **PRAVOTOČIVÉ** (*curved*) koleje a dále **VÝHYBKY S ODBOČKOU DOPRAVA** (*divergent*) a **VÝHYBKY S PŘIPOJENÍM ZPRAVA** (*convergent*). Některé dětské sady však mají koleje pro vláček i zezdola (tzn. že pravotočivou kolej lze obrátit a získáme kolej levotočivou). Tato univerzalita však není v důsledku své složitosti v tomto řešení zohledněna. Koleje tudíž uvažujeme pouze na jedné straně.

Základem pro řešení tohoto problému je přechod ze **spojitého** prostředí do **diskrétního**, a tedy zobrazení kolejí do kartézské soustavy souřadnic. Je důležité si uvědomit, že rovné a pravotočivé koleje jsou součástí obou typů výhybek. Rovné koleje mají velikost 3, pravotočivé 2 a výhybky tak vzniknou kombinací předchozích. Vzhledem k tomu, že zatáčky mají úhel 45°, lze se po mřížce pohybovat až v 8 různých úhlech: 0°, 45°, 90°, 135°, 180°, 225°, 270° a 315° (tedy i diagonálně). Zatáčky kreslíme **pouze diagonálně**, avšak rovné úseky můžeme kreslit jak **horizontálně/vertikálně, tak i diagonálně** (avšak vždy se stejnou velikostí 3!). To může zejména u větších sad způsobovat pnutí mezi kolejemi.

![](images/1.png)

## Spuštění

`py main.py A B C D`

* **A** = počet **rovných** kolejí (*straight*)
* **B** = počet **pravotočivých** kolejí (*curved*)
* **C** = počet **výhybek s odbočkou doprava** (*divergent*)
* **D** = počet **výhybek s připojením zprava** (*convergent*)

## Výstupy

Na každém obrázku je uveden výstup algoritmu pro zadaný počet kolejí, zakreslení tratě do mřížky a u menších vstupů i spojitá varianta. Každý řádek výstupu znamená jednu položenou kolej ve formátu: (**(x, y, úhel)** na začátku koleje, **(x, y, úhel)** na konci koleje, **typ koleje**). Šipky v mřížce pak značí jednotlivé úhly.

![](images/2.png)
![](images/3.png)
![](images/4.png)
![](images/5.png)
![](images/6.png)
![](images/7.png)

Následuje výstup pro počty kolejí uvedené v zadání úlohy. Algoritmu trvalo necelých 5 hodin pro nalezení tohoto řešení. To svědčí o velké (exponenciální) složitosti prohledávání a nepraktičnosti/nepoužitelnosti pro velké sady kolejí.

![](images/8a.png)

Jako důkaz realizace jsou uvedeny i následující útržky spojitých variant. Bohužel jsem neměl k dispozici dostatečný počet kolejí, avšak pro ukázku snad stačí.

![](images/8b.png)

Pro některá zadání však algoritmus řešení nenašel. Například pro 16 pravotočivých kolejí by musel vytvořit dva identické kruhy po 8 kolejích. Proto je toto zadání vyhodnoceno jako **overlapping** (překrývání). 

![](images/No1.png)

Naopak nedostatek pravotočivých kolejí způsobí to, že trať nebude nikdy uzavřená. Počet pravotočivých kolejí musí být vždy takový, aby se jejich úhly nasčítaly na velikost 360° (tedz minimálně 8).

![](images/No2.png)

Výhybky způsobují „rozdvojení“ rekurze. Počet divergentních a konvergentních výhybek tak musí být vždy roven, protože jinak riskujeme neuzavřenost tratě.

![](images/No3.png)
