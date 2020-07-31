import requests

if __name__ == "__main__":
    keep_going = True
    while keep_going:
        code = input("""
            Inserire il codice corrispondente all'operazione desiderata:\n
            1->Stampa il message broker.\n
            2->Lista utenti.\n
            3->Lista dispostivi.\n
            4->Lista servizi.\n
            5->Cerca utente.\n
            6->Cerca dispositivo.\
            0->Termina ed esci.
        """)
        if code=="1":
            r1 = requests.get("http://localhost:8080/ip")
            print(r1)
        elif code=="2":
            r2 = requests.get("http://localhost:8080/users/list")
            print(r2)
        elif code=="3":
            r3 = requests.get("http://localhost:8080/devices/list")
            print(r3)
        elif code=="4":
            r4 = requests.get("http://localhost:8080/services/list")
            print(r4)
        elif code=="5":
            x=input("Please write now which user you want to find: ")
            r5 = requests.get("http://localhost:8080/users/search/"+x)
            print(r5)
        elif code =="6":
            x=input("Please write now which device you want to find: ")
            r6 = requests.get("http://localhost:8080/devices/search/"+x)
        elif code =="0":
            keep_going = False
            print("Bye!")
