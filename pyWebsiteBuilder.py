# comments in python
indexHtml = open("index.html","w")
indexHtml.write("<!DOCTYPE html><html>")
siteName = "Website"
headHtmlString = "<head><title>"+siteName+"</title><link href='/normalize.css' rel='stylesheet'></head>"
indexHtml.write(headHtmlString)
bodyHtmlString = """<body>
    					<header>
					     	<img src="/assets/jeff.png">
					      	<h1>Jeff's Blog</h1>
						    <div class="nav">
						     	<ul>
						        	<li><a href="#">Home</a></li>
						        	<li><a href="#">Archive</a></li>
						        	<li><a href="#">Contact</a></li>
						      	</ul>
						    </div>
					    </header>
					    <p>
					    And then a whole  bunch of content below in this area right here. And then a whole  bunch of content below in this area right here. And then a whole  bunch of content below in this area right here. And then a whole  bunch of content below in this <a href="www.google.com">google</a> area right here. And then a whole  bunch of content below in this area right here. And then a whole  bunch of content below in this area right here. And then a whole <img src="/assets/jeff-terrible.png"> bunch of content below in this area right here. And then a whole  bunch of content below in this area right here.
					    </p>
					</body>"""
indexHtml.write(bodyHtmlString)
indexHtml.write("</html>")
