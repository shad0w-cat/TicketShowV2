<template>
    <div v-if="showModal" class="add-show-modal">
        <div class="modal-content">
            <!-- Modal content for adding shows to the venue -->
            <!-- You can add input fields and other elements to collect show information -->
            <h3>Add Show to {{ venue.name }}</h3>
            <!-- Add show input fields here -->
            <button @click="addShow">Add Show</button>
            <button @click="hideModal">Cancel</button>
        </div>
    </div>
</template>

<script>
export default {
    props: ['venue'],
    data() {
        return {
            showModal: false,
        };
    },
    methods: {
        addShow() {
            // Implement the logic to add a new show to the venue
            // For example, create a new show object and add it to the venue.shows array
            console.log('Add show to venue:', this.venue.name);
            // After adding the show, close the modal
            this.hideModal();
        },
        hideModal() {
            // Hide the modal
            this.showModal = false;
        },
        // eslint-disable-next-line vue/no-dupe-keys
        showModal() {
            // Show the modal
            this.showModal = true;
        },
    },
};
</script>

<style>
/* Add styles for the add show modal */
</style>
