Przygotowanie nowej witryny
===========================

## Wymagane pakiety:
* nginx
* Python 3
* Git
* pip
* virtualenv

Na przykład w systemie Ubuntu należy wydać polecenia:
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Konfiguracja wirtualnych hostów w Nginx

* Zobacz plik nginx.template.conf
* SITENAME należy zastąpić odpowiednią nazwą, na przykład staging.my-domain.com

## Zadanie Upstart

* Zobacz plik gunicorn-upstart.template.conf
* SITENAME należy zastąpić odpowiednią nazwą, na przykład staging.my-domain.com

## Struktura katalogów
Przyjmujemy założenie o istnieniu konta użytkownika w postaci /home/USER

/home/USER
    sites
        SITENAME
            database
            source
            static
            venv