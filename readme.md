# Django Template

This is a basic Django project and singular application, which includes login
and registration features, along with validations. This is a useful django 1.11
template to build larger projects, with the basic login and validation features
ready to go.

*Note: This project must be updated after being cloned. Instructions for updating
core Django files is listed below.* Any failures updating Django variables
to your own project and application variables, will cause the application to break.

## Instructions:

1. Clone this repository into a folder where you'd like it to live.
2. Rename the `django_template` folder to your `{{project_name}}` of choice.
*Note: {{variables}} will be used from now on to denote variables you must update.
The double curly brackets are not to be included*
3. Open your now renamed project folder, and rename the containing `django_template` folder
(whose path is now, `{{project_name}}\django_template`), to the same `{{project_name}}` used previously. Your path to this folder should now be, `{{project_name}}\{{project_name}}`.
4. Open `manage.py` in the root of your project folder. The path should be:
`{{project_name}}\manage.py`.
5. On line 6 in `manage.py`, rename the second parameter in `setdefault()` from:
`django_template.settings` to `{{project_name}}.settings`. Save changes and close this file.
6. In the root of your `{{project_name}}` folder, navigate into the `\apps` folder
(`{{project_name}}\apps`). Rename the containing folder from `template` to the
name of your app (usually a shorthand of your `{{project_name}}`). In this case,
we'll call it `{{app_name}}`. So, `{{project_name}}\apps\template` should now be
named `{{project_name}}\apps\{{app_name}}`.
7. Navigate into the newly renamed `{{app_name}}` folder.
8. Open `apps.py` (`{{project_name}}\apps\{{app_name}}\apps.py`). On line 7, rename `template` to your `{{app_name}}`. Save and close the file.
9. Open `views.py` in the same folder (`{{project_name}}\apps\{{app_name}}\views.py`).
10. In the first method, `index()`, at the very bottom of the method, change the
line `return render(request, "template/index.html")` to `return render(request, "{{app_name}}/index.html")`.
11. In second to last method, `get_dashboard_data()`, at the very bottom of the `try`
statement, update the line `return render(request, "template/dashboard.html", dashboard_data)`
to `return render(request, "{{app_name}}/dashboard.html", dashboard_data)`. Save the file
and close it. *Note: Currently, the only dashboard data retreived is that of the current user.* This could be vastly added onto, and if not needed can be removed (be sure to remove the `from . import dashboard` if not needed).
12. Open `\template` folder inside of the `{{app_name}}` folder (`{{project_name}}\apps\{{app_name}}\templates`).
13. Rename the containing folder, `template` to `{{app_name}}`. This name
must be your app name.
14. Navigate now into the newly renamed `{{app_name}}` folder (`{{project_name}}\apps\{{app_name}}\templates\{{app_name}}`).
15. Once inside, open both `index.html` and `dashboard.html`. Edit the
`<link rel="stylesheet">` lines from `<link rel="stylesheet" href="{% static 'template/css/style.css' %}">` to `<link rel="stylesheet" href="{% static '{{app_name}}/css/style.css' %}">`, replacing any references to `template` and
instead to your `{{app_name}}`.
16. Also change the the `<title>` tags in each header, updating the name of the
page to whatever your needs may be. Save and close both files.
17. Navigate up a directory back to the `{{project_name}}\apps\{{app_name}}\`.
18. Navigate into `/static`, `{{project_name}}\apps\{{app_name}}\static`.
19. Change `template` to `{{app_name}}`. This should be the same name you used
when you renamed your last folder. The previous folder `{{project_name}}\apps\{{app_name}}\static\template` should now be:
`{{project_name}}\apps\{{app_name}}\static\{{app_name}}`.
20. The folder structures have all been updated now. We've got to now update
all of the Django settings, and make a few changes to a handful more files. Take
a breath and let's finish this up.
21. Navigate back to the `{{project_name}}` folder (root of your project). Once
in this folder, navigate into the `{{app_name}}` directory (not `apps`). You should
now be in `{{project_name}}\{{app_name}}`.
22. Open `urls.py` (`{{project_name}}\{{app_name}}\urls.py`), change the line:
`url(r'^', include("apps.template.urls"))`, to `url(r'^', include("apps.{{app_name}}.urls")),`
updating your application name in the `include()` parameters. Close and save this file.
23. Open `wsgi.py` in the same folder (`{{project_name}}\{{app_name}}\wsgi.py`). Change
the line `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_template.settings")`
to `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings")`. We
are changing the `django_template.settings` to our `{{project_name}}.settings` -- *this is not
your `{{app_name}}`, but `{{project_name}}`*
24. Open `settings.py` file in the same folder (`{{project_name}}\{{app_name}}\settings.py`).
Once in this file, make the following changes:
    - `SECRET_KEY` : Change the hash by changing 1 or 2 characters to different characters.
    Do not change the character count, just change a few characters so that the hash is now
    unique in comparison to the original file.
    - `INSTALLED_APPS` : Change `'apps.template'` to `'apps.{{app_name}}'`. This
    updates our settings.py file to point to our renamed app folder inside of `apps`.
    - `ROOT_URLCONF` : Update `django_template.urls` to `{{project_name}}.urls`. This is
    *not `{{app_name}}`*.
    - `WSGI_APPLICATION` : Update `django_template.wsgi.application` to `{{project_name}}.wsgi.application`, updating the name to `{{project_name}}`,
    *not `{{app_name}}`*
    - `TIME_ZONE` : Note, this is currently set to `America/Los_Angeles`. You can
    set this back to `UTC` if needed or adjust for your own timezone needs.
    - Save all changes and close this file.
25. Delete all `*.pyc` files in `{{project_name}}\{{project_name}}` (should be ~4 files).
26. Delete all `*.pyc` files in `{{project_name}}\apps` (should be ~1 files).
27. Delete all `*.pyc` files in `{{project_name}}\apps\{{app_name}}` (should be ~6 files).
28. Delete all files **EXCEPT** `__init__.py` in `{{project_name}}\apps\{{app_name}}\migrations`
29. Save all changes to any files that may have not been saved. We are done editing files
now and we've essentially created a unique project, and a new database with the new project
and app name dictating table nomenclature.
30. Open terminal. Navigate to the `{{project_name}}` folder in terminal.
31. Create a new `virtualenv` for this project. `pip install` all packages in `{{project_name}}\requirements.txt`. If you do not create a new virtualenv and if
you do not install the pip packages, then the server will not start.
32. Once inside the root of our project, and once all packages are installed,
`makemigrations` via `python manage.py makemigrations` in terminal. This will generate `.pyc` files again and prepare our models for generation.
33. Then `migrate` via `python manage.py migrate` to actually generate the models.
34. Start the server: `python manage.py runserver`. Once the server attempts to run,
any misnamed or missed variables from our updating process will break the application.
If the server runs, then all app variables should now be updated properly.
35. 
