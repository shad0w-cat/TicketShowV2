<template>
    <div class="admin-dashboard">
        <div class="venue-cards-container-admin">
            <VenueCardAdmin v-for="venue in venues" :key="venue.id" :venue="venue" />
        </div>
        <button class="addButton" @click="showAddVenueModal">+</button>
        <AddVenueModal :showVenueModal="showAddVenue" @addVenue="addVenue" @closeModal="hideAddVenueModal" />

        <!-- Additional modal and logic for adding venues if needed -->
    </div>
</template>

<script>
import VenueCardAdmin from './VenueCardAdmin.vue';
import AddVenueModal from './AddVenueModal.vue';

export default {
    data() {
        return {
            venues: [], // Array to store the venues
            showAddVenue: false, // Boolean value used as a flag to display add venue modal
        };
    },
    methods: {
        showAddVenueModal() {
            this.showAddVenue = true;
        },
        hideAddVenueModal() {
            this.showAddVenue = false;
        },
        async addVenue(newVenue) {
            const rawResponse = await fetch('http://127.0.0.1:8081/api/create_venue', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newVenue)
            });
            // const content = await rawResponse.json();
            console.log(rawResponse)
        },

        // Fetch data for venues and shows from the API and update the "venues" array
        async mounted() {
            try {
                const venuesResponse = await fetch('http://127.0.0.1:8081/api/get-venue');
                const venuesData = await venuesResponse.json();
                this.venues = venuesData;
            } catch (error) {
                console.error('Error fetching venues:', error);
            }
        },
    },
    components: {
        VenueCardAdmin,
        AddVenueModal,
    },
};
</script>

<style>
.admin-dashboard {
    height: 100%;
}

.addButton {
    position: relative;
    left: 95%;
    top: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    border-radius: 120px;
    background-color: aqua;
    font-size: x-large;
}
</style>
