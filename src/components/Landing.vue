<template>
    <div id="welcome">
        <div id="text-container">
            <img id="main-logo" :src="require('@/assets/logo.png')" alt="">
            <h1 id="welcome-text">SereniGuide</h1>
        </div>
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
    display: flex;
    justify-content: center;
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

#text-container {
    display: flex;
    align-items: center;
    gap: 25px;
}

#welcome-text{
    font-size: 7vw;
    color: #fff;
}

#main-logo{
    height: 7vw;
}

button {
    background-color: #fff;
    color: #000;
    height: 4.5vw; 
    width: 18vw; 
    padding: 0.25vw 0.75vw; 
    margin: 5px;
    border: 2px solid #fff; 
    border-radius: 20vw;
    cursor: pointer;
    text-decoration: none;
    font-size: 1.8vw; 
    font-family: inherit;
    transition: background-color 0.4s, color 0.4s; 
}

button:hover {
    color: #fff;
    background-color: #383364;
    border: 2px solid #fff; 
}

</style>