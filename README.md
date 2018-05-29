# Bat-Around Baseball Sim

Baseball Sim is a beginner friendly open-source project which allows you to simulate baseball games. Using real data from the 2017 season, the sim predicts the outcome of each at-bat.  

The project will have a React front-end and a Flask/Python back-end.  

## Install requirements

**NodeJS**  
In your terminal enter:  
```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install npm
```
Or visit https://nodejs.org/en/  
**Python3**  
**PyEnv or PipEnv or VirtualEnv** (any virtual enviroment manager that works with pip)  
First, activate your virtual environment  

```python
pip install -r requirements.txt
```

## Build React

The React app uses `create-react-app` and is contained in the top-level folder `frontend`. The flask app sets its static directory to the `build` folder contained in `frontend` in order to serve the react app.

```
cd frontend
# install node modules
npm install
# build the app
npm run build
```

## Run Flask

```
cd ..
python -m flask run
```
