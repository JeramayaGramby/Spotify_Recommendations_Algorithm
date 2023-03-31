import os
import json
from pathlib import Path
import pandas as pd
from decouple import config
import sqlite3
import spotipy
import spotipy.oauth2 as oauth2
import boto3