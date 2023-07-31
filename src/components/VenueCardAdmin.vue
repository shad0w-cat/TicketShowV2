<template>
    <EditVenueModal :showVenueModal="showEditVenue" @editVenue="editVenue" @closeModal="hideEditVenueModal" :title="'Edit'"
        :editVenue="venue" />
    <div class="containerV">
        <div class="venue-card-admin">
            <h2>{{ venue.name }}</h2>
            <h6>{{ venue.place }}, {{ venue.location }}</h6>

            <div class="shows-container-admin">
                <ShowCard v-for="show in venue.shows" :key="show.id" :show="show" />
            </div>
            <button @click="showAddShowModal" class="addButtonV">+</button>
            <br />
            <br />
            <div class="venue-card-admin-footer">
                <button @click="showEditVenueModal">Edit</button>
                <button @click="deleteVenue">Delete</button>
            </div>
        </div>
    </div>
</template>

<script>
import ShowCard from './ShowCard.vue';
import AddShowModal from './AddShowModal.vue';
import EditVenueModal from './VenueModal.vue';


export default {
    data: () => {
        return {
            showEditVenue: false,
        }
    },
    props: ['venue'],
    components: {
        ShowCard,
        // eslint-disable-next-line vue/no-unused-components
        AddShowModal,
        EditVenueModal,
    },
    methods: {
        showEditVenueModal() {
            this.showEditVenue = true;
        },
        hideEditVenueModal() {
            this.showEditVenue = false;
        },
        async editVenue(editVenue) {
            console.log(editVenue)
            const rawResponse = await fetch(`http://127.0.0.1:8081/api/venue/${this.venue.venue_id}`, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(editVenue)
            });
            console.log(rawResponse)

        },
        async deleteVenue() {
            const rawResponse = fetch(`http://127.0.0.1:8081/api/venue/${this.venue.venue_id}`, { method: 'DELETE' })
            console.log('Delete venue:', rawResponse);
        },
        showAddShowModal() {
            // Show the modal to add shows to the venue
            this.$refs.addShowModal.showModal();
        },
    },
    async mounted() {
        try {
            const venuesResponse = await fetch('http://127.0.0.1:8081/api/getVenue');
            const venuesData = await venuesResponse.json();
            this.venues = Object.values(venuesData).pop();

        } catch (error) {
            console.error('Error fetching venues:', error);
        }
    }
};
</script>

<style>
.venue-card-admin {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background-color: white;
    width: max-content;
    padding: 20px;
    border-radius: 10px;
}

.containerV {
    margin: 10px;
    border-radius: 10px;
    padding: 20px;
    background-color: cornflowerblue;
}

.venue-card-admin button {
    background: white;
    border: 1px solid black;
    padding: 5px;
    margin: 5px;
}

.addButtonV {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    border-radius: 120px;
    background-color: aqua;
    font-size: x-large;
}

.venue-card-admin-footer>button {
    border-radius: 10px;
}
</style>
