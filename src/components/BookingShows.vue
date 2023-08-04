<template>
    <div class="show-modal-content">
        <h3>Booking - {{ show.showName }}</h3>
        <form @submit.prevent="bookMyShow">
            <div class="form-group">
                <label for="price">Price:</label>
                <input type="number" id="price" v-model="newShow.price" required disabled>
                <label for="availableSeats">No of seats</label>
                <input type="number" id="availableSeats" v-model="newShow.available_seats" required>
                <label for="rating">Rating (1-10):</label>
                <input type="text" id="rating" v-model="newShow.rating" required>
                <label for="tags">Tags:</label>
                <input type="text" id="tags" v-model="newShow.tags" required>
                <label for="datetime">Date and Time:</label>
                <input type="datetime-local" id="datetime" v-model="newShow.dateTime" required>
            </div>
            <div class="form-btns">
                <button type="submit">Book Show</button>
                &nbsp;
                <button @click.prevent="hideModal">Cancel</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            show: '',
            booking: {
                userId: '',
                showId: '',
                rating: '',
                seats: 0,
            }
        }
    },
    methods: {},
    async mounted() {
        try {
            const getShow = await fetch(`http://127.0.0.1:8081/api/show/${this.$route.params.showId}`,
                {
                    headers: {
                        'access-token': localStorage.getItem("token")
                    }
                });

            const showInfo = await getShow.json();
            this.shows = Object.values(showInfo).pop();

        } catch (error) {
            console.error('Error fetching venues:', error);
        }
    }
}
</script>

<style>
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
