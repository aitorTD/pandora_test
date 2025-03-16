<h1>Pandora FMS technical test</h1>

<h2>Paquetes requeridos</h2>

<ul>
<li>Click</li>
<li>Requests</li>
</ul>

<h2>Cómo instalar</h2>
1. Clonar el repositorio de GitHub: <br>
<code>git clone https://github.com/aitorTD/pandora_test.git</code>
<br><br>
2. Instalar los paquetes requeridos:<br>
<code>pip install -r requirements.txt</code>

<h2>Cómo ejecutar</h2>
<code>python cli.py --mode modo --photos número_de_fotos </code>
<br><br>
Donde <code>modo</code> puede ser:
<ul>
<li>secuencial</li>
<li>multihilo</li>
<li>multiprocesos</li>
</ul>
<br>
Y <code>número_de_fotos</code> puede ser un número entero positivo, o dejarlo en blanco para que se descarguen todas las fotos.
<br>
<h4>Ejemplo de uso:</h4>
Para ejecutar el programa en modo secuencial y mostrar 2 fotos, utiliza:
<br>
<code>python cli.py --mode secuencial --photos 2</code>
<br><br>
<stong>Resultado esperado:</strong>
<br>
<code>Modo de ejecucion: Secuencial<br>
Success receiving data<br>
Pic ID: 1<br>
Title: Accusamus Beatae Ad Facilis Cum Similique Qui Sunt<br>
URL: https://via.placeholder.com/600/92c952<br>
Album ID: 1<br>
Album Title: quidem molestiae enim<br>
------------------------------------------<br>
Pic ID: 2<br>
Title: Reprehenderit Est Deserunt Velit Ipsam<br>
URL: https://via.placeholder.com/600/771796<br>
Album ID: 1<br>
Album Title: quidem molestiae enim<br>
------------------------------------------<br>
Time taken: 0.20 seconds<br>
</code>