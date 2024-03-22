<template>
    <div id="top-half">
        <div id="results" class="text-container">
            <div class="image-container">
                    <img v-if="sleepType === 'Deep Sleep'" id= "moon" :src="require('@/assets/moonv3.png')" alt="Image" />
                    <img v-else-if="sleepType === 'Light Sleep'" id= "moon" :src="require('@/assets/light-sleep-icon.png')" alt="Image" />
            </div>
            <h1>Your sleep last night showed more signs of </h1>
            <h1 id="type" class="type">{{ sleepType }}</h1>
        </div>
        <div class="button-container">
            <!-- <router-link to="/save"><button>Save Results</button></router-link> -->
            <router-link to="/"><button>Retake</button></router-link>
        </div>
        <span class="disclaimer">Disclaimer: This is not a professional diagnosis. Please consult a healthcare professional for a proper diagnosis.</span>
        <div class="text-container">
            <h4>Additional Information</h4>
            <h5>Light Sleep - The stage of sleep where your heart rate decreases, your body temperature drops, 
                and your breathing slows. This phase only lasts for 10 to 25 minutes. </h5>
            <h5>Deep Sleep - The stage of sleep that allows the the body to repair and regrow tissues, build bones 
                and muscles, and helps strengthen the immune system. Deep sleep ideally comprises 70% of your sleep 
                time: around 105 - 120 minutes for a healthy 8 hours.  </h5>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Results',
    data() {
        return {
            sleepType: '',
            sleepTypeIcon: ''
        };
    },
    mounted() {
        const responseData = JSON.parse(this.$route.query.responseData);
        
        const type = responseData[0]
        if (type === 0) {
            this.sleepType = 'Deep Sleep';
            this.sleepTypeIcon = '@/assets/moonv3.png';
        } else if (type === 1) {
            this.sleepType = 'Light Sleep';
            this.sleepTypeIcon = '@/assets/light-sleep-icon.png';
        } else {
            this.sleepType = 'Sleep Type Cannot Be Determined';
        }
    }
}
</script>

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
    margin-top: 10px;
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
    font-size: 0.8vw;
    margin-bottom: 60px;
}

h1 {
    font-size: 2.5vw;
    text-align: center;

}

h4 {
    font-weight: bold;
    font-size: 1.5vw;
}

h5 {
    font-size: 1.2vw;
    margin-top: 5px;
    margin-bottom: 5px;
}

</style>
