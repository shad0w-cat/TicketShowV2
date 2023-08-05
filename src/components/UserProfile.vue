<template>
    <div class="user-profile">
        <div class="bookedShowsContainer">
            <div v-for="booking, index in userBookedShows" :key="index" class="bookedShowCard">
                <h2>{{ booking.Venue }} -
                    {{ booking.Show }}</h2>
                <h4> Seats Booked: {{ booking.SeatsBooked }} </h4>
                <h4> Time : {{ new Date(booking.ShowDateTime).toLocaleString() }} </h4>
                <h4 v-if="booking.Rate">{{ booking.Rate }} ⭐</h4>
                <button v-else @click="() => rateShow(booking.bookingId)"> Rate Show </button>
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
        };
    },
    methods: {
        async rateShow(bookingId) {
            try {
                const userRatingToShowRaw = await fetch(`http://127.0.0.1:8081/api/rating/${bookingId}/5`,
                    {
                        method: "PUT",
                        headers: {
                            'access-token': localStorage.getItem("token")
                        }
                    });

                const userRatingToShow = await userRatingToShowRaw.json();
                console.log(userRatingToShow);

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
    /* background-color: blue; */
}

.bookedShowCard {
    display: grid;
    place-items: center;
    grid-template-columns: 40% 20% 30% 10%;
    align-items: center;
    justify-content: space-between;
    padding: 2%;
    border-radius: 100px;
    width: 100%;
    border: 1px solid salmon;
}

.bookedShowCard>h2 {
    align-self: flex-start;
}
</style>
