# LMS - learning 


## Algorytm implementacyjny funkcjonalności w django:
1. Czy potrzebuje django app?
    -`python manage.py startapp <app label?`
   -Następnie dodać do settings.py - INSTALLED_APPS
 2. Czy potrzebuje dane?
 - stworzyć modele w models.py(Django Models ORM)
 - robię migracje: `python.manage.py makemigrations <app lebel>`
 - Aplikuje zmianę scheme ab `python manage.py migrate <app lebel>`
 - piszę Unit tests
3. Czy potrzebuje zarządzać danymi z CMS(Content management system, Django Admin)
    - rejestruje modle w admin.py
   4. Czy potrzebuje wprowadzania danych od użytkownika?
   - Django Forms , plik forms.py
   5. czy potrzebuje obsłużyć request?
    - tworze logikę we views.py za pomoc funk
   6. czy potrzebuje html?
   -Djang templates -> './templates/<app label>/<file>
   7. Czy potrzebuje router?
   -tworze lokalne urls.py, pamiętam o app_name i name do każdego endpointa
   8. Podpinam lokalne urls.py do globalny 'include'
   9. Podpinam widok do menu w templatkach
   10. Profit! Idę testować.