### About:

This app is a mini full-stack app that uses Vue.js and Flask to compare CSV data against [Benford's Law](https://en.wikipedia.org/wiki/Benford's_law).

It allows a user to upload a CSV file and see how any column's numerical distribution compares to Benford's.

### Demo:
A working demo of this app is available at [VueToots](http://www.vuetoots.com/).


### Docker:
If you want to run the app locally, a *Dockerfile* is included, which you may pull from [Docker Hub](https://hub.docker.com/r/stcybrdgs/scb-apps/tags) :

```
docker pull stcybrdgs/scb-apps:benapp
```

The Docker container will run the app on a Flask dev server from the container's port 80.
