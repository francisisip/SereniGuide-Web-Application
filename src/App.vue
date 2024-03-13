<template>
  <Navbar />
  <div class="container">
    <h1 style="color: white;"> Hello! </h1>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;  
  background: linear-gradient(-45deg, #383364, #2c2751, #1f1a3e, #140e2b, #0c051a);
  animation: gradient 5s ease infinite;
	height: 100vh;

}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}

.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}

.btn:focus {
  outline: none;
}

.btn:active {
  transform: scale(0.98);
}

.btn-block {
  display: block;
  width: 100%;
}

.aocw-button {
    background-color: rgb(10,102,194);
    color: white;
    height: 40px;
    width: 240px;
    border: none;
    border-radius: 20px;
    font-weight: bold;
    font-size: 15px;
    cursor: pointer;
    margin-right: 8px;
    transition: background-color 0.25s;
}

.aocw-button:hover {
    background-color: rgb(2, 70, 138);
}


</style>
