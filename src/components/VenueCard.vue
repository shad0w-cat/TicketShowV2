<template>
    <div class="containerV">
        <div class="venue-card-user">
            <div>
                <h2>{{ venue.name }}</h2>
                <br />
                <h6>{{ venue.place }}, {{ venue.location }}</h6>
            </div>
            <br />
            <div class="shows-container-user">
                <ShowCard v-for="show in venue.shows" :key="show.id" :show="show" />
            </div>
            <br />
        </div>
    </div>
</template>

<script>
import ShowCard from './ShowCard.vue';

export default {
    data: () => {
        return {
            shows: [],
        }
    },
    props: ['venue'],
    components: {
        ShowCard,
    },
    methods: {
    },
    async mounted() {
        // console.log(this.venue)
    }
};
</script>

<style>
.venue-card-user {
    gap: 3px;
    justify-content: space-around;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    background-color: white;
    padding: 20px;
    border-radius: 10px;
}

.containerV {
    max-width: 100%;
    margin: 10px;
    border-radius: 10px;
    padding: 20px;
    background-color: cornflowerblue;
}

.show-card-user button {
    background: white;
    border: 1px solid black;
    padding: 5px;
    margin: 5px;
}

.shows-container-user {
    display: flex;
    flex-direction: row;
    max-height: 100%;
    overflow: auto;
}

.venue-card-user-footer>button {
    border-radius: 10px;
}
</style>
