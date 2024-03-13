<template>
    <div>
        <h1 class="contact-us">Contact Us</h1>
        <div class="people-container">
            <div v-for="person in topPeople" :key="person.id" class="person">
                <img :src="require(`@/assets/${person.picture}`)" alt="Image of Person" class="person-image" />
                <h3>{{ person.name }}</h3>
                <p>{{ person.email }}</p>
            </div>
        </div>
        <div class="people-container">
            <div v-for="person in bottomPeople" :key="person.id" class="person">
                <img :src="require(`@/assets/${person.picture}`)" alt="Image of Person" class="person-image" />
                <h3>{{ person.name }}</h3>
                <p>{{ person.email }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            people: [
                {
                    id: 1,
                    picture: "bawa.jpg",
                    name: "Francis Bawa",
                    email: "francis_bawa@dlsu.edu.ph",
                },
                {
                    id: 2,
                    picture: "logo.png",
                    name: "Zachary Gomez",
                    email: "zachary_gomez@dlsu.edu.ph",
                },
                {
                    id: 3,
                    picture: "logo.png",
                    name: "Enrique Lejano",
                    email: "enrique_rafael_a_lejano@dlsu.edu.ph",
                },
                {
                    id: 4,
                    picture: "logo.png",
                    name: "Cymon Nadela",
                    email: "cymon_nadela@dlsu.edu.ph",
                },
                {
                    id: 5,
                    picture: "logo.png",
                    name: "Luis Roxas",
                    email: "luis_roxas@dlsu.edu.ph",
                }
            ],
        };
    },
    computed: {
        topPeople() {
            return this.people.slice(0, 3);
        },
        bottomPeople() {
            return this.people.slice(3);
        },
    },
};
</script>

<style>

.contact-us {
    text-align: center;
    font-size: 3px;
    margin-top: 20px;
    margin-bottom: 20px;
    color: #EBEBEB;
}

.people-container {
    display: flex;
    justify-content: center;
}

.person {
    text-align: center;
    margin: 20px;
    color: #EBEBEB;
    font-size: 12px;
}

.person-image {
    max-width: 175px;
    max-height: 175px;
}
</style>
