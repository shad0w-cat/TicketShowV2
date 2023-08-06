<template>
    <div class="user-dashboard">
        <div class="search-container">
            <input type="text" v-model="searchText" placeholder="Search...">
            <button>Search</button>
        </div>
        <div class="venue-cards-container-user">
            <VenueCard v-for="venue in filteredVenues" :key="venue.id" :venue="venue" @onUpdate="fetchVenues" />
        </div>
    </div>
</template>

<script>
import VenueCard from './VenueCard.vue';

export default {
    components: {
        VenueCard,
    },
    data() {
        return {
            venues: [],
            searchText: '',
        };
    },
    methods: {
        async fetchVenues() {
            try {
                // Fetch the venues data
                const venuesResponse = await fetch('http://127.0.0.1:8081/api/getVenue', {
                    headers: {
                        'access-token': localStorage.getItem('token'),
                    },
                });

                const venuesData = await venuesResponse.json();
                this.venues = Object.values(venuesData).pop();
            } catch (error) {
                console.error('Error fetching venues:', error);
            }
        },
    },
    computed: {
        filteredVenues() {
            return this.venues.filter((venue) => {
                return (
                    venue.name.toLowerCase().includes(this.searchText.toLowerCase()) ||
                    venue.shows.some((show) =>
                        show.name.toLowerCase().includes(this.searchText.toLowerCase())
                    )
                );
            });
        },
    },
    mounted() {
        this.fetchVenues();
    },
};
</script>

<style>
.user-dashboard {
    height: 100%;
}

.show-cards-container-admin {
    margin-top: 20px;
    display: flex;
    height: 92vh;
}

.search-container {
    display: flex;
    align-items: center;
    max-width: 400px;
    margin: 20px auto;
    border: 2px solid #ccc;
    padding: 10px;
    border-radius: 5px;
}

.search-container input[type="text"] {
    flex: 1;
    padding: 8px;
    font-size: 16px;
    border: none;
    outline: none;
}

.search-container button {
    padding: 8px 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.search-container button:hover {
    background-color: #0056b3;
}
</style>
