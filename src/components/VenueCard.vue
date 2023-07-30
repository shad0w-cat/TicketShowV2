<template>
    <div class="venue-card">
        <h2>{{ venue.name }}</h2>
        <div class="shows-container">
            <ShowCard v-for="show in shows" :key="show.id" :show="show" />
        </div>
    </div>
</template>

<script>
import ShowCard from './ShowCard.vue';

export default {
    props: ['venue'],
    components: {
        ShowCard,
    },
    data() {
        return {
            shows: [], // Array to store the shows for this venue
        };
    },
    async mounted() {
        // Fetch shows data for this venue from the API
        try {
            const response = await fetch(`http://127.0.0.1:8081/api/get-shows/${this.venue.id}`);
            const data = await response.json();
            this.shows = data;
        } catch (error) {
            console.error('Error fetching shows:', error);
        }
    },
};
</script>

<style>
/* Add styles for the venue card component */
</style>
