<template>
    <div id="top-half">
        <div id="results" class="text-container">
            <div class="image-container">
                    <img id= "moon" :src="require('@/assets/moonv3.png')" alt="Image" />
            </div>
            <h1>You are more inclined towards being a </h1>
            <h1 class="type">Light Sleeper</h1>
        </div>
        <div class="button-container">
            <router-link to="/save"><button>Save Results</button></router-link>
            <router-link to="/"><button>Retake</button></router-link>
        </div>
        <span class="disclaimer">Disclaimer: This is not a professional diagnosis. Please consult a healthcare professional for a proper diagnosis.</span>
        <div class="text-container">
            <h4>Additional Information</h4>
            <h5>REM Sleep - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ac sem in justo lacinia faucibus eu consectetur purus. </h5>
            <h5>Light Sleep - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ac sem in justo lacinia faucibus eu consectetur purus. </h5>
            <h5>Deep Sleep - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ac sem in justo lacinia faucibus eu consectetur purus. </h5>
        </div>
    </div>
</template>

<style scoped>
#top-half {
    display: flex;
    flex-direction: column;
    justify-content: center; 
    align-items: center; 
    height: 100vh;
    color: #fff;
    padding: 15px;
}

.image-container {
    display: flex; 
    justify-content: center;
    align-items: center; 
    margin-bottom: 10px;
}

#moon {
    width: 11vw;
}

.type {
    font-weight: bold;
    text-align: center;
}

.button-container {
    margin-top: 20px;
    display: flex;
    gap: 15px; 
}

button {
    background-color: #fff;
    color: #000;
    height: 3vw; 
    width: 10vw; 
    padding: 0.25vw 0.75vw; 
    margin: 5px;
    border: 2px solid #fff; 
    border-radius: 20vw;
    cursor: pointer;
    text-decoration: none;
    font-size: 1.2vw; 
    font-family: inherit;
    transition: background-color 0.4s, color 0.4s; 
}

button:hover {
    color: #fff;
    background-color: #383364;
    border: 2px solid #fff; 
}

.disclaimer {
    margin-top: 5px;
    font-size: 0.6vw;
    margin-bottom: 60px;
}

h4 {
    font-weight: bold;
}
</style>
