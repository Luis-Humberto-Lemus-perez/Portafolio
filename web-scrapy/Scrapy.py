import scrapy
lista_datos=[]
class Scrapear (scrapy.Spider):
    name="web-scraping"
    #dominio y url que se desea scrapear
    allowed_domains=['https://elblogpython.com/tutoriales-python/los-mejores-proyectos-de-python-de-principiante-a-avanzado/#calculadorapropinas']
    start_urls=['https://elblogpython.com/tutoriales-python/los-mejores-proyectos-de-python-de-principiante-a-avanzado/#calculadorapropinas']
    def parse(self,response):
        print("parseando " + response.url)
        next_urls=response.css('a::attr(href)').getall()
        for next_url in next_urls:
            if next_url is not None:
                yield scrapy.Request(response.urljoin(next_url))
        frases = response.css('p::text').getall()
        for frase in frases:
            if frase is not lista_datos:
                lista_datos.append(frase)

        for datos in lista_datos:
            print(datos)

        #en terminal ejecutar lo siguiente : scrapy runspider --nolog  Scrapy.py