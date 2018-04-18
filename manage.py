#!/usr/bin/env python
import logging
import os
import sys
import time
import psycopg2

if __name__ == "__main__":
    # Wait for the database to be up
    db_up = False
    while not db_up:
        try:
            conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="db")
        except psycopg2.OperationalError:
            logging.log("Couldn't connect to database")
            time.sleep(2)
        else:
            db_up = True

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kk.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
