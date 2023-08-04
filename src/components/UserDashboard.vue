<template>
    <div class="user-dashboard">
        <div class="venue-cards-container-user">
            <VenueCard v-for="venue in venues" :key="venue.id" :venue="venue" @onUpdate="fetchVenues" />
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
    methods: {
        async fetchVenues() {
            try {
                const venuesResponse = await fetch('http://127.0.0.1:8081/api/getVenue',
                    {
                        headers: {
                            'access-token': localStorage.getItem("token")
                        }
                    });

                const venuesData = await venuesResponse.json();
                this.venues = Object.values(venuesData).pop();

            } catch (error) {
                console.error('Error fetching venues:', error);
            }
        }
    },
    mounted() {
        this.fetchVenues()
    },
};
</script>

<style>
.user-dashboard {
    height: 100%;
}

.show-cards-container-admin {
    margin-top: 20px;
    display: flex;
    height: 92vh;
}
</style>
