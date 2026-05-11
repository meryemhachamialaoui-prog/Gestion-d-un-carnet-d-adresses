
from contact import Contact
from  address_book import AddressBook
import os
def main():
    book = AddressBook()

    while True:
        print("\n===== MENU =====")
        print("1. Ajouter un contact")
        print("2. Supprimer un contact")
        print("3. Afficher les contacts")
        print("4. Quitter")

        choice = input("Choix: ")

        if choice == "1":
            nom = input("Nom: ")
            email = input("Email: ")
            numtele = input("Téléphone: ")   

            try:
                contact = Contact(nom, email, numtele)
                book.add_contact(contact)
            except:
                print("Erreur dans les données")

        elif choice == "2":
            email = input("email du contact à supprimer: ")
            book.remove_contact(email)

        elif choice == "3":
            book.display_contacts()

        elif choice == "4":
            break

        else:
            print("Choix invalide")


main()