# Server of Page a day.club

## Setup

```bash
# Create a virtual env and activate it.
virtualenv gb
source gb/bin/activate
pip install -r requirements.txt

# Make sure redis server is running.
redis-server &

# Start bottle server.
python app.py
```
