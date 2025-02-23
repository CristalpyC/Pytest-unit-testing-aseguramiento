# Pruebas de la API de Pokémon
<img src="https://cdn.prod.website-files.com/619e15d781b21202de206fb5/6304ea816823cf0a4b06f777_what-is-testing.jpg" alt="testing" />


## 1. <span style="color: #007bff;">test_obtener_listado_pokemon</span>
### <span style="font-style: italic;">Objetivo:</span> Simular la obtención de una lista de Pokémon desde la API.
### <span style="font-style: italic;">Escenario:</span> Un usuario o sistema solicita la lista de todos los Pokémon disponibles.
### <span style="font-style: italic;">Detalles:</span>
<p>La prueba simula una respuesta de la ruta <code>/pokemon</code> con el Pokémon "bulbasaur". Se verifica que la respuesta sea 200 y que el primer Pokémon listado sea "bulbasaur".</p>

---

## 2. <span style="color: #007bff;">test_obtener_pokemon_especifico</span>
### <span style="font-style: italic;">Objetivo:</span> Simular la consulta de un Pokémon específico (Ivysaur) por su ID.
### <span style="font-style: italic;">Escenario:</span> Un usuario busca detalles sobre Ivysaur (ID 2).
### <span style="font-style: italic;">Detalles:</span>
<p>La prueba simula una respuesta de la ruta <code>/pokemon/2</code> con la información de Ivysaur. Se verifica que la respuesta sea 200 y que el nombre y ID del Pokémon sean "ivysaur" y 2, respectivamente.</p>

---

## 3. <span style="color: #007bff;">test_obtener_tipos_pokemon</span>
### <span style="font-style: italic;">Objetivo:</span> Simular la obtención de todos los tipos de Pokémon disponibles.
### <span style="font-style: italic;">Escenario:</span> Un usuario quiere conocer los tipos de Pokémon, como "fuego" o "agua".
### <span style="font-style: italic;">Detalles:</span>
<p>La prueba simula una respuesta de la ruta <code>/type</code> con los tipos "fire" y "water". Se valida que la respuesta sea 200 y que contenga al menos un tipo de Pokémon.</p>

---

## 4. <span style="color: #007bff;">test_obtener_especie_pokemon</span>
### <span style="font-style: italic;">Objetivo:</span> Simular la obtención de información sobre la especie de un Pokémon (Ivysaur).
### <span style="font-style: italic;">Escenario:</span> Un usuario desea obtener información sobre la especie de Ivysaur.
### <span style="font-style: italic;">Detalles:</span>
<p>La prueba simula una respuesta de la ruta <code>/pokemon-species/2</code> con los datos sobre la especie de Ivysaur. Se comprueba que la respuesta sea 200 y que el nombre de la especie sea "ivysaur".</p>

---

<h3>Asegure tener instalado <strong style="color:blue">pytest</strong></h3>
<h3>Ejecutar "python -m "test_pokemonApi.test" para ver los resultados</h3>
