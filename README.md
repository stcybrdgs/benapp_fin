### About:

This app is a mini full-stack app that uses Vue.js and Flask to compare CSV data against Benford's Law.

It allows a user to upload a CSV file, pick a column from it, and then compare the numerical distribution of that column against [Benford's Law](https://en.wikipedia.org/wiki/Benford's_law).

### Demo:
A working demo of this app is available at [VueToots](http://www.vuetoots.com/).


### Docker:
If you want to run the app locally, a *Dockerfile* is included, which you may pull from [Docker Hub](https://hub.docker.com/r/stcybrdgs/scb-apps/tags) :

```
docker pull stcybrdgs/scb-apps:benapp
```

The Docker container will run the app on a Flask dev server from the container's port 80.
