# Cvičení 2

## Zadání

![](images/Assignment.png)

## Řešení

Z výše uvedených algoritmů jsem vypracoval **BT** (*backtracking* včetně *forward checking*), **MAC_BT** (*backtracking* včetně *maintaining arc consistency*), **BJ** (*backjumping*) a **DBT** (*dynamic backtracking*). Jejich implementace se nachází v příslušných souborech ve složce **algorithms**. Při tvorbě jsem se snažil v maximální míře vycházet z pseudokódů uvedených v přednáškách. I přesto jsou v implementaci drobné rozdíly, tudíž jsem celý kód **příslušně okomentoval** pro rychlejší pochopení.

Pro testování jsem použil **8 náhodně vybraných zadání sudoku** rozřazených do různých kategorií obtížnosti (pro člověka). U každé instance byl navíc měřen čas CPU (vzhledem k malému počtu instancí však nelze činit obecné závěry). Níže uvedené výsledky pouze dokumentují **správnost jednotlivých algoritmů**.

## Spuštění

`py main.py ALG [-v]`

* **ALG** = zvolený algoritmus (povolené hodnoty: *BT*, *MAC_BT*, *BJ*, *DBT*)
* **v** = volitelný parametr *verbose* (ve výchozím nastavení jsou veškeré výstupy programu velmi stručné; tento parametr aktivuje obšírnější výstupy rozšířené o *vstupní zadání sudoku*, *výstupní řešení sudoku* a *řešení očekávané*)

## Výstupy

*Backtracking* včetně *Forward Checking*:

![](images/BT.png)

*Backtracking* včetně *Maintaining Arc Consistency*:

![](images/MAC_BT.png)

*Backjumping*:

![](images/BJ.png)

*Dynamic Backtracking*:

![](images/DBT.png)

## Použité sudoku a získaná řešení

**SUDOKU 1** (*lehké*):

![](images/Sudoku1.png)

**SUDOKU 2** (*lehké*):

![](images/Sudoku2.png)

**SUDOKU 3** (*lehké*):

![](images/Sudoku3.png)

**SUDOKU 4** (*střední*):

![](images/Sudoku4.png)

**SUDOKU 5** (*těžké*):

![](images/Sudoku5.png)

**SUDOKU 6** (*těžké*):

![](images/Sudoku6.png)

**SUDOKU 7** (*těžké*):

![](images/Sudoku7.png)

**SUDOKU 8** (*velmi těžké*):

![](images/Sudoku8.png)
