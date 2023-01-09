# Eindproject_Jesse_Dierckx_API


[![Contributors][contributors-shield]][contributors-url]


  <h3 align="center">Api development Eindproject Jesse Dierckx</h3>



## Voordat we starten

Voordat we starten met elke screenshot zie je foto's bijkomen dit zijn de screenshots dat ik nam terwijl ik deze readme file aan het maken was dus maak u daar maar geen zorgen over


## Beschrijving thema

Als thema heb ik gekozen om een api te maken waar je users mee kunt maken waarvan elk van deze een lijstje kunnen maken,
waar ze informatie op kunnen zetten bijvoorbeeld dingen dat ze willen meenemen van de supermarkt of de mediamarkt.
Dit kan natuurlijk ook hgebruikt worden als memo voor dingen dat ze moeten doen.

## Algemene eisen & documentatie

- [x] Minstens 3 GET, 1 POST, 1 PUT en 1 DELETE endpoints
- [x] Minstens 3 entiteiten in je API via een SQLite databank
- [x] Minstens hashing en OAuth implementeren
- [x] Beschrijving van het gekozen thema, je API(s) en je uitbreidingen + link naar de zaken die hosted zijn op GitHub README.md
- [x] Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
- [x] Volledige OpenAPI docs screenshot(s) op GitHub README.md
- [x] Logisch gebruik van path parameters, query parameters en body
- [x] Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt
- [x] Deployment van de API container(s) op Okteto Cloud via Docker Compose

## Volledige OpenAPI docs screenshot(s) op GitHub README.md

Als eerste zal ik de openapi docs screenshots laten zien omdat dit een goede overview geeft
![img_1.png](images/img_1.png)
![img_3.png](images/img_3.png)
![img_4.png](images/img_4.png)
![img_5.png](images/img_5.png)
![img_6.png](images/img_6.png)
![img_7.png](images/img_7.png)
![img_14.png](images/img_14.png)
![img_8.png](images/img_8.png)
![img_9.png](images/img_9.png)
![img_10.png](images/img_10.png)
Zoals je hieronder ook kan zien heb ik juist de user michiel aangemaakt ik zal wat screenshots verder naar onder dan ook een item aanmaken voor de user michiel
![img_11.png](images/img_11.png)
![img_12.png](images/img_12.png)
![img_13.png](images/img_13.png)
![img_15.png](images/img_15.png)
### Nu zal ik even de 2 post en 3 get functies laten zien:
![img.png](images/img.png)
![img.png](images/img_2.png)
Zoals je hierboven kunt zien heb ik 2 post functions en 3 get functions exclusief de post voor de bearer token van een user op te vragen


## hashing en oauth implementatie:
Zoals je hieronder kan zien is oauth en hashing correct geimplementeerd in een aparte python file zoals in de klas gedemonstreerd
![img_16.png](images/img_16.png)
![img_17.png](images/img_17.png)

## werking API door screenshots van postman requests:
Eerst zal ik de 3 gets laten zien en daarna zal ik de twee posts laten zien


### GET Requests
![img_18.png](images/img_18.png)
![img_19.png](images/img_19.png)
![img_21.png](images/img_21.png)
![img_22.png](images/img_22.png)

### POST Requests

![img_23.png](images/img_23.png)
![img_24.png](images/img_24.png)

Zoals je kan zien werken de 3 gets en 2 posts helemaal correct

## Logisch gebruik van path parameters, query parameters en body:

Hieronder zal ik laten zien dat ik de correcte manier heb gebruikt om een crus op te stellen

### database file
![img_25.png](images/img_25.png)
### crud file
![img_26.png](images/img_26.png)
![img_27.png](images/img_27.png)
### models file
![img_28.png](images/img_28.png)
### schemas file
![img_29.png](images/img_29.png)
![img_30.png](images/img_30.png)

### Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt:
## De Dockerfile
![img_32.png](images/img_32.png)

## De docker-compose file
![img_33.png](images/img_33.png)

## De workflow file
![img_50.png](images/img_50.png)
Zoals je kan zien is alles op een fatsoenlijke manier opgebouwd.

### Github actions
![img40.png](images/img40.png)
![img41.png](images/img41.png)
![img42.png](images/img42.png)

## deployment naar okteto
![img_43.png](images/img_43.png)
![img_44.png](images/img_44.png)
![img_45.png](images/img_45.png)
![img_46.png](images/img_46.png)
![img_47.png](images/img_47.png)
### Als extra nog een screenshot van de database in DB browser for sqlite
![img_31.png](images/img_31.png)




p.s De link helemaal vanboven is om naar mijn contributors pagina te gaan van mijn API repository.
En als je ziet dat de foto's weg zijn in mijn github repository ik heb deze later in de images map gezet.
+ Ik heb er nog een file bijgestoken met de passwords van de aangemaakte users zodat u ook zelf zou kunnen checken of het daadwerkelijk werkt of niet deze staat in de images map.

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/JesseDierckx/eindproject-Jesse-Dierckx-api/graphs/contributors