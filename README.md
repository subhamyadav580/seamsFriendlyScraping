# Installation instructions

Setting up project on your local machine is really easy. You can setup this project by following steps:

1. Get the source code on to your machine via git.

    ```git clone https://github.com/subhamyadav580/seamsFriendlyScraping.git```


2. Now change the directory.

    ```cd seamsFriendlyScraping```

3. Now activate the virtual environment.

    ```source myvenv/bin/activate```

4. If you want to install all dependencies on your local computer the this step is required (then 3rd step is optional)

    ```pip3 install -r requirements.txt```

5. Now change the directory into project directory.

    ```cd seamsFriendlyScraping```

6. Now execute the code and scrap the website.

    ```scrapy crawl seamsFriendlySpider```

7. For saving the scraped data into JSON format.

    ```scrapy crawl seamsFriendlySpider -o file_name.json```

8. For saving the scraped data into CSV format.

    ```scrapy crawl seamsFriendlySpider -o file_name.csv```