# Django Evaluation - final
#Problem Set I - Regex

<p>json_text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): </p>
<p>orange_background_indicator = 'orange'</p>
<p>pattern = r'"id":(\d+).*?"background-color:\s*{}.*?"'.format(orange_background_indicator)</p>
<p>matches = re.findall(pattern, json_text)</p>
<p>numbers = [int(match) for match in matches]</p>
<p>print(numbers)</p>

#Problem Set 2 - A functioning web app with API

<p>(A).https://task-system-38db.onrender.com/</p>

<p>(B).https://task-system-38db.onrender.com/api/v1/docs/</p>


#Problem Set 3

For scheduling periodic tasks, especially in a production environment, I would recommend using a reliable and scalable task scheduler like Celery combined with a message broker such as RabbitMQ or Redis.

<p>i'd prefer celery </p>

Reasons:

<p><b>Distributed Task Execution</b>: Celery allows for the distribution of tasks across multiple worker nodes, enabling parallel execution and efficient resource utilization.</p>

<p><b>Flexible Task Scheduling</b>: It provides a robust scheduling mechanism that supports periodic tasks, making it suitable for scenarios like downloading a list of ISINs every 24 hours.</p>

<p>Message Brokers: Celery's integration</p>

<p>(B).i'd use flask instead of django when creating a single page website or landing page</p> 

<p><h3>How i hosted the Website</h3><p>
i used gunicorn and whitenoise
<ul>
  <li> whitenoise for staticfiles rendering </li>
  <li>gunicorn for building and deployment</li>
</ul>



