# Svelte + Flask

A super simple example of using Flask to serve a Svelte app and use it as a backend server.
This example just queries the Flask server for a random number.

## Install the dependencies and run or build the frontend
```
cd frontend 
npm install
npm run dev
# or 
npm run build 
```

## Install the dependencies and run the backend
```bash
cd backend
python3 -m venv . && source bin/activate
pip install -r requirements.txt
flask --app src/app.py --debug run 
```