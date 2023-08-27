the task
Bajtazar jedzie nad morze swoim nowym sportowym autem. Jedzie autostradą i jak przystało na porządnego
kierowcę, porusza się prawym pasem. Jednak przed nim prawym pasem autostrady jedzie też n ciężarówek,
które będzie musiał wyprzedzić.
Ciężarówki numerujemy od 1 do n, poczynając od tej najbliższej auta Bajtazara; i-ta z nich porusza
się z prędkością vi
, ma długość di oraz w chwili początkowej znajduje się xi przed autem Bajtazara. Dla
uproszczenia samochody traktujemy jak prostokąty bez brzegu, a za ich pozycję przyjmujemy przedni bok.
Jeśli z powodu różnicy prędkości przód i-tej ciężarówki zrówna się z tyłem ciężarówki ją poprzedzającej
(tej o numerze i + 1), to i-ta ciężarówka zwalnia do prędkości (i + 1)-szej ciężarówki (czyli ciężarówki nie
wyprzedzają się nawzajem).
Bajtazar jedzie z prędkością V , szybciej niż każda z ciężarówek (V > vi dla każdego i), a jego auto
ma długość D. W momencie, gdy przód auta zrówna się z tyłem jakiejś ciężarówki, Bajtazar momentalnie
wykonuje manewr zmiany pasa i kontynuuje jazdę lewym pasem. Gdy tylko będzie możliwa zmiana pasa na
prawy, Bajtazar wykonuje ten manewr (nawet gdyby w tym samym momencie musiał znów zmienić pas na
lewy).
Bajtazar zastanawia się, ile razy podczas wyprzedzania wszystkich ciężarówek wykona manewr zmiany pasa
z prawego na lewy. Zakładamy, że w chwili obecnej autostradą nie jedzie żaden inny samochód.
Wejście
W pierwszym wierszu wejścia znajdują się cztery liczby całkowite n, D, W, M (1 ≤ n ≤ 100 000, 1 ≤ D ≤ 109
,
1 ≤ W, M ≤ 1000) oznaczające liczbę ciężarówek, długość auta Bajtazara i jego prędkość daną wzorem
V = W/M.
W kolejnych n wierszach znajdują się opisy ciężarówek; i-ty z nich zawiera cztery liczby całkowite xi
, di
,
wi
, mi (1 ≤ xi
, di ≤ 109
, 1 ≤ wi
, mi ≤ 1000). Prędkość ciężarówki to vi = wi/mi
.
Pojazdy nie nachodzą na siebie, czyli 0 ≤ x1 − d1 oraz xi ≤ xi+1 − di+1 dla 1 ≤ i < n.
Wszystkie długości i położenia wyrażone są w jednostkach odległości, a prędkości w jednostkach odległości
na jednostkę czasu.
Wyjście
Twój program powinien wypisać na wyjście jeden wiersz zawierający liczbę całkowitą oznaczającą, ile razy
Bajtazar wykona manewr zmiany pasa na lewy.
Przykład
Dla danych wejściowych:
3 1 1 1
3 2 1 4
6 3 1 2
10 2 1 4
poprawnym wynikiem jest:
2
