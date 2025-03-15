from flask import Flask, request, jsonify
from datetime import datetime
import cx_Oracle
import random
from sklearn.ensemble import IsolationForest
import numpy as np

app = Flask(__name__)

LOG_LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]
