from flask import Flask

app = Flask(__name__)
app.config.from_object('household.config')

import household.views