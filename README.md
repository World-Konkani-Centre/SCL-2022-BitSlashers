<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/World-Konkani-Centre/SCL-2022-BitSlashers/blob/main/README.md">
    <img src="https://ibb.co/HgSjzSG" alt="Logo" width="250" height="250">
  </a>


  <h3 align="center">WeGroW</h3>

  <p align="center">
    A single stop solution for fair crop trade
    <br/>
    By Team-BitSlashers
    <br />
    <a href="https://github.com/World-Konkani-Centre/SCL-2022-BitSlashers/blob/main/README.md">View Demo</a>
    ·
    <a href="https://github.com/World-Konkani-Centre/SCL-2022-BitSlashers/issues">Report Bug</a>
    ·
    <a href="https://github.com/World-Konkani-Centre/SCL-2022-BitSlashers/issues">Request Feature</a>
  </p>
  

</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Hello, welcome to WeGroW. Extremely glad you’re here. You might have observed farmers bearing huge loss during crop trade due to lack of market knowledge and predominance of intermediaries. Hence we are a single stop solution where farmers meet consumers, aided with analytical insights and regular price visibility.

### Built With
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>

* [Bootstrap](https://getbootstrap.com)
* HTML
* CSS
* [Python](https://www.python.org/downloads/)
* [Django](https://www.djangoproject.com/)

<!-- GETTING STARTED -->
## Getting Started


   
### Installation


1. Fork and Clone
    <ol>
    <li>Fork WeGroW Repo</li>
    <li>Clone the repo to your computer.</li>
    <li>Navigate through the directory</li>
    </ol>

2. Navigate Through the directory Create a Virtual Environment for the Project

    In Windows
    ```bash
    cd SCL-2022-BitSlashers/SCL_Project
    
    python -m venv venv
    
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    cd SCL-2022-BitSlashers/SCL_Project
    
    python -m virtualenv venv
    
    source venv/bin/activate
    ```
   
   If you are giving a different name then `venv`, then please mention it in `.gitigonre` first

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
   
4. Checkout to develop branch
     ```git
    git status
    git pull
    git branch
    git checkout develop
    
    ```   

5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    ```
6. Create a super user.
    In django if you want to access admin page, you need to create an account first.
    ```djangotemplate
    python manage.py createsuperuser
    ```
   Then select your username and password.
   
7. Run server
    ```bash
    python manage.py runserver
    ```
8. Do the Development and send us a PR referencing the issue.
 

