<template>
    <div class="admin-dashboard">
        <div class="venue-cards-container-admin">
            <VenueCardAdmin v-for="venue in venues" :key="venue.id" :venue="venue" @onUpdate="fetchVenues" />
        </div>
        <button class="addButtonVM" @click="showAddVenueModal">+</button>
        <AddVenueModal :showVenueModal="showAddVenue" @addVenue="addVenue" @closeModal="hideAddVenueModal"
            :title="'Add New'" />
    </div>
</template>

<script>
import VenueCardAdmin from './VenueCardAdmin.vue';
import AddVenueModal from './VenueModal.vue';

export default {
    data() {
        return {
            venues: [],
            showAddVenue: false,
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
            const rawResponse = await fetch('http://127.0.0.1:8081/api/venue/1', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newVenue)
            });
            // const content = await rawResponse.json();
            console.log(rawResponse)
            this.fetchVenues()
        },
        async fetchVenues() {
            try {
                const venuesResponse = await fetch('http://127.0.0.1:8081/api/getVenue');
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

.addButtonVM {
    position: absolute;
    right: .5%;
    top: 6.5%;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    border-radius: 120px;
    background-color: aqua;
    font-size: x-large;
}

.venue-cards-container-admin {
    margin-top: 20px;
    display: flex;
}
</style>
