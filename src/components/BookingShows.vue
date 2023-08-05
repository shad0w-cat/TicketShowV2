<template>
    <div class="show-modal-content">
        <h3>Booking - {{ show.name }} @ {{ new Date(show.dateTime) }}</h3>
        <h5>available Seats = {{ availableSeats }}</h5>
        <form @submit.prevent="bookMyShow">
            <div class="form-group">
                <label for="availableSeats">No of seats</label>
                <input type="number" id="availableSeats" v-model="booking.seats" min="1" :max="availableSeats" required>
                <label for="price">Price:</label>
                <input type="number" id="price" v-model="show.price" required disabled>
                <label for="total">Rating (1-10):</label>
                <input type="text" id="total" :value="bookingTotal" required disabled>
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
            availableSeats: 0,
            show: '',
            booking: {
                userId: localStorage.getItem('userId'),
                showId: this.$route.params.showId,
                rating: '',
                seats: 0,
            }
        }
    },
    methods: {
        async bookMyShow() {
            const rawResponse = await fetch('http://127.0.0.1:8081/api/booking', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'access-token': localStorage.getItem("token")
                },
                body: JSON.stringify(this.booking)
            });
            // const content = await rawResponse.json();
            console.log(rawResponse)
        }
    },
    async mounted() {
        try {
            const getShow = await fetch(`http://127.0.0.1:8081/api/show/${this.$route.params.showId}`,
                {
                    headers: {
                        'access-token': localStorage.getItem("token")
                    }
                });

            const showInfo = await getShow.json();
            this.show = showInfo;
            console.log(this.show)

            const seatsResponse = await fetch(`http://127.0.0.1:8081/api/booking/${this.$route.params.showId}`,
                {
                    headers: {
                        'access-token': localStorage.getItem("token")
                    }
                });

            const availableSeats = await seatsResponse.json();
            this.availableSeats = showInfo.available_seats - availableSeats.data;
            console.log(availableSeats)
        } catch (error) {
            console.error('Error fetching venues:', error);
        }
    },
    computed: {
        bookingTotal() {
            return this.booking.seats * this.show.price;
        },
    },
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
