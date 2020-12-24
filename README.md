## The Benny App

**The Benny App** is a Vue-Flask app that compares *.csv* files to **[Benford's Law](https://en.wikipedia.org/wiki/Benford's_law)**.

Users may upload a **.csv** file and select any column to see how its numerical distribution compares to Benford's.

The **Live App** is available on **[Heroku](https://the-benny-app.herokuapp.com/)**.

A **Docker Image** is available on **[Docker Hub](https://hub.docker.com/r/stcybrdgs/scb-apps)**.

```
docker pull stcybrdgs/scb-apps:thebennyapp
docker run -p 5000:80 stcybrdgs/scb-apps:thebennyapp
```

After issuing the run command locally, you may view the app in your browser at **localhost:5000**.

Within the Docker container, the Flask app serves to port 80.
