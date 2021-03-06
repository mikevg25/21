# Projectplan #21 Recipes
### Webprogrammeren en Databases
Sebastiaan van Dijk
Alex Hakvoort
Jasmine Evers
Mike van Gils

### Onze productvideo
Onze productvideo staat verborgen op YouTube maar is te vinden via deze link:
 https://youtu.be/nx9MeS-tG3o

## Overzicht van project
Voor het vak ‘Webprogrammeren en Databases IK’ is de opdracht om een eigen website te bouwen. Groep 21 heeft gekozen voor een ‘photo sharing’-website.
Daarin kunnen gebruikers foto’s uploaden die door andere gebruikers kunnen worden beoordeeld. Onze doelgroep is kookliefhebbers.
Een gebruiker maakt een profiel aan op basis van haar favoriete gerecht. Gebruikers kunnen op onze website met een Tinder-achtig interface
kiezen of zij een bepaald gerecht wel of niet leuk vinden om vervolgens wel of niet met de eigenaar in contact te komen. Na een match van elkaars
gerecht kunnen deze gebruikers contact met elkaar opnemen. Op een overzichtspagina kunnen zij een gerecht dus naar links of naar rechts vegen.
Op een account-pagina kan de gebruikers vervolgens zien welke gerechten hij naar rechts heeft geveegd. Op deze pagina kan de gebruikers doorklikken
naar een gerecht en de contactgegevens van de eigenaar. Een leuke naam voor de website: FoodieMatch.

## Projectdoelstelling
Onze doelstelling is het samenbrengen van kookliefhebbers die elkaar graag hun gerecht willen leren. We hopen de liefhebbers enthousiast te maken
maar ook nieuwe mensen te laten ontmoeten. Op onze website komt men namelijk in contact met andere kookliefhebbers die misschien naast het leren
van een nieuw gerecht, ook wel zin hebben in een leuke tijd met een andere hobbyist. Het is belangrijk dat onze site een leuke interactie biedt.
Dat hopen wij met de Tinder-layout te gaan bereiken.

## Features
-   Registratie-pagina
	-   Invullen van naam, wachtwoord, email, andere gegevens (additional)
	-   Het uploaden van je (eerste gerecht)
		-   Afbeelding, titel, allergiën (ingredienten en bereidingswijze niet want dat moet men elkaar juist real-life leren)
-   Log In-pagina
	-   Functie wachtwoord vergeten
-   Browse-pagina, waar men elkaar gerechten kan liken of disliken.
	-   Foto van het gerecht
	-   Allergiën (additional)
	-   Locatie van de eigenaar (additional)
	-   De like en dislike button
-   Match-pagina, hier komt het gerecht van een persoon dat jij hebt geliket, als hij ook jouw gerecht heeft geliket.
	-   Bij het klikken op het gerecht verschijnen contactgegevens van de eigenaar.
	-   Of de mogelijkheid om te unliken. (additional)
-   ChangeRecipe-pagina, hier komt je huidige gerecht te staan maar ook de mogelijkheid om deze aan te passen.
-   Account-pagina
	-   Gegevens en wachtwoord wijzigen.
	-   Account verwijderen
	-   Uitloggen

## Layout, de screenshots
De screenshots van ons eindproduct zijn te vinden onder het mapje docs maar wij raden aan om onze productvideo te bekijken waarin wij per scherm en feature toelichting geven.

## Layout, de schetsen
![enter image description here](https://lh3.googleusercontent.com/plZgqXmlpuy6YpRWbDfXFlHnCvLFc1NSGLyadCqEJu8LaKtnmnMuEHNhx7GcGbDu4aSt3kA-R5vl)
Registratie pagina

![enter image description here](https://lh3.googleusercontent.com/tSAA0sD7tmG0cqqWeSUHi-0VS-dAPGHwzpIlLiY1E5btXE1XH6FMLdiayp0hEw-zPACpfdoZg8sO)
Login pagina

![enter image description here](https://lh3.googleusercontent.com/zkc5Ob_evkH29DvDUkiqfd7hzPqH_LUL7eGyolkzuGbtnCytkG-ukljYyqm-rbQu6zQT73UUckz8)
Browsing pagina

![enter image description here](https://lh3.googleusercontent.com/0ei5u6CnUNZUMg_CS4xhAQRmsPLvH1MynJ1jNXPn30cYp3DSFxtuacn9fYK0eCVguzRuvkSkzu0I)
Pagina met matches

![enter image description here](https://lh3.googleusercontent.com/K_gHOck9C03DnGqWqyCmCdcVc7_DZUxaE6-WJbqmki39EUnxZfo8sAWqGAUCypfy6XmMUfuL5bEq)
Account pagina

## Databronnen
API:
-   [https://www.programmableweb.com/category/food/api](https://www.programmableweb.com/category/food/api)
-   [https://www.esha.com/resources/additional-databases/](https://www.esha.com/resources/additional-databases/)
-   [https://airtable.com/universe/expHZcS7kWEyq5gUH/recipe-database?explore=true](https://airtable.com/universe/expHZcS7kWEyq5gUH/recipe-database?explore=true)
-   [https://spoonacular.com](https://spoonacular.com)
-   [http://api2.bigoven.com](http://api2.bigoven.com)
-   [https://developer.edamam.com](https://developer.edamam.com)
-   [https://developer.edamam.com/edamam-docs-recipe-api](https://developer.edamam.com/edamam-docs-recipe-api)
-   [https://sightengine.com](https://sightengine.com)

### Externe componenten
-   Bootstrap
-   GitHub
-   Flask

### Concurrerende sites
-   [https://www.ylona.nl](https://www.ylona.nl)
-   [https://www.tinder.com](https://www.tinder.com)

### Moeilijkheden
De moeilijkste elementen zullen te maken hebben met het uploaden van de afbeeldingen en/of gifs. Daarnaast moeten we veel tijd steken in het
uitzoeken hoe we matchende gebruikers ontdekken. We zullen met id's moeten gaan werken en wanneer er een wederzijdse like is, moeten wij een
match maken.

### Rolverdeling
We hebben met z'n allen aan de website gewerkt. De een hield zich wat meer bezig met het back-end programmeerwerk en de ander wat meer met het
HTML/CSS front-end programmeerwerk maar we ondersteunden elkaar op de plekken waar dat nodig was. Over het algemeen hebben Sebastiaan en Jasmine
het meeste aan het uiterlijk gewerkt en Alex en Mike wat meer aan het python programmeerwerk.

### Repository
Onze repository hebben wij zo klein mogelijk proberen te houden. Het mapje git kwam er automatisch bij omdat het anders niet werkt. In het mapje doc
kan onze DESIGN.md en README.md worden gevonden, daarnaast zie je daar ook onze oorspronkelijke schetsen en de screenshots van het eindproduct. In de static map
zitten een aantal css-bestanden, achtergronden voor verschillende pagina's maar ook alle recipe-images/gifs van alle gebruiker (vernoemd naar hun user-id).

De mappen partials en scss bevatten toevoegingen voor het algemene CSS bestand die er voornamelijk zijn voor het goed functioneren van de navigation bar.

Onze templates zijn al onze pagina's te vinden waarin je navigeert door onze website. De pagina's worden aangedreven door de functies die te vinden zijn in application.py
waarvan sommige daarvan dan weer ondersteunt worden door functies uit helpers.py. Hierin staan codelines die vaker terugkomen en handiger werden om ze een vaste functie te geven.

Tot slot onze database foodiematch.db. Hierin staan drie tabellen (users, recipes en like). In users staan de gebruikersgegevens, in recipes hun gerecht en de locatie van de afbeelding
of gif in de repository, en in likes staan de acties waarin mensen zijn geliket of zelf geliket hebben.

