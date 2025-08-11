Acest proiect este o aplicatie care ofera operatii matematice de baza sub forma:
- unei interfete de tip CLI (Command Line Interface)
- unui microserviciu ca API REST cu FastAPI
- ridicare la putere (pow)
- calculul sirului Fibonacci (fib)
- calculul factorialului (fact)

Exemple de rulare: 
- python cli/main.py pow --base 2 --exp 8
- python cli/main.py fib --n 10
- python cli/main.py fact --n 5
- python cli/main.py view  

Functionalitatile implementate:
- pow – ridicare la putere
- fib – termenul n din sirul Fibonacci
- fact – factorialul unui numar
- Salvare in baza de date (SQLite) a fiecarei operatii efectuate
- Interfata interactiva Swagger UI la /docs
- Validare input cu Pydantic
- Structura modulara: CLI, API, servicii, modele, persistare

