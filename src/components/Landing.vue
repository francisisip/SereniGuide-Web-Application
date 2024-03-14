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