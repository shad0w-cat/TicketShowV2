<template>
    <div class="user-profile">
        <div class="bookedShowsContainer">
            <div v-for="booking, index in userBookedShows" :key="index" class="bookedShowCard">
                <h2>{{ booking.Venue }} -
                    {{ booking.Show }}</h2>
                <h4> Seats Booked: {{ booking.SeatsBooked }} </h4>
                <h4> Time : {{ new Date(booking.ShowDateTime).toLocaleString() }} </h4>
                <h4 v-if="booking.Rate">{{ booking.Rate }} ⭐</h4>
                <div v-else class="rate-container">
                    <input type="number" min="1" max="5" v-model="rating" placeholder="Rate (1-5)">
                    <button @click="() => rateShow(booking.bookingId)"> Rate Show </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    components: {
    },
    data() {
        return {
            userBookedShows: [],
            rating: 0,
        };
    },
    methods: {
        async rateShow(bookingId) {
            try {
                const userRatingToShowRaw = await fetch(`http://127.0.0.1:8081/api/rating/${bookingId}/${this.rating}`,
                    {
                        method: "PUT",
                        headers: {
                            'access-token': localStorage.getItem("token")
                        }
                    });

                const userRatingToShow = await userRatingToShowRaw.json();
                console.log(userRatingToShow);
                this.$router.go(0);

            } catch (error) {
                console.error('Error fetching venues:', error);
            }

        },
        async fetchUserBookedShows() {
            try {
                const bookedShowsRaw = await fetch(`http://127.0.0.1:8081/api/userProfile/${localStorage.getItem('userId')}`,
                    {
                        headers: {
                            'access-token': localStorage.getItem("token")
                        }
                    });

                const bookedShows = await bookedShowsRaw.json();
                this.userBookedShows = bookedShows

            } catch (error) {
                console.error('Error fetching venues:', error);
            }
        }
    },
    mounted() {
        this.fetchUserBookedShows()
    },
};
</script>

<style>
.user-profile {
    height: 100%;
}

.bookedShowsContainer {
    margin: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    /* background-color: blue; */
}

.bookedShowCard {
    display: grid;
    place-items: center;
    grid-template-columns: 35% 15% 25% 20%;
    align-items: center;
    justify-content: space-between;
    padding: 2%;
    border-radius: 100px;
    width: 100%;
    border: 1px solid salmon;
}

.rate-container {
    display: flex;
    align-items: center;
    max-width: 400px;
    /* margin: 20px auto; */
    border: 2px solid #ccc;
    /* padding: 10px; */
    border-radius: 5px;
}

.rate-container input[type="number"] {
    flex: 1;
    padding: 8px;
    font-size: 16px;
    border: none;
    outline: none;
}

.rate-container button {
    padding: 8px 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 0px 5px 5px 0px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.rate-container button:hover {
    background-color: #0056b3;
}
</style>
