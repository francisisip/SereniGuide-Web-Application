<template>
    <div id="welcome">
        <h1 id="welcome-text">SereniGuide</h1>
        <button>Get Started</button>
    </div>
</template>

<script>
export default {
    name: 'Landing',
}
</script>

<style>
body {
  font-family: 'Poppins', sans-serif;
  background-color: linear-gradient(-45deg, #13072e, #3f2182);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
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
#welcome {
    display: flex;
    margin: auto;
    justify-content: center;
    align-items: center;
    width: 65%;
    height: 100%;
    color: #111;
    flex-direction: column;
}

#welcome-text{
    font-size: 7vw;
    color: #fff;
}

button {
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 15px;
    font-family: inherit;
    background-color: #fff;
    color: #000;
    border: none;
}
</style>