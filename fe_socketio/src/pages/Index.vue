<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 450px; height: 450px"
    />
    github.com/selmanbaskaya
    youtube.com/selmanbaskaya
  </q-page>
</template>

<script>
import { io } from "socket.io-client"
export default {
  name: "PageIndex",
  mounted: function() {
    const socket = io('http://localhost:5004')
    socket.on('connect', function () {
      socket.emit('my-url', 'https://www.google.com');
    })

    socket.on('response',function(response){
      console.log(response);
    })
  }
};
</script>
