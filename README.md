## The Benny App

This app uses **Vue.js** and **Flask** to compare **.csv** data against **[Benford's Law](https://en.wikipedia.org/wiki/Benford's_law)**.
Users may upload a **.csv** file and select any column to see how its numerical distribution compares to Benford's. A working **Demo** is available at **[VueToots](http://www.vuetoots.com/)**.

A **Docker Image** of this app is available on **[Docker Hub](https://hub.docker.com/r/stcybrdgs/scb-apps/tags)**:

```
docker pull stcybrdgs/scb-apps:benapp
```

The Docker container will run the app on a Flask dev server from the container's port 80.
