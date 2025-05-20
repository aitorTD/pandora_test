<h1>Pandora FMS technical test</h1>

<h2>Purpose</h2>
<p>This is a Python CLI application that downloads and displays photos from JSONPlaceholder API. It supports three different execution modes:</p>
<ul>
<li>Sequential - Processes photos one by one</li>
<li>Multithreaded - Uses threads for parallel processing</li>
<li>Multiprocess - Uses separate processes for maximum performance</li>
</ul>

<h2>Required Packages</h2>
<ul>
<li>Click</li>
<li>Requests</li>
</ul>

<h2>Installation</h2>
1. Clone the GitHub repository:<br>
<code>git clone https://github.com/aitorTD/pandora_test.git</code><br>
<code>cd pandora_test</code><br><br>
2. Install required packages:<br>
<code>python -m pip install --upgrade pip</code><br>
<code>pip install -r requirements.txt</code>

<h2>How to Run</h2>
<code>python cli.py --mode mode --photos number_of_photos</code>
<br><br>
Where <code>mode</code> can be:
<ul>
<li>sequential</li>
<li>multithread</li>
<li>multiprocess</li>
</ul>
<br>
And <code>number_of_photos</code> can be a positive integer, or leave it blank to download all photos.
<br>
<h4>Usage Example:</h4>
To run the program in sequential mode and display 2 photos, use:
<br>
<code>python cli.py --mode sequential --photos 2</code>
<br><br>
<strong>Expected Output:</strong>
<br>
<code>Execution mode: Sequential<br>
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