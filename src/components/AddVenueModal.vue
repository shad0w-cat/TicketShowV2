<template>
    <div v-if="showVenueModal" class="add-venue-modal">
        <div class="venue-modal-content">
            <h3>Add New Venue</h3>
            <form @submit.prevent="addVenue">
                <div class="form-group">
                    <label for="venue_name">Venue Name:</label>
                    <input type="text" id="venue_name" v-model="newVenue.venue_name" required>
                    <label for="place">Place:</label>
                    <input type="text" id="place" v-model="newVenue.place" required>
                    <label for="location">Location:</label>
                    <input type="text" id="location" v-model="newVenue.location" required>
                    <label for="capacity">Capacity:</label>
                    <input type="number" id="capacity" v-model="newVenue.capacity" min="1" required>
                </div>
                <div class="form-btns">
                    <button type="submit">Add Venue</button>
                    &nbsp;
                    <button @click.prevent="hideModal">Cancel</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            // showModal: this.$props.showVenueModal,
            newVenue: {
                venue_name: '',
                place: '',
                location: '',
                capacity: 0,
            },
        };
    },
    methods: {
        addVenue() {
            this.$emit('addVenue', this.newVenue);
            this.hideModal();
            this.resetForm();
        },
        hideModal() {
            this.resetForm();
            this.$emit('closeModal');
        },
        resetForm() {
            this.newVenue = {
                venue_name: '',
                place: '',
                location: '',
                capacity: 0,
            }
        },
    },
    props: {
        showVenueModal: {
            type: Boolean,
            required: true,
        },
    },
};
</script>

<style>
.add-venue-modal {
    background-color: #0f0f0f6c;
    position: absolute;
    top: 0%;
    left: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.venue-modal-content {
    background-color: aliceblue;
    padding: 2%;
    border-radius: 10px;
}

.form-group>* {
    padding: 7px;
    margin-block: 10px;
}

.form-group {
    display: grid;
    grid-template-columns: 50% 50%;
}

.form-btns {
    margin-top: 10px;
    display: flex;
    justify-content: flex-end;
}

.form-btns>* {
    padding: 5px;
}
</style>
