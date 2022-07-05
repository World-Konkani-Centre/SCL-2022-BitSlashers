<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Karthik-Shenoy/Team-Ankuram-maxo/blob/main/README.md">
    <img src="https://firebasestorage.googleapis.com/v0/b/ankuram-maxo-website.appspot.com/o/Project_Git%2FAnkuram%20Logo.png?alt=media&token=ac69eb50-5050-408c-a058-e1fcb11f2487" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">Team-Ankuram</h3>

  <p align="center">
    A website to enhance your coding and aptitude abilities
    <br />
    <a href="https://github.com/Karthik-Shenoy/Team-Ankuram-maxo/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Karthik-Shenoy/Team-Ankuram-maxo/blob/main/README.md">View Demo</a>
    ·
    <a href="https://github.com/Karthik-Shenoy/Team-Ankuram-maxo/issues">Report Bug</a>
    ·
    <a href="https://github.com/Karthik-Shenoy/Team-Ankuram-maxo/issues">Request Feature</a>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Hello, welcome to Coder Connect. Extremely glad you’re here. Have you ever been frustrated/discouraged while looking out for a bunch of aptitude questions? Were the level of questions not able to meet your expectations? Ever felt the need of an associate to discuss and clear your doubts? This portal has been designed to guide you through this strenuous journey and pave an easier path for the destination.

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

### Prerequisites

1. Fork and Clone
    <ol>
    <li>Fork the Team-Ankuram-maxo Repo</li>
    <li>Clone the repo to you computer.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    python -m venv venv
    
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv
    
    source venv/bin/activate
    ```
   
   If you are giving a different name then `venv`, then please mention it in `.gitigonre` first
   
   3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
   
### Installation
   

  4. Checkout to develop branch
       ```git
      git status
      git pull
      git branch
      git checkout develop
     
     
  6. Create a super user.
      In django if you want to access admin page, you need to create an account first.
      ```djangotemplate
      python manage.py createsuperuser
      ```
     Then select your username and password.

  8. Run server
      ```bash
      python manage.py runserver
      ```
 
 <!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
