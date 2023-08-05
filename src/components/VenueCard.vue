<template>
    <div class="containerV">
        <div class="venue-card-user">
            <div>
                <h2>{{ venue.name }}</h2>
                <br />
                <h6>{{ venue.place }}, {{ venue.location }}</h6>
            </div>
            <br />
            <div class="shows-container-user">
                <ShowCard v-for="show in shows" :key="show.id" :show="show" />
            </div>
            <br />
        </div>
    </div>
</template>

<script>
import ShowCard from './ShowCard.vue';

export default {
    data: () => {
        return {
            shows: [],
            showEditVenue: false,
            showAddShow: false,
        }
    },
    props: ['venue'],
    components: {
        ShowCard,
    },
    methods: {
        showEditVenueModal() {
            this.showEditVenue = true;
        },
        hideEditVenueModal() {
            this.showEditVenue = false;
        },
        showAddShowModal() {
            this.showAddShow = true;
        },
        hideAddShowModal() {
            this.showAddShow = false;
        },
        async addShow(newShow) {
            newShow.venue = this.venue.name;
            const rawResponse = await fetch(`http://127.0.0.1:8081/api/show/1/1`, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'access-token': localStorage.getItem("token")
                },
                body: JSON.stringify(newShow),
            });
            console.log(rawResponse)
            this.$emit('onUpdate');
        },
        async editVenue(editVenue) {
            const rawResponse = await fetch(`http://127.0.0.1:8081/api/venue/${this.venue.venue_id}`, {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'access-token': localStorage.getItem("token")
                },
                body: JSON.stringify(editVenue)
            });
            console.log(rawResponse)
            this.$emit('onUpdate');
        },
        async deleteVenue() {
            const rawResponse = fetch(`http://127.0.0.1:8081/api/venue/${this.venue.venue_id}`, {
                method: 'DELETE',
                headers: {
                    'access-token': localStorage.getItem("token")
                }
            })
            console.log('Delete venue:', rawResponse);
        },
    },
    async mounted() {
        try {
            const getVenueShow = await fetch(`http://127.0.0.1:8081/api/getVenueShow/${this.venue.venue_id}`,
                {
                    headers: {
                        'access-token': localStorage.getItem("token")
                    }
                }
            );
            const showsData = await getVenueShow.json();
            this.shows = Object.values(showsData).pop();
        } catch (error) {
            console.error('Error fetching venues:', error);
        }
    }
};
</script>

<style>
.venue-card-user {
    gap: 3px;
    justify-content: space-around;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    background-color: white;
    padding: 20px;
    border-radius: 10px;
}

.containerV {
    max-width: 100%;
    margin: 10px;
    border-radius: 10px;
    padding: 20px;
    background-color: cornflowerblue;
}

.show-card-user button {
    background: white;
    border: 1px solid black;
    padding: 5px;
    margin: 5px;
}

.shows-container-user {
    display: flex;
    flex-direction: row;
    max-height: 100%;
    overflow: auto;
}

.venue-card-user-footer>button {
    border-radius: 10px;
}
</style>
