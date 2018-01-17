URL_Permission
===============
1. Install app::

    pip install url_permission


2. Add "url_permission" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'url_permission',
    ]
    MIDDLEWARE = [
        ...
        'url_permission.middleware.URLPermissionMiddleWare',
    ]

3. Include the comments URLconf in your project urls.py like this::

     url(r'^permission/', include('url_permission.urls', namespace='permission'), ),

4. Run migrate  and permission_url to create the permission models and write url_source::

    python manage.py migrate
    python manage.py permission_url

5. Start the development server and visit http://127.0.0.1:8000/admin/
