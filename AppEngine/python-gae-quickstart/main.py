from flask import Flask, render_template, request

from google.appengine.api import memcache

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def counter():
    if 'reset' in request.args:
      memcache.flush_all()
    # set up names if it doesn't exist
    memcache.add('names','')
    name = "Franciso"
    if request.method == 'GET' and 'person_name' in request.args:
      name = request.args['person_name']
      # Check to see if that name is in names
      names = memcache.get('names')
      if name in names.split('/'):
      	# that person is already there
      	memcache.incr(name)
      else:
        memcache.set('names', names + '/' + name)
        memcache.set(name,1)
    names = memcache.get('names').split('/')
    counts = []
    for n in names:
      counts.append( (n, memcache.get(n) ) )
    #counts = [("bob",5),("mary",6)]
    return render_template('counter.html', counts=counts, name=name)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
    
    
    
    
    
    
    
    
    
