{% extends "base.jinja2" %}

{% block subtitle %}Add them up!{% endblock subtitle %}

{% block content %}
    <p>Total: <span id="total">FILL ME</span></p>
    <form method="POST">
        <label for="number">Number: </label><input type="number" id="number" name="number">
        <input type="submit" value="Add It!">
    </form>
{% endblock content %}