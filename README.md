# django

.center-httpcodes {
    margin-left: auto;
    margin-right: auto;
}

<h1>HTTP Status Codes</h1>
<hr>
    <table class="center-httpcodes">
        <tr>
            <th>Status Code</th>
            <th>Description</th>
        </tr>
        <tr><td>200</td><td>OK</td></tr>
        <tr><td>301</td><td>Moved Permanently</td></tr>
        <tr><td>403</td><td>Forbidden</td></tr>
        <tr><td>404</td><td>Not Found</td></tr>
        <tr><td>500</td><td>Internal Server Error</td></tr>
    </table>
<hr>

<h1>Commands</h1>
    <h2>Installing using pip</h2>
        <p>>>pip install django</p>
    <h2>Create a Django project </h2>
        <p>>>django-admin startproject PROJECT_NAME</p>
    <h2>Run the webserver</h2>
        <p>>>python manage.py runserver</p>
    <h2>Creating an App inside project and configure</h2>
        <p>>>python manage.py startapp hello</p>
        <p>Add the hello app to INSTALLED_APPS in settings.py</p>
<hr>
<h2>django files description</h2>
    <h3>manage.py</h3>
        <p>be able to execute commands in our project</p>
    <h3>settings.py</h3>
        <p>important configurations for django application</p>
    <h3>urls.py</h3>
        <p>Table of contents for our web(routes)</p>
    <h3>views.py</h3>
        <p>What a sees when they visit a particular route</p>
    