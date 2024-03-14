<template>
    <div>
        <div class="input-form">

            <div id="top-half">
                <div class="title-prompt">
                    <h1>Title Prompt</h1>
                </div>
                <div class="image-container">
                    <img src="path/to/image.jpg" alt="Image" />
                </div>
            </div>

            <div id="bottom-half">
                <form class="form-container" action="">
                    <input type="number">
                    <input type="number">
                    <input type="number">
                    <input type="number">
                    <input type="number">
                    <input type="number">
                </form>
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

<style>
#app {
    display: flex;
    justify-content: center;   
}

.input-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    color: #fff;
}

#top-half {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 10vw;
    width: 100%;
    height: 30%;
    color: #fff;
}

.form-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 1vw;
    width: 100%;
    height: 100%;
    color: #fff;
}

.form-btn {
    
}
</style>