<template>
    <div class="user-profile">
        <div class="venue-cards-container-user">

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
        async fetchUserBookedShows() {
            try {
                const bookedShowsRaw = await fetch(`http://127.0.0.1:8081/api/userProfile/${localStorage.getItem('userId')}`,
                    {
                        headers: {
                            'access-token': localStorage.getItem("token")
                        }
                    });

                const bookedShows = await bookedShowsRaw.json();
                console.log(bookedShows)

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

.bookedShows {
    margin-top: 20px;
    display: flex;
    height: 92vh;
}
</style>
