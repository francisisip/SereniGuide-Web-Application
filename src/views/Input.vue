<template>
    <div>
        <div class="input-form">

            <div id="top-half">
                <div class="title-prompt">
                    <h3>SereniGuide</h3>
                    <h1>Learn Your Sleep Habits</h1>
                    <h3>start your tracking today</h3>
                </div>
                <div class="image-container">
                    <img id= "moon" :src="require('@/assets/moon.png')" alt="Image" />
                </div>
            </div>

            <div id="bottom-half">
                <form class="form-container" action="">
                    <input id="age" class="inpt" type="number">
                    <input id="sleep-duration" class="inpt" type="number">
                    <input id="awakenings" class="inpt" type="number">
                    <input id="exercise" class="inpt" type="number">
                    <input id="caffeine" class="inpt" type="number">
                    <input id="alcohol" class="inpt" type="number">
                </form>
                <br>
                <button class="form-btn"> Submit </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Input-Form',
}
</script>

<style scoped>

.input-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    color: #fff;
}

#top-half {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 10vw;
    width: 80%;
    height: 30%;
    color: #fff;
    padding: 15px;
    margin-bottom: 30px;
}

.title-prompt h3{
    font-size: 1.6vw;
}

.title-prompt h1{
    font-size: 4.2vw;
}

#bottom-half {
    width: 80%;
}

#moon {
    width: 15vw;
}

.form-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 1vw;
    width: 100%; 
    height: auto;
    color: #fff;
}

.form-container .inpt {
    width: 15%; /* Adjusted to 15% */
}

.form-btn {
   
}
</style>
