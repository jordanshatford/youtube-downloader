# Flask Server

This project is made using [Flask](https://flask.palletsprojects.com/en/1.1.x/) for the server.

*Note that you will need to have [Flask](https://flask.palletsprojects.com/en/1.1.x/) installed.*


## Get started

Install the dependencies:
*Note that you will need to have [ffmpeg](https://www.ffmpeg.org/) installed.*

```bash
pip install -r requirements.txt
```

Once the dependencies have been installed, you can start the server. To start the development server run:

```bash
npm run serve
```
To start the production server run:
```bash
npm run start
```

## Using Docker
The server has a [Docker](https://www.docker.com/)  file which creates the enviroment setup with everything needed to run the server.

You can create a docker container mapping to an inner port of 8000. For more information see the docker-compose.yml in root directory which is used to run the frontend and backend together.