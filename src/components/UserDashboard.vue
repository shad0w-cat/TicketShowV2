<template>
    <div class="user-dashboard">
        <h1>User Dashboard</h1>
        <div class="venue-cards-container">
            <VenueCard v-for="venue in venues" :key="venue.id" :venue="venue" />
        </div>
    </div>
</template>

<script>
import VenueCard from './VenueCard.vue';

export default {
    components: {
        VenueCard,
    },
    data() {
        return {
            venues: [], // Array to store the venues
        };
    },
    async mounted() {
        // Fetch venues data from the API
        try {
            const response = await fetch('http://127.0.0.1:8081/api/get-venue');
            const data = await response.json();
            this.venues = data;
        } catch (error) {
            console.error('Error fetching venues:', error);
        }
    },
};
</script>

<style>
/* Add styles for the user dashboard component */
</style>
