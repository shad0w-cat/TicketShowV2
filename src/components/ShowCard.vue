<template>
    <div class="show-card">
        <h3>{{ show.name }}</h3>
        <p>Seats Available: {{ show.seatsAvailable }}</p>
        <div v-if="show.seatsAvailable > 0">
            <!-- Show the "Book Seats" button if seats are available -->
            <button @click="bookSeats" :disabled="isBookingDisabled">Book Seats</button>
        </div>
        <div v-else>
            <!-- Show "Houseful" message if no seats are available -->
            <p>Houseful</p>
        </div>
    </div>
</template>

<script>
export default {
    props: ['show'],
    methods: {
        bookSeats() {
            // Implement the logic to book seats for the show
            // For example, show a dialog, handle seat selection, etc.
            console.log('Book Seats clicked for show:', this.show.name);
        },
    },
    computed: {
        isBookingDisabled() {
            // Determine if the "Book Seats" button should be disabled based on seats availability
            return this.show.seatsAvailable <= 0;
        },
    },
};
</script>

<style>
/* Add styles for the show card component */
</style>
