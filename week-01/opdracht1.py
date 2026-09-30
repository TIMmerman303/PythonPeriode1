 # Oefening 1
# Print de volgende zin "Hello World"

print("Hello World")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Tim Lavrijssen"
leeftijd = 17
woonstad = "Utrecht"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print(f"Mijn naam is {naam}")
print(f"Ik ben {leeftijd} jaar oud")
print(f"Ik woon in {woonstad}")


# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"
Fav_game = "Lords of the Fallen"
Hours_played = 213
Score = 9.5
print (f"Mijn favoriete game is {Fav_game}")
print (f"Ik heb deze game {Hours_played} uur gespeeld")
print (f"Ik geef deze game een {Score}")
# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit
number1 = 10
number2 = 5 
som = number1 + number2
verschil = number1 - number2
product = number1 * number2
print(f"De som van {number1} en {number2} is {som}")
print(f"Het verschil van {number1} en {number2} is {verschil}")
print(f"Het product van {number1} en {number2} is {product}")

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit
name = "Arthas"
health = 100
level = 1
damage = 20
print(f"Naam: {name}")
print (f"level: {level}")
print (f"Health: {health - damage}")
# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 
health = 100
level = 2
name = "Thor"
weapon = "Mjolnir"
damage = 95

print(f"Naam: {name}")
print(f"Health: {health}-{weapon} = {health - damage}")
# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe
name = "John Doe"
age = 25
favouriteGame = "Call of Duty"
hoursPlayed = 150
level = 10
score = 5000