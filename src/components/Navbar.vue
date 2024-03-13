<template>
    <nav class="navbar">
        <div class="navbar-left">
            <h1 class="navbar-title">SereniGuide</h1>
        </div>
        <div class="navbar-right">
            <ul class="navbar-links">
                <li class="navbar-link"><a href="#">Home</a></li>
                <li class="navbar-link"><a href="#">About</a></li>
                <li class="navbar-link"><a href="#">Contact Us</a></li>
            </ul>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Navbar',
}
</script>

<style scoped>
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #84A98C;
    padding: 10px;
    color: rgb(0, 0, 0);
    padding-top: 12px;
    padding-bottom: 12px;
}

.navbar-left {
    flex: 1;
    margin-left: 50px;
}

.navbar-title {
    font-size: 30px;
    margin: 0;
}

.navbar-right {
    flex: 1;
    text-align: right;
    margin-right: 100px;

}

.navbar-links {
    list-style: none;
    margin: 0;
    padding: 0;
    font-size: 16px
}

.navbar-link {
    display: inline-block;
    margin-left: 50px;
}

.navbar-link a {
    text-decoration: none;
    color: rgb(0, 0, 0);
}

.navbar-link a:hover {
    color: #EBEBEB;
}


</style>