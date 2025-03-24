from flask import Flask

# Create Flask app
app = Flask(__name__)

# Create a route to test Docker setup
@app.route('/')
def home():
    return "Docker setup is working!"

if __name__ == '__main__':
    # Make the app accessible from any network using '0.0.0.0'
    app.run(host='0.0.0.0', port=5000)



