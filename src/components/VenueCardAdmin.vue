<template>
    <div class="venue-card-admin">
        <h2>{{ venue.name }}</h2>
        <div class="shows-container-admin">
            <ShowCard v-for="show in venue.shows" :key="show.id" :show="show" />
        </div>
        <button @click="showAddShowModal">+</button>
        <div class="venue-card-admin-footer">
            <button @click="editVenue">Edit</button>
            <button @click="deleteVenue">Delete</button>
        </div>
    </div>
</template>

<script>
import ShowCard from './ShowCard.vue';
import AddShowModal from './AddShowModal.vue';

export default {
    props: ['venue'],
    components: {
        ShowCard,
        // eslint-disable-next-line vue/no-unused-components
        AddShowModal,
    },
    methods: {
        editVenue() {
            // Implement the logic to edit the venue details
            // For example, show a modal to edit the venue details
            console.log('Edit venue:', this.venue.name);
        },
        deleteVenue() {
            // Implement the logic to delete the venue
            // For example, show a confirmation modal and then delete the venue
            console.log('Delete venue:', this.venue.name);
        },
        showAddShowModal() {
            // Show the modal to add shows to the venue
            this.$refs.addShowModal.showModal();
        },
    },
};
</script>

<style>
/* Add styles for the admin venue card component */
</style>
