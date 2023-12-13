import hashlib
import json
import random

#Variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_maj = alphabet.upper()
numbers = "0123456789"
special_characters = "!@#$%^&*"

#Fonctions 

#mot de passe hachée
def hashed(password):
    return hashlib.sha256(password.encode()).hexdigest()

#sauvegarder le fichier json
def save_password(password):
    with open("passwords.json","a") as file:
        file.write(f'"{password}"\n')

#ouvrir le fichier json
def load_passwords():
    with open("passwords.json", "r") as file:
        return [line.strip().strip('"') for line in file]

#Trouver si le mot de passe existe deja  
def duplicate(hashed_password):
    file_content = load_passwords()
    for i in file_content:
        if i == hashed_password:
            return True
    return False 

#Mot de passe aléatoire
def generate_password():
    global alphabet, alphabet_maj, numbers, special_characters

    password_gen=""
    len_alp=random.randint(3,9)
    password_gen += ''.join(random.sample(alphabet, k=len_alp))
    len_alp_maj=random.randint(3,9)
    password_gen += ''.join(random.sample(alphabet_maj, k=len_alp_maj))
    len_numbers=random.randint(3,9)
    password_gen += ''.join(random.sample(numbers, k=len_numbers))
    len_spe_char=random.randint(1,4)
    password_gen += ''.join(random.sample(special_characters, k=len_spe_char))

    password_gen_list = list(password_gen)
    random.shuffle(password_gen_list)
    password_gen = ''.join(password_gen_list)
    hashed_password_gen = hashed(password_gen)

    print("Le mot de passe aléatoire est", password_gen,"et le mot de passe haché est",hashed_password_gen)
    save_password(hashed_password_gen)
    file_content =input("Voulez vous lire le fichier avec les mots de passes ? Yes/No ")
    if file_content == "Yes":
        print(load_passwords())


#Run la logique de la vérification du mdp

while True:
    password_guest = input("Votre mot de passe doit au moins contenir : 8 caractères, 1 lettre majuscule, 1 lettre minuscule, 1 chiffre et 1 caractère spécial (!, @, #, $, %, ^, &, *)\nGénérer un mot de passe en entrant 'oui' ou Entrez votre mot de passe: ")

    if password_guest == "oui":
            generate_password()
            break
    if len(password_guest) < 8:
        print("Le mot de passe est trop court.")
    else:
        alphabet_found = False
        alphabet_maj_found = False
        numbers_found = False
        special_characters_found = False
        hashed_password = hashed(password_guest)

        for char in password_guest:
            if char in alphabet:
                alphabet_found = True
            elif char in alphabet_maj:
                alphabet_maj_found = True
            elif char in numbers:
                numbers_found = True
            elif char in special_characters:
                special_characters_found = True

        if not alphabet_found:
            print("Le mot de passe doit contenir au moins une lettre minuscule.")
        if not alphabet_maj_found:
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
        if not numbers_found:
            print("Le mot de passe doit contenir au moins un chiffre.")
        if not special_characters_found:
            print("Le mot de passe doit contenir au moins un caractère spécial.")
        if duplicate(hashed_password) == True:
            print("Le mot de passe est déjà enregistré")

        if alphabet_found and alphabet_maj_found and numbers_found and special_characters_found and not duplicate(hashed_password):
            print("Votre mot de passe est correct.")
            print("Votre mot de passe crypté avec SHA-256 :",hashed_password)
            save_password(hashed_password)
            file_content =input("Voulez vous lire le fichier avec les mots de passes ? Yes/No ")
            if file_content == "Yes":
                print(load_passwords())

            break


