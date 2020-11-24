## The Benny App

**The Benny App** is a Vue-Flask app that compares *.csv* files to **[Benford's Law](https://en.wikipedia.org/wiki/Benford's_law)**.

Users may upload a **.csv** file and select any column to see how its numerical distribution compares to Benford's.

A working **Demo** is available on AWS at **[VueToots.com](https://www.vuetoots.com/)**.

A  **Demo Video** is available on **[YouTube](https://youtu.be/rowh15YFsgw)**.

A **Docker Image** is available on **[Docker Hub](https://hub.docker.com/r/stcybrdgs/scb-apps/tags)**.

```
docker pull stcybrdgs/scb-apps:thebennyapp
docker run -p 5000:80 stcybrdgs/scb-apps:thebennyapp
```

After issuing the run command locally, you may view the app in your browser at **localhost:5000**.

Within the Docker container, the Flask app serves to port 80.
